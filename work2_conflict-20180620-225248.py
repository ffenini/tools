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
m = pt.formula(formula)  
massa=round(m.mass,3) #formula weight of the compound
drop=25*micro #grams of material deposited on the disk
print(drop)
Fcos=3*sp.constants.value('Faraday constant')


selector=[81,85,144,92]#[12,31,76,81,85,89,92]
label_book= ['MnCu25 GG \noldGC R=0.5 V', 'NiCr2 \n 0.5V','graphite\nblank', 'glassy carbon','MnCu25 GG \noldGC R=1.2 V', 'bare oldGCPt \n R=1.2 V', 'GG2 exch \n R=1.2 V', 'bare oldGCPt \n R=1.2 V', 'NiCr2 \n 1.2V']
ranges=cycplot(selector,cyc_plot=1)
das=[]#disk areas, for all the experiments
ras=[]#ring peak areas, for all the 
#fig,ring_disk=plt.subplots(figsize=(12 , 12))
fig,ring_disk=plt.subplots(figsize=(12 , 8))
colors=[]
for i in selector: 
    labz=label_book
    ring_disk=plt.subplot(111) #ring_disk=plt.subplot(gs[0:,1])
    
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
    colors.append(cm.inferno(int(0+si*255/(len(selector)))))##color map divided by the number of files
    for p in ranges:
        sr=ranges.index(p)
        
        colori.append(cm.autumn(int(0+sr*255/(len(ranges)))))##color map divided by the number of files
        cores.append(cm.winter(int(0+sr*255/(len(ranges)))))##color map divided by the number of files
        #colors.append(cm.tab20(si))  
        rm=p[0][si] #single plot range minimum
        rh=p[4][si]
      #  print('rh',rh)
      #  print('rm',rm)
      #  print(rh-rm)
        rM=p[1][si] #single plot range maximum
      #  print('rh',rh,'rm',rm,'rM',rM)
        Ar=dimen[i][1] # RING area
        ce=dimen[i][2] # collection efficiency
        Ad=dimen[i][0] # DISK area
        time=data[i]['Time/s'].values #time 
        if i==76:
            time=data[i]['Time/s'].values+16.05
        potential=0.658+data[i]['Potential/V'].values #potential vs SHE (V)
        try:
            datD=data[i]['i1/A'].values#-data[57]['i1/A'].values
            datR=data[i]['i2/A'].values#-data[57]['i2/A'].values
        except KeyError:
            datD=data[i]['Current/A'].values
            datR=0*data[i]['Current/A'].values
        curr2=10*datR/Ar/ce #current density RING (A cm-2)
        curr1=datD/Ad ##current density DISK (A cm-2) 
        milli=1000
        a=milli*curr2[rh+1:rM] # generating the cathodic branch mirroring for subtraction of the ring OER-dependent ORR current
        c=np.flipud(a)
        b=np.concatenate((c,a))
        d=milli*curr1[rh+1:rM]
        e=np.flipud(d)
        f=np.concatenate((e,d))  
        xMIN=0 #range
        xMAX=150 #range
        if i!=76:
            for u in np.arange(0,150,10):
                if u%2==0:
                    col='k'
                    linst='--'
                else:
                    col='k'
                    linst=':'
                lll=np.where(time[rm-rm:rM-rm]==u)[0][0]
                ring_disk.axvline(time[rm-rm:rM-rm][lll],ymin=-10,ymax=10,alpha=0.4,linestyle=linst,color=col)
                if time[rm-rm:rM-rm][lll]<xMAX and time[rm-rm:rM-rm][lll]>xMIN and p==ranges[0]:
                    ring_disk.text(time[rm-rm:rM-rm][lll],-0.75,str(round(potential[rm:rM][lll],3))+' V',color=col,alpha=0.75,fontsize=15)
        ring_disk.plot(time[rm-rm:rM-rm],milli*curr1[rm:rM],color=colors[selector.index(i)],label=label_book[si])
        #ring_disk.plot(time[rm-rm:rM-rm-1],milli*curr1[rm:rM-1]-f,color=colors[ranges.index(p)],linestyle='-.') ##sub
        ring_disk.plot(time[rm-rm:rM-rm],milli*curr2[rm:rM],color=colors[selector.index(i)],linestyle='--')
        #ring_disk.plot(time[rm-rm:rM-rm-1],milli*curr2[rm:rM-1]-b,color=colors[ranges.index(p)],linestyle=':') ##sub
        #poten=ring_disk.twinx()
        #potenz=zoom.twinx()
        #poten.plot(time[rm-rm:rM-rm],potential[rm:rM],color='r',linewidth=0.51,linestyle='--')
        #poten.plot(time[rm-rm:rM-rm],0.5+0*potential[rm:rM],color='b',linewidth=0.51,linestyle='--')
        #zoom.plot(time[rm-rm:rM-rm],milli*curr2[rm:rM]-0.2,color=colors[ranges.index(p)],linestyle='--')
        ### area determination
        am=np.where(time[rm-rm:rM-rm]==109)[0][0]# cathodic peals
        aM=np.where(time[rm-rm:rM-rm]==113)[0][0]
        area=np.trapz(curr1[rm:rM][am:aM]*Ad,time[rm-rm:rM-rm][am:aM])# orange cathodic multiplied by Ad because is current and not curr dens
        em=np.where(time[rm-rm:rM-rm]==100)[0][0]# cathodic peals
        eM=np.where(time[rm-rm:rM-rm]==109)[0][0]
        dm=np.where(time[rm-rm:rM-rm]==113)[0][0]# cathodic peals
        dM=np.where(time[rm-rm:rM-rm]==145)[0][0]
        #zoom.fill_between(time[rm-rm:rM-rm][em:eM],
                          #milli*curr1[rm:rM][em:eM],
                          #color=cores[ranges.index(p)],alpha=0.2)
       # zoom.fill_between(time[rm-rm:rM-rm][dm:dM],
                         # milli*curr1[rm:rM][dm:dM],
                         # color=cores[ranges.index(p)],alpha=0.2)
        area2=np.trapz(curr1[rm:rM][em:eM]*Ad,time[rm-rm:rM-rm][em:eM]) #blue cathodic
        area3=np.trapz(curr1[rm:rM][dm:dM]*Ad,time[rm-rm:rM-rm][dm:dM]) #blue cathodic
        raa.append(np.abs(area/Fcos))
        raas.append(sum(raa))
        raap.append(((sum(raa))/(drop/pm[0][1]))*100)
        raa1.append(np.abs((area2+area3)/Fcos))
        raas1.append((sum(raa1)))
        raap1.append(((sum(raa1))/(drop/pm[0][1]))*100)
        #zoom.text(100,-0.18+0.015*sr,str(area),color=colors[ranges.index(p)])
        bm=np.where(time[rm-rm:rM-rm]==35)[0][0]
        bM=np.where(time[rm-rm:rM-rm]==75)[0][0]
        #ring_disk.fill_between(time[rm-rm:rM-rm][bm:bM],
        #                  milli*curr1[rm:rM][bm:bM],
        #                  color=colors[ranges.index(p)],alpha=0.2)
        #ring_disk.fill_between(time[rm-rm:rM-rm][bm:bM],
        #                  milli*curr2[rm:rM][bm:bM],
        #                  color=colors[ranges.index(p)],alpha=0.2)
        sm=np.where(time[rm-rm:rM-rm]==40)[0][0]
        sM=np.where(time[rm-rm:rM-rm]==63)[0][0]
        print(len(time[rm-rm:rM-rm][sm:sM]))
        #ring_disk.fill_between(time[rm-rm:rM-rm][sm:sM], #full area arounf the clear peak DISK
        #                  milli*curr1[rm:rM][sm:sM],
        #                  color=colors[ranges.index(p)],alpha=0.5)
        #ring_disk.fill_between(time[rm-rm:rM-rm][sm:sM], #full area arounf the clear peak RING
        #                  milli*curr2[rm:rM][sm:sM],
        #                  color=colors[ranges.index(p)],alpha=0.5)
        x_line=np.linspace(time[rm-rm:rM-rm][sm],time[rm-rm:rM-rm][sM],len(time[rm-rm:rM-rm][sm:sM]))
        y_line=np.linspace(milli*curr1[rm:rM][sm],milli*curr1[rm:rM][sM],len(milli*curr1[rm:rM][sm:sM]))
        y_line_RING=np.linspace(milli*curr2[rm:rM][sm],milli*curr2[rm:rM][sM],len(milli*curr1[rm:rM][sm:sM]))
       # ring_disk.plot(x_line,y_line,color=colors[ranges.index(p)],alpha=1)
       # ring_disk.plot(x_line,y_line_RING,color=colors[ranges.index(p)],alpha=1)
        #ring_disk.fill_between(time[rm-rm:rM-rm][sm:sM],  ##area around the peak RING
        #                  milli*curr1[rm:rM][sm:sM],y_line,
        #                  color=colors[ranges.index(p)],alpha=1)
        #ring_disk.fill_between(time[rm-rm:rM-rm-1][sm:sM], ##area around the peak RING after OER-derived ORR current
        #                  milli*curr2[rm:rM-1][sm:sM]-b[sm:sM],
        #                  color=colors[ranges.index(p)],alpha=1)
        ## the integration is performed on current and not millicurrent
        area1=np.trapz(curr1[rm:rM][bm:bM]*Ad,time[rm-rm:rM-rm][bm:bM]) #integration of the whole range DISK (multiplpied by area beacause curr and not curr dens)
        area5=np.trapz(curr1[rm:rM][sm:sM]*Ad,time[rm-rm:rM-rm][sm:sM]) #integration of the full area arounf the clear peak DISK (multiplpied by area beacause curr and not curr dens)
        area6=np.trapz((curr1[rm:rM][sm:sM]-y_line/milli)*Ad,time[rm-rm:rM-rm][sm:sM]) #integration of the undercut peak DISK (multiplpied by area beacause curr and not curr dens)
        area7=np.trapz((curr2[rm:rM])[bm:bM]*Ar,time[rm-rm:rM-rm][bm:bM],axis=-1) #integration of the whole range RING (multiplpied by area beacause curr and not curr dens)
        area8=np.trapz(curr2[rm:rM][sm:sM]*Ar,time[rm-rm:rM-rm][sm:sM]) #integration of the full area arounf the clear peak RING (multiplpied by area beacause curr and not curr dens)
        area9=np.trapz((curr2[rm:rM-1]-b/milli)[sm:sM]*Ar,time[rm-rm:rM-rm-1][sm:sM],axis=-1) #integration of the undercut peak RING, after OER subtraction (multiplpied by area beacause curr and not curr dens)
        #ring_disk.plot(time[rm-rm:rM-rm],milli*curr2[rm:rM],color=colors[ranges.index(p)],linestyle='--')
       # ring_disk.plot(time[rm-rm:rM-rm-1],milli*curr2[rm:rM-1]-b,color=colors[ranges.index(p)],linestyle=':') ##       
        print('DISK','i: ',area1,'ii: ',area5,'iii: ',area6)
        print('RING','i: ',area7,'ii: ',area8,'iii: ',area9)
        print('DISK/RING',area1/area7,area5/area8,area6/area9)
        mol_dep=2*drop/massa
        print('deposited Cr (moles)', mol_dep,massa)
        print('DISK mol (% of dep)',(area1/Fcos)/mol_dep*100,(area5/Fcos)/mol_dep*100,(area6/Fcos)/mol_dep*100)
        print('RING mol (% of dep)',(area7/Fcos)/mol_dep*100,(area8/Fcos)/mol_dep*100,(area9/Fcos)/mol_dep*100)
        daa.append((area1)/Fcos)
        daas.append(sum(daa))
        daap.append(((sum(daa))/(drop/pm[0][1]))*100)
        #ring_disk.text(20,2+0.5*sr,str(area1),color=colors[ranges.index(p)])
        #print(i,area)
    ring_disk.set_xlim(xMIN,xMAX)
    #zoom.set_ylim(min(milli*curr1[0:2999])+min(milli*curr1[0:2999])*0.05,0.05)
    #zoom.set_xlim(80,150)
    #zoom.set_xlabel('Time (s)')
    ring_disk.set_xlabel('Time (s)')
    ring_disk.set_ylabel('Current density  (mA cm$^{-2}$)')
    ring_disk.legend()
    #fig.suptitle('NiCr$_{2}$O$_4$', fontsize=35)
    fig.subplots_adjust(top=0.7)
    plt.tight_layout()
    d = {'cycles': np.arange(1,11,1) , 'test': 12, 'formula':formula, 'FW':massa,
         'mol_an': daa, 'mol_an_cum': daas, 
        'mol_cath1': raa, 'mol_cath1_cum': raas,
        'mol_cath2': raa1, 'mol_cath2_cum': raas1}
fig.savefig('C:/M_drive_docs/Lab/RDE/chromates/12V.tif')
#fig.savefig('C:/M_drive_docs/Lab/RDE/chromates/nicro_ranges.tif')
