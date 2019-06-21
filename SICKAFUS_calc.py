''' 
ASSUMPTIONS:
    -the formula from sickafus is valid
    - Mn in Td is Mn2+
    - Mn in Oh is Mn3+
    - Mn in Td is Mn2+
    - site chi (electronegativity) is defined as sum of weighed chi per occupant of site
    '''
    

    
r={
   'Cr':{'Oh':0.0615,'Td':None,'chi':1.66},
   'Mn2+':{'Oh':0.0083,'Td':0.066,'chi':1.55},
   'Mn3+':{'Oh':0.0645,'Td':None,'chi':1.55},
   'Cu':{'Oh':0.073,'Td':0.057,'chi':1.90},
   'Ti4+':{'Oh':0.0605,'Td':0.042,'chi':1.54},
   'Ti3+':{'Oh':0.067,'Td':None,'chi':1.54},
   'Li':{'Oh':0.076,'Td':0.059,'chi':0.98},
   'Ni':{'Oh':0.069,'Td':0.055,'chi':1.91},
   'Mg':{'Oh':0.072,'Td':0.057,'chi':1.31},
   'Zn':{'Oh':0.074,'Td':0.06,'chi':1.65},
   'O':{'Oh':0.14,'Td':0.138,'VIII':0.142,'chi':3.44},
   '':{'Oh':0,'Td':0,'chi':0}
   }

spini=[#OCTA,TETRA
       ['Cr','Mg'],
       ['Cr','Mn2+'],       
       ['Cr','Zn'],
       ['Cr','Ni'],
       ['Cr','Mg'],
       ['Ti3+','Mn2+'],
       ['Ti3+','Mg'],
       [['Ti3+','Ti4+'],'Li'],
       ]
for fg in spini:
    occ=0 #fraction of mn in Td site and therefore of DOP in Oh site
    dop=0 #doping level
    DOPANT='' #dopant element
    OCTA=fg[0] #Oh species
    TETRA=fg[1] #Td species
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
        chi_octaR=0.5*r[OCTA[0]]['chi']+0.5*r[OCTA[1]]['chi']
        OCTAname='('+OCTA[0]+OCTA[1]+ ')'
    else:
        octaR=r[OCTA]['Oh']
        chi_octaR=r[OCTA]['chi']
        OCTAname=OCTA
    r_oxy,chi_oxy=r['O']['Td'],r['O']['chi']
    tetra=r[TETRA]['Td']*(1+dop*(occ-1))+r[DOPANT]['Td']*(dop*(1-occ))
    chi_tetra=r[TETRA]['chi']*(1+dop*(occ-1))+r[DOPANT]['chi']*(dop*(1-occ))
    octa=(1-dop/2)*octaR+(dop/2)*(r[DOPANT]['Oh']*occ+r[TETRAOh]['Oh']*(1-occ))
    chi_octa=(1-dop/2)*chi_octaR+(dop/2)*(r[DOPANT]['chi']*occ+r[TETRAOh]['chi']*(1-occ))
    r_medio=0.33*tetra+0.67*octa
    a_SICKAFUS=0.5815+4.143*r_medio
    a_BRIK=1.27084*10*(tetra+r_oxy)+2.49867*10*(octa+r_oxy)+0.08640*(chi_oxy-chi_octa)+0.05141*(chi_oxy-chi_tetra)+0.60340
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
    print('a parameter (from Sickafus formula): ',round(a_SICKAFUS*10,5),' Å')
    print('a parameter (from Brick formula): ',round(a_BRIK,5),' Å')
    print()
    print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
    print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
    print()  