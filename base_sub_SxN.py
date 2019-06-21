

########peaks from peak analysis
from data_importer import *

def base_sub_SxN(selector,selex=[],labz=['SET LABLE '],baseline=[],subtract=True,base_plot=False,numb_cyc=10,cycles=10,plot_type='c1',disk_peaks=[],ring_peaks=[],
                 disk_shldrs=[],ring_shldrs=[],plotstitle='Baseline subtraction: SETCURRTYPE current',save_fig=False,filename='plot_',fontlegend=15,
                 savepath='C:/M_drive_docs/test/',zoom_x=(None,None),zoom_y=(None,None),cur_x=(None,None) ,cur_y=(None,None),text_plot=True):
    '''
    ^^ selector, [list]: indicates the data to select from 'data' to be plotted, 
                 indicized by the importing index (tre.style)
    selex, [list]: indicate the cycles to display; if not entered, displays all the cycles,
                (given bu 'cycles'). same entry style as 'selector'
                default: selex=[]
    labz, [list of strings]: list of the labels for the selctor elements,
                default: lbls=['SET LABLE ']
    baseline, [list]: indicates the data to use as a baseline, only baseline[0] will be used
                if empty, no baseline subtraction is performed
                default: baseline=[]
    subtract, boolean, enables baseline subtraction
                default: subtract=True
    base_plot, boolean: in order to plot the baseline raw data in the plot 
                default: base_plot=False
    numb_cyc, integer: number of cycles in the experiment (need to be the same for
               all the data used
                default: numb_cyc=10
    cycles, integer: define how many cycles to plot,
                default: cycles=10 
    plot_type, str, # can be 'c1' or 'c2', in order to select 'i1/A' or 'i2/A' in the dataframe  
                default:plot_type='c1' 
    disk_peaks, [list]: list of points that are the peaks of the disk signal
                default:disk_peaks=[]
    ring_peaks, [list]: list of points that are the peaks of the ring signal
                default:ring_peaks=[]
    disk_shldrs,[list of (tuples)]: list of ranges (tuples) of areas of the plot
                to higlight corresponding to disk area of interest
                default: disk_shldrs=[]
    ring_shldrs,[list of (tuples)]: list of ranges (tuples) of areas of the plot
                to higlight corresponding to ring area of interest
                default: ring_shldrs=[]
    plotstitle, str: title to give to the figure
                default: plotstitle='Baseline subtraction: SETCURRTYPE current'
    save_fig, boolean: save the figure as a .tif file or not
                default: save_fig=False
    filename, str: name to give to the .tif file that will be saved
                default: filename='plot_'
    fontlegend, int: fontsize of the legend text
                default: fontlegend=15
    savepath, str: path where to save the figure to the .tif file that will be saved
                default: savepath='C:/M_drive_docs/test/'  
    zoom_x, tuple: setting the X limits of the right plot; can be (None, value) if only one limit
                    has to be set
                 default: full cycle   
    zoom_y, tuple: setting the X limits of the right plot; can be (None, value) if only one limit
                    has to be set
                 default: +/- 5% if the Y max/min 
    cur_x, tuple: setting the X limits of the left plot; can be (None, value) if only one limit
                    has to be set
                 default: full cycle 
    zoom_y, tuple: setting the X limits of the left plot; can be (None, value) if only one limit
                    has to be set
                 default: +/- 5% if te Y max/min
    text_plot, boolean,: activate 'Potential' labels for the points
                default:text_plot=True
                '''
    labz.append('baseline')
    if base_plot and len(baseline)>0 and selector[len(selector)-1]!=baseline[0]:
        selector.append(baseline[0])
    rtu=[] ### this ranges are made when experimetns with different potential ranges are compared; rtu will be converted to 'ranges' in the cycle that reads 'selex'
    for i in range(cycles):  ## the same number of cycles is required
        a=[]
        b=[]
        f=[]
        for t in selector:
            aa=int(len(data[t])/numb_cyc)*i
            bb=aa+int(len(data[t])/numb_cyc)
            ff=int(bb/2)
            a.append(aa)
            b.append(bb)
            f.append(ff)
        d=str(i+1)+'th'
        if i==0:
            d=str(i+1)+'st'
        if i==1:
            d=str(i+1)+'nd'
        if i==2:
            d=str(i+1)+'rd'
        e=i+1
        c=(a,b,d,e,f)
        rtu.append(c)
    ranges=[]
    if len(selex)==0:
        selex=np.arange(1,cycles+1,1)
    for y in selex:
        for p in rtu:
            if y==p[3]:
                ranges.append(p)
    #print(ranges)
    if len(baseline)>0 and subtract:   # add B.S. to the material legend name and to the figure filename if baseline is subtracted
        savepath=savepath+'BS_'
        for z in range(len(labz)):
            if labz[z]!='baseline' and ' B.S.' not in labz[z]:
                labz[z]=labz[z]+' B.S.'
    fig=plt.figure(figsize=(15,6*len(ranges)))## muar be out of ranges to have a single figure
    for p in ranges:
        cur=plt.subplot(len(ranges),2,(ranges.index(p)+1)*2-1)
        zoom=plt.subplot(len(ranges),2,(ranges.index(p)+1)*2)
        colors=[]
        for i in selector:  
            si=selector.index(i)
            rm=p[0][si] #single plot range minimum
            rh=p[4][si]
            rM=p[1][si] #single plot range maximum
            Ar=dimen[i][1] # RING area
            ce=dimen[i][2] # collection efficiency
            Ad=dimen[i][0] # DISK area
            #colors.append(cm.tab20(si))
            colors.append(cm.copper(int(0+si*255/(len(selector)))))##color map divided by the number of files
            time=data[i]['Time/s'].values #time 
            potential=0.658+data[i]['Potential/V'].values #potential vs SHE (V)
            try:
                datD=data[i]['i1/A'].values
                datR=data[i]['i2/A'].values
            except KeyError:
                datD=data[i]['Current/A'].values
                datR=0*data[i]['Current/A'].values
            try:
                bD=data[baseline[0]]['i1/A'].values
                bR=data[baseline[0]]['i2/A'].values
            except KeyError:
                bD=data[baseline[0]]['Current/A'].values 
                bR=0*data[baseline[0]]['Current/A'].values 
            curr2=datR/Ar/ce #current density RING (A cm-2)
            curr1=datD/Ad ##current density DISK (A cm-2) 
            if len(baseline)>0 and i!=baseline[0] and subtract:  # BASELINE SUBTRACTION starts 
                if len(data[baseline[0]].values)-len(data[i].values)>0: # in case baseline data are longer than data data            
                    c=(len(data[baseline[0]].values)-len(data[i].values))/2 # length difference divided by two
                    if int(c)==c: # in case the lenght difference is an even number
                        d=int(c)
                        e=int(c)
                    else: # in case the lenght difference is an odd number
                        d=int(c+0.5)
                        e=int(c-0.5)
                    curr2=(datR-bR[d:-e])/Ar/ce
                    curr1=(datD-bD[d:-e])/Ad ##current density DISK (A cm-2)
                elif len(data[baseline[0]].values)-len(data[i].values)<0: # in case 'baseline' data are shorter than 'data' data
                    c=(len(data[i].values)-len(data[baseline[0]].values))/2 # length difference divided by two
                    if int(c)==c: # in case the lenght difference is an even number
                        d=int(c)
                        e=int(c)
                    else: # in case the lenght difference is an odd number
                        d=int(c+0.5)
                        e=int(c-0.5)
                    curr2=(datR[d:-e]-bR)/Ar/ce
                    curr1=(datD[d:-e]-bD)/Ad ##current density DISK (A cm-2)       # BASELINE SUBTRACTION ends  
                else:     # in case baseline data are the same length than data data
                    curr2=(datR-bR)/Ar/ce #current density RING (A cm-2)
                    curr1=(datD-bD)/Ad ##current density DISK (A cm-2)            
            if plot_type=='c2':#select which current to plot
                current=curr2 #####select which current to plot
            if plot_type=='c1':
                current=curr1
    ##############  RING
            #cur.plot(time[rm:rM]-time[rm:rM][(rm+rM)//2-rm],1000*current[rm:rM], linestyle='-',color = colors[si],label=labz[si])
           # zoom.plot(time[rm:rM]-time[rm:rM][(rm+rM)//2-rm],1000*current[rm:rM], linestyle='-',color = colors[si],label=labz[si])
            cur.plot(time[rm:rM],1000*current[rm:rM], linestyle='-',color = colors[si],label=labz[si])
            zoom.plot(time[rm:rM],1000*current[rm:rM], linestyle='-',color = colors[si],label=labz[si])
           # for g in range(0,1000,100):            
                #zoom.text(time[len(time)-g-1]-time[0],1000*current[len(time)-g-1],str(data[i]['Time/s'].values(time[len(time)-g-1])),rotation='vertical')
            #cur.plot(time,((1000*current)/ce)/Ar,linestyle='-', color = colors[si],label=labz[si])
            if len(ring_shldrs)>0 and (i in baseline)==False :        
                for r in ring_shldrs:   
                    cur.plot(time[r[0]:r[1]],1000*(current[r[0]+rm:r[1]+rm]),color = 'g', linewidth=4) 
                    zoom.plot(time[r[0]:r[1]],1000*(current[r[0]+rm:r[1]+rm]),color = 'g', linewidth=4)
                    if r==ring_shldrs[0]:
                        cur.plot(time[r[0]:r[1]],1000*(current[r[0]+rm:r[1]+rm]),color = 'g', linewidth=4,label='Ring shoulders')                 
            if len(disk_shldrs)>0 and (i in baseline)==False :        
                for d in disk_shldrs:   
                    cur.plot(time[d[0]:d[1]],1000*(current[d[0]+rm:d[1]+rm]),color = 'yellow', linewidth=4) 
                    zoom.plot(time[d[0]:d[1]],1000*(current[d[0]+rm:d[1]+rm]),color = 'yellow', linewidth=4)
                    if d==disk_shldrs[0]:
                        cur.plot(time[d[0]:d[1]],1000*(current[d[0]+rm:d[1]+rm]),color = 'yellow', linewidth=4,label='Disk shoulders') 
            if len(disk_peaks)>0 and (i in baseline)==False :
                for h in disk_peaks:
                    cur.plot(time[rm:rM][h]-time[rm:rM][0],1000*current[rm:rM][h],marker='+', markersize=15,mew=3, color='b')
                    zoom.plot(time[rm:rM][h]-time[rm:rM][0],1000*current[rm:rM][h],marker='+', markersize=15,mew=3, color='b')
                    if text_plot and (time[rm:rM][h]-time[rm:rM][0])>cur_x[0]and (time[rm:rM][h]-time[rm:rM][0])<cur_x[1]:
                        cur.text(time[rm:rM][h]-time[rm:rM][0],1000*current[rm:rM][h],str(round(potential[rm:rM][h],3)) +' V',color='b',rotation='vertical')
                    if text_plot and (time[rm:rM][h]-time[rm:rM][0])>zoom_x[0]and (time[rm:rM][h]-time[rm:rM][0])<zoom_x[1]:                
                        zoom.text(time[rm:rM][h]-time[rm:rM][0],1000*current[rm:rM][h],str(round(potential[rm:rM][h],3)) +' V',color='b',rotation='vertical')
                    if h==disk_peaks[0]:
                        cur.plot(time[rm:rM][h]-int(time[rm:rM][0]),1000*current[rm:rM][h],marker='|', markersize=15,mew=3, color='b',label='Disk peaks')
            if len(ring_peaks)>0 and (i in baseline)==False :
                for t in ring_peaks:
                    cur.plot(time[rm:rM][t]-time[rm:rM][0],1000*current[rm:rM][t],marker='|', markersize=15,mew=3, color='r')
                    zoom.plot(time[rm:rM][t]-time[rm:rM][0],1000*current[rm:rM][t],marker='|', markersize=15,mew=3, color='r')
                    if text_plot and (time[rm:rM][t]-time[rm:rM][0])>cur_x[0]and (time[rm:rM][t]-time[rm:rM][0])<cur_x[1]:
                        cur.text(time[rm:rM][t]-time[rm:rM][0],1000*current[rm:rM][t],str(round(potential[rm:rM][t],3)) +' V',color='r',rotation='vertical')
                    if text_plot and (time[rm:rM][t]-time[rm:rM][0])>zoom_x[0]and (time[rm:rM][t]-time[rm:rM][0])<zoom_x[1]:                
                        zoom.text(time[rm:rM][t]-time[rm:rM][0],1000*current[rm:rM][t],str(round(potential[rm:rM][t],3)) +' V',color='r',rotation='vertical')
                    if t==ring_peaks[0]:
                        cur.plot(time[rm:rM][t]-int(time[rm:rM][0]),1000*current[t],marker='|', markersize=15,mew=3, color='r',label='Ring peaks')
            
            cur.set_xlim(cur_x) 
            zoom.set_xlim(zoom_x) 
            cur.set_ylim(cur_y)
            zoom.set_ylim(zoom_y)
            cur.set_title(p[2]+' Cycle',fontsize=30)
            zoom.set_title('- zoom -',fontsize=20)
            zoom.tick_params(axis='both', which='major', labelsize=15)
            cur.tick_params(axis='both', which='major', labelsize=15)        
            cur.set_ylabel('Current density (mA cm$^{-2}$)',fontsize=15)
            cur.set_xlabel('Time (s)',fontsize=15)
            zoom.set_ylabel('Current density (mA cm$^{-2}$)',fontsize=15)
            zoom.set_xlabel('Time (s)',fontsize=15) 
            #cur.legend(labz,fontsize=12)
        if p==ranges[0]:
            #cur.text(0,0,plotstitle,fontsize=35)
            cur.legend( loc=0,ncol=1,fontsize=fontlegend)
        else:
            continue 
    plt.tight_layout()
    fig.suptitle(plotstitle,fontsize=35)
    plt.subplots_adjust()#0.95-(10-cycles)*(1/60))
    path=savepath+p[2]+'_'+plot_type+'.tif'
    if save_fig:
        fig.savefig(path)















