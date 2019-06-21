'''
1) Select the folders to import
2) Give the NOTEBOOKname with the same name of the the .ipynb file

The script imports the the files in 'data' and collects the dimensions of the electrode for each experiment in
'dimen'. The script creates a .list file were the the files imported are listed in the 'data' order, together 
with the 'dimen' order.
'''
NOTEBOOKname='RRDE-180324-OCV_Pt_RING_satO2_current_vs_time'
folders=['180314/chronoamp','180320','180321','180323']

data=[]
filez=[]
dimen=[]
name=[]
folz=[]
main='C:/M_drive_docs/Lab/RDE/'
oldGCPt=(0.2436,0.1695541,0.38,'oldGCPt') ## (DISK area, RING area, collection efficiency of the ring, electrode name)
exchGCPt=(0.19634,0.1099557,0.26,'exchGCPt')
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
            if '_oldGC' in file or '_OldGC' in file:
                dimen.append(oldGCPt) 
            if '_exchGC' in file or '_Pt' in file or 'Ptring' in file:
                dimen.append(exchGCPt)
for i in range(len(filez)):         
    data.append(pd.read_csv(main+str(filez[i]),delimiter = '\t'))

file_list_path='C:/M_drive_docs/JUPYTER/NOTE_BOOKS/imp_file_list/'+NOTEBOOKname+'.list'     
with open(file_list_path,'w') as can:   
    can.write('Folder \t File \t Electrode \n')
    for i in range(len(filez)):
        can.write(folz[i]+'\t'+name[i]+'\t'+dimen[i][3]+'\n')
tre=pd.read_csv(file_list_path,delimiter = '\t')

### tre.style : to display the .list file entirely without missing characters in the lines