import os, glob

try:
    os.mkdir("output")

except:
    pass

nxdir="input/nx"

try:
    os.makedirs(nxdir)

    print('The directories have been made.')
    
    input('Insert your textures in input/nx and then run the tool again to convert it.')

except:
    pass

dir = 'input/temp'

try:
    os.makedirs(dir)

except:
    pass

try:
    for ckdtextures in os.listdir(nxdir):
    
        with open(nxdir+'/'+ckdtextures,'rb') as f:
            f.read(44)
            data = f.read()
    
        dds=open('input/temp/'+ckdtextures.replace('.tga.ckd','.xtx').replace('.png.ckd','.xtx'),'wb')
        dds.write(data)
        dds.close()

except:
    pass

try:
    for xtx in os.listdir(dir):
        print('making '+xtx.replace(".xtx","")+'...')
        os.system("xtx_extract -o output/"+xtx.replace(".xtx",".dds")+" input/temp/"+xtx)

except:
    pass

