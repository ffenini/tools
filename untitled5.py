volta,curre=data[21]['Potential/V'],data[21]['Current/A']
MIN,MAX=round(min(voltage),3),round(max(voltage),3)
chunks = [voltage[x:x+3200] for x in range(0, len(voltage), 3200)]
a=len(chunks)
g=type(chunks)

def cv_splitter(voltage,current):
    cv,cur=[],[]
    check=[]
    voltage_list=voltage.tolist()
    current_list=current.tolist()
    what=[]#BBBBBBBB   script testing
    df=pd.DataFrame()
    datan={}
    ciclo={'Voltage':[],'Current':[]} #creating the new entry for data frame
    MIN,MAX=round(min(voltage_list),3),round(max(voltage_list),3)
    f= open("C:/M_drive_docs/Thesis/tables/guru99.txt","w+")
    for t in range(len(voltage_list)):
        i=t-cycle*(len(ciclo['Voltage'])+1)
        check.append([round(voltage_list[t],3),0])
        if check[i][0]==check[0][0] and i>0:
            chunks_V = [voltage[x:x+i] for x in range(0, len(voltage), i)] 
            chunks_C = [current[x:x+i] for x in range(0, len(current), i)]
            for u in range(0,len(chunks_V),1):
                #print(len(chunks_V[u]),'lklkl')
                cv = np.asarray(chunks_V[u])
                cur = np.asarray(chunks_C[u])            
                ciclo={'Voltage':cv,'Current':cur} #creating the new entry for data frame
                cycle_name='C'+str(u+1) #defining the name of the new entry
                #check=[] #resetting counter
                datan[cycle_name]=ciclo #creating new entry (as a dictionary)
            df=pd.DataFrame(data=datan)
            break
    return df

dati=cv_splitter(volta,curre)
print(dati)
#a=df['C5']['Voltage']
#print(len(a))