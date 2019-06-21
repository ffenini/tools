from data_importer import *
selector=[12,97,57]#[12,31,76,81,85,89,92]
label_book= ['MnCu25 GG \noldGC R=0.5 V', 'NiCr2 \n 0.5V', 'MnCu25 GG \noldGC R=1.2 V', 'bare oldGCPt \n R=1.2 V', 'GG2 exch \n R=1.2 V', 'bare oldGCPt \n R=1.2 V', 'NiCr2 \n 1.2V']
ranges=cycplot(selector,cyc_plot=1)
i=97
fig,(ring_disk,zoom,poten)=plt.subplots(1,3, figsize=(25,20))
labz=label_book
ring_disk=plt.subplot(221) #ring_disk=plt.subplot(gs[0:,1])
zoom=plt.subplot(222)
powe=plt.subplot(223)
expo=plt.subplot(224)
colors=[]
si=selector.index(i) 
#print(infor[i])
for p in ranges:
    sr=ranges.index(p)
    colors.append(cm.copper(int(0+sr*255/(len(ranges)))))##color map divided by the number of files
    #colors.append(cm.tab20(si))  
    rm=p[0][si] #single plot range minimum
    rh=p[4][si]
    rM=p[1][si] #single plot range maximum
    Ar=dimen[i][1] # RING area
    ce=dimen[i][2] # collection efficiency
    Ad=dimen[i][0] # DISK area
    time=data[i]['Time/s'].values #time 
    potential=0.658+data[i]['Potential/V'].values #potential vs SHE (V)
    try:
        datD=data[i]['i1/A'].values
        datR=data[i]['i2/A'].values
    except KeyError:
        datD=data[i]['Current/A'].values
        datR=0*data[i]['Current/A'].values
    curr2=(datR/ce)/Ar #current density RING (A cm-2)
    curr1=datD/Ad ##current density DISK (A cm-2) 
    milli=1000
    #generating the miirrored cathodic branch of the ring current
    a=milli*curr2[rh+1+8:rM+8]
    c=np.flipud(a)
    b=np.concatenate((c,a))
    d=milli*curr2[rh+1:rM]
    e=np.flipud(d)
    f=np.concatenate((e,d))        
    ring_disk.plot(time[rm-rm:rM-rm],milli*curr1[rm:rM],color=colors[ranges.index(p)], label='disk')
    zoom.plot(time[rm-rm:rM-rm],milli*curr1[rm:rM],color=colors[ranges.index(p)], marker='v',label='disk')
    #ring_disk.plot(time[rm-rm:rM-rm-1],milli*curr1[rm:rM-1]-f,color=colors[ranges.index(p)],linestyle='-.') ##sub
    ring_disk.plot(time[rm-rm:rM-rm],milli*curr2[rm:rM],color=colors[ranges.index(p)],linestyle='--', label='ring current x 10')
    ring_disk.plot(time[rm-rm:rM-rm-1],milli*curr2[rm:rM-1]-f,color=colors[ranges.index(p)],linestyle=':', label='cathodic branch\n subtracted x 10') ##sub
    #poten=ring_disk.twinx()
    ring_disk.plot(time[rm-rm:rM-rm-1],-b,label='- mirrored \n cathodic branch ring \n current')
    zoom.plot(time[rm-rm:rM-rm-1],-b,marker='v',label='- mirrored \n cathodic branch ring \n current x17')
    cinqan=np.where(time[rm-rm:rM-rm-1]==75)[0][0]
    ci=np.where(time[rm-rm:rM-rm-1]==95)[0][0]
    print(cinqan,ci)
    ring_disk.plot(time[rm:rM-1][1500:1900],10*milli*curr2[rm:rM-1][1500+rm:1900+rm],linestyle='-',
                   color='r',label='- portion used to fit the exponential')
    #poten.plot(time[rm-rm:rM-rm],potential[rm:rM],color='r',linewidth=0.51,linestyle='--')
    #poten.plot(time[rm-rm:rM-rm],0.5+0*potential[rm:rM],color='b',linewidth=0.51,linestyle='--')
    #ring_disk.set_xlim(0,80)
    #ring_disk.set_ylim(0,6)
    ring_disk.set_title(infor[i][3])
    ring_disk.legend(fontsize=15)
    zoom.set_xlim(0,75)
    zoom.set_ylim(0,3.5)
    zoom.legend(fontsize=15)
    plt.tight_layout()
    c=np.flipud(a)
    #b=np.concatenate((c,a))
    z=time[rm-rm:rh-rm]
    logx = np.log10(z)
    logc = np.log10(-c)
    loga = np.log10(-a)
    powe.plot(z,logc,label='logc')
    powe.plot(z,loga,label='loga')
    potenzi=powe.twinx()
    potenzi.plot(z,potential[rm-rm:rh-rm])
    intersection=55
    powe.plot(z[np.where(z==intersection)],logc[np.where(z==intersection)],marker='o',markersize=20) ##dot np.where is to locate the index of a value
    limit=np.where(z==intersection)[0][0]
    fit=np.polyfit(z[limit:],logc[limit:],1)
    fit_fn = np.poly1d(fit)
    print(fit)
    powe.plot(z[limit:],fit_fn(z[limit:]))
    curr_fit=(np.exp(fit[1]*3.4)*np.exp(3.2*z*fit[0]))
    OER=np.flipud(-curr_fit)
    expo.plot(z,-c)
    expo.plot(z,curr_fit)
    expo.set_ylim(top=max(-c))
    ring_disk.plot(time[rh:rM-1],OER,linestyle='-',
                   color='g',label='- exponential fitting')
    ring_disk.fill_between(time[rm:rh],milli*curr1[rm:rh],curr_fit)
    #ring_disk.plot(time[rm:rh],milli*curr1[rm:rh]-curr_fit,color='b', label='exponential subts')
    powe.legend()
