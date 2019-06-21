from header import *
def OCV(sample,exp,numbexp,folder_date,time=600,electrode='oldGCPt',):
    print('############ OCV vs time '+str(time)+' s')
    print('tech: ocpt')
    print('st:'+str(time))
    print('eh:1')
    print('el:-1')
    print('run')
    print('folder:C:\\Data\\filfe\\'+str(folder_date))
    name=str(folder_date)+'_exp'+str(exp)+'_'+str(numbexp)+'_'+str(sample)+'_'+str(electrode)+'_OCVdiskvstime_Ardear_05Msulf_1600rpm'
    print('save:'+name)
    print('tsave:'+name)
    print('')

#OCV(sample='MnCu25ring05',exp=77,numbexp='02',folder_date=180503,electrode='oldGCPt' )
pu=np.arange(1.1,2.10,0.05)
#pu=np.array(2)
for i in pu:
    if i!=pu[len(pu)-1]:
        j=pu.tolist()
        s=str(j.index(i)+1)
        if len(s)==1:
            s='0'+s
        print('')
        print('############ CV - 2 cycles 0.5/'+str(round(i,3))+' V (-0.158/'+str(round(i-0.658,6))+' V vs Hg/HgSO4)')
        print('tech:cv')
        print('ei:-0.158')
        print('eh:'+str(round(i-0.658,6)))
        print('el:-0.158')
        print('pn:p')
        print('v:0.02')
        print('cl:4')  ## 2*number of cycles
        print('si:0.001')
        print('qt:0')
        print('sens:1e-3')
        print('e2on')
        print('e2:-0.158')
        print('sens2:1e-4')
        print('run')
        print("folder:C:\\Data\\filfe\\180505")
        name='180505_exp79_'+s+'_NiCr2ring05V_exchGCPt_dearAr_cvvshghgso4_27c_05mH2SO4_-0158_'+str(round(i,3)).replace('.','')+'v_20mv_1cyc_1600rpm'
        print('save:'+name)
        print('tsave:'+name)
        print('')
    
#OCV(sample='NiCr2ring12V',exp=76,numbexp='04',folder_date=180503,electrode='exchGCPt' )   
