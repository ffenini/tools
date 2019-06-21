

source='C:/M_drive_docs\Lab/MaterialsSynth/Mn,NiCr2O4/Nitrate synthesis/Lidoped/Li_spinels_aft10at1000/'

hsize_thesis=cm2inch(21.4)*4
vsize_thesis=hsize_thesis/2
plt.rcParams['axes.linewidth'] = 0.07*hsize_thesis
plt.rcParams['axes.labelsize'] =1.6*hsize_thesis
#fig,ax=plt.subplots(figsize=(hsize_thesis,vsize_thesis))



chrom=list_files1(source,'xye')
print(chrom)
labby=['$\mathregular{MnLi_{0.25}Cr_{1.75}}$','$\mathregular{NiLi_{0.25}Cr_{1.75}}$','$\mathregular{MnLi_{0.5}Cr_{1.5}}$','$\mathregular{NiLi_{0.5}Cr_{1.5}}$','$\mathregular{MnCr_{2}}$','$\mathregular{NiCr_{2}}}$']
w=255
corz=[(204/w,0,0),(0,153/w,0),(204/w,102/w,0),(0,204/w,0),(102/w,0,0),(0,102/w,0)]
#print(chrom)
cucro=[31.33,36.27,40.73,55.75,65.37]
fig,(ax0,ax1,ax2,ax3,ax4,ax5)=plt.subplots(1,6,figsize=(hsize_thesis,vsize_thesis),sharex=True)
gs = gridspec.GridSpec(3, 2,
                       width_ratios=[1,1],
                       height_ratios=[ 1,1,1]
                       )
ax3=plt.subplot(gs[4])
ax1=plt.subplot(gs[2],sharex=ax3)
ax5=plt.subplot(gs[0],sharex=ax3)
ax2=plt.subplot(gs[5])
ax0=plt.subplot(gs[3],sharex=ax2)
ax4=plt.subplot(gs[1],sharex=ax2)

#ax2=plt.subplot(gs[0:,-1])
colors=[]
#for g in chrom: 
#    sg=chrom.index(g)
#    colors.append(cm.copper(int(70+sg*125/len(bisno))))
path0,path1,path2,path3,path4,path5=source+chrom[0],source+chrom[1],source+chrom[2],source+chrom[3],source+chrom[4],source+chrom[5]
#peaks position taken from the patter of CuCrO2
test0=pd.read_csv(path0, delimiter=' ',names=['2theta', 'Intensity','unc'],skiprows=1)
test1=pd.read_csv(path1, delimiter=' ',names=['2theta', 'Intensity','unc'],skiprows=1)
test2=pd.read_csv(path2, delimiter=' ',names=['2theta', 'Intensity','unc'],skiprows=1)
test3=pd.read_csv(path3, delimiter=' ',names=['2theta', 'Intensity','unc'],skiprows=1)
test4=pd.read_csv(path4, delimiter=' ',names=['2theta', 'Intensity','unc'],skiprows=1)
test5=pd.read_csv(path5, delimiter=' ',names=['2theta', 'Intensity','unc'],skiprows=1)


x0,x1,x2,x3,x4,x5=test0['2theta']-1.14,test1['2theta']-1.15,test2['2theta']-1.14,test3['2theta']-1.11,test4['2theta'],test5['2theta']
y0,y1,y2,y3,y4,y5=test0['Intensity']/max(test0['Intensity']),test1['Intensity']/max(test1['Intensity']),test2['Intensity']/max(test2['Intensity']),test3['Intensity']/max(test3['Intensity']),test4['Intensity']/max(test4['Intensity']),test5['Intensity']/max(test5['Intensity'])

ax0.plot(x0,y0,label=labby[0],linewidth=0.08*hsize_thesis,color=corz[0])
ax1.plot(x1,y1,label=labby[1],linewidth=0.08*hsize_thesis,color=corz[1])
ax2.plot(x2,y2,label=labby[2],linewidth=0.08*hsize_thesis,color=corz[2])
ax3.plot(x3,y3,label=labby[3],linewidth=0.08*hsize_thesis,color=corz[3])
ax4.plot(x4,y4,label=labby[4],linewidth=0.08*hsize_thesis,color=corz[4])
ax5.plot(x5,y5,label=labby[5],linewidth=0.08*hsize_thesis,color=corz[5])
    #plotting arrpws fpr CuCrO2 peaks
  #  xstr = [str(i) for i in x] 
  #  for j in cucro:
  #      for t in range(len(xstr)):
  #          if xstr[t].startswith(str(j)) and i==samples[0]:
  #              ax.annotate('',xy=(j,y[t]+0.02),xytext=(j,y[t]+0.12),arrowprops=dict(arrowstyle="->"))
  
#figure labels
ax0.text(0.62,0.75,labby[0],transform=ax0.transAxes,fontsize=hsize_thesis*1.4)
ax1.text(0.62,0.75,labby[1],transform=ax1.transAxes,fontsize=hsize_thesis*1.4)
ax2.text(0.65,0.75,labby[2],transform=ax2.transAxes,fontsize=hsize_thesis*1.4)  
ax3.text(0.65,0.75,labby[3],transform=ax3.transAxes,fontsize=hsize_thesis*1.4)  
ax4.text(0.725,0.75,labby[4],transform=ax4.transAxes,fontsize=hsize_thesis*1.4)  
ax5.text(0.725,0.75,labby[5],transform=ax5.transAxes,fontsize=hsize_thesis*1.4)  
  

#vertical lines to highlight the shifts due to doping and the position of Si  
LINES=False
if LINES:
    ax3.axvline(35.81,0,1,color='k')
    ax1.axvline(35.81,0,1,color='k')
    ax5.axvline(35.81,0,1,color='k')
    ax1.axvline(35.825,0,1,color='r')
    ax5.axvline(35.825,0,1,color='r')
    ax5.axvline(35.825,0,1,color='r')
    ax5.axvline(35.5,0,1,color='g',linestyle='--')
    ax5.axvline(35.98,0,1,color='g',linestyle='--')
    
    ax4.axvline(35.29,0,1,color='k')
    ax0.axvline(35.29,0,1,color='k') 
    ax0.axvline(35.52,0,1,color='r') 
    ax2.axvline(35.52,0,1,color='r') 
    ax2.axvline(35.78,0,1,color='b') 
    ax2.axvline(35.29,0,1,color='k')   



#plot limits
lim,Lim,tick_spacing=15,80,5
ax0.set_xlim(lim,Lim)
ax1.set_xlim(lim,Lim)
ax2.set_xlim(lim,Lim)
ax3.set_xlim(lim,Lim)
ax4.set_xlim(lim,Lim)
ax5.set_xlim(lim,Lim)
ax2.set_xticks(np.arange(lim,Lim,tick_spacing))
ax3.set_xticks(np.arange(lim,Lim,tick_spacing))


#ax2.set_xticks(None)
ax2.set_xlabel('2'+r'$\theta$ (°)',fontsize=hsize_thesis*1.3)
ax3.set_xlabel('2'+r'$\theta$ (°)',fontsize=hsize_thesis*1.3)
ax3.set_ylabel('Arbitrary units',fontsize=hsize_thesis*1.5)
ax0.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax1.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax2.tick_params(axis='both',labelsize=hsize_thesis*1)
ax3.tick_params(axis='both',labelsize=hsize_thesis*1.1)
ax4.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax5.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax3.yaxis.set_label_coords(-0.025, 1.6)
#ax.set_ylim(0,0.4)
#ax.legend(title='Bi content:', ncol=3,frameon=False)
#ax.tick_params(axis='both',labelsize=hsize_thesis*1.3)
#ax1.tick_params(axis='both',labelsize=hsize_thesis*1.3)
#ax2.tick_params(axis='both',labelsize=hsize_thesis*1.3,pad=hsize_thesis/4)#
#plt.tight_layout()


#putting indices labels on the peaks
si=[28.47,47.35,56.18,69.20,76.45]
for z in si:
    ax0.axvline(z,0,1,color='k',alpha=0.5,linestyle='--')
    ax1.axvline(z,0,1,color='k',alpha=0.5,linestyle='--')
    ax2.axvline(z,0,1,color='k',alpha=0.5,linestyle='--')
    ax3.axvline(z,0,1,color='k',alpha=0.5,linestyle='--')
   # ax3.text(x3[np.where(x3==min(x3, key=lambda x3:abs(x3-z)))[0][0]]-0.2,
   #           0.03+y3[np.where(x3==min(x3, key=lambda x3:abs(x3-z)))[0][0]],
   #           '*',fontsize=hsize_thesis*0.75,rotation=90)
zncr2=[(18.46,'(111)'),
       (30.36,'(220)'),
       (35.76,'(311)'),
       (37.41,'(222)'),
       (43.47,'(400)'),
       (53.94,r'$\mathrm{(2\bar{2}4)}$'),
       (57.51,r'$\mathrm{(1\bar{1}5)}$'),
       (63.16,r'$\mathrm{(40\bar{4})}$'),
       (71.68,'(260)'),
       (74.76,r'$\mathrm{(53\bar{3})}$'),
       (75.78,'(226)'),     
       ]
plane=False
if plane:
    for h in zncr2:
        if h[1]=='(311)':
            ax3.text(x3[np.where(x3==min(x3, key=lambda x3:abs(x3-h[0])))[0][0]]+0.3,
                      y3[np.where(x3==min(x3, key=lambda x3:abs(x3-h[0])))[0][0]],
                      h[1],fontsize=hsize_thesis*0.75,rotation=90)
        else:
            ax3.text(x3[np.where(x3==min(x3, key=lambda x3:abs(x3-h[0])))[0][0]]-0.3,
                      0.35+y3[np.where(x3==min(x3, key=lambda x3:abs(x3-h[0]-0.05)))[0][0]],
                      h[1],fontsize=hsize_thesis*0.75,rotation=90)
    #ax3.axvline(h[0],0,1)


plt.setp( ax0.get_yticklabels(), visible=False)
plt.setp( ax1.get_yticklabels(), visible=False)
plt.setp( ax2.get_yticklabels(), visible=False)
plt.setp( ax3.get_yticklabels(), visible=False)
plt.setp( ax4.get_xticklabels(), visible=False)
plt.setp( ax5.get_xticklabels(), visible=False)
plt.setp( ax4.get_yticklabels(), visible=False)
plt.setp( ax5.get_yticklabels(), visible=False)
plt.setp( ax0.get_xticklabels(), visible=False)
plt.setp( ax1.get_xticklabels(), visible=False)
#plt.setp( ax2.get_xticklabels(), visible=False)
plt.subplots_adjust(left=0.085, bottom=0.125, right=0.93, top=0.93,wspace=0.05, hspace=0.11)
#fig.savefig('C:/M_drive_docs/Thesis/graphics/chromites.pdf')
#fig.savefig('C:/M_drive_docs/Thesis/graphics/chromites.png')