# -*- coding: utf-8 -*-
for g in [0.5,1,1.5,2,3,4,5]:
    Bi=g
    Sn=100-Bi
    O_bi=Bi*1.5
    O_sn=Sn*2
    mass_bi2o3=Bi*pt.Bi.mass+O_bi*pt.O.mass
    mass_sno2=Sn*pt.Sn.mass+O_sn*pt.O.mass
    perc_bi2o3=mass_bi2o3*100/(mass_bi2o3+mass_sno2)
    #print( round(perc_bi2o3,1))
    
print()
for g in [0.5,1,1.5,2,3,4,5]:
    Bi=g
    Sn_pyro=Bi
    Sn=100-Bi-Sn_pyro
    O_pyro=Bi*3.5
    O_sn=Sn*2
    mass_pyro=Bi*pt.Bi.mass+O_pyro*pt.O.mass+Sn_pyro*pt.Sn.mass
    mass_sno2=Sn*pt.Sn.mass+O_sn*pt.O.mass
    perc_pyro=mass_pyro*100/(mass_pyro+mass_sno2)
    print(round(perc_pyro,1))