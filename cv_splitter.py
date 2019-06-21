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


def cv_splitter(voltage,current):
    cv,cur=[],[]
    check=[]
    voltage_list=voltage.tolist()
    current_list=current.tolist()
    df=pd.DataFrame()
    datan={}
    ciclo={'Voltage':[],'Current':[]} #creating the new entry for data frame
    MIN,MAX=round(min(voltage_list),3),round(max(voltage_list),3)
    f= open("C:/M_drive_docs/Thesis/tables/guru99.txt","w+")
    for t in range(len(voltage_list)):
        #i=t-cycle*(len(ciclo['Voltage'])+1)
        check.append([round(voltage_list[t],3),0])
        if check[t][0]==check[0][0] and t>0:
            chunks_V = [voltage[x:x+t] for x in range(0, len(voltage), t)] 
            chunks_C = [current[x:x+t] for x in range(0, len(current), t)]
            for u in range(0,len(chunks_V),1):
                #print(len(chunks_V[u]),'lklkl')
                cv = np.asarray(chunks_V[u])
                cur = np.asarray(chunks_C[u])            
                ciclo={'Voltage':cv,'Current':cur} #creating the new entry for data frame
                if len(str(u+1))<2:
                    cycle_name='C0'+str(u+1) #defining the name of the new entry
                else:
                    cycle_name='C'+str(u+1)
                datan[cycle_name]=ciclo #creating new entry (as a dictionary)
            df=pd.DataFrame(data=datan)
            break
    return df


for de in [21]:#,13,9]:
    try:
        volta,curre=data[de]['Potential/V'],data[de]['Current/A']
    except KeyError:
        volta,curre=data[de]['Potential/V'],data[de]['i1/A']
    #chunks = [voltage[x:x+3200] for x in range(0, len(voltage), 3200)]
    #a=len(chunks)
    #g=type(chunks)
    
    
    
    dati=cv_splitter(volta,curre)
    #print(dati)
    #print(dati.columns)
    #a=df['C5']['Voltage']
    #print(len(a))
    fig,(ax.ax1)=plt.subplots(figsize=(30,12),facecolor='white')
    ax=plt.subplot(121)
    ax1=plt.subplot(122)
    o=0
    #print(dati)
    for i in dati.columns[0:]:
        #print(i)#,'C6','C7','C8','C9','C10']:
        ax1.plot(dati[i]['Voltage']+0.658,dati[i]['Current'],color='k',alpha=0.5)
    ave=[]
    avi=[]
    for k in range(len((dati['C01']['Current']))):
        aver=[abs(dati[d]['Current'][k]) for d in dati.columns[1:]]
        ave.append(np.gradient(aver))
        #avi.append(mean(aver))  #mean value of all the potential points
        #avi.append(abs(sp.stats.linregress(np.arange(0,len(aver),1),aver)[0]))
        avi.append(np.std(aver))
        #print(sp.stats.linregress(np.arange(0,len(aver),1),aver))
   # print(mean(avi))
    #avi=np.asarray(avi)
    avi=np.asarray(avi)
    print(avi)
    avi=avi/max(avi)
    print(avi)
    ax.axhline(0,0,1,linestyle='--')
    ax.set_ylabel('Current (A) ')
    ax.set_xlabel('Potential (V) vs SHE')
    ax1.set_xlabel('Potential  vs SHE')
    last_cyc_name=dati.columns[len(dati.columns)-1]
    ax.scatter(dati[last_cyc_name]['Voltage']+0.658,dati[last_cyc_name]['Current'],c=avi,cmap='jet')
    y_MIN,y_MAX=min(dati[last_cyc_name]['Current']),max(dati[last_cyc_name]['Current'])
    ax.set_ylim(y_MIN+0.1*y_MIN,y_MAX+0.05*y_MAX)
    fig.savefig('C:/M_drive_docs/Thesis/graphics/gradient_'+str(de)+'.png',bbox_inches='tight')
    fig.savefig('C:/M_drive_docs/Thesis/graphics/gradient_'+str(de)+'.pdf',bbox_inches='tight')
    #C:\M_drive_docs\Thesis\graphics
    #img = ax.imshow()
    #plt.colorbar(img, ax=ax)
    #plt.colorbar(mappable=fig)

#print(avi)

