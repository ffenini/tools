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




hsize_thesis=cm2inch(21.4)*2.5
vsize_thesis=hsize_thesis/4
spines_ticks_width=0.1*hsize_thesis
plt.rcParams['axes.linewidth'] = spines_ticks_width
plt.rcParams['axes.labelsize'] =1.6*hsize_thesis
fig,(ax,ax1,ax2)=plt.subplots(1,3,figsize=(hsize_thesis,vsize_thesis),facecolor='w')


gs0 = gridspec.GridSpec(1, 2)

gs00 = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=gs0[0],wspace=0.4)
gs01 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[1])
#gs00.update(hspace=0.05)

#gs = gridspec.GridSpec(1, 3,
#                       width_ratios=[1,1, 2],
#                       height_ratios=[ 1]
#                       )
colors=[]
ax1=plt.subplot(gs00[0])
ax=plt.subplot(gs00[1])
ax2=plt.subplot(gs01[0])
#ax3=plt.subplot(gs00[2])
#ax3=plt.subplot(224)
peak29=[]
peak48=[]
peak56=[]
for g in bisno: 
    sg=bisno.index(g)
    colors.append(cm.copper(int(70+sg*125/len(bisno))))
    path=source+g
    #peaks position taken from the patter of CuCrO2
    test_MAX=test=pd.read_csv(source+bisno[1], delimiter=' ',names=['2theta', 'Intensity','Error'],skiprows=1)
    test=pd.read_csv(path, delimiter=' ',names=['2theta', 'Intensity','Error'],skiprows=1)

    x=test['2theta']
    if g==bisno[4]:
        y1=test['Intensity']/max(test['Intensity'])-0.0015
    else:
        y1=test['Intensity']/max(test['Intensity'])
    y1_MAX=test_MAX['Intensity']/max(test_MAX['Intensity'])
    y=savitzky_golay(y1.values,15,3)
    y_MAX=savitzky_golay(y1_MAX.values,15,3)

    labby=g[0]+'.'+g[1]#+' %at'
    if g==bisno[0]:
        labby='pure SnO$_2$'
    
    ax.plot(x,y,label=labby,linewidth=0.08*hsize_thesis,color=colors[sg])
    ax1.plot(x,y,label=labby,linewidth=0.08*hsize_thesis,color=colors[sg])
    #ax3.plot(x,y,label=labby,linewidth=0.08*hsize_thesis,color=colors[sg])
    
    
    ##INTEGRATING INTENSITY

    limd,limu=np.where(x==min(x, key=lambda x:abs(x-47.5)))[0][0],np.where(x==min(x, key=lambda x:abs(x-48.5)))[0][0]
    limd1,limu1=np.where(x==min(x, key=lambda x:abs(x-28.5)))[0][0],np.where(x==min(x, key=lambda x:abs(x-29.5)))[0][0]
    limd2,limu2=np.where(x==min(x, key=lambda x:abs(x-26)))[0][0],np.where(x==min(x, key=lambda x:abs(x-27.5)))[0][0]
    limd3,limu3=np.where(x==min(x, key=lambda x:abs(x-51)))[0][0],np.where(x==min(x, key=lambda x:abs(x-53)))[0][0]
    limd4,limu4=np.where(x==min(x, key=lambda x:abs(x-56)))[0][0],np.where(x==min(x, key=lambda x:abs(x-57.5)))[0][0]
    limd5,limu5=np.where(x==min(x, key=lambda x:abs(x-57.5)))[0][0],np.where(x==min(x, key=lambda x:abs(x-58.5)))[0][0]
    # MAX values
    area48_MAX=np.trapz(y_MAX[limd:limu],x[limd:limu]) #area of the peak at 48 of Bi2Sn2O7
    area29_MAX=np.trapz(y_MAX[limd1:limu1],x[limd1:limu1]) #area of the peak at 29 of Bi2Sn2O7
    area56_MAX=np.trapz(y_MAX[limd4:limu4],x[limd4:limu4])
    area110=np.trapz(y[limd2:limu2],x[limd2:limu2]) #area of the peak 110 of SnO2
    area211=np.trapz(y[limd3:limu3],x[limd3:limu3]) #area of the peak 211 of SnO2
    areaXXX=np.trapz(y[limd5:limu5],x[limd5:limu5])
    #minu=min(x, key=lambda x:abs(x-27)) # determines the values in a list that is the closest to the number given e.g.27
    if sg>0:
        area48=np.trapz(y[limd:limu],x[limd:limu])/area48_MAX #area of the peak at 48 of Bi2Sn2O7
        area29=np.trapz(y[limd1:limu1],x[limd1:limu1])/area29_MAX #area of the peak at 29 of Bi2Sn2O7
        area56=np.trapz(y[limd4:limu4],x[limd4:limu4])
        area110=np.trapz(y[limd2:limu2],x[limd2:limu2]) #area of the peak 110 of SnO2
        area211=np.trapz(y[limd3:limu3],x[limd3:limu3]) #area of the peak 211 of SnO2
        areaXXX=np.trapz(y[limd5:limu5],x[limd5:limu5])
        ar=13
        #peak48.append(area48/area48_MAX)
        print(round(area48,5),round(area29,5))
        #peak29.append(area29/area29_MAX)
        #peak56.append(area56/area56_MAX)
        peak48.append(area48)#/area110)
        peak29.append(area29)#/area110)
        #peak56.append(area56/area110)
        #peak56.append(area29/areaXXX/ar

    if sg==1:
        #peak48.append(area48/area48_MAX)
        #peak29.append(area29/area29_MAX)
        #peak56.append(area56/area56_MAX)
        peak48.append(area48)#/area110)
        peak29.append(area29)#/area110)
        #peak56.append(area56/area110)
        #peak56.append(area29/areaXXX/ar)
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
#f3=np.poly1d(polyfit([1.5,2,3,4,5],peak56[3:],1))
x_new=np.linspace(-0.250,5.250,50)
x_lin=np.linspace(1.55,5.5,50)

ax2.plot(cont,peak29,linestyle='',markersize=hsize_thesis/1.5,marker='v',color='dodgerblue',fillstyle='none',markeredgewidth =hsize_thesis/8)
ax2.plot(cont,peak48,linestyle='',markersize=hsize_thesis/1.5,marker='o',color='firebrick',fillstyle='none',markeredgewidth =hsize_thesis/8)
#ax2.plot(cont,peak56,linestyle='',markersize=hsize_thesis/1.5,marker='s',color='green',fillstyle='none',markeredgewidth =hsize_thesis/8)
ax2.plot(x_lin, f1(x_lin),linestyle='--',linewidth =hsize_thesis/12,alpha=0.75) #guide line
ax2.plot(x_lin, f2(x_lin),linestyle='--',linewidth =hsize_thesis/12,alpha=0.75) #guide line
#ax2.plot(x_lin, f3(x_lin),linestyle='--',linewidth =hsize_thesis/12,alpha=0.75) #guide line
ax2.plot(cont,peak29,linestyle='',markersize=hsize_thesis/1.5,marker='v',color='dodgerblue',fillstyle='none',markeredgewidth =hsize_thesis/8)
ax2.plot(cont,peak48,linestyle='',markersize=hsize_thesis/1.5,marker='o',color='firebrick',fillstyle='none',markeredgewidth =hsize_thesis/8)

ax.set_xlim(47.1,48.9)
ax.set_ylim(0.005,0.041)

ax1.set_xlim(28.3,29.4)
ax1.set_ylim(0.0025,0.14)

ax3.set_xlim(56,57.5)
#ax3.set_xlim(57.5,58.5)
ax3.set_ylim(0.0025,0.04)

#ax2.set_ylim(0.025,0.24)

#figure labels
ax1.text(0.008025,0.865,'(a)',transform=ax1.transAxes,fontsize=hsize_thesis*1.6)
ax.text(0.008025,0.865,'(b)',transform=ax.transAxes,fontsize=hsize_thesis*1.6)
ax2.text(0.007022,0.865,'(c)',transform=ax2.transAxes,fontsize=hsize_thesis*1.6)

#ax2.set_xlim(25.5,28)
#ax2.set_ylim(0.005,1.1)
#ax3.set_xlim(50,53)
#ax3.set_ylim(0.01,0.6)
ax.set_xlabel('2'+r'$\theta$ (°)',fontsize=hsize_thesis*1.6)
ax1.set_xlabel('2'+r'$\theta$ (°)',fontsize=hsize_thesis*1.6)
ax.yaxis.set_label_coords(-0.250, 1.15) #position the yaxis label to span muliple plots
ax1.set_ylabel('Arbitrary units',fontsize=hsize_thesis*1.6)
ax2.set_ylabel('Integrated \n intensities (a.u.)',fontsize=hsize_thesis*1.6,labelpad=hsize_thesis/4)
ax2.set_xlabel('at.%$_\mathrm{Bi}$',fontsize=hsize_thesis*1.6)
lg=ax2.legend([r"I$_\mathrm{(40 \bar{4})_\mathrm{Bi_2Sn_2O_7}}$",
                            r'I$_\mathrm{(44\bar{8})_\mathrm{Bi_2Sn_2O_7}}$'],
                           bbox_to_anchor=(0.4078,0.3512),ncol=1,frameon=False,fontsize=hsize_thesis*1.2)
lg.get_title().set_fontsize(hsize_thesis*1)
yticks=[0.01,0.03]
ax.set_yticks(yticks)
xticks=[47.5,48.5]
ax.set_xticks(xticks)
yticks2=[0.1,0.2]
#ax2.set_yticks(yticks2)
ax2.set_xticks(cont)
ax.tick_params(axis='both',which='major',width=0.1*hsize_thesis,length=0.5*hsize_thesis,labelsize=hsize_thesis*1.3)
ax.tick_params(axis='both',which='minor',width=0.1*hsize_thesis,length=0.5*hsize_thesis,labelsize=hsize_thesis*1.3)
ax1.tick_params(axis='both',which='major',width=0.1*hsize_thesis,length=0.5*hsize_thesis,labelsize=hsize_thesis*1.3)
ax1.tick_params(axis='both',which='minor',width=0.1*hsize_thesis,length=0.5*hsize_thesis,labelsize=hsize_thesis*1.3)
ax2.tick_params(axis='y',which='major',width=0.1*hsize_thesis,length=0.5*hsize_thesis,labelsize=hsize_thesis*1.3,pad=hsize_thesis/4)
ax2.tick_params(axis='x',which='major',width=0.1*hsize_thesis,length=0.5*hsize_thesis,labelsize=hsize_thesis*1.3,pad=hsize_thesis/4,labelrotation=90)#
ax2.tick_params(axis='x',which='minor',width=0.1*hsize_thesis,length=0.3*hsize_thesis,labelsize=hsize_thesis*1.3,pad=hsize_thesis/4,labelrotation=90)#
#lg=ax.legend(title='at.%$_\mathrm{Bi}$:',ncol=2,frameon=False,fontsize=hsize_thesis*0.8)
#lg.get_title().set_fontsize(hsize_thesis*1)
#lg.set_title('Bi content:', fontsize=)
plt.subplots_adjust(left=0.085, bottom=0.3, right=0.91, top=0.95,wspace=0.35, hspace=0.2025)
fig.savefig('C:/M_drive_docs/Thesis/graphics/peakratio.pdf')
fig.savefig('C:/M_drive_docs/Thesis/graphics/peakratio.png')

