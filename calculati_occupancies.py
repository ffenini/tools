dop=0.25 ##doping level of Cu
coeff=1,round(dop,2),round(2-dop,2),4
formula='Mn'+str(coeff[0])+'Li'+str(coeff[1])+'Cr'+str(coeff[2])+'O4'
atomic=pt.formula(formula).atoms #dictionary with atoms and coefficient; access coeffiecient: atomic[pt.ELEMENTSYMBOL] (atomic[getattr(pt, key)]
m = pt.formula(formula)  
print(m)
Td,Oh,Ox=(8,1,0.24169),(16,2,0.1),(32,4,0.86898) #multiplicity, stoichiometry and Biso of the spinel sites. general AB2O4
col_width=10

#information required to compile the .pcr in full prof 
#entry=(Site, multiplicity of the site,stoichiometry of the site, stoichiometry doping, name, x,y,z,atom_type(FP),Biso(FP), ref_x,ref_y,ref_z,ref_Biso,ref_occ)
#####ref_ are the numbers indicating if a parameter is refined or not (ref_x  ref_y  ref_z  ref_Biso  ref_occ)  , same number means correlated refinement (opposite numbers, inversely correlated)
fullprof=[('Td',Td[0],Td[1],round(coeff[0]-dop,2),'Mn1',-0.125,-0.125,-0.125,'Mn+2',Td[2],0.00,0.00,0.00,0.00,0.00), 
       ('Td ¤1',Td[0],Td[1],round(dop,2),'Mn2',-0.125,-0.125,-0.125,'Mn+2',Td[2],0.00,0.00,0.00,0.00,201.00),
       ('Td ¤1',Td[0],Td[1],round(dop,2),'LiTd',-0.125,-0.125,-0.125,'Li+1',Td[2],0.00,0.00,0.00,0.00,-201.00),
       ('Oh ¤2',Oh[0],Oh[1],round(dop,2),'LiOh',0.5,0.5,0.5,'Li+1',Oh[2],0.00,0.00,0.00,0.00,211.00),
       ('Oh ¤2',Oh[0],Oh[1],round(dop,2),'Mn3',0.5,0.5,0.5,'Mn+3',Oh[2],0.00,0.00,0.00,0.00,-211.00),
       ('Oh',Oh[0],Oh[1],round(coeff[2],2),'Cr',0.5,0.5,0.5,'Cr+3',Oh[2],0.00,0.00,0.00,0.00,0.00),
       ('Ox',Ox[0],Ox[1],4,'O',0.26219,0.26219,0.26219,'O-2',Ox[2],0.00,0.00,0.00,0.00,0.00)]

print()
print('The competing species("¤") occupy the site equally at the beginning (half if two, 1/3 if three ...)')
print()
#info
print("%s%s%s%s%s%s%s%s  " % ('Site'.ljust(col_width),'Mult.'.ljust(col_width),'Stoich.'.ljust(col_width), 
                                'Element'.ljust(col_width),'x'.ljust(col_width),
                                'y'.ljust(col_width),'z'.ljust(col_width),'Occup.'.ljust(col_width)))
print()



tot_sym=192
for entry in fullprof:
    occucy=round(((entry[1]/tot_sym)*entry[3])/entry[2],5)##occupancy
    if '¤' in entry[0]:
        occucy=round((((entry[1]/tot_sym)*entry[3])/entry[2])/2,5)
    entry=entry+(occucy,) #concatenating tuples
    #print(entry)
    site,mult,site_stoch,stoich,element, x,y,z,at_type,biso,ref_x,ref_y,ref_z,ref_Biso,ref_occ,occ=entry

    #print(x,y,x)
    print("%s %s %s %s %s %s %s %s" % (site.ljust(col_width),str(mult).ljust(col_width),str(stoich).ljust(col_width),
                                    element.ljust(col_width),str(x).ljust(col_width),
                                    str(y).ljust(col_width),str(z).ljust(col_width),str(occ).ljust(col_width)))
    
print()
print('Fullprof .pcr entry')
#fullprof
print("%s%s%s%s%s%s%s%s%s%s%s%s  " % ('!Atom'.ljust(7),'Typ.'.ljust(6),'X'.rjust(9), 'Y'.rjust(9),
                                'Z'.rjust(9),'Biso'.rjust(9),'Occ'.rjust(10),'In'.rjust(4),
                                'Fin'.rjust(4),'N_t'.rjust(4),'Spc'.rjust(4),'/Codes'.rjust(5)))    
for entry in fullprof:
    occucy=round(((entry[1]/tot_sym)*entry[3])/entry[2],5)##occupancy
    if '¤' in entry[0]:
        occucy=round((((entry[1]/tot_sym)*entry[3])/entry[2])/2,5)
    entry=entry+(occucy,) #concatenating tuples
    #print(entry)
    site,mult,site_stoch,stoich,element, x,y,z,at_type,biso,ref_x,ref_y,ref_z,ref_Biso,ref_occ,occ=entry
#entry=(Site, multiplicity of the site,stoichiometry of the site, stoichiometry doping, name, x,y,z,atom_type(FP),Biso(FP), ref_x,ref_y,ref_z,ref_Biso,ref_occ)
    if occ==0:
        occ_p='0.'
    else:
        occ_p=occ
    #print(x,y,x)
    print("%s%s%s  %s  %s  %s   %s%s%s%s%s  " % (element.ljust(7),at_type.ljust(8),str(x).ljust(7,'0'),str(y).ljust(7,'0'),str(z).ljust(7,'0'),
                                    str(biso).ljust(7,'0'),str(occ).ljust(7,'0'),'0'.rjust(4),'0'.rjust(4),'0'.rjust(4),'0'.rjust(5)))
    if ref_x==0.00:
        ref_x_p='0.00'
    else:
       ref_x_p=str(ref_x) 
    if ref_y==0.00:
        ref_y_p='0.00'
    else:
       ref_y_p=str(ref_y)
    if ref_z==0.00:
        ref_z_p='0.00'
    else:
       ref_z_p=str(ref_z) 
    if ref_Biso==0.00:
        ref_biso_p='0.00'
    else:
       ref_biso_p=str(ref_Biso) 
    if ref_occ==0.00:
        ref_occ_p='0.00'
    else:
       ref_occ_p=str(ref_occ) 
       
    print("%s%s%s%s%s" % (ref_x_p.rjust(22),ref_y_p.rjust(9),ref_z_p.rjust(9),ref_biso_p.rjust(9),ref_occ_p.rjust(10)))