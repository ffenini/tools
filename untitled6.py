with open('C:/M_drive_docs/JUPYTER/NOTE_BOOKS/tools/myfile.py','w+') as mf:
    mf.write('"""This file is changed anytime the cell is executed for different NOTEBOOKS\n')
    mf.write('The file tells the data_importer which folders upload"""\n')
    mf.write("NOTEBOOKname='RRDE-180618_NiCr2-MnCu025_5mVsec' # Name of the NOTEBOOK, used for creating\n") 
    mf.write("folders=['180407','180404','180405','180407','180412','180414','180415',\n")
    mf.write("         '180417','180424','180503','171107/activ/','180615','180616','180618',\n")
    mf.write("        '171030/LTE','171115/lt2e','180308','180318','180315','180316','180321','180721','180303'] #folders to be imported in the NOTEBOOK\n")
mf.close()



from data_importer import *
summary=False
if summary:
    with pd.option_context('display.max_rows', None, 'display.max_columns', None,'display.max_colwidth',300,'display.expand_frame_repr',False,'display.colheader_justify','left'):
        #print(tre[tre["Folder"] == "180315"])
        print(tre[tre["Folder"] == "180303"])
hsize_thesis=cm2inch(14)

vsize_thesis=(1.42*hsize_thesis)/1.5
plt.rcParams['axes.linewidth'] = 0.07*hsize_thesis
plt.rcParams['ytick.labelsize'] = hsize_thesis*1
plt.rcParams['ytick.major.width'] = 0.07*hsize_thesis
plt.rcParams['ytick.major.size'] = 0.35*hsize_thesis
plt.rcParams['ytick.minor.width'] = 0.07*hsize_thesis
plt.rcParams['ytick.minor.size'] = 0.18*hsize_thesis
plt.rcParams['xtick.labelsize'] = hsize_thesis*1
plt.rcParams['xtick.major.width'] = 0.07*hsize_thesis
plt.rcParams['xtick.major.size'] = 0.35*hsize_thesis
plt.rcParams['xtick.minor.width'] = 0.07*hsize_thesis
plt.rcParams['xtick.minor.size'] = 0.18*hsize_thesis
plt.rcParams['axes.labelsize'] =1.15*hsize_thesis
plt.rcParams['axes.labelpad'] =0.1*hsize_thesis

figuresize=hsize_thesis,vsize_thesis
print()
print('FIGURE SIZE: ',figuresize[0],' x ',figuresize[1],'in')
print()


data_book=[245,169] ##data to plot
label_book=['1:1 ceramic/graphite ink',  'ceramic only','graphite blank ',
            'bare oldGCPt ']
selector=data_book
cycleexp=[10,20,5,5,30] #how many cycles per experiment,following the order of 'selector'
    ### this ranges are made when experimetns with different potential ranges are compared
    ## the same number of cycles is required

    ########peaks from peak analysis
disk_peaks=[]
ring_peaks=[]
shoulder_min=870
shoulder_max=870
ranges=[]

for i in range(1): ####define how many cycles to plot 
    a=[]
    b=[]
    for t in selector:
        ti=selector.index(t)
        aa=int(len(data[t])/cycleexp[ti])*i
        bb=aa+int(len(data[t])/cycleexp[ti])
        a.append(aa)
        b.append(bb)
    d=str(i+1)+'th'
    if i==0:
        d=str(i+1)+'st'
    if i==1:
        d=str(i+1)+'nd'
    if i==2:
        d=str(i+1)+'rd'
    c=(a,b,d)
    ranges.append(c)
print(ranges)
wspacing=np.full((1, 12), 1, dtype=int).tolist()
fig,(ring_disk,zoom)=plt.subplots(1,2, figsize=(figuresize))
gs = gridspec.GridSpec(3, 13,
                       width_ratios=[1,1,1,1,1,1,1,1,1,1,1,1,1],
                       height_ratios=[1,1,1.5],wspace=1.05,hspace=0.35
                       )
ring_disk=plt.subplot(gs[0,1:6]) #ring_disk=plt.subplot(gs[0:,1])
zoom=plt.subplot(gs[0,7:12])
nogr=plt.subplot(gs[1,1:6]) #ring_disk=plt.subplot(gs[0:,1])
grgr=plt.subplot(gs[1,7:12])
assia=plt.subplot(gs[2,2:11])
for p in ranges:
    labz=label_book
 ##### identifies the 
    colors=[]
    #interval=rng_min[selector.index(i)]rng_max[selector.index(i)]
    for i in selector:        
        si=selector.index(i)
        rng_min=p[0][si]
        rng_max=p[1][si]
        time=data[i]['Time/s'].values[rng_min:rng_max] #time 
        potential=data[i]['Potential/V'].values[rng_min:rng_max]+0.658 #potential vs SHE (V)
        try:
            curr2=data[i]['i2/A'].values[rng_min:rng_max] #current  DISK (A )
        except KeyError:    
            pass
        try:
            curr1=data[i]['i1/A'].values[rng_min:rng_max] ##current  RING (A )
        except KeyError:
            curr1=data[i]['Current/A'].values[rng_min:rng_max] #current  (A )
        Ar=dimen[i][1] # RING area
        ce=dimen[i][2] # collection efficiency
        Ad=dimen[i][0] # DISK area
        #colors.append(cm.tab20(si))
        colors.append(cm.viridis(int(50+si*255/(len(selector)))))##color map divided by the number of files   
        farve=colors[si]
        labs=['DISK','RING (raw data)','RING (collection   '+'\n'+'efficiency considered)']
        if True:  ##this loop is here in orfer 
            marco='-'
            if i==85:
                marco='--'
            try:
                ring_disk.plot(potential,1000*curr1/Ad,linestyle=marco,color=farve,linewidth=0.12*hsize_thesis,label=labz[si]) #,color = colors[si] 
                for h in disk_peaks:
                    ring_disk.plot(potential[h],1000*curr1[h]/Ad,marker='o', markersize=10, color='r')
                for t in ring_peaks:
                    ring_disk.plot(potential[t],1000*curr1[t]/Ad,marker='+',mew=5, markersize=20, color='b')
                #ring_disk.plot(data[i]['Potential/V'].values[shoulder_min:shoulder_max]+0.658, 
                        # 1000*data[i]['i1/A'].values[shoulder_min:shoulder_max]/Ad, 
                         #color = 'g', linewidth=4,
                        #label=labz[si]) 
            except KeyError: ###in case column i2/A does not exist (RDE instead of RRDE)
                ring_disk.plot(potential,1000*curr/Ad,color = colors[si],label=labz[si])

        #print('data'+str(i)+' '+str(disk))
        #ring_disk.set_title('RRDE EXPERIMENT '+p[2]+' Cycle',fontsize=20)
        ring_disk.set_ylabel('Current density (mA cm$^{-2}$)')
        ring_disk.set_xlabel('Disk Potential vs SHE (V)')
        ring_disk.set_facecolor('white')
       # ring_disk.set_xlim( 0.48,2 ) 
        #ring_disk.set_ylim(-3,13) 
        ring_disk.legend(loc=0,fontsize=0.99*hsize_thesis, frameon=False) # bbox_to_anchor=(0.56, 0.75),


#################  CATHODIC peaks zoom        
        labs=['DISK','RING (raw data)']
        if True:  ##this loop is here in orfer
            
            try:
                zoom.plot(potential,1000*curr1/Ad,linestyle=marco,color=farve,linewidth=0.12*hsize_thesis,label='k')                
               # zoom.plot(potential,1000*curr2/Ar, linestyle=':',color = colors[si], label='k')
                for h in disk_peaks:
                    zoom.plot(potential[h]+0.658,1000*curr1[h]/Ad,marker='o', color='r',markersize=10)
                for t in ring_peaks:
                    zoom.plot(potential[t]+0.658,1000*curr1[t]/Ad,marker='+',mew=5, markersize=20,color='b')
                zoom.plot(data[i]['Potential/V'].values[shoulder_min:shoulder_max]+0.658, 
                         1000*data[i]['i1/A'].values[shoulder_min:shoulder_max]/Ad,color='g',linewidth=5,label=labz[si]) 
                for h in disk_peaks:
                    zoom.plot(potential[h],1000*curr2[h]/Ar,marker='o', markersize=10, color='r')
                for t in ring_peaks:
                    zoom.plot(potential[t]+0.658,1000*curr2[t]/Ar,marker='+',mew=5, markersize=20, color='b')
                zoom.plot(data[i]['Potential/V'].values[shoulder_min:shoulder_max]+0.658, 
                         1000*data[i]['i2/A'].values[shoulder_min:shoulder_max]/Ar,color='g',linewidth=4,label=labz[si]) 
            except KeyError: ###in case column i2/A does not exist (RDE instead of RRDE)
                zoom.plot(potential,1000*curr1/Ad,linewidth=0.12*hsize_thesis,color = farve,label=labz[si])
        #zoom.set_title('CV - cathodic peaks',fontsize=20)

        #zoom.set_yscale('symlog')
        #zoom.legend(labs,loc=0, fontsize=18)        
        #ring.set_yscale('log')
 
## FIGURE C
data_book=[254,165,167,169,171] ##data to plot
label_book=['127 µg cm$^{-2}$','255 µg cm$^{-2}$','382 µg cm$^{-2}$','510 µg cm$^{-2}$','637 µg cm$^{-2}$',]
selector=data_book
cycleexp=[20,20,20,20,20,5,5,5,5] #how many cycles per experiment,following the order of 'selector'
    ### this ranges are made when experimetns with different potential ranges are compared
    ## the same number of cycles is required
    ########peaks from peak analysis
disk_peaks=[]
ring_peaks=[]
shoulder_min=870
shoulder_max=870
ranges=[]

for i in range(1): ####define how many cycles to plot 
    a=[]
    b=[]
    for t in selector:
        ti=selector.index(t)
        aa=int(len(data[t])/cycleexp[ti])*i
        bb=aa+int(len(data[t])/cycleexp[ti])
        a.append(aa)
        b.append(bb)
    d=str(i+1)+'th'
    if i==0:
        d=str(i+1)+'st'
    if i==1:
        d=str(i+1)+'nd'
    if i==2:
        d=str(i+1)+'rd'
    c=(a,b,d)
    ranges.append(c)
print(ranges)
wspacing=np.full((1, 12), 1, dtype=int).tolist()
for p in ranges:
    plot_size=1/3*1.5
    labz=label_book
 ##### identifies the 
    w=255
    colors=[(0/w,128/w,255/w),(255/w,128/w,0/w),(0/w,255/w,0/w),(255/w,51/w,51/w),(0/w,0/w,204/w)]
    #interval=rng_min[selector.index(i)]rng_max[selector.index(i)]
    for i in selector:        
        si=selector.index(i)
        rng_min=p[0][si]
        rng_max=p[1][si]
        time=data[i]['Time/s'].values[rng_min:rng_max] #time 
        potential=data[i]['Potential/V'].values[rng_min:rng_max]+0.658 #potential vs SHE (V)
        try:
            curr2=data[i]['i2/A'].values[rng_min:rng_max] #current  DISK (A )
        except KeyError:    
            pass
        try:
            curr1=data[i]['i1/A'].values[rng_min:rng_max] ##current  RING (A )
        except KeyError:
            curr1=data[i]['Current/A'].values[rng_min:rng_max] #current  (A )
        Ar=dimen[i][1] # RING area
        ce=dimen[i][2] # collection efficiency
        Ad=dimen[i][0] # DISK area
        #colors.append(cm.tab20(si))
        #colors.append(cm.inferno(int(80*si)))##color map divided by the number of files   
        farve=colors[si]
        labs=['DISK','RING (raw data)','RING (collection   '+'\n'+'efficiency considered)']
        if True:  ##this loop is here in orfer 
            marco='-'
            if i==85:
                marco='--'
            try:
                nogr.plot(potential,1000*curr1/Ad,linestyle=marco,color=farve,linewidth=0.12*hsize_thesis,label=labz[si]) #,color = colors[si] 
                for h in disk_peaks:
                    nogr.plot(potential[h],1000*curr1[h]/Ad,marker='o', markersize=10, color='r')
                for t in ring_peaks:
                    nogr.plot(potential[t],1000*curr1[t]/Ad,marker='+',mew=5, markersize=20, color='b')
                #nogr.plot(data[i]['Potential/V'].values[shoulder_min:shoulder_max]+0.658, 
                        # 1000*data[i]['i1/A'].values[shoulder_min:shoulder_max]/Ad, 
                         #color = 'g', linewidth=4,
                        #label=labz[si]) 
            except KeyError: ###in case column i2/A does not exist (RDE instead of RRDE)
                nogr.plot(potential,1000*curr/Ad,color = colors[si],linewidth=0.12*hsize_thesis,label=labz[si])

        #print('data'+str(i)+' '+str(disk))
        #nogr.set_title('RRDE EXPERIMENT '+p[2]+' Cycle',fontsize=20)
        nogr.set_ylabel('Current density\n(mA cm$^{-2}$)')
        nogr.set_xlabel('Disk Potential vs SHE (V)')
        nogr.set_facecolor('white')
       # nogr.set_xlim( 0.48,2 ) 
        #nogr.set_ylim(-3,13) 
        nogr.legend(bbox_to_anchor=(0.55,0.15),fontsize=0.8*hsize_thesis, frameon=False,title='ceramic loading:') # bbox_to_anchor=(0.56, 0.75),
        nogr.get_legend().get_title().set_fontsize(hsize_thesis*1)
        nogr.text(0.05,0.9,'ceramic ink',transform=nogr.transAxes,fontsize=hsize_thesis*1.4,horizontalalignment='left')
       
## FIGURE D
data_book=[245,249] ##data to plot
label_book=['127 µg cm$^{-2}$','255 µg cm$^{-2}$',]
selector=data_book
cycleexp=[10,5,5,5,5] #how many cycles per experiment,following the order of 'selector'
    ### this ranges are made when experimetns with different potential ranges are compared
    ## the same number of cycles is required
    ########peaks from peak analysis
disk_peaks=[]
ring_peaks=[]
shoulder_min=870
shoulder_max=870
ranges=[]

for i in range(1): ####define how many cycles to plot 
    a=[]
    b=[]
    for t in selector:
        ti=selector.index(t)
        aa=int(len(data[t])/cycleexp[ti])*i
        bb=aa+int(len(data[t])/cycleexp[ti])
        a.append(aa)
        b.append(bb)
    d=str(i+1)+'th'
    if i==0:
        d=str(i+1)+'st'
    if i==1:
        d=str(i+1)+'nd'
    if i==2:
        d=str(i+1)+'rd'
    c=(a,b,d)
    ranges.append(c)
print(ranges)
wspacing=np.full((1, 12), 1, dtype=int).tolist()
for p in ranges:
    plot_size=1/3*1.5
    labz=label_book
 ##### identifies the 
    w=255
    colors=[(0/w,128/w,255/w),(255/w,128/w,0/w),(0/w,255/w,0/w),(0/w,204/w,102/w),(0/w,102/w,51/w)]
    #interval=rng_min[selector.index(i)]rng_max[selector.index(i)]
    for i in selector:        
        si=selector.index(i)
        rng_min=p[0][si]
        rng_max=p[1][si]
        time=data[i]['Time/s'].values[rng_min:rng_max] #time 
        potential=data[i]['Potential/V'].values[rng_min:rng_max]+0.658 #potential vs SHE (V)
        try:
            curr2=data[i]['i2/A'].values[rng_min:rng_max] #current  DISK (A )
        except KeyError:    
            pass
        try:
            curr1=data[i]['i1/A'].values[rng_min:rng_max] ##current  RING (A )
        except KeyError:
            curr1=data[i]['Current/A'].values[rng_min:rng_max] #current  (A )
        Ar=dimen[i][1] # RING area
        ce=dimen[i][2] # collection efficiency
        Ad=dimen[i][0] # DISK area
        #colors.append(cm.tab20(si))
        #colors.append(cm.viridis(int(35*si+255/(6))))##color map divided by the number of files   
        farve=colors[si]
        labs=['DISK','RING (raw data)','RING (collection   '+'\n'+'efficiency considered)']
        if True:  ##this loop is here in orfer 
            marco='-'
            if i==85:
                marco='--'
            try:
                grgr.plot(potential,1000*curr1/Ad,linestyle=marco,color=farve,linewidth=0.12*hsize_thesis,label=labz[si]) #,color = colors[si] 
                for h in disk_peaks:
                    grgr.plot(potential[h],1000*curr1[h]/Ad,marker='o', markersize=10, color='r')
                for t in ring_peaks:
                    grgr.plot(potential[t],1000*curr1[t]/Ad,marker='+',mew=5, markersize=20, color='b')
                #grgr.plot(data[i]['Potential/V'].values[shoulder_min:shoulder_max]+0.658, 
                        # 1000*data[i]['i1/A'].values[shoulder_min:shoulder_max]/Ad, 
                         #color = 'g', linewidth=4,
                        #label=labz[si]) 
            except KeyError: ###in case column i2/A does not exist (RDE instead of RRDE)
                grgr.plot(potential,1000*curr/Ad,color = colors[si],linewidth=0.12*hsize_thesis,label=labz[si])

        #print('data'+str(i)+' '+str(disk))
        #grgr.set_title('RRDE EXPERIMENT '+p[2]+' Cycle',fontsize=20)
        grgr.set_ylabel('Current density (mA cm$^{-2}$)')
        grgr.set_xlabel('Disk Potential vs SHE (V)')
        grgr.set_facecolor('white')
       # grgr.set_xlim( 0.48,2 ) 
        #grgr.set_ylim(-3,13) 
        grgr.legend(bbox_to_anchor=(0.55,0.9),fontsize=0.8*hsize_thesis, frameon=False,title='ceramic loading:') # bbox_to_anchor=(0.56, 0.75),
        grgr.get_legend().get_title().set_fontsize(hsize_thesis*1)
        grgr.text(0.05,0.9,'ceramic/graphite ink',transform=grgr.transAxes,fontsize=hsize_thesis*1.4,horizontalalignment='left')

        
## FIGURE E
data_book=[230,226,228,232,224] ##data to plot
label_book=['1:2','1:1','1.6:1','2.5:1','5:1']
selector=data_book
cycleexp=[5,5,5,5,5] #how many cycles per experiment,following the order of 'selector'
    ### this ranges are made when experimetns with different potential ranges are compared
    ## the same number of cycles is required

    ########peaks from peak analysis
disk_peaks=[]
ring_peaks=[]
shoulder_min=870
shoulder_max=870
ranges=[]

for i in range(1): ####define how many cycles to plot 
    a=[]
    b=[]
    for t in selector:
        ti=selector.index(t)
        aa=int(len(data[t])/cycleexp[ti])*i
        bb=aa+int(len(data[t])/cycleexp[ti])
        a.append(aa)
        b.append(bb)
    d=str(i+1)+'th'
    if i==0:
        d=str(i+1)+'st'
    if i==1:
        d=str(i+1)+'nd'
    if i==2:
        d=str(i+1)+'rd'
    c=(a,b,d)
    ranges.append(c)
print(ranges)
wspacing=np.full((1, 12), 1, dtype=int).tolist()
for p in ranges:
    plot_size=1/3*1.5
    labz=label_book
 ##### identifies the 
    colors=[]
    #interval=rng_min[selector.index(i)]rng_max[selector.index(i)]
    for i in selector:        
        si=selector.index(i)
        rng_min=p[0][si]
        rng_max=p[1][si]
        time=data[i]['Time/s'].values[rng_min:rng_max] #time 
        potential=data[i]['Potential/V'].values[rng_min:rng_max]+0.658 #potential vs SHE (V)
        try:
            curr2=data[i]['i2/A'].values[rng_min:rng_max] #current  DISK (A )
        except KeyError:    
            pass
        try:
            curr1=data[i]['i1/A'].values[rng_min:rng_max] ##current  RING (A )
        except KeyError:
            curr1=data[i]['Current/A'].values[rng_min:rng_max] #current  (A )
        Ar=dimen[i][1] # RING area
        ce=dimen[i][2] # collection efficiency
        Ad=dimen[i][0] # DISK area
        #colors.append(cm.tab20(si))
        colors.append(cm.viridis(int(50+si*255/(len(selector)))))##color map divided by the number of files   
        farve=colors[si]
        labs=['DISK','RING (raw data)','RING (collection   '+'\n'+'efficiency considered)']
        if True:  ##this loop is here in orfer 
            marco='-'
            if i==85:
                marco='--'
            try:
                assia.plot(potential,1000*curr1/Ad,linestyle=marco,color=farve,linewidth=0.12*hsize_thesis,label=labz[si]) #,color = colors[si] 
                for h in disk_peaks:
                    assia.plot(potential[h],1000*curr1[h]/Ad,marker='o', markersize=10, color='r')
                for t in ring_peaks:
                    assia.plot(potential[t],1000*curr1[t]/Ad,marker='+',mew=5, markersize=20, color='b')
                #assia.plot(data[i]['Potential/V'].values[shoulder_min:shoulder_max]+0.658, 
                        # 1000*data[i]['i1/A'].values[shoulder_min:shoulder_max]/Ad, 
                         #color = 'g', linewidth=4,
                        #label=labz[si]) 
            except KeyError: ###in case column i2/A does not exist (RDE instead of RRDE)
                assia.plot(potential,1000*curr/Ad,color = colors[si],linewidth=0.12*hsize_thesis,label=labz[si])

        #print('data'+str(i)+' '+str(disk))
        #assia.set_title('RRDE EXPERIMENT '+p[2]+' Cycle',fontsize=20)
        assia.set_ylabel('Current density (mA cm$^{-2}$)')
        assia.set_xlabel('Disk Potential vs SHE (V)')
        assia.set_facecolor('white')
       # assia.set_xlim( 0.48,2 ) 
        #assia.set_ylim(-3,13) 
        assia.legend(loc=0,fontsize=0.99*hsize_thesis, frameon=False,title='ceramic/graphite ratio:') # bbox_to_anchor=(0.56, 0.75),
        assia.get_legend().get_title().set_fontsize(hsize_thesis*1.3)
#### Scan direction arrows   
      #  if p==ranges[0]:
      #      #ring.arrow(0.6, -2.75, 0.2, 0.1, head_width=0.05, head_length=0.1, fc='k', ec='k')
      #      ring.annotate("", xy=(0.8, -3.3), xytext=(0.6, -3.5),
      #          arrowprops=dict(arrowstyle="->"))        
      #      ring.annotate("", xy=(0.6, -1.15), xytext=(0.8, -1.1),
      #          arrowprops=dict(arrowstyle="->"))
      #  if p==ranges[0]:
      #      disk.annotate("", xy=(1, 0.07), xytext=(0.75, 0.05),
      #          arrowprops=dict(arrowstyle="->"))        
      #      disk.annotate("", xy=(1, -0.055), xytext=(1.25, -0.045),
      #          arrowprops=dict(arrowstyle="->"))  
      #  
        #ring_disk.annotate("Peak D1", xy=(1.45, 0.35), xytext=(1.15, 0.6),fontsize=12,horizontalalignment='right',arrowprops=dict(arrowstyle="->"))
        #ring_disk.annotate("Peak D2", xy=(1.8, 0.65), xytext=(1.45, 1),fontsize=12,horizontalalignment='right',arrowprops=dict(arrowstyle="->"))
        #zoom.annotate("Peak D3", xy=(1.05, -0.06), xytext=(1, -0.09),fontsize=12,horizontalalignment='right',arrowprops=dict(arrowstyle="->"))
        #zoom.annotate("Peak D4",#xy=(1, -0.09), xytext=(1.25, -0.06),xy=(1.3, -0.03), xytext=(1.55, -0.08),fontsize=12,horizontalalignment='left',arrowprops=dict(arrowstyle="->"))
ring_disk.set_ylabel('Current density\n(mA cm$^{-2}$)')
ring_disk.set_xlabel('Potential vs SHE (V)')
zoom.set_ylabel('Current density\n(mA cm$^{-2}$)')
zoom.set_xlabel('Potential vs SHE (V)')
nogr.set_ylabel('Current density\n(mA cm$^{-2}$)')
nogr.set_xlabel('Potential vs SHE (V)')
grgr.set_ylabel('Current density\n(mA cm$^{-2}$)')
grgr.set_xlabel('Potential vs SHE (V)')
zoom.set_ylim(-0.15,0.1)
assia.set_ylabel('Current density\n(mA cm$^{-2}$)')
assia.set_xlabel('Potential vs SHE (V)')
ml=MultipleLocator(0.01)# set the distance of the minor thicks,, based on the arugument of the axis
Ml=MultipleLocator(0.05)# set the distance of the minor thicks, based on the arugument of the axis   
zoom.yaxis.set_major_locator(Ml)
zoom.yaxis.set_minor_locator(ml)  
mlu=MultipleLocator(0.1)# set the distance of the minor thicks,, based on the arugument of the axis
Mlu=MultipleLocator(0.5)
ring_disk.yaxis.set_major_locator(Mlu)
ring_disk.yaxis.set_minor_locator(mlu)  
mlV=MultipleLocator(0.05)# set the distance of the minor thicks,, based on the arugument of the axis
MlV=MultipleLocator(0.125)# set the distance of the minor thicks, based on the arugument of the axis  
zoom.xaxis.set_major_locator(MlV)
zoom.xaxis.set_minor_locator(mlV)   
ring_disk.xaxis.set_major_locator(MlV)
ring_disk.xaxis.set_minor_locator(mlV)  
assia.xaxis.set_minor_locator(mlV) 
nogr.xaxis.set_minor_locator(mlV) 
grgr.xaxis.set_minor_locator(mlV) 
ring_disk.set_xticks(np.arange(0.5,2.25,0.25))
zoom.set_xticks(np.arange(0.5,2.25,0.25))
assia.set_xticks(np.arange(0.5,2.25,0.25))
ring_disk.text(-0.2,0.975,'a)',transform=ring_disk.transAxes,fontsize=hsize_thesis*2,horizontalalignment='center')
zoom.text(-0.2,0.975,'b)',transform=zoom.transAxes,fontsize=hsize_thesis*2,horizontalalignment='center')
nogr.text(-0.2,0.975,'c)',transform=nogr.transAxes,fontsize=hsize_thesis*2,horizontalalignment='center')
grgr.text(-0.2,0.975,'d)',transform=grgr.transAxes,fontsize=hsize_thesis*2,horizontalalignment='center')
assia.text(-0.1,0.975,'e)',transform=assia.transAxes,fontsize=hsize_thesis*2,horizontalalignment='center')
plt.subplots_adjust(left=0.085, bottom=0.125, right=0.93, top=0.93,wspace=0.05, hspace=0.11)
#fig.savefig('C:/M_drive_docs/Thesis/graphics/rrde_graph_nograph.pdf',bbox_inches='tight')
#fig.savefig('C:/M_drive_docs/Thesis/graphics/rrde_graph_nograph.png',bbox_inches='tight')