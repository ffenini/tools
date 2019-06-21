filename='180316_test111_LaNiCr_0492x0300_air100mlmin'
corr_data=open('C:/M_drive_docs/Lab/Conductivity_rig91/tests/test_cond.txt','r')
m=corr_data.readlines()
lns=[]
for b in range(len(m)):
    i=m[b].split(' ')
    lns.append(i)
with open('C:/M_drive_docs/Lab/Conductivity_rig91/test_extract_cond.rig91','w') as cav:
    cav.write('Date\t Time (s)\tFurnace setpoint  (o^C)\tT furnace (o^C)\tT sample a (o^C)\tT sample b (o^C)\tmicro_forward (Ohm)\tmicro_reverse (Ohm)\tT pO2 (o^C) \tpo2 (V)\tph2o (V)\n')
    for line in lns:
        if line==lns[0]:
            j=time.strptime(line[1], "%Y:%m:%d:%H:%M:%S")
            time_zero=time.mktime(j) 
        date=time.strftime('%a, %d %b %Y %H:%M:%S',time.strptime(line[1], "%Y:%m:%d:%H:%M:%S"))
        clock=str(time.mktime(time.strptime(line[1], "%Y:%m:%d:%H:%M:%S"))-time_zero)
        furn_set=str(round(float(line[31]),1))
        furn_temp=str(round(float(line[35]),1))
        t_samp1=str(round(float(line[7]),1))
        t_samp2=str(round(float(line[27]),1))
        u_for=str(round(float(line[11]),4))
        u_rev=str(round(float(line[15]),4))
        po2=str(round(float(line[23]),6))
        t_po2=str(round(float(line[3]),1))
        ph2o=str(round(float(line[19]),6))
        cav.write(date+'\t'+clock+'\t'+furn_set+'\t'+furn_temp+'\t'+t_samp1+'\t'+t_samp2+'\t'+u_for+'\t'+u_rev+'\t'+po2+'\t'+t_po2+'\t'+ph2o+'\n')
cav.close()

test=pd.read_csv('C:/M_drive_docs/Lab/Conductivity_rig91/test_extract_cond.rig91', delimiter='\t')
    #condata.append(pd.read_csv(main+str(filez[i]),delimiter = '\t'))


print(test.values)



#print(b)
#print(b[1])
#print(c[1])
#clock=time.strptime(b[1], "%Y:%m:%d:%H:%M:%S") 
#clock2=time.strptime(c[1], "%Y:%m:%d:%H:%M:%S")
#g=(time.mktime(clock2) - time.mktime(clock))
#print(time.strftime('%a, %d %b %Y %H:%M:%S',clock))
#print(time.strftime('%a, %d %b %Y %H:%M:%S',clock2))
#print(g)