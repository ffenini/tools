from data_importer import *

### FW of the compounds
formulas=['MnCu0.25Cr1.75O4','NiCr2O4']
pm=[]
for formula in formulas:
    mat=[]
    mat.append(formula)
    m = pt.formula(formula)  
    mas=round(m.mass,3)
    mat.append(mas)
    pm.append(mat)
    
formula='NiCr2O4'
atomic=pt.formula(formula).atoms #dictionary with atoms and coefficient; access coeffiecient: atomic[pt.ELEMENTSYMBOL]
m = pt.formula(formula)  
massa=round(m.mass,3) #formula weight of the compound
drop=25*micro #grams of material deposited on the disk
#print(drop)
mechanism=3 #how many electrons are involved in the reaction considered
Fcos=mechanism*sp.constants.value('Faraday constant')# a tre electron process is assumed


key_val={'A':[],'B':[]}
key_sum={'A':[],'B':[]}
#integration ranges
##mode A
intrngA=[
        ((1.21,1.71),(1.11,1.73))]#,
        #((1.71,1.98),(1.73,1.98))
        #]# structure intrng=[((rangeD1),(rangeR1)),((rangeD2),(rangeR2)),...] range 1
for q in range(len(intrngA)):
    key_val['A'].append({'DISK':{},'RING':{}})
    key_sum['A'].append({'DISK':{},'RING':{}})
    for key in atomic.keys():
        strkey=str(key)
        key_sum['A'][q]['DISK'][getattr(pt,strkey)]=[]
        key_sum['A'][q]['RING'][getattr(pt,strkey)]=[]
        key_val['A'][q]['DISK'][getattr(pt,strkey)]=[]
        key_val['A'][q]['RING'][getattr(pt,strkey)]=[]
           # key_sum[getattr(pt,strkey)]=[]
##mode B
intrngB=[
        ((1.21,1.71),(1.21,1.71))]
        #,((1.71,1.971),(1.73,1.971))]
for q in range(len(intrngA)):
    key_val['B'].append({'DISK':{},'RING':{}})
    key_sum['B'].append({'DISK':{},'RING':{}})
    for key in atomic.keys():
        strkey=str(key)
        key_sum['B'][q]['DISK'][getattr(pt,strkey)]=[]
        key_sum['B'][q]['RING'][getattr(pt,strkey)]=[]
        key_val['B'][q]['DISK'][getattr(pt,strkey)]=[]
        key_val['B'][q]['RING'][getattr(pt,strkey)]=[]
    

selector=[157]#[12,31,76,81,85,89,92]
baseline=161
label_book= ['MnCu25 GG \noldGC R=0.5 V', 'NiCr2 \n 0.5V', 'MnCu25 GG \noldGC R=1.2 V', 'bare oldGCPt \n R=1.2 V', 'GG2 exch \n R=1.2 V', 'bare oldGCPt \n R=1.2 V', 'NiCr2 \n 1.2V']
ranges=cycplot(selector,cyc_plot=5, cycleexp=[5])
#print(ranges)
das=[]#disk areas, for all the experiments
ras=[]#ring peak areas, for all the 
for i in selector: 
    DIM=5
    fig,ring_disk=plt.subplots(figsize=(5*DIM , 3*DIM))
    labz=label_book
    ring_disk=plt.subplot(111) #ring_disk=plt.subplot(gs[0:,1])
    colors=[]
    colori=[]
    cores=[]
    si=selector.index(i) 
    #print(infor[i]) #single experiments anodic disk peak area, 
            #it is saved as a tuple of a list(area per cycle) and  a tuple with the integration limits
    raa=[] # single areas, orange peak
    raas=[] #cumulative areas, orange peak
    raap=[] #cumulative percentage
    raa1=[] #single areas, blue peak
    raas1=[] #cumulative areas, blue peak
    raap1=[] #single areas, blue peak
    daa=[] 
    raas=[] #cumulative areas
    daas=[]
    daap=[]
    print('{0:35}  {1:35} {2:30}'.format('Sample:', str(formula),''))
    print('{0:35}  {1:35} {2:30}'.format("PM:",str( massa),"g/mol"))
    print('{0:35}  {1:35} {2:30}'.format("Mat. deposited:",str(drop),"g"))
    print('{0:35}  {1:35} {2:30}'.format("Moles:",str(drop/massa),"mol"))
    for key in atomic.keys():
        key=str(key) ## needs to be a string to be used in 'getattr'
        print('{0:35}  {1:35} {2:30}'.format(str(getattr(pt, key))+" (mol)",str((drop/massa)*atomic[getattr(pt, key)]),"mol "))
    print()
    for p in ranges:
        ###### GENERATING THE DATA
        sr=ranges.index(p)
        rm=p[0][si] #single plot range minimum
        rh=p[4][si]
        rM=p[1][si] #single plot range maximum
        Ar=dimen[i][1] # RING area
        ce=dimen[i][2] # collection efficiency
        Ad=dimen[i][0] # DISK area
        time=data[i]['Time/s'].values #time 
        potential=0.658+data[i]['Potential/V'].values #potential vs SHE (V)
        if baseline!=None:
            try:
                datD=data[i]['i1/A'].values-data[baseline]['i1/A'].values
                datR=data[i]['i2/A'].values-data[baseline]['i2/A'].values
            except KeyError:
                datD=data[i]['Current/A'].values
                datR=0*data[i]['Current/A'].values
        else:
            try:
                datD=data[i]['i1/A'].values
                datR=data[i]['i2/A'].values
            except KeyError:
                datD=data[i]['Current/A'].values
                datR=0*data[i]['Current/A'].values
        curr2=datR/Ar/ce #current density RING (A cm-2)
        curr1=datD/Ad ##current density DISK (A cm-2) 
        if baseline!=None:
            for ty in range(len(curr1)) : ### taking out the EVIDENT artifacts due to the subtraction
                if np.sign(curr1[ty])!=np.sign(data[baseline]['i1/A'].values[ty]) :
                    curr1[ty]=0
                if potential[ty]>1.6 and ty>rh:
                    curr1[ty]=0
        milli=1000
        
        ## PLOT RANGE
        xMIN=-5 #range
        xMAX=time[rm-rm:rM-rm][rM-rm-1] #range
        
        ###### GENERATING THE COLORS
        colors.append(cm.viridis(int(0+sr*255/(len(ranges)))))##color map divided by the number of files
        colori.append(cm.jet(int(0+sr*255/(len(ranges)))))##color map divided by the number of files
        cores.append(cm.winter(int(0+sr*255/(len(ranges)))))##color map divided by the number of files
        
        #a=milli*curr2[rh+1:rM] # generating the cathodic branch mirroring for subtraction of the ring OER-dependent ORR current
        #c=np.flipud(a)
        #b=np.concatenate((c,a))
        #d=milli*curr1[rh+1:rM]
        #e=np.flipud(d)
        #f=np.concatenate((e,d)) 
        
        # generating the vertical POTENTIAL lines
        if p[3]==1:
            for u in np.arange(0,xMAX,30):
                #print(u)
                if u%40==0:
                    col='k'
                    linst='--'
                else:
                    col='k'
                    linst=':'
                lll=np.where(time[rm-rm:rM-rm]==u)[0][0]
                ring_disk.axvline(time[rm-rm:rM-rm][lll],ymin=-10,ymax=10,alpha=0.4,linestyle=linst,color=col)
                if time[rm-rm:rM-rm][lll]<xMAX and time[rm-rm:rM-rm][lll]>xMIN:
                    ring_disk.text(time[rm-rm:rM-rm][lll],-0.095,str(round(potential[rm:rM][lll],3))+' V',color=col,alpha=0.75,fontsize=DIM*3)
        
        # PLOTTING
        ring_disk.plot(time[rm-rm:rM-rm],milli*curr1[rm:rM],color=colors[ranges.index(p)])
        ring_disk.plot(time[rm-rm:rM-rm],milli*curr2[rm:rM],color=colors[ranges.index(p)],linestyle='--')
        ring_disk.plot(time[rm-rm:rM-rm],0*curr2[rm:rM],color='r',linestyle='-',linewidth=1) #zero mline
        
        ##### AREA determination
        
        ### ANODIC
        ##integration mode A
        intrng=[((1.23,1.69),(1.23,1.71)),((1.71,1.98),(1.73,1.98))]# structure intrng=[((rangeD1),(rangeR1)),((rangeD2),(rangeR2)),...]
        intA=[] # integration data for different rangese structure intA=[((areadiskA range 1),(arearingA range 1)),((areadiskA range 2),(arearingA range 2)),...]
        for t in range(len(intrngA)):
            intA.append([])
        for q in range(len(intrngA)):
            Drange=(intrngA[q][0]) #integration range DISK
            Rrange=(intrngA[q][1]) #integration range RING
            bm=np.where(potential[rm-rm:rM-rm]==Drange[0])[0][0]
            bM=np.where(potential[rm-rm:rM-rm]==Drange[1])[0][0]  
            if len(Rrange)!=0:
                bmr=np.where(potential[rm-rm:rM-rm]==Rrange[0])[0][0]
                bMr=np.where(potential[rm-rm:rM-rm]==Rrange[1])[0][0]   
            else:
                bmr=bm
                bMr=bM
            # cathodic peaks
            #bm=np.where(potential[rm-rm:rM-rm]==1)[0][0] 
            #bM=np.where(potential[rm-rm:rM-rm]==1.73)[0][0]
            diskA=np.trapz(curr1[rm:rM][bm:bM]*Ad,time[rm-rm:rM-rm][bm:bM]) #integration of the whole range DISK (multiplpied by area beacause curr and not curr dens)
            ringA=np.trapz((curr2[rm:rM])[bmr:bMr]*Ar,time[rm-rm:rM-rm][bmr:bMr],axis=-1) #integration of the whole range RING (multiplpied by area beacause curr and not curr dens)
            intA[q].append(diskA)
            intA[q].append(ringA)
            
            ring_disk.fill_between(time[rm-rm:rM-rm][bm:bM],milli*curr1[rm:rM][bm:bM],color=colors[ranges.index(p)],alpha=0.5)
            ring_disk.fill_between(time[rm-rm:rM-rm][bmr:bMr],milli*curr2[rm:rM][bmr:bMr],color=colori[ranges.index(p)],alpha=0.5)        
        ##integration mode B
        intB=[]
        for t in range(len(intrngB)):
            intB.append([])
        intrng=[((1.23,1.69),(1.23,1.71)),((1.71,1.971),(1.73,1.971))]
        for q in range(len(intrngB)):
            Drange=(intrngB[q][0]) #integration range DISK
            Rrange=(intrngB[q][1]) #integration range RING
            sm=np.where(potential[rm-rm:rM-rm]==Drange[0])[0][0]
            sM=np.where(potential[rm-rm:rM-rm]==Drange[1])[0][0]  
            if len(Rrange)!=0:
                smr=np.where(potential[rm-rm:rM-rm]==Rrange[0])[0][0]
                sMr=np.where(potential[rm-rm:rM-rm]==Rrange[1])[0][0]   
            else:
                smr=sm
                sMr=sM
            x_line=np.linspace(time[rm-rm:rM-rm][sm],time[rm-rm:rM-rm][sM],len(time[rm-rm:rM-rm][sm:sM])) #from where, to where, how many points
            y_line=np.linspace(milli*curr1[rm:rM][sm],milli*curr1[rm:rM][sM],len(milli*curr1[rm:rM][sm:sM]))
            x_line_RING=np.linspace(time[rm-rm:rM-rm][smr],time[rm-rm:rM-rm][sMr],len(time[rm-rm:rM-rm][smr:sMr])) #from where, to where, how many points
            y_line_RING=np.linspace(milli*curr2[rm:rM][smr],milli*curr2[rm:rM][sMr],len(milli*curr1[rm:rM][smr:sMr]))
            ring_disk.plot(x_line_RING,y_line_RING,color=colori[ranges.index(p)],alpha=1)
            if p[3]==1:
                ring_disk.plot(x_line,y_line,color=colors[ranges.index(p)],alpha=1)
                diskB=np.trapz((curr1[rm:rM][sm:sM]-y_line/milli)*Ad,time[rm-rm:rM-rm][sm:sM]) #integration of the undercut peak DISK (multiplpied by area beacause curr and not curr dens)
                ringB=np.trapz(curr2[rm:rM][smr:sMr]*Ar,time[rm-rm:rM-rm][smr:sMr]) #integration of the full area arounf the clear peak RING (multiplpied by area beacause curr and not curr dens)
                ring_disk.fill_between(time[rm-rm:rM-rm][sm:sM],milli*curr1[rm:rM][sm:sM],y_line,color=colors[ranges.index(p)],alpha=1)  ##area around the peak RING
                ring_disk.fill_between(time[rm-rm:rM-rm-1][smr:sMr],milli*curr2[rm:rM-1][smr:sMr],y_line_RING,color=colori[ranges.index(p)],alpha=1) ##area around the peak RING after OER-derived ORR current
            else:
                diskB=nan
                ringB=nan
            intB[q].append(diskB)
            intB[q].append(ringB)            

        
                          
                          
        
                          
                          

        ### CATHODIC
        
        ##integration mode A
        DrangeC=(0.73,1.42) #integration range DISK
        RrangeC=() #integration range RING
        bm=np.where(potential[rm-rm:rM-rm]==DrangeC[1])[0][1]
        bM=np.where(potential[rm-rm:rM-rm]==DrangeC[0])[0][1]  
        if len(RrangeC)!=0:
            bmr=np.where(potential[rm-rm:rM-rm]==RrangeC[1])[0][1]
            bMr=np.where(potential[rm-rm:rM-rm]==RrangeC[0])[0][1]   
        else:
            bmr=bm
            bMr=bM
        # cathodic peaks
        #bm=np.where(potential[rm-rm:rM-rm]==1)[0][0] 
        #bM=np.where(potential[rm-rm:rM-rm]==1.73)[0][0]
        diskAc=np.trapz(curr1[rm:rM][bm:bM]*Ad,time[rm-rm:rM-rm][bm:bM]) #integration of the whole range DISK (multiplpied by area beacause curr and not curr dens)
        ringAc=np.trapz((curr2[rm:rM])[bmr:bMr]*Ar,time[rm-rm:rM-rm][bmr:bMr],axis=-1) #integration of the whole range RING (multiplpied by area beacause curr and not curr dens)
        
        ##integration mode B
        DrangeCB=(0.73,1.42) #integration range DISK
        RrangeCB=() #integration range RING
        sm=np.where(potential[rm-rm:rM-rm]==DrangeCB[1])[0][1]
        sM=np.where(potential[rm-rm:rM-rm]==DrangeCB[0])[0][1]  
        if len(RrangeCB)!=0:
            smr=np.where(potential[rm-rm:rM-rm]==RrangeCB[1])[0][1]
            sMr=np.where(potential[rm-rm:rM-rm]==RrangeCB[0])[0][1]   
        else:
            smr=sm
            sMr=sM
        x_line=np.linspace(time[rm-rm:rM-rm][sm],time[rm-rm:rM-rm][sM],len(time[rm-rm:rM-rm][sm:sM])) #from where, to where, how many points
        y_line=np.linspace(milli*curr1[rm:rM][sm],milli*curr1[rm:rM][sM],len(milli*curr1[rm:rM][sm:sM]))
        x_line_RING=np.linspace(time[rm-rm:rM-rm][smr],time[rm-rm:rM-rm][sMr],len(time[rm-rm:rM-rm][smr:sMr])) #from where, to where, how many points
        y_line_RING=np.linspace(milli*curr2[rm:rM][smr],milli*curr2[rm:rM][sMr],len(milli*curr1[rm:rM][smr:sMr]))
        ring_disk.plot(x_line,y_line,color=colors[ranges.index(p)],alpha=1)
        ring_disk.plot(x_line_RING,y_line_RING,color=colori[ranges.index(p)],alpha=1)
        diskBc=np.trapz((curr1[rm:rM][sm:sM]-y_line/milli)*Ad,time[rm-rm:rM-rm][sm:sM]) #integration of the undercut peak DISK (multiplpied by area beacause curr and not curr dens)
        ringBc=np.trapz(curr2[rm:rM][smr:sMr]*Ar,time[rm-rm:rM-rm][smr:sMr]) #integration of the full area arounf the clear peak RING (multiplpied by area beacause curr and not curr dens)
       # print(diskAc,ringAc,diskBc,ringBc)
        ring_disk.fill_between(time[rm-rm:rM-rm][bm:bM],
                          milli*curr1[rm:rM][bm:bM],
                          color=colors[ranges.index(p)],alpha=0.5)
        ring_disk.fill_between(time[rm-rm:rM-rm][bmr:bMr],
                          milli*curr2[rm:rM][bmr:bMr],
                          color=colori[ranges.index(p)],alpha=0.5)



        ring_disk.fill_between(time[rm-rm:rM-rm][sm:sM],  ##area around the peak RING
                          milli*curr1[rm:rM][sm:sM],y_line,
                          color=colors[ranges.index(p)],alpha=1)
        ring_disk.fill_between(time[rm-rm:rM-rm-1][smr:sMr], ##area around the peak RING after OER-derived ORR current
                          milli*curr2[rm:rM-1][smr:sMr],y_line_RING,
                          color=colori[ranges.index(p)],alpha=1)

        #raa.append(np.abs(area/Fcos))
        #raas.append(sum(raa))
        #raap.append(((sum(raa))/(drop/pm[0][1]))*100)
        #raa1.append(np.abs((area2+area3)/Fcos))
        #raas1.append((sum(raa1)))
        #raap1.append(((sum(raa1))/(drop/pm[0][1]))*100)
        #


        print('--------------------------- Cycle '+str(p[3])+' ------------------------')
        print()

        print('¤¤¤¤¤¤ ANODIC peaks')  
        print()
        print('{0:35}  {1:35} {2:30}'.format("Int. mode:","A","B"))
        print('{0:35}  {1:35} {2:30}'.format("DISK (C)",str(diskA),str(diskB)))
        print('{0:35}  {1:35} {2:30}'.format("RING (C)",str(ringA),str(ringB)))
        print('{0:35}  {1:35} {2:30}'.format("DISK/RING ratio",str(abs(round(diskA/ringA,2))),str(abs(round(diskB/ringB,2)))))
        print()
        print('Considering a '+str(mechanism)+' electron process:')        
        print()
        for q in range(len(intrngA)): #DISK ELEMENTS
            print('Range '+str(q+1)+' : '+ str(intrng[q][0]))
            for key in atomic.keys():
                if key!=pt.O:
                    strkey=str(key) ## needs to be a string to be used in 'getattr'
                    print('{0:35}  {1:35} {2:30}'.format("DISK mol " + str(getattr(pt, strkey))+" (% of dep)",
                          str(round(abs((intA[q][0]/Fcos)/(atomic[getattr(pt, strkey)]*drop/massa)*100),1)),
                          str(round((abs(intB[q][0]/Fcos)/(atomic[getattr(pt, strkey)]*drop/massa)*100),1))))
                    key_val['A'][q]['DISK'][getattr(pt, strkey)].append(round(abs((intA[q][0]/Fcos)/(atomic[getattr(pt, strkey)]*drop/massa)*100),1))
                    syu=key_val['A'][q]['DISK'][getattr(pt, strkey)]
                    #print(syu)
                    key_sum['A'][q]['DISK'][getattr(pt, strkey)].append(sum(syu))
                    key_val['B'][q]['DISK'][getattr(pt, strkey)].append(round(abs((intB[q][0]/Fcos)/(atomic[getattr(pt, strkey)]*drop/massa)*100),1))
                    syu=key_val['B'][q]['DISK'][getattr(pt, strkey)]
                    key_sum['B'][q]['DISK'][getattr(pt, strkey)].append(sum(syu))
        print()

        for q in range(len(intrngA)): # RING ELEMENTS # it is looped over intA length only, but they are always the same
            print('Range '+str(q+1)+' : '+ str(intrng[q][0]))
            for key in atomic.keys():
                if key!=pt.O:
                    strkey=str(key) ## needs to be a string to be used in 'getattr'
                    print('{0:35}  {1:35} {2:30}'.format("RING mol " + str(getattr(pt, strkey))+" (% of dep)",
                          str(round(abs((intA[q][1]/Fcos)/(atomic[getattr(pt, strkey)]*drop/massa)*100),1)) ,
                          str(round(abs((intB[q][1]/Fcos)/(atomic[getattr(pt, strkey)]*drop/massa)*100),1))))
                    gf=round(abs((intA[q][1]/Fcos)/(atomic[getattr(pt, strkey)]*drop/massa)*100),1)
                    key_val['A'][q]['RING'][getattr(pt, strkey)].append(round(abs((intA[q][1]/Fcos)/(atomic[getattr(pt, strkey)]*drop/massa)*100),1))
                    syu=key_val['A'][q]['RING'][getattr(pt, strkey)]
                    key_sum['A'][q]['RING'][getattr(pt, strkey)].append(sum(syu))
                    key_val['B'][q]['RING'][getattr(pt, strkey)].append(round(abs((intB[q][1]/Fcos)/(atomic[getattr(pt, strkey)]*drop/massa)*100),1))
                    syu=key_val['B'][q]['RING'][getattr(pt, strkey)]
                    key_sum['B'][q]['RING'][getattr(pt, strkey)].append(sum(syu))
                    #print(syu)
                    #print('rrrrrrrrrrrrrr',key_sum)
                    #key_sum[getattr(pt, strkey)].append(sum(a))
                    #cumul['A'][q][1][getattr(pt, strkey)]=key_sum[q][getattr(pt, strkey)]
        print()
        print('¤¤¤¤¤¤ CATHODIC peaks') 
        print()
        print('{0:35}  {1:35} {2:30}'.format("Int. mode:","A","B"))
        print('{0:35}  {1:35} {2:30}'.format("DISK (C)",str(diskAc),str(diskBc)))
        print('{0:35}  {1:35} {2:30}'.format("RING (C)",str(ringAc),str(ringBc)))
        print('{0:35}  {1:35} {2:30}'.format("DISK/RING ratio",str(abs(round(diskAc/ringAc,2))),str(abs(round(diskBc/ringBc,2)))))
        print()
        print('Considering a '+str(mechanism)+' electron process:')        
        print()
        for key in atomic.keys():
            if key!=pt.O:
                key=str(key) ## needs to be a string to be used in 'getattr'
                print('{0:35}  {1:35} {2:30}'.format("DISK mol " + str(getattr(pt, key))+" (% of dep)",
                      str(round(abs((diskAc/Fcos)/(atomic[getattr(pt, key)]*drop/massa)*100),1)),
                      str(round((abs(diskBc/Fcos)/(atomic[getattr(pt, key)]*drop/massa)*100),1))))
        print()
        for key in atomic.keys():
            if key!=pt.O:
                key=str(key) ## needs to be a string to be used in 'getattr'
                print('{0:35}  {1:35} {2:30}'.format("RING mol " + str(getattr(pt, key))+" (% of dep)",
                      str(round(abs((ringAc/Fcos)/(atomic[getattr(pt, key)]*drop/massa)*100),1)),
                      str(round(abs((ringBc/Fcos)/(atomic[getattr(pt, key)]*drop/massa)*100),1))))
        print()                
        

    
    
        #print('DISK','i: ',area1,'ii: ',area5,'iii: ',diskB)
        #print('RING','i: ',ringA,'ii: ',ringB,'iii: ',area9)
        #print('DISK/RING',area1/ringA,area5/ringB,area6/area9)
        #mol_dep=2*drop/massa
        #print('deposited Cr (moles)', mol_dep,massa)
        #print('DISK mol (% of dep)',(area1/Fcos)/mol_dep*100,(area5/Fcos)/mol_dep*100,(area6/Fcos)/mol_dep*100)
        #print('RING mol (% of dep)',(ringA/Fcos)/mol_dep*100,(ringB/Fcos)/mol_dep*100,(area9/Fcos)/mol_dep*100)
        #daa.append((area1)/Fcos)
        #daas.append(sum(daa))
        #daap.append(((sum(daa))/(drop/pm[0][1]))*100)
        #ring_disk.text(20,2+0.5*sr,str(area1),color=colors[ranges.index(p)])
        #print(i,area)
    ring_disk.set_xlim(xMIN,xMAX)
    #zoom.set_ylim(min(milli*curr1[0:2999])+min(milli*curr1[0:2999])*0.05,0.05)
    #zoom.set_xlim(80,150)
    #zoom.set_xlabel('Time (s)')
    ring_disk.set_xlabel('Time (s)')
    ring_disk.set_ylabel('Current density  (mA cm$^{-2}$)')
    fig.suptitle('NiCr$_{2}$O$_4$', fontsize=35)
    fig.subplots_adjust(top=0.7)
    plt.tight_layout()
    d = {'cycles': np.arange(1,11,1) , 'test': 12, 'formula':formula, 'FW':massa,
         'mol_an': daa, 'mol_an_cum': daas, 
        'mol_cath1': raa, 'mol_cath1_cum': raas,
        'mol_cath2': raa1, 'mol_cath2_cum': raas1}
#fig.savefig('C:/M_drive_docs/Lab/RDE/chromates/mncu25.tif')
#ig.savefig('C:/M_drive_docs/Lab/RDE/chromates/nicro_ranges.tif')
    
fig,cumul=plt.subplots(figsize=(10,10))
cumul=plt.subplot(111)
cumul.plot(np.arange(1,len(key_sum['A'][0]['DISK'][pt.Cr])+1),key_sum['A'][0]['DISK'][pt.Cr], marker='o',label='Cr AD')
cumul.plot(np.arange(1,len(key_sum['B'][0]['DISK'][pt.Cr])+1),key_sum['B'][0]['DISK'][pt.Cr], marker='o',label='Cr BD')

cumul.plot(np.arange(1,len(key_sum['A'][0]['RING'][pt.Cr])+1),key_sum['A'][0]['RING'][pt.Cr], marker='o',label='Cr AR')
cumul.plot(np.arange(1,len(key_sum['B'][0]['RING'][pt.Cr])+1),key_sum['B'][0]['RING'][pt.Cr], marker='o',label='Cr BR')

cumul.set_ylim(0,20)
cumul.legend()

print(key_sum)









