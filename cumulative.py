selector=[12,97]#[12,31,76,81,85,89,92]
label_book= ['MnCu25 GG \noldGC R=0.5 V', 'NiCr2 \n 0.5V', 'MnCu25 GG \noldGC R=1.2 V', 'bare oldGCPt \n R=1.2 V', 'GG2 exch \n R=1.2 V', 'bare oldGCPt \n R=1.2 V', 'NiCr2 \n 1.2V']
ranges=cycplot(selector,cyc_plot=1)
das=[]#disk areas, for all the experiments
ras=[]#ring peak areas, for all the 
for i in selector: 
    fig,(ring_disk,zoom,poten)=plt.subplots(1,3, figsize=(15,5))
    labz=label_book
    ring_disk=plt.subplot(121) #ring_disk=plt.subplot(gs[0:,1])
    zoom=plt.subplot(122)
    colors=[]
    si=selector.index(i) 
    #print(infor[i])
    da=[] #single experiments anodic disk peak area, 
            #it is saved as a tuple of a list(area per cycle) and  a tuple with the integration limits
    ra=[] # the same for cathodic peaks
    raa=[] #single areas
    daa=[] 
    raas=[] #cumulative areas
    daas=[]
    for p in ranges:
        sr=ranges.index(p)
        colors.append(cm.viridis(int(0+sr*255/(len(ranges)))))##color map divided by the number of files
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
        potential=0.658+data[i]['Potential/V'].values #potential vs SHE (V)
        try:
            datD=data[i]['i1/A'].values#-data[57]['i1/A'].values
            datR=data[i]['i2/A'].values#-data[57]['i2/A'].values
        except KeyError:
            datD=data[i]['Current/A'].values
            datR=0*data[i]['Current/A'].values
        curr2=datR/Ar/ce #current density RING (A cm-2)
        curr1=datD/Ad ##current density DISK (A cm-2) 
        milli=1000
        a=milli*curr2[rh+1:rM]
        c=np.flipud(a)
        b=np.concatenate((c,a))
        d=milli*curr1[rh+1:rM]
        e=np.flipud(d)
        f=np.concatenate((e,d))        
        ring_disk.plot(potential[rm-rm:rM-rm],milli*curr1[rm:rM],color=colors[ranges.index(p)])
        #ring_disk.plot(time[rm-rm:rM-rm-1],milli*curr1[rm:rM-1]-f,color=colors[ranges.index(p)],linestyle='-.') ##sub
        #ring_disk.plot(time[rm-rm:rM-rm],milli*curr2[rm:rM],color=colors[ranges.index(p)],linestyle='--')
        #ring_disk.plot(potential[rm-rm:rM-rm],milli*data[57]['i1/A'].values[rm-rm:rM-rm]/Ad,color=colors[ranges.index(p)]) #baseline
        #ring_disk.plot(time[rm-rm:rM-rm-1],milli*curr2[rm:rM-1]-b,color=colors[ranges.index(p)],linestyle=':') ##sub
        z=time[rm-rm:rh-rm]
        curr_fit=(np.exp(-3.02286024*3.4)*np.exp(3.2*z*0.04944584))
        #ring_disk.plot(potential[rm-rm:rh-rm],curr_fit,linestyle='--',color=colors[ranges.index(p)])
        poten=ring_disk.twinx()
        potenz=zoom.twinx()
        #poten.plot(time[rm-rm:rM-rm],potential[rm:rM],color='r',linewidth=0.51,linestyle='--')
        #poten.plot(time[rm-rm:rM-rm],0.5+0*potential[rm:rM],color='b',linewidth=0.51,linestyle='--')
        #zoom.plot(time[rm-rm:rM-rm],milli*curr1[rm:rM],color=colors[ranges.index(p)])
        #zoom.plot(time[rm-rm:rM-rm],milli*curr2[rm:rM]-0.2,color=colors[ranges.index(p)],linestyle='--')
        ### area determination
        Fcos=sp.constants.value('Faraday constant')
        am=np.where(time[rm-rm:rM-rm]==105)[0][0]# cathodic peals
        aM=np.where(time[rm-rm:rM-rm]==140)[0][0]
        zoom.fill_between(potential[rm-rm:rM-rm][am:aM],
                          milli*curr1[rm:rM][am:aM],
                          color=colors[ranges.index(p)],alpha=0.05)     
        area=np.trapz(curr1[rm:rM][am:aM],time[rm-rm:rM-rm][am:aM])
        raa.append(area/Fcos)
        raas.append(sum(raa))
        #zoom.text(100,-0.18+0.015*sr,str(area),color=colors[ranges.index(p)])
        bm=np.where(time[rm-rm:rM-rm]==40)[0][0]
        bM=np.where(time[rm-rm:rM-rm]==75)[0][0]
        #print(am,aM)
        ring_disk.fill_between(potential[rm-rm:rh-rm],#[bm:bM],
                               milli*curr1[rm-rm:rh-rm],milli*data[57]['i1/A'].values[rm-rm:rh-rm]/Ad,alpha=0.1)
        #ring_disk.fill_between(potential[rm-rm:rh-rm],#[bm:bM],
                             #  milli*curr1[rm-rm:rh-rm],curr_fit,alpha=0.1)
                          #milli*curr1[rm:rM][bm:bM],#hatch='o*|||---////-',
                          #color=colors[ranges.index(p)],alpha=0.05)
        area1=np.trapz(curr1[rm:rM][bm:bM],time[rm-rm:rM-rm][bm:bM])
        daa.append(area1/Fcos)
        daas.append(sum(daa))
        #ring_disk.text(20,2+0.5*sr,str(area1),color=colors[ranges.index(p)])
        #print(i,area)
    ra.append(raa)#create the list for te´he single element in selcter with the list of peak areas and the integration limits
    ra.append(raas)
    ra.append((time[rm-rm:rM-rm][am],time[rm-rm:rM-rm][aM]))
    ra.append(i)
    da.append(daa)
    da.append(daas)
    da.append((time[rm-rm:rM-rm][bm],time[rm-rm:rM-rm][bM]))
    da.append(i)
   # potenz.plot(time[rm-rm:rM-rm],potential[rm:rM],color='r',linewidth=0.51,linestyle='--')
    #potenz.plot(time[rm-rm:rM-rm],0.5+0*potential[rm:rM],color='b',linewidth=0.51,linestyle='--')
  # ring.plot(potential[rm:rM],1000*curr2[rm:rM],color=colors[ranges.index(p)])
  # zoomR.plot(potential[rm:rM],1000*curr2[rm:rM],color=colors[ranges.index(p)])
    #[ 0.04944584 -3.02286024]

    ring_disk.set_xlim(0.5,2.5)
    zoom.set_ylim(min(milli*curr1[0:2999])+min(milli*curr1[0:2999])*0.05,0.05)
    ring_disk.set_xlabel('Potential vs SHE')
    ring_disk.set_ylabel('Current density')
    #ring_disk.set_ylim(-0.5,2)
    zoom.set_xlim(80,150)
    zoom.set_title(infor[i][3])
    #ring_disk.set_title(infor[i][3])
    plt.tight_layout()
    ras.append(ra)
    das.append(da)
    fig.savefig('C:/M_drive_docs/Lab/RDE/chromates/baselinenake'+str(i)+'.tif')