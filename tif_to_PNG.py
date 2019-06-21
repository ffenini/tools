#for i in ['1BiSnO2','2BiSnO2','3BiSnO2','4BiSnO2','05BiSnO2','15BiSnO2','pyro','pyro_sint']:
#    source='O:/Buildings and labs/Microscopes/Microscopy archive/2017 Archive/MERLIN/Filfe/PlainImages/20170406/'+i+'/'#SnO2/PlainImages/'
#source='O:/Buildings and labs/Microscopes/Microscopy archive/2017 Archive/MERLIN/Filfe/PlainImages/5BiSnO2/'#SnO2/PlainImages/'
source='D:/M_drive_docs/Lab/SEM/TEM3000/180221_NiCr2mill_Ti_SS_felts/'


#bisno=os.listdir(source)
imtif=list_files1(source,'tif')


print(imtif)
for t in imtif:    
    im = Image.open(source+t)
    print(t[:-4])
    im.save(source+t[:-4]+'.png')
imtif=list_files1(source,'png')
print(imtif)
plain=False
if plain:
    source_plain=source+'PlainImages/'
    imtif_plain=list_files1(source_plain,'tif')
    print(imtif_plain)
    for t in imtif_plain:    
        im = Image.open(source_plain+t)
        print(t[:-4])
        im.save(source_plain+t[:-4]+'.png')
    imtif_plain=list_files1(source_plain,'png')
    print(imtif_plain)
    
    