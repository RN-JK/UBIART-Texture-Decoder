import os

try:
    os.mkdir("output")

except:
    pass

pcdir="input/pc"

try:
    os.makedirs(pcdir)

    print('The directories have been made.')
    
    input('Insert your textures in input/pc and then run the tool again to convert it.')

except:
    pass

for ckdtextures in os.listdir(pcdir):
	
	with open(pcdir+'/'+ckdtextures,'rb') as f:
            f.read(44)
            data = f.read()
	
	dds=open('output/'+ckdtextures.replace('.tga.ckd','.dds').replace('.png.ckd','.dds'),'wb')
	print('making '+ckdtextures.replace('.tga.ckd','').replace('.png.ckd','')+'...')
	dds.write(data)
	dds.close()