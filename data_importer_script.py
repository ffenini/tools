'''
1) Select the folders to import
2) Give the NOTEBOOKname with the same name of the the .ipynb file

The script imports the the files in 'data' and collects the dimensions of the electrode for each experiment in
'dimen'. The script creates a .list file were the the files imported are listed in the 'data' order, together 
with the 'dimen' order.
'''
from  header_script import *
from  myfile import *
data=[]
filez=[]
dimen=[]
name=[]
folz=[]
main='C:/M_drive_docs/Lab/RDE/'
oldGCPt=(0.2436,0.1695541,0.38,'oldGCPt') ## (DISK area, RING area, collection efficiency of the ring, electrode name)
exchGCPt=(0.19634,0.1099557,0.26,'exchGCPt')
Ptplate=('-','-','-','Pt(OCV)')
Audisk=(0.19634,0,0,'Au disk')
GCAu=(0.2436,0.1695541,0.38,'GCAu')
GC=(0.19634,0,0,'GC')
for folder in folders:    
    path=main+folder
    make=os.listdir(path)
    for file in make:  
        if file.endswith('.ch760'): 
            filez.append(folder+'/'+file)
            name.append(file)
            folz.append(folder)
            if '_GC' in file:
                dimen.append(GC)
            if '_oldGCPt' in file or '_OldGC' in file:
                dimen.append(oldGCPt) 
            if '_exchGCPt' in file:
                dimen.append(exchGCPt)
            if '_Audisk' in file:
                dimen.append(Audisk)
            if '_rrdeGCAu' in file:
                dimen.append(GCAu)
            if '_platePt' in file or '_platewirePt' in file or '_ocvPtprobe' in file:
                dimen.append(Ptplate)
            if len(name)!=len(dimen):
                print('No dimensions detected for ' + str(file)+'!')
                break
          #  print(file)
          #  print(dimen)
for i in range(len(filez)):         
    data.append(pd.read_csv(main+str(filez[i]),delimiter = '\t'))

file_list_path='C:/M_drive_docs/JUPYTER/NOTE_BOOKS/imp_file_list/'+NOTEBOOKname+'.list'     
with open(file_list_path,'w') as can:   
    can.write('Folder \t File \t Electrode \n')
   # print('filez: '+str(len(filez))+ '; folz: '+str(len(folz))+'; name: '+str(len(name))+'; dimen: '+str(len(dimen)))
    for i in range(len(filez)):
        can.write(folz[i]+'\t'+name[i]+'\t'+dimen[i][3]+'\n')
tre=pd.read_csv(file_list_path,delimiter = '\t')
summary=tre.style
print('')
### tre.style : to display the .list file entirely without missing characters in the lines
