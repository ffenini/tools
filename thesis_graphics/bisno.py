hsize_thesis=cm2inch(21.4)
vsize_thesis=hsize_thesis*0.5
spines_ticks_width=0.1*hsize_thesis
plt.rcParams['axes.linewidth'] = spines_ticks_width
plt.rcParams['axes.labelsize'] =1.6*hsize_thesis

figu_numx,figu_numy,fig_num_size=0.94, 1.05,2.5*hsize_thesis
fig,(ax,ax2,ax3,ax4)=plt.subplots(1,4,figsize=(hsize_thesis,vsize_thesis),facecolor='w',edgecolor='w',frameon=True)

gs = gridspec.GridSpec(2, 2,
                       width_ratios=[1, 2],
                       height_ratios=[2.5, 1],
                       hspace=0.08)
ax = plt.subplot(gs[0:2])
#ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2:4])
#ax4 = plt.subplot(gs[3])


###plot 1 
source='C:/M_drive_docs/Lab/MaterialsSynth/XRD/SnO2/BsnO2_new_samples/fixed/'
#bisno=os.listdir(source)
bisno=list_files1(source,'xy')
pyro=[28.89,33.485,48.067,57.10]
si=[28.467,47.346,56.175]
siy=[1.575,1.575,1.575]
colors=[]
for x in pyro:
    ax.axvline(x,-3,3,lInestyle='--',color='r',alpha=0.35,linewidth=0.085*hsize_thesis)
for g in bisno: 
    sg=bisno.index(g)
    colors.append(cm.copper(int(70+sg*125/len(bisno))))
    path=source+g
    if sg==0:
        ax.scatter(si,siy,s=2,marker='*',color='k')
    #peaks position taken from the patter of CuCrO2
    test=pd.read_csv(path, delimiter=' ',names=['2theta', 'Intensity','Error'],skiprows=1)
    x=test['2theta']
    y=test['Intensity']/max(test['Intensity'])
    labby=g[0]+'.'+g[1]+' %at'
    if g==bisno[0]:
        labby='pure SnO$_2$'
    ax.plot(x,y+1.5-0.2*sg,label=labby,linewidth=0.09*hsize_thesis,color=colors[sg])

source='C:/M_drive_docs/Lab/MaterialsSynth/XRD/SnO2/BsnO2_new_samples/'
#bisno=os.listdir(source)
g='Bi2Sn2O7_exported.dat'
path=source+g
#peaks position taken from the patter of CuCrO2
test=pd.read_csv(path, delimiter=' ',names=['2theta', 'Intensity','Error'])
x=test['2theta']
y=test['Intensity']/max(test['Intensity'])
ax3.plot(x,y,label='Bi$_2$Sn$_2$O$_7$',linewidth=0.09*hsize_thesis,color='r')


ax.set_xlim(10,140)
ax3.set_xlim(10,140)
#ax.set_xlabel('2'+r'$\theta$ (°)',fontsize=hsize_thesis*1.6)
ax.set_ylabel('Arbitrary units',fontsize=hsize_thesis*1.6)
ax.tick_params(axis='both',labelsize=hsize_thesis*1.3)
lg=ax.legend(title='Bi content:',ncol=3,frameon=False,fontsize=hsize_thesis*1.1)
lg.get_title().set_fontsize(hsize_thesis*1.4)
ax3.set_xlabel('2'+r'$\theta$ (°)',fontsize=hsize_thesis*1.6)
ax3.set_ylabel('Arbitrary units',fontsize=hsize_thesis*1.6)
lg=ax3.legend(title=None,ncol=3,frameon=False,fontsize=hsize_thesis*1.2)

#ticks and ticks labels
majorLocator = MultipleLocator(10)
minorLocator = MultipleLocator(5)
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_minor_locator(minorLocator)
ax3.xaxis.set_major_locator(majorLocator)
ax3.xaxis.set_minor_locator(minorLocator)
ax.tick_params(axis='y',which='major',width=0.1*hsize_thesis,length=0.5*hsize_thesis,labelsize=hsize_thesis*1.3)
ax.tick_params(axis='x',which='major',width=0.1*hsize_thesis,length=0.5*hsize_thesis,labelsize=hsize_thesis*1.3,labelcolor='w')
ax.tick_params(axis='both',which='minor',width=0.1*hsize_thesis,length=0.3*hsize_thesis,labelsize=hsize_thesis*1.3)
ax3.tick_params(axis='both',which='major',width=0.1*hsize_thesis,length=0.5*hsize_thesis,labelsize=hsize_thesis*1.3)
ax3.tick_params(axis='both',which='minor',width=0.1*hsize_thesis,length=0.3*hsize_thesis,labelsize=hsize_thesis*1.3)
xticks=np.arange(10,150,10).tolist()
ax.set_xticks(xticks)
xticks3=np.arange(10,150,10).tolist()
ax3.set_xticks(xticks3)
yticks3=[0.0,0.5]
ax3.set_yticks(yticks3)
plt.subplots_adjust(left=0.085, bottom=0.15, right=0.91, top=0.99,wspace=0.24, hspace=0.25) #set the distance between the plot
fig.savefig('C:/M_drive_docs/Thesis/graphics/bisno.png')
fig.savefig('C:/M_drive_docs/Thesis/graphics/bisno.pdf')