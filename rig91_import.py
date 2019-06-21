
''' 
The script extracts the concuctivity data from the files with format ' path_raa=date_t+'_'+test_num+'_'+name+'_'+dimen+'_'+atm.txt'
created with 'url_raadata.py' and creates three types of files:
   
    - .rig91 : file where all the data from raadata are put into columns, one for each test
           Date\tTime (s)\tFurnace setpoint  (o^C)\tT furnace (o^C)\tT sample a (o^C)\tT sample b (o^C)\tmicro_forward (Ohm)\tmicro_reverse (Ohm)\tT pO2 (o^C) \tpo2 (V)\tph2o (V)\n'     
           
           all the data are imported into the DataFrame 'condata'
           
    - .dots : the resistance measurements are taken from the file and averaged when the setpointT is constant to 
                extract fixed-temperature values (Arrhenius plots),  one for each test
            Tset(o^C)\tstd.dev1\tTfur(o^C)\tstd.dev2\tTsample_a(o^C)\tstd.dev3\tTsample_a(o^C)\tstd.dev4\tmicro_forward(Ohm)\tstd.dev5\tmicro_reverse(Ohm)\tstd.dev6\n'
            
            all the data are imported into the DataFrame 'condots'
            
    - COND_summary.list :all the available files/test are listed in this file, one general file
            'Date\tTest num\tMaterial\tDim1(cm)\tDim2(cm)\tAtmosphere\n'
            
            all the data are imported into the DataFrame 'condexp'


'''
path='C:/M_drive_docs/Lab/Conductivity_rig91/GLOSSYraw/'
make=os.listdir(path)

condata=[]
for file in make:
    if file.endswith('.txt') and file.endswith('_info.txt')==False:
        corr_data=open(path+file,'r')
        m=corr_data.readlines()
        lns=[]
        for b in range(len(m)):
            i=m[b].split(' ')
            lns.append(i)
        with open(path+file[:-4]+'.rig91','w') as cav:
            cav.write('Date\tTime (s)\tFurnace setpoint  (o^C)\tT furnace (o^C)\tT sample a (o^C)\tT sample b (o^C)\tmicro_forward (Ohm)\tmicro_reverse (Ohm)\tT pO2 (o^C) \tpo2 (V)\tph2o (V)\n')
            for line in lns:
                if line==lns[0]:
                    j=time.strptime(line[1], "%Y:%m:%d:%H:%M:%S")
                    time_zero=time.mktime(j) 
                date=time.strftime('%a, %d %b %Y %H:%M:%S',time.strptime(line[1], "%Y:%m:%d:%H:%M:%S"))
                clock=str(time.mktime(time.strptime(line[1], "%Y:%m:%d:%H:%M:%S"))-time_zero)
                furn_set=str(round(float(line[31]),1))
                if abs(float(furn_set))>1E4 or float(furn_set)<0:
                    furn_set=str()
                furn_temp=str(round(float(line[35]),1))
                if abs(float(furn_temp))>1E4 or float(furn_temp)<0:
                    furn_temp=str()
                t_samp1=str(round(float(line[7]),1))
                if abs(float(t_samp1))>1E4 or float(t_samp1)<0:
                    t_samp1=str()
                t_samp2=str(round(float(line[27]),1))
                if abs(float(t_samp2))>1E4 or float(t_samp2)<0:
                    t_samp2=str()
                u_for=str(round(float(line[11]),4))
                if abs(float(u_for))>1E9 or float(u_for)<0:
                    u_for=str()
                u_rev=str(round(float(line[15]),4))
                if abs(float(u_rev))>1E9 or float(u_rev)<0:
                    u_rev=str()
                po2=str(round(float(line[23]),6))
                t_po2=str(round(float(line[3]),1))
                if abs(float(t_po2))>1E4 or float(t_po2)<0:
                    t_po2=str()
                ph2o=str(round(float(line[19]),6))
                cav.write(date+'\t'+clock+'\t'+furn_set+'\t'+furn_temp+'\t'+t_samp1+'\t'+t_samp2+'\t'+u_for+'\t'+u_rev+'\t'+po2+'\t'+t_po2+'\t'+ph2o+'\n')
        cav.close()
    if file.endswith('.rig91'):
        condata.append(pd.read_csv(path+file[:-6]+'.rig91',delimiter = '\t'))
print(len(condata))

condexp=[]
with open('C:/M_drive_docs/Lab/Conductivity_rig91/COND_summary.list','w') as cav:
    cav.write('Date\tTest num\tMaterial\tDim1(cm)\tDim2(cm)\tAtmosphere\n')
    for file in make:
        if file.endswith('.rig91'):
            print(file)
            i=file[:-6].split('_') #removes the extension from file name and splits it in a list
            print(i)
            date=time.strftime('%a, %d %b %Y ',time.strptime(i[0], "%y%m%d"))
            test_num=i[1]
            mat=i[2]
            if i[3]=='nodimen':
                dim1='nodimen'
                dim2='nodimen'
            else:
                dim1=i[3][0]+'.'+i[3][1:4]
                dim2=i[3][5]+'.'+i[3][6:9]
            atm=i[4]
            a=(i[0],test_num,mat,dim1,dim2,atm)
            condexp.append(a)
            cav.write(date+'\t'+test_num+'\t'+mat+'\t'+dim1+'\t'+dim2+'\t'+atm+'\n')   
cav.close() 
summ_cond=(pd.read_csv('C:/M_drive_docs/Lab/Conductivity_rig91/COND_summary.list',delimiter='\t')).style

#obtain averaged dots from the condcutivity measurements
# the script takes the values of the furnace setpoints to evaluate the stable setpoints were
# to take a a value for the conductivity when it is stable.
# the script return the average values per setpoint together with the std deviation associated with it
condots=[]
for k in range(len(condata)):
    w=condata[k]['Furnace setpoint  (o^C)'].values
    medium=[] # medium will be a list of tuples composed as (a,b)  where 'a' is list of all the indexes of the point where the T setpoint = 'b'
    a=[]
    #for j in [50,60,65,70,75,80,85,90,100,127,171,227,298,394,527,727]:
    for i in range(len(w)-1):
        if i!=len(w) and i!=0 and w[i]==w[i+1] and w[i]==w[i-1]:
            b=w[i] #b is a single value of temperature
            a.append(i) #a is a list of all the indexes of the point where the T setpoint = b = w[i] = condata[k]['Furnace setpoint  (o^C)'].values[i]
        else:
            c=(a,b) #tuple formed by a list a and a float b (see above for description)
            medium.append(c) 
            a=[]
            #print(i,w[i])
    fraud=[] # 'fraud' will be a 'black' list of integers which are the indexes of 'medium' elements where len(a) is below a certain threshold (2) and are therefore positive false of the harvesting
    for i in range(len(medium)):
        h=medium[i]
        if len(h[0])<2: # h[0] = a and 2 is the threshold value
            fraud.append(i)
    setpoints=[] # 'medium' will be a list of tuples composed as (a,b)  where 'a' is list of all the indexes of the point where the T setpoint = 'b', cleaned from the positive false
    for i in range(len(medium)):
        if i in fraud: # checking if the value is an index which is listed in the 'black' list fraud
            continue
        else:
            if i!=0 and medium[i-1][1]-medium[i][1]>2: # in order not to double take a specific value of T set, in case there is a spike in the T setpoint data
                setpoints.append(medium[i])
    doth=path+condexp[k][0]+'_'+condexp[k][1]+'_'+condexp[k][2]+'_'+condexp[k][5]+'.dots'
    with open(doth,'w') as can:
        can.write('Tset(o^C)\tstd.dev1\tTfur(o^C)\tstd.dev2\tTsample_a(o^C)\tstd.dev3\tTsample_b(o^C)\tstd.dev4\tmicro_forward(Ohm)\tstd.dev5\tmicro_reverse(Ohm)\tstd.dev6\n')
        for i in setpoints:
            rm=i[0][0]
            rM=i[0][len(i[0])-1]
            tset=str(round(np.mean(condata[k]['Furnace setpoint  (o^C)'].values[rm:rM]),2))
            tset_std=str(round(np.std(condata[k]['Furnace setpoint  (o^C)'].values[rm:rM]),2))
            tfur=str(round(np.mean(condata[k]['T furnace (o^C)'].values[rm:rM]),2))
            tfur_std=str(round(np.std(condata[k]['T furnace (o^C)'].values[rm:rM]),2))
            temp1=str(round(np.mean(condata[k]['T sample a (o^C)'].values[rm:rM]),2))
            temp1_std=str(round(np.std(condata[k]['T sample a (o^C)'].values[rm:rM]),2))
            temp2=str(round(np.mean(condata[k]['T sample b (o^C)'].values[rm:rM]),2))
            temp2_std=str(round(np.std(condata[k]['T sample b (o^C)'].values[rm:rM]),2))
            u_for=str(round(np.nanmean(condata[k]['micro_forward (Ohm)'].values[rm:rM]),3))
            u_for_std=str(round(np.std(condata[k]['micro_forward (Ohm)'].values[rm:rM]),3))
            u_rev=str(round(np.nanmean(condata[k]['micro_reverse (Ohm)'].values[rm:rM]),3))
            u_rev_std=str(round(np.std(condata[k]['micro_reverse (Ohm)'].values[rm:rM]),3))
            can.write(tset+'\t'+tset_std+'\t'+tfur+'\t'+tfur_std+'\t'+temp1+'\t'+temp1_std+'\t'+temp2+'\t'+temp2_std+'\t'+u_for+'\t'+u_for_std+'\t'+u_rev+'\t'+u_rev_std+'\n')
            
    condots.append(pd.read_csv(doth,delimiter = '\t'))
can.close()

print('For importing the data from Rig 91 ("GLOSSY"):')
print('    - copy the "raadata"')
print('Headers:')
print()
print('{0:35}  {1:35} {2:30}'.format('######CONDATA#####', "#######CONDOTS#####","#######CONDEXP#####"))
print('{0:35}  {1:35} {2:30}'.format("['Date']", "['Tset(o^C)']","[i][0] = test date"))
print('{0:35}  {1:35} {2:30}'.format("['Time (s)']","['std.dev1']","[i][1] =  test n°"))
print('{0:35}  {1:35} {2:30}'.format("['Furnace setpoint  (o^C)']","['Tfur(o^C)']","[i][2] = material "))
print('{0:35}  {1:35} {2:30}'.format("['T furnace (o^C)']","['std.dev2']","[i][3] = bar height"))
print('{0:35}  {1:35} {2:30}'.format("['T sample a (o^C)']","['Tsample_a(o^C)']","[i][4] = bar width"))
print('{0:35}  {1:35} {2:30}'.format("['T sample b (o^C)']","['std.dev3']","[i][5] = atmosphere "))
print('{0:35}  {1:35} {2:30}'.format("['micro_forward (Ohm)']","['Tsample_b(o^C)']",""))
print('{0:35}  {1:35} {2:30}'.format("['micro_reverse (Ohm)']","['std.dev4']",""))
print('{0:35}  {1:35} {2:30}'.format("['T pO2 (o^C) ']","['micro_forward(Ohm)']",""))
print('{0:35}  {1:35} {2:30}'.format("['po2 (V)']","['std.dev5']",""))
print('{0:35}  {1:35} {2:30}'.format("['ph2o (V)']","['micro_reverse(Ohm)']",""))
print('{0:35}  {1:35} {2:30}'.format(" ","['std.dev6']",""))

      
      
      
      
      
      
      
      
      
summ_cond