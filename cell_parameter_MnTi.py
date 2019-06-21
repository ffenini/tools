# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:09:52 2018

@author: filfe
"""





#source='C:/M_drive_docs/Lab/StAndrews/filippo/XRD/1010-MGT2/'

hsize_thesis=cm2inch(14)*2

vsize_thesis=(1.42*hsize_thesis)/1.42
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
plt.rcParams['axes.labelsize'] =1.3*hsize_thesis
plt.rcParams['axes.labelpad'] =0.1*hsize_thesis

figuresize=hsize_thesis,vsize_thesis
print()
print('FIGURE SIZE: ',figuresize[0],' x ',figuresize[1],'in')
print()
labby=[r'$\mathregular{MnTi_2O_4}$ after',r'$\mathregular{LiTi_2O_4}$ after',r'$\mathregular{LiTi_2O_4}$ before','$\mathregular{MnCu_{0.5}Cr_{1.5}}$','$\mathregular{NiCu_{0.5}Cr_{1.5}}$','$\mathregular{MnCr_{2}}$','$\mathregular{NiCr_{2}}}$']
w=255
g1,r1,g2,r2,g3,r3,c1,c2,c3=(204/w,0,0),(0,153/w,0),(204/w,102/w,0),(0,204/w,0),(102/w,150/w,0),(0,102/w,0),(124/w,8/w,225/w),(225/w,0/w,0/w),(255/w,119/w,0/w)
corz=[g1,g2,g3,r1,r2,r3]#print(chrom)
corzo=[(153/w,14/w,14/w),(53/w,227/w,227/w),c1,c2,c3,(227/w,204/w,53/w),(227/w,146/w,53/w),(102/w,0,0),(0,102/w,0)]
cucro=[31.33,36.27,40.73,55.75,65.37]
fig,ax=plt.subplots(figsize=(figuresize),sharex=True,facecolor='white')
gs = gridspec.GridSpec(1, 1,
                       width_ratios=[1],
                       height_ratios=[1]
                       )

X=[0,1]
a=[8.627,8.6803]
nu = sp.stats.linregress(X, a)
rangeX=np.linspace(0,1,10)
ax.plot(rangeX,nu[0]*rangeX+nu[1],linestyle='-', linewidth=0.075*hsize_thesis,color=r1,alpha=1)
ax.plot(0.1,8.628894,color='k', markersize=40)

for i in [8.628894,8.62966]:
    y=(i-nu[1])/nu[0]
    print(round(y,3),2-round(y,3))



