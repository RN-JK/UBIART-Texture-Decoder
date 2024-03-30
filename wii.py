import os, glob, struct
from PIL import Image

try:
    os.mkdir("output")

except:
    pass

wiidir="input/wii"

try:
    os.makedirs(wiidir)

    print('The directories have been made.')
    
    input('Insert your textures in input/wii and then run the tool again to convert it.')

except:
    pass

dir = 'input/temp'
os.makedirs(dir,exist_ok=True)
for ckdtextures in os.listdir(wiidir):
    alpha=False
    with open(wiidir+'/'+ckdtextures,'rb') as f:
        filename=ckdtextures.split('.')[0]
        #print(ckdtextures)
        #f.read(172)
        f.read(56)
        height=struct.unpack('>I',f.read(4))[0]
        width=struct.unpack('>I',f.read(4))[0]
        f.read(64)
        header=f.read(4)
        if header==b'APMC':
            alpha=True
            f.read(40)
            height=height*2
            #sizeorder=struct.pack('>H',width)+struct.pack('>H',height)
            sizeorder=struct.pack('>H',height)+struct.pack('>H',width)
        if header==b'1TXD':
            alpha=False
            f.read(40)
            sizeorder=struct.pack('>H',height)+struct.pack('>H',width)
        data=f.read()
    
    cmpr=open('input/temp/'+filename+'.tpl','wb')
    cmpr.write(b'\x00\x20\xAF\x30\x00\x00\x00\x01\x00\x00\x00\x0C\x00\x00\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'+sizeorder+b'\x00\x00\x00\x0E\x00\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    cmpr.write(data)
    cmpr.close()

    if alpha==True:
        os.system("wimgt dec input/temp/"+filename+".tpl --overwrite --dest input/temp/"+filename+".png")
        img=Image.open("input/temp/"+filename+".png")
        w,h=img.size
        base_img=Image.open("input/temp/"+filename+".png").crop((0,0,w,int(h/2)))
        alpha_img=Image.open("input/temp/"+filename+".png").crop((0,int(h/2),w,h)).convert('L')

        img_output=base_img.copy()
        img_output.putalpha(alpha_img)
        img_output.save("output/"+filename+".png")

    else:
        os.system("wimgt dec input/temp/"+filename+".tpl --overwrite --dest output/"+filename+".png")

filelist = glob.glob(os.path.join(dir, "*"))
for f in filelist:
    os.remove(f)

os.rmdir(dir)
