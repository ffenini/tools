def cm2inch(a):
    inch = 2.54
    a=a/inch
    return a


#only selecting the files with a specific extension
def list_files1(directory, extension):
    return [f for f in os.listdir(directory) if f.endswith('.' + extension)]
# reading .ras files from Rigaku Smartlab
source='C:/M_drive_docs/Lab/MaterialsSynth/XRD/SnO2/BsnO2_new_samples/fixed/'
#bisno=os.listdir(source)
bisno=list_files1(source,'xy')
cucro=[31.33,36.27,40.73,55.75,65.37]




hsize_thesis=cm2inch(21.4)
vsize_thesis=hsize_thesis/2
plt.rcParams['axes.linewidth'] = 0.07*hsize_thesis
plt.rcParams['axes.labelsize'] =1.6*hsize_thesis
fig,(ax,ax1,ax2)=plt.subplots(1,3,figsize=(hsize_thesis,vsize_thesis))
gs = gridspec.GridSpec(2, 2,
                       width_ratios=[1, 2],
                       height_ratios=[ 1,1]
                       )
colors=[]
ax1=plt.subplot(gs[0])
ax=plt.subplot(gs[2])
ax2=plt.subplot(gs[0:,-1])
#ax3=plt.subplot(224)
peak29=[]
peak48=[]
for g in bisno: 
    sg=bisno.index(g)
    colors.append(cm.copper(int(70+sg*125/len(bisno))))
    path=source+g
    #peaks position taken from the patter of CuCrO2
    test=pd.read_csv(path, delimiter=' ',names=['2theta', 'Intensity','Error'],skiprows=1)

    x=test['2theta']
    if g==bisno[4]:
        y1=test['Intensity']/max(test['Intensity'])-0.0015
    else:
        y1=test['Intensity']/max(test['Intensity'])
    y=savitzky_golay(y1.values,15,3)

    labby=g[0]+'.'+g[1]#+' %at'
    if g==bisno[0]:
        labby='pure SnO$_2$'
    
    ax.plot(x,y,label=labby,linewidth=0.08*hsize_thesis,color=colors[sg])
    ax1.plot(x,y,label=labby,linewidth=0.08*hsize_thesis,color=colors[sg])
    
    
    ##INTEGRATING INTENSITY

    #minu=min(x, key=lambda x:abs(x-27)) # determines the values in a list that is the closest to the number given e.g.27
    if sg>0:
        limd,limu=np.where(x==min(x, key=lambda x:abs(x-47.5)))[0][0],np.where(x==min(x, key=lambda x:abs(x-48.5)))[0][0]
        limd1,limu1=np.where(x==min(x, key=lambda x:abs(x-28.5)))[0][0],np.where(x==min(x, key=lambda x:abs(x-29.5)))[0][0]
        limd2,limu2=np.where(x==min(x, key=lambda x:abs(x-26)))[0][0],np.where(x==min(x, key=lambda x:abs(x-27.5)))[0][0]
        limd3,limu3=np.where(x==min(x, key=lambda x:abs(x-51)))[0][0],np.where(x==min(x, key=lambda x:abs(x-53)))[0][0]
        area48=np.trapz(y[limd:limu],x[limd:limu]) #area of the peak at 48 of Bi2Sn2O7
        area29=np.trapz(y[limd1:limu1],x[limd1:limu1]) #area of the peak at 29 of Bi2Sn2O7
        area110=np.trapz(y[limd2:limu2],x[limd2:limu2]) #area of the peak 110 of SnO2
        area211=np.trapz(y[limd3:limu3],x[limd3:limu3]) #area of the peak 211 of SnO2
        peak48.append(area48/area211)
        peak29.append(area29/area110)
    if sg==1:
        peak48.append(area48/area211)
        peak29.append(area29/area110)
    if sg>3: # making labels for the plots 
        ax.text(x[np.where(x==min(x, key=lambda x:abs(x-48)))[0][0]],0.002+y[np.where(x==min(x, key=lambda x:abs(x-48)))[0][0]],labby,fontsize=hsize_thesis*0.75)
        ax1.text(x[np.where(x==min(x, key=lambda x:abs(x-28.85)))[0][0]],0.005+y[np.where(x==min(x, key=lambda x:abs(x-28.85)))[0][0]],labby,fontsize=hsize_thesis*0.75)
    if sg==0: # making labels for the plots 
        ax.text(x[np.where(x==min(x, key=lambda x:abs(x-47.275)))[0][0]],1.1*y[np.where(x==min(x, key=lambda x:abs(x-47.275)))[0][0]],'Si',fontsize=hsize_thesis*0.75)
        ax1.text(x[np.where(x==min(x, key=lambda x:abs(x-28.445)))[0][0]],1.1*y[np.where(x==min(x, key=lambda x:abs(x-28.445)))[0][0]],'Si',fontsize=hsize_thesis*0.75)

# PEAK RATIOS 
cont=[0,0.5,1,1.5,2,3,4,5]
f1=np.poly1d(polyfit([1.5,2,3,4,5],peak29[3:],1))
f2=np.poly1d(polyfit([1.5,2,3,4,5],peak48[3:],1))
x_new=np.linspace(-0.250,5.250,50)
x_lin=np.linspace(0.55,5.5,50)

ax2.plot(cont,peak29,linestyle='',markersize=hsize_thesis/1.5,marker='v',color='dodgerblue',fillstyle='none',markeredgewidth =hsize_thesis/8)
ax2.plot(cont,peak48,linestyle='',markersize=hsize_thesis/1.5,marker='o',color='firebrick',fillstyle='none',markeredgewidth =hsize_thesis/8)
ax2.plot(x_lin, f1(x_lin),linestyle='--',linewidth =hsize_thesis/12,alpha=0.75) #guide line
ax2.plot(x_lin, f2(x_lin),linestyle='--',linewidth =hsize_thesis/12,alpha=0.75) #guide line
ax2.plot(cont,peak29,linestyle='',markersize=hsize_thesis/1.5,marker='v',color='dodgerblue',fillstyle='none',markeredgewidth =hsize_thesis/8)
ax2.plot(cont,peak48,linestyle='',markersize=hsize_thesis/1.5,marker='o',color='firebrick',fillstyle='none',markeredgewidth =hsize_thesis/8)

ax.set_xlim(47.1,48.9)
ax.set_ylim(0.005,0.041)

ax1.set_xlim(28.3,29.4)
ax1.set_ylim(0.01,0.14)

ax2.set_ylim(0.025,0.24)

#figure labels
ax1.text(0.85,0.8,'(a)',transform=ax1.transAxes,fontsize=hsize_thesis*1.6)
ax.text(0.85,0.8,'(b)',transform=ax.transAxes,fontsize=hsize_thesis*1.6)
ax2.text(0.02,0.915,'(c)',transform=ax2.transAxes,fontsize=hsize_thesis*1.6)

#ax2.set_xlim(25.5,28)
#ax2.set_ylim(0.005,1.1)
#ax3.set_xlim(50,53)
#ax3.set_ylim(0.01,0.6)
ax.set_xlabel('2'+r'$\theta$ (°)',fontsize=hsize_thesis*1.6)
ax.yaxis.set_label_coords(-0.250, 1.15) #position the yaxis label to span muliple plots
ax.set_ylabel('Arbitrary units',fontsize=hsize_thesis*1.6)
ax2.set_ylabel('Peak ratio (a.u.)',fontsize=hsize_thesis*1.6,labelpad=hsize_thesis/4)
ax2.set_xlabel('at.%$_\mathrm{Bi}$',fontsize=hsize_thesis*1.6)
lg=ax2.legend([r"I$_\mathrm{(40 \bar{4})_\mathrm{Bi_2Sn_2O_7}}$/I$_\mathrm{(110)_\mathrm{SnO_2}}$",
                            r'I$_\mathrm{(44\bar{8})_\mathrm{Bi_2Sn_2O_7}}$/I$_\mathrm{(211)_\mathrm{SnO_2}}$'],
                           bbox_to_anchor=(0.55,0.8),ncol=1,frameon=False,fontsize=hsize_thesis*1.5)
lg.get_title().set_fontsize(hsize_thesis*1)
yticks2=[0.1,0.2]
ax2.set_yticks(yticks2)
ax2.set_xticks(cont)
ax.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax1.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax2.tick_params(axis='both',labelsize=hsize_thesis*1.3,pad=hsize_thesis/4)#
#lg=ax.legend(title='at.%$_\mathrm{Bi}$:',ncol=2,frameon=False,fontsize=hsize_thesis*0.8)
#lg.get_title().set_fontsize(hsize_thesis*1)
#lg.set_title('Bi content:', fontsize=)
plt.subplots_adjust(left=0.085, bottom=0.125, right=0.91, top=0.95,wspace=0.26, hspace=0.2025)
fig.savefig('C:/M_drive_docs/Thesis/graphics/peakratio.pdf')
fig.savefig('C:/M_drive_docs/Thesis/graphics//peakratio.png')

