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
   'Cu2+':{'Oh':0.073,'Td':0.057},
   'Ti4+':{'Oh':0.0605,'Td':0.042},
   'Ti3+':{'Oh':0.067,'Td':None},
   'Li':{'Oh':0.076,'Td':0.059},
   'Ni':{'Oh':0.069,'Td':0.055},
   'Mg':{'Oh':0.072,'Td':0.057}
   }
r.keys()
spin={
        'MnCr2':{'tetra':['Mn2+'],'octa':['Cr'],'t_c': [1],'t_o': [1]},
        'NiCr2':{'tetra':['Ni'],'octa':['Cr'],'t_c': [1],'t_o': [1]},
        'MgTi2':{'tetra':['Mg'],'octa':['Ti3+'],'t_c': [1],'t_o': [1]},
        'MnTi2':{'tetra':['Mn2+'],'octa':['Ti3+'],'t_c': [1],'t_o': [1]},
        'LiTi2':{'tetra':['Mn2+'],'octa':['Ti3+','Ti4+'],'t_c': [1],'t_o': [0.5,0.5]},
        }
print(' a parameter (from Sickafus formula): ')
for s in spin:
    tetra=[]
    for t in range(len(spin[s]['tetra'])):
        print(t)
        tetra.append(r[spin[s]['tetra'][t]]['Td']*spin[s]['t_c'][t])
    tetra=sum(tetra)
    octa=[]
    for o in range(len(spin[s]['octa'])):
        print(j)
        octa.append(r[spin[s]['octa'][o]]['Oh']*spin[s]['t_o'][o])
    octa=sum(octa)
    r_medio=0.33*tetra+0.67*octa
    a=0.5815+4.143*r_medio
    print()
    print(s,round(a*10,5),' nm')
    print()
