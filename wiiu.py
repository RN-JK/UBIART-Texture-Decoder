import os, glob

try:
    os.mkdir("output")

except:
    pass

wiiudir="input/wiiu"

try:
    os.makedirs(wiiudir)

    print('The directories have been made.')
    
    input('Insert your textures in input/wiiu and then run the tool again to convert it.')

except:
    pass

dir = 'input/temp'

try:
    os.makedirs(dir)

except:
    pass

try:
    for ckdtextures in os.listdir(wiiudir):
    
        with open(wiiudir+'/'+ckdtextures,'rb') as f:
            f.read(44)
            data = f.read()
    
        dds=open('input/temp/'+ckdtextures.replace('.tga.ckd','.gtx').replace('.png.ckd','.gtx'),'wb')
        dds.write(data)
        dds.close()

except:
    pass

try:
    for gtx in os.listdir(dir):
        print('making '+gtx.replace(".gtx","")+'...')
        os.system("texconv2 -i input/temp/"+gtx+" -o output/"+gtx.replace(".gtx",".dds"))

except:
    pass

filelist = glob.glob(os.path.join(dir, "*"))
for f in filelist:
    os.remove(f)

os.rmdir(dir)