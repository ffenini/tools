# reading .ras files from Rigaku Smartlab
source='C:/M_drive_docs/Lab/MaterialsSynth/XRD/MnCr2018/Refinement/MnCu25_0407/'
samples=[
         'cif25a32.prf']
fig,ax=plt.subplots(figsize=(15,8))
for i in samples:
    #print(i)
    path=source+i
    test=pd.read_csv(path, delimiter='\t',names=['2Theta','Yobs','Ycalc','Backg','posr'],
                     skiprows=4,skipfooter=91)
    #extracting the peak positions
    with open(path, 'r') as h:
        tu=h.readlines()
    indexes=[] #structure (tuple) : (2theta angle(float), Millerindices(str), 1(ka1) or 2(ka2)(str))
    for i in tu[-90:]:
        i=i.replace('\n','')
        j=i.split('\t')
        j[0]=j[0].replace(' ','')
        j[6]=j[6].replace(' ','')
        j[7]=j[7].replace(' ','')
        j[7]=j[7].replace('0','')
        c=(float(j[0]),j[6],j[7])
        indexes.append(c)
    h.close()   
    x=test['2Theta']
    if max(test['Yobs'])>max(test['Ycalc']):
        den=max(test['Yobs'])
    else:
        den=max(test['Ycalc'])
    y=test['Yobs']/den
    yc=test['Ycalc']/den
    yr=(test['Yobs']-test['Ycalc'])/max(test['Ycalc'])
    #yw2=(test['Yobs']-test['Ycalc'])/test['Ycalc']-0.2#max(test['Ycalc'])
    #yw=(test['Yobs']-test['Ycalc'])/test['Yobs']-0.4#max(test['Ycalc'])
    yr2=(test['Yobs']/den-test['Ycalc']/den)#max(test['Ycalc'])
    ax.plot(x,yc,color='k',label='calc')
    ax.plot(x,y,label='obs',color='r',linestyle=':')
    #ax.plot(x,yc,color='k',label='calc')
    #ax.plot(x,yr,label='diff',linewidth=0.8)
    #ax.plot(x,yw,label='diff wcalc',linewidth=0.8)
    #ax.plot(x,yw2,label='diff wobs',linewidth=0.8)
    ax.plot(x,yr2,label='diff ratios',linewidth=0.8)
    for k in indexes:
        if k[2]=='1':
            ax.text(k[0],-0.2,k[1],rotation=90)

    y=y.tolist()
    yc=yc.tolist()
    x=x.tolist()
    lines=False
    if lines:
        for i in range(len(yr)):
            if yr[i]>0.006:
                ax.axvline(x[i],ymin=-10,ymax=10,alpha=0.5,linestyle='-',color='g')
            if yr[i]<-0.006:
                ax.axvline(x[i],ymin=-10,ymax=10,alpha=0.5,linestyle='-',color='r')
ax.set_xlim(10,150)
#ax.set_ylim(-0.051,0.051)


#peak positions calculated from FullProf
#peak positions calculated from FullProf             
for i in indexes:
    for t in x:
        if abs(i[0]-t)<0.0051 and i[2]=='1':
            for p in range(len(x)):
                if x[p]==t:
                    if y[p]<yc[p] and y[p]>0.05:
                        ax.axvline(t,ymin=-10,ymax=10,alpha=0.3,linestyle='-',color='g')
                        if i==indexes[1]:
                            ax.axvline(t,ymin=-10,ymax=10,alpha=0.3,linestyle='-',color='g',label='Iobs<Icalc')
                    elif y[p]>yc[p] and y[p]>0.05:
                        ax.axvline(t,ymin=-10,ymax=10,alpha=0.3,linestyle='-',color='orange')
                        if i==indexes[4]:
                            ax.axvline(t,ymin=-10,ymax=10,alpha=0.3,linestyle='-',color='orange',label='Iobs>Icalc')
                            
ax.legend()
ax.set_title('MnCu$_{0.25} 07/03$',fontsize=30)