import os, glob

try:
    os.mkdir("output")

except:
    pass

ps3dir="input/ps3"

try:
    os.makedirs(ps3dir)

    print('The directories have been made.')
    
    input('Insert your textures in input/ps3 and then run the tool again to convert it.')

except:
    pass

dir = 'input/temp'

try:
    os.makedirs(dir)

except:
    pass

try:
    for ckdtextures in os.listdir(ps3dir):
    
        with open(ps3dir+'/'+ckdtextures,'rb') as f:
            f.read(44)
            data = f.read()
    
        dds=open('input/temp/'+ckdtextures.replace('.tga.ckd','.gtf').replace('.png.ckd','.gtf'),'wb')
        dds.write(data)
        dds.close()

except:
    pass

try:
    for gtf in os.listdir(dir):
        print('making '+gtf.replace(".gtf","")+'...')
        os.system("gtf2dds - input/temp/"+gtf+" -o output/"+gtf.replace(".gtf",".dds"))

except:
    pass

filelist = glob.glob(os.path.join(dir, "*"))
for f in filelist:
    os.remove(f)

os.rmdir(dir)