test_range=[825, 50]
a=np.logspace(log10(test_range[0]), log10(test_range[1]), num=15, endpoint=True, base=10.0, dtype=None)
a=a.tolist()
a.insert(0,25)
for i in range(len(a)):
    a[i]=int(a[i])
ramp_rate=30 #degC/h
programs_fold='C:/M_drive_docs/Lab/Conductivity_rig91/CONDUCT/Programs/'
test_name='180823_NiCr2Cu025_new'
test=open(programs_fold+test_name+'.txt','w+')
#print(a)
tot_time=[]
ekstra=60 #extra minutes per step, equilibration time, decreases as the temperature increase and the ramp rate decreases
step_size=60 #minutes per step, equilibration time, ten points of measurement per step

test.write('\n')        
test.write(test_name)
test.write('\n')
test.write('text = Test type: stepped ramping down\n')
test.write('\n')
test.write('text = Sampled temperatures: '+str(a)+'\n')
test.write('\n')
test.write('text = Ramp rate: '+str(ramp_rate)+' °C/h // '+str(round(ramp_rate/60,2))+' °C/min\n')
test.write('\n')
test.write('text = Dwell time per step: '+str(step_size)+' min\n')
test.write('\n')
test.write('text = Extra time per step: '+str(ekstra)+' x (Ramp rate / T_step)\n')
test.write('\n')
#Project: 49511 E-sipi

#Plan: Conductivity measurements across the sample in air and in safety gas, between room temperature and 300 C

#text = Measurements at 300C every 10 min for 6 hours
#mail: sipi@dtu.dk this is a test, everything is fine so far

for k in range(len(a)-1):
    diff=abs(a[k]-a[k+1])
    timetime=diff/ramp_rate*60+ekstra*(ramp_rate/a[k+1])
    tot_time.append(timetime)
    #print(a[k],' to', a[k+1],': ',int(diff/ramp_rate*60),' min' )
    test.write('ramp = '+str(ramp_rate)+' furnace\n')
    test.write('temp = '+str(int(a[k+1]))+' furnace\n')
    test.write('wait = '+str(int(timetime))+'\n')
    for i in range(0,10,1):
        test.write('measure\n')
        test.write('wait = '+str(int(step_size/10))+'\n')
        tot_time.append(step_size/10)
    
TOTAL=np.asarray(tot_time)
print('Measured T: ',a)
print('Ramp rate: ',round(ramp_rate/60,2),' degC/min')
print('TOT time: ',sum(TOTAL)/60,' hours')