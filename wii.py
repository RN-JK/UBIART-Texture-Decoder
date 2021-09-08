import os, glob

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

try:
    os.makedirs(dir)

except:
    pass

try:
    for ckdtextures in os.listdir(wiidir):
    
        with open(wiidir+'/'+ckdtextures,'rb') as f:
            f.read(172)
            data = f.read()
    
        cmpr=open('input/temp/'+ckdtextures.replace('.tga.ckd','.tpl').replace('.png.ckd','.tpl'),'wb')
        cmpr.write(b'\x00\x20\xAF\x30\x00\x00\x00\x01\x00\x00\x00\x0C\x00\x00\x00\x14\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x0E\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        cmpr.write(data)
        cmpr.close()

except:
    pass

try:
    for tpl in os.listdir(dir):
        print('making '+tpl.replace(".tpl","")+'...')
        os.system("wimgt dec input/temp/"+tpl+" --dest output/"+tpl.replace(".tpl",".png"))

except:
    pass

filelist = glob.glob(os.path.join(dir, "*"))
for f in filelist:
    os.remove(f)

os.rmdir(dir)