

source='C:/M_drive_docs/Lab/MaterialsSynth/XRD/MCr2O4/'

hsize_thesis=cm2inch(21.4)*4
vsize_thesis=hsize_thesis/2
plt.rcParams['axes.linewidth'] = 0.07*hsize_thesis
plt.rcParams['axes.labelsize'] =1.6*hsize_thesis
#fig,ax=plt.subplots(figsize=(hsize_thesis,vsize_thesis))



chrom=list_files1(source,'xy')
labby=['MgCr$_2$O$_4$','NiFeCrO$_4$','NiCr$_2$O$_4$','ZnCr$_2$O$_4$']
#print(chrom)
cucro=[31.33,36.27,40.73,55.75,65.37]
fig,(ax0,ax1,ax2,ax3)=plt.subplots(1,4,figsize=(hsize_thesis,vsize_thesis),sharex=True)
gs = gridspec.GridSpec(4, 1,
                       width_ratios=[1],
                       height_ratios=[ 1,1,1,1]
                       )
ax3=plt.subplot(gs[3])
ax3.set_xticks(np.arange(10,90,5))
ax0=plt.subplot(gs[0],sharex=ax3)
ax1=plt.subplot(gs[1],sharex=ax3)
ax2=plt.subplot(gs[2],sharex=ax3)

#ax2=plt.subplot(gs[0:,-1])
colors=[]
#for g in chrom: 
#    sg=chrom.index(g)
#    colors.append(cm.copper(int(70+sg*125/len(bisno))))
path0,path1,path2,path3=source+chrom[0],source+chrom[1],source+chrom[2],source+chrom[3]
#peaks position taken from the patter of CuCrO2
test0=pd.read_csv(path0, delimiter=' ',names=['2theta', 'Intensity'],skiprows=1)
test1=pd.read_csv(path1, delimiter=' ',names=['2theta', 'Intensity'],skiprows=1)
test2=pd.read_csv(path2, delimiter=' ',names=['2theta', 'Intensity'],skiprows=1)
test3=pd.read_csv(path3, delimiter=' ',names=['2theta', 'Intensity'],skiprows=1)
x0,x1,x2,x3=test0['2theta'],test1['2theta'],test2['2theta'],test3['2theta']
y0,y1,y2,y3=test0['Intensity']/max(test0['Intensity']),test1['Intensity']/max(test1['Intensity']),test2['Intensity']/max(test2['Intensity']),test3['Intensity']/max(test3['Intensity'])

ax0.plot(x0,y0,label=labby[0],linewidth=0.08*hsize_thesis,color='k')
ax1.plot(x1,y1,label=labby[1],linewidth=0.08*hsize_thesis,color='g')
ax2.plot(x2,y2,label=labby[2],linewidth=0.08*hsize_thesis,color='r')
ax3.plot(x3,y3,label=labby[3],linewidth=0.08*hsize_thesis,color='b')
    #plotting arrpws fpr CuCrO2 peaks
  #  xstr = [str(i) for i in x] 
  #  for j in cucro:
  #      for t in range(len(xstr)):
  #          if xstr[t].startswith(str(j)) and i==samples[0]:
  #              ax.annotate('',xy=(j,y[t]+0.02),xytext=(j,y[t]+0.12),arrowprops=dict(arrowstyle="->"))
  
#figure labels
ax0.text(0.02,0.75,labby[0],transform=ax0.transAxes,fontsize=hsize_thesis*1.6)
ax1.text(0.02,0.75,labby[1],transform=ax1.transAxes,fontsize=hsize_thesis*1.6)
ax2.text(0.02,0.75,labby[2],transform=ax2.transAxes,fontsize=hsize_thesis*1.6)  
ax3.text(0.02,0.75,labby[3],transform=ax3.transAxes,fontsize=hsize_thesis*1.6)  
  
  
  
  
ax0.set_xlim(20,80)
ax1.set_xlim(20,80)
ax2.set_xlim(20,80)
ax3.set_xlim(20,80)
ax3.set_xticks(np.arange(10,85,5))
#ax2.set_xticks(None)
ax3.set_xlabel('2'+r'$\theta$ (°)',fontsize=hsize_thesis*1.5)
ax3.set_ylabel('Arbitrary units',fontsize=hsize_thesis*1.5)
ax0.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax1.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax2.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax3.tick_params(axis='both',labelsize=hsize_thesis*1.3)
ax3.yaxis.set_label_coords(-0.025, 2)
#ax.set_ylim(0,0.4)
#ax.legend(title='Bi content:', ncol=3,frameon=False)
#ax.tick_params(axis='both',labelsize=hsize_thesis*1.3)
#ax1.tick_params(axis='both',labelsize=hsize_thesis*1.3)
#ax2.tick_params(axis='both',labelsize=hsize_thesis*1.3,pad=hsize_thesis/4)#
#plt.tight_layout()


#putting indices labels on the peaks
si=[28.47,47.35,56.18,69.20,76.45]
for z in si:
    ax3.text(x3[np.where(x3==min(x3, key=lambda x3:abs(x3-z)))[0][0]]-0.2,
              0.03+y3[np.where(x3==min(x3, key=lambda x3:abs(x3-z)))[0][0]],
              '*',fontsize=hsize_thesis*0.75,rotation=90)
zncr2=[(18.46,'(111)'),
       (30.36,'(220)'),
       (35.76,'(311)'),
       (37.41,'(222)'),
       (43.47,'(400)'),
       (53.94,r'$\mathregular{(2\bar{2}4)}$'),
       (57.51,r'$\mathregular{(1\bar{1}5)}$'),
       (63.16,r'$\mathregular{(40\bar{4})}$'),
       (71.68,'(260)'),
       (74.76,r'$\mathregular{(53\bar{3})}$'),
       (75.78,'(226)'),     
       ]
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
plt.setp( ax0.get_xticklabels(), visible=False)
plt.setp( ax1.get_xticklabels(), visible=False)
plt.setp( ax2.get_xticklabels(), visible=False)
plt.subplots_adjust(left=0.085, bottom=0.125, right=0.93, top=0.93,wspace=0.26, hspace=0.2025)
fig.savefig('C:/M_drive_docs/Thesis/graphics/chromites.pdf')
fig.savefig('C:/M_drive_docs/Thesis/graphics/chromites.png')