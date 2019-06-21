dum={}
source='C:/M_drive_docs/Lab/EIS/MEE0124/'
samples=os.listdir(source)
#fig,ax=plt.subplots(figsize=(10,6))
for i in samples:
    #print(i)
    path=source+i
    #test=pd.read_csv(path, delimiter='\t',names=['2Theta','Yobs','Ycalc','Backg','posr'],
                     #skiprows=4,engine='python')
    #extracting the peak positions
    with open(path, 'r') as h:
        tu=h.readlines()       
    if i.endswith('.i2p') :
        current=[] #structure (tuple) : (2theta angle(float), Millerindices(str), 1(ka1) or 2(ka2)(str))
        potential=[]
        time=[]
        zero=float(tu[6].replace('\n','').split(',')[0].split(' ')[0])
        for hj in tu[6:]:
            hj=hj.replace('\n','')
            j=hj.split(',')
            a=j[0].split(' ')
            j[0]=a[1]
            j.append(float(a[0])-zero)   
            #print(j)
            j[0]=j[0].replace(' ','')
            j[0]=j[0].replace('+','')
            j[1]=j[1].replace(' ','')
            j[1]=j[1].replace('+','')
            j[1]=j[1].replace('A','')
            j[0],j[1]=float(j[0]),float(j[1])
            potential.append(j[0])
            current.append(j[1])
            time.append(j[2])
        exper={'name':i, 'Potential(V)':potential,'Current(A)':current,'Time(s)':time}
        dum[i+'CV_P']=exper
    if  i.endswith('.i2c'):
        bias=tu[3].split(',')[0]
        bias=bias.replace('Bias: ','')
        current=[] #structure (tuple) : (2theta angle(float), Millerindices(str), 1(ka1) or 2(ka2)(str))
        potential=[]
        time=[]
        zero=float(tu[6].replace('\n','').split(',')[0].split(' ')[0])
        for hj in tu[6:]:
            hj=hj.replace('\n','')
            j=hj.split(',')
            a=j[0].split(' ')
            j[0]=a[1]
            j.append(float(a[0])-zero)   
            #print(j)
            j[0]=j[0].replace(' ','')
            j[0]=j[0].replace('+','')
            j[1]=j[1].replace(' ','')
            j[1]=j[1].replace('+','')
            j[1]=j[1].replace('A','')
            j[0],j[1]=float(j[0]),float(j[1])
            potential.append(j[0])
            current.append(j[1])
            time.append(j[2])
        exper={'name':i, 'Potential(V)':potential,'Current(A)':current,'Time(s)':time}
        dum[i+'CHRONO_'+bias]=exper
    if i.endswith('.i2b') and not i.endswith('_long.i2b') :
        bias=tu[3].split(',')[0]
        bias=bias.replace('Bias: ','')
        amplitude=tu[3].split(',')[1]
        amplitude=amplitude.replace('Ampltude ','')
        freq=[] #structure (tuple) : (2theta angle(float), Millerindices(str), 1(ka1) or 2(ka2)(str))
        Zreal=[]
        Zimag=[]
        for hj in tu[7:-1]:
            hj=hj.replace('\n','')
            j=hj.split(' ')
            #print(i,j)
            j[0],j[1],j[2]=float(j[0]),float(j[1]),float(j[2])
            freq.append(j[0])
            Zreal.append(j[1])
            Zimag.append(j[2])
        exper={'name':i, 'Freq':freq,'Zreal(Ohm)':Zreal,'Zreal(Ohm)':Zimag,'Bias':bias,'Amplitude':amplitude}
        dum[i+'EIS_'+bias]=exper
    h.close()   
print(dum.keys())
#print(dum['s4_0011.i2pPotenChrono'])