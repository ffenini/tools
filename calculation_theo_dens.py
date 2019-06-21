dens_meas=3.158
NAv=sp.constants.value('Avogadro constant')
a=8.3063 #cell param in Å
oxy=32 #number of O anions per spinel cell
td=8 #number of Td cations per spinel cell
oh=16 #number of Oh cations per spinel cell
O=pt.O.mass
mg=pt.Mg.mass
cr=pt.Cr.mass
fe=pt.Fe.mass
ni=pt.Ni.mass
zn=pt.Zn.mass
grO=oxy*O/NAv #grams of oxygen per cryst cell
grTd=td*fe/NAv #grams of Mg per cryst cell
grOh=0.5*oh*cr/NAv+0.5*oh*ni/NAv #grams of Cr per cryst cell
dens=(grO+grTd+grOh)/(a*1e-8)**3
dens_eff=dens_meas*100/dens
print(dens,'g/cm3 THEO')
print(dens_eff,' % of theo density')
''' 
ASSUMPTIONS:
    -the formula from sickafus is valid
    - Mn in Td is Mn2+
    - Mn in Oh is Mn3+
- Mn in Td is Mn2+
-
    '''
    

    
r={
   'Cr':{'Oh':0.0615,'Td':None},
   'Mn2+':{'Oh':0.0083,'Td':0.066},
   'Mn3+':{'Oh':0.0645,'Td':None},
   'Cu':{'Oh':0.073,'Td':0.057},
   'Ti4+':{'Oh':0.0605,'Td':0.042},
   'Ti3+':{'Oh':0.067,'Td':None},
   'Li':{'Oh':0.076,'Td':0.059},
   'Ni':{'Oh':0.069,'Td':0.055},
   'Mg':{'Oh':0.072,'Td':0.057},
   '':{'Oh':0,'Td':0}
   }

spini=[#OCTA,TETRA
       ['Cr','Mg'],
       ['Cr','Mn2+'],       
       ['Cr','Zn'],
       ['Cr','Ni'],
       ['Cr','Mg'],
       ]

occ=0 #fraction of mn in Td site and therefore of DOP in Oh site
dop=0 #doping level
DOPANT='' #dopant element
OCTA='Cr' #Oh species
TETRA='Mg' #Td species
print()
print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
print('¤¤¤¤¤¤¤¤ SICKAFUS CALCULATION OF a ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
print()
TETRAOh='' #state of Td species when in Oh site
if TETRAOh=='':
    TETRAOh=TETRA

if isinstance(OCTA, list):
    octaR=0.5*r[OCTA[0]]['Oh']+0.5*r[OCTA[1]]['Oh']
    OCTAname='('+OCTA[0]+OCTA[1]+ ')'
else:
    octaR=r[OCTA]['Oh']
    OCTAname=OCTA
tetra=r[TETRA]['Td']*(1+dop*(occ-1))+r[DOPANT]['Td']*(dop*(1-occ))
octa=(1-dop/2)*octaR+(dop/2)*(r[DOPANT]['Oh']*occ+r[TETRAOh]['Oh']*(1-occ))
r_medio=0.33*tetra+0.67*octa
a=0.5815+4.143*r_medio
if DOPANT=='':
    formula='('+TETRA+str(1-dop+occ*dop)+') ['+OCTAname+str(2-dop)+TETRAOh+str(dop*(1-occ))+' ]'
else:
    formula='('+TETRA+str(1-dop+occ*dop)+DOPANT+str((1-occ)*dop)+') ['+OCTAname+str(2-dop)+TETRAOh+str(dop*(1-occ))+DOPANT+str(dop*(occ))+' ]'
print()
print('DOP: '+DOPANT)
print('medium Oh radius (nm) : ',octa)
print('medium Td radius (nm) : ',tetra)
print('medium radius (nm) : ',r_medio)
print(formula)
print('a parameter (from Sickafus formula): ',round(a,5),' nm')
print()
print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
print()  
hsize_thesis=cm2inch(14)*4
vsize_thesis=(1.42*hsize_thesis)/4
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



w=255
corz=[(0,120/w,153/w),(0,153/w,0),(204/w,102/w,0),(0,204/w,0),(102/w,0,0),(0,102/w,0)]
figuresize=hsize_thesis,vsize_thesis
print()
print('FIG. SIZE: ',round(figuresize[0],2),'in(w) x ',round(figuresize[1],2),'in(h)')
print()
fig,(ax,ax1)=plt.subplots(1,2,figsize=(figuresize),sharex=True,facecolor='w')
ax=plt.subplot(121)
ax1=plt.subplot(122)

g1,r1,g2,r2,g3,r3,c1,c2,c3=(204/w,0,0),(0,153/w,0),(204/w,102/w,0),(0,204/w,0),(102/w,0,0),(0,102/w,0),(124/w,8/w,225/w),(225/w,0/w,0/w),(255/w,119/w,0/w)
corz=[(g1,g2),(r1,r2),g3,r3,g2,r2,g2,g1,g2,g3,r1,r2,g3]#print(chrom)

cells_param=[(8.4176,8.380178),(8.382312,8.321347)]
occupancy=np.arange(0,1.05,0.05)
dopants=['Cu']
for DPP in dopants:
    tri=dopants.index(DPP)
    doping=[0.25,0.5]
    for dope in doping:
        tre=doping.index(dope)
        cell=[]
        for i in occupancy:
            occ=i #fraction of mn in Td site and therefore of DOP in Oh site
            dop=dope #doping level
            DOPANT=DPP
            OCTA='Cr' #Oh species
            TETRA='Mn2+' #Td species
            TETRAOh='Mn3+' #state of Td species when in Oh site
            if TETRAOh=='':
                TETRAOh=TETRA
            if isinstance(OCTA, list):
                octaR=0.5*r[OCTA[0]]['Oh']+0.5*r[OCTA[1]]['Oh']
                OCTAname='('+OCTA[0]+OCTA[1]+ ')'
            else:
                octaR=r[OCTA]['Oh']
                OCTAname=OCTA
            tetra=r[TETRA]['Td']*(1+dop*(occ-1))+r[DOPANT]['Td']*(dop*(1-occ))
            octa=(1-dop/2)*octaR+(dop/2)*(r[DOPANT]['Oh']*occ+r[TETRAOh]['Oh']*(1-occ))
            r_medio=0.33*tetra+0.67*octa
            a=0.5815+4.143*r_medio           
            cell.append(a)
        ax.plot(occupancy, cell,label='D='+DPP+', d='+str(dope),color=corz[tri][tre])
        ax.axhline(0.1*cells_param[tri][tre],0,1,color=corz[tri][tre],linestyle='--')
        
dopants=['Li']
for DPP in dopants:
    tri=dopants.index(DPP)
    doping=[0.25,0.5]
    for dope in doping:
        tre=doping.index(dope)
        cell=[]
        for i in occupancy:
            occ=i #fraction of mn in Td site and therefore of DOP in Oh site
            dop=dope #doping level
            DOPANT=DPP
            OCTA='Cr' #Oh species
            TETRA='Mn2+' #Td species
            TETRAOh='Mn3+' #state of Td species when in Oh site
            if TETRAOh=='':
                TETRAOh=TETRA
            if isinstance(OCTA, list):
                octaR=0.5*r[OCTA[0]]['Oh']+0.5*r[OCTA[1]]['Oh']
                OCTAname='('+OCTA[0]+OCTA[1]+ ')'
            else:
                octaR=r[OCTA]['Oh']
                OCTAname=OCTA
            tetra=r[TETRA]['Td']*(1+dop*(occ-1))+r[DOPANT]['Td']*(dop*(1-occ))
            octa=(1-dop/2)*octaR+(dop/2)*(r[DOPANT]['Oh']*occ+r[TETRAOh]['Oh']*(1-occ))
            r_medio=0.33*tetra+0.67*octa
            a=0.5815+4.143*r_medio           
            cell.append(a)
        ax1.plot(occupancy, cell,label='D='+DPP+', d='+str(dope),color=corz[tri+1][tre])
        ax1.axhline(0.1*cells_param[tri+1][tre],0,1,color=corz[tri+1][tre],linestyle='--')
#ax.set_xticks(np.arange(0,1.1,0.1))
#ax1.set_xticklabels(atoms,fontsize=0.75*hsize_thesis)
#ax.set_xticks(np.arange(0,11,1))
ax1.set_xlabel('Fraction of D in $O_h$ site ')
ax.set_xlabel('x')
f_tit=r'$\mathregular{(Mn^{II}_{1+d(x-1)}D_{d(1-x)})[Cr_{2-d}Mn^{III}_{d(1-x)}D_{dx}]}$'
plt.suptitle(f_tit,fontsize=1.2*hsize_thesis)
#ax.annotate(f_tit,( 0.3, 0.848),fontsize=1.2*hsize_thesis)
#ml=MultipleLocator(0.01)# set the distance of the minor thicks,, based on the arugument of the axis
#Ml=MultipleLocator(0.05)# set the distance of the minor thicks, based on the arugument of the axis
#ax1.yaxis.set_major_locator(Ml)
#ax1.yaxis.set_minor_locator(ml)
ax.legend(frameon=False,fontsize=0.9*hsize_thesis)
ax1.legend(frameon=False,fontsize=0.9*hsize_thesis)