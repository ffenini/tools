def cv_splitter(voltage,current):
    cv,cur=[],[]
    check=[]
    voltage_list=voltage.tolist()
    current_list=current.tolist()
    what=[]#BBBBBBBB   script testing
    df=pd.DataFrame()
    datan={}
    cycle=0
    ciclo={'Voltage':[],'Current':[]} #creating the new entry for data frame
    MIN,MAX=round(min(voltage_list),3),round(max(voltage_list),3)
    print(MIN,MAX)
    f= open("C:/M_drive_docs/Thesis/tables/guru99.txt","w+")
    for t in range(len(voltage_list)):
        #print(len(ciclo['Voltage']))
        i=t-cycle*(len(ciclo['Voltage'])+1)
        #vi=voltage_list.index(i)
        what.append(i)#BBBBBBBB   script testing
        check.append([round(voltage_list[t],3),0])
        #print(check)
        print(t,i)
        lk=(i, check[i][0], len(check))
        f.write(str(lk)+' \n')
        print(lk)
        if check[i][0]==check[0][0] and i>0:
            print('finded the value where V is the same as the beginning: ',i)
            
            print(cv[len(cv)-1],len(cv))
            if check[t][0]==MIN:
                print('chcek if check[i][0] is the minimum voltage;', check[i][0], 'and', MIN)#BBBBBBBB   script testing
                cycle=cycle+1 #moving to next cycle
                cv = np.asarray(cv)
                cur = np.asarray(cur)
                ciclo={'Voltage':cv,'Current':cur} #creating the new entry for data frame
                print('check if the length of the CVx is correcte',len(ciclo['Voltage']))
                cycle_name='C'+str(cycle) #defining the name of the new entry
                check=[] #resetting counter
                datan[cycle_name]=ciclo #creating new entry (as a dictionary)
                df=pd.DataFrame(data=datan)
                print('voltage list length before cutting',len(voltage_list))#BBBBBBBB   script testing
                #voltage_list=voltage_list[i:] 
                print('voltage list length after cutting',len(voltage_list))#BBBBBBBB   script testing
                print('length of the key element for voltage','cv')#BBBBBBBB   script testing
                print(df)#BBBBBBBB   script testing
                #current_list=current_list[i:]
                cv,cur=[],[]
                cv.append(voltage_list[i])
                cur.append(current_list[i]) 
                if  len(voltage_list)==0: # in order to avoid to create a phantom entry 'C lastcyc +1 ':{'Voltage':[],'Current':[]}
                    print('Done!')
            elif check[t][0]!=MIN or check[t][0]!=MAX:             
                if check[0][1]==0:
                    print(str('----------------------')+str(i))#BBBBBBBB   script testing
                    cv.append(round(voltage_list[i],3))
                    cur.append(round(current_list[i],3))
                    check[0][1]=1
                else:
                    ciclo={'Voltage':cv,'Current':cur} #creating the new entry for data frame
                    cycle_name='C'+str(cycle) #defining the name of the new entry
                    cycle=cycle+1 #moving to next cycle
                    check=[] #resetting counter
                    datan[cycle_name]=ciclo #creating new entry (as a dictionary)
                    df=pd.DataFrame(data=datan)
                    voltage_list=voltage_list[i:] 
                    print(len(voltage_list))
                    current_list=current_list[i:]
                    if  len(voltage_list)==0: # in order to avoid to create a phantom entry 'C lastcyc +1 ':{'Voltage':[],'Current':[]}
                        print('Done!')#BBBBBBBB   script testing
        else:
            cv.append(voltage_list[i])
            cur.append(current_list[i]) 
            #print(len(cv),round(voltage_list[i],3))
            #print(i)         
    return df,what
tutticli,cosa=cv_splitter(data[21]['Potential/V'],data[21]['Current/A'])
yui=[]
for i in range(int(len(data[21]['Potential/V'])/5)):
    yui.append(i)
    
#print(tutticli.size)
plt.plot(np.arange(1,len(cosa)+1,1),cosa)
#plt.plot(np.arange(1,len(yui)+1,1),yui)
        
        
        
        
        
        
        
        