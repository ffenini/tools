'''
1) Select the folders to import
2) Give the NOTEBOOKname with the same name of the the .ipynb file

The script imports the the files in 'data' and collects the dimensions of the electrode for each experiment in
'dimen'. The script creates a .list file were the the files imported are listed in the 'data' order, together 
with the 'dimen' order
'dimen' is a tuple of 5 elements; for the element i:
dimen[i][0]= disk area
dimen[i][1]= ring area
dimen[i][2]= collection efficiency of the RRDE
dimen[i][3]= name of the electrode
dimen[i][4]= experiment date and number

'''
from  header import *
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
infor=[]
for folder in folders:    
    path=main+folder
    make=os.listdir(path)
    for file in make:
        if file.endswith('.ch760'): 
            i=file.split('_')
            infor.append(i)
            #print(info)
            filez.append(folder+'/'+file)
            name.append(file)
            #print(file[7:15])
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
            dimen[len(dimen)-1]=list(dimen[len(dimen)-1])# adds experiment date and number at the end of dimen 
            dimen[len(dimen)-1].append(file[7:15])
            dimen[len(dimen)-1]=tuple(dimen[len(dimen)-1])
            if len(name)!=len(dimen):
                print('No dimensions detected for ' + str(file)+'!')
                break
          #  print(file)
            #print(dimen[make.index(file)]) 
for i in range(len(filez)):         
    data.append(pd.read_csv(main+str(filez[i]),delimiter = '\t'))

file_list_path='C:/M_drive_docs/JUPYTER/NOTE_BOOKS/imp_file_list/'+NOTEBOOKname+'.list'     
with open(file_list_path,'w') as can:   
    can.write('Folder\tFile\t Electrode\n')
   # print('filez: '+str(len(filez))+ '; folz: '+str(len(folz))+'; name: '+str(len(name))+'; dimen: '+str(len(dimen)))
    for i in range(len(filez)):
        can.write(folz[i]+'\t'+name[i]+'\t'+dimen[i][3]+'\n')
tre=pd.read_csv(file_list_path,delimiter = '\t')
summary=tre.style
### tre.style : to display the .list file entirely without missing characters in the lines
def cycplot(selector,cyc_plot,selex=[],cycleexp=[]):
    '''NEEDS SELECTOR 
       RETURNS: ranges
    in 'data_importer.py'
    cyc_plot: number of cycles to display
    selex: which cycles to display, default all
    cycleexp: array, must be the same length of 'selector',number of cycles of each experiment ordered as the entries of selector
                default: 10 cycles (automatically generated for each experiment)
    '''
    rtu=[]
    if len(cycleexp)==0:
        cycleexp=np.full(len(selector),10)
    for i in range(cyc_plot):  ## the same number of cycles is required
        a=[]
        b=[]
        f=[]
        for t in selector:
            ti=selector.index(t)
            aa=int(len(data[t])/cycleexp[ti])*i
            bb=aa+int(len(data[t])/cycleexp[ti])
            ff=int(bb-(bb-aa)/2)
            a.append(aa)
            b.append(bb)
            f.append(ff)
        d=str(i+1)+'th'
        if i==0:
            d=str(i+1)+'st'
        if i==1:
            d=str(i+1)+'nd'
        if i==2:
            d=str(i+1)+'rd'
        e=i+1
        c=(a,b,d,e,f)
        rtu.append(c)
    ranges=[]
    if len(selex)==0:
        selex=np.arange(1,cyc_plot+1,1)
    for y in selex:
        for p in rtu:
            if y==p[3]:
                ranges.append(p)
    return ranges