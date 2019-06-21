data = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['', 'bbbbbbbbbb', 'c']]

col_width = max(len(word) for row in data for word in row) + 2  # padding
#print(col_width)
#for row in data:
   # print(row,'\a')
    #print("".join(word.ljust(col_width) for word in row))
    #print("This is row %d and weight is %d kg!" % (data.index(row), 'jhdjhdj'))

dop=0.5
coeff=1,round(dop,2),round(2-dop,2),4
formula='Mn'+str(coeff[0])+'Cu'+str(coeff[1])+'Cr'+str(coeff[2])+'O4'
atomic=pt.formula(formula).atoms #dictionary with atoms and coefficient; access coeffiecient: atomic[pt.ELEMENTSYMBOL] (atomic[getattr(pt, key)]
m = pt.formula(formula)  
print(m)
Td,Oh,Ox=(8,1),(16,2),(32,4) #multiplicity  and stoichiometry of the spinel sites. general AB2O4
col_width=10
compt=[('Td',Td[0],Td[1],round(coeff[0]-dop,2),'Mn1',0.125,0.125,0.125),
       ('Td ¤1',Td[0],Td[1],round(dop,2),'Mn2',0.125,0.125,0.125),
       ('Td ¤1',Td[0],Td[1],round(dop,2),'CuTd',0.125,0.125,0.125),
       ('Oh ¤2',Oh[0],Oh[1],round(dop,2),'CuOh',0.5,0.5,0.5),
       ('Oh ¤2',Oh[0],Oh[1],round(dop,2),'Mn3',0.5,0.5,0.5),
       ('Oh',Oh[0],Oh[1],round(coeff[2],2),'Cr',0.5,0.5,0.5),
       ('Ox',Ox[0],Ox[1],4,'O',0.26227,0.26227,0.26227)]
print()
print('The competing species("¤") occupy the site equally at the beginning (half if two, 1/3 if three ...)')
print()
print("%s %s %s %s %s %s %s %s" % ('Site'.ljust(col_width),'Mult.'.ljust(col_width),'Stoich.'.ljust(col_width), 
                                'Element'.ljust(col_width),'x'.ljust(col_width),
                                'y'.ljust(col_width),'z'.ljust(col_width),'Occup.'.ljust(col_width)))
print()
tot_sym=192
for entry in compt:
    occucy=round(((entry[1]/tot_sym)*entry[3])/entry[2],5)##occupancy
    if '¤' in entry[0]:
        occucy=round((((entry[1]/tot_sym)*entry[3])/entry[2])/2,5)
    entry=entry+(occucy,) #concatenating tuples
    #print(entry)
    site,mult,site_stoch,stoich,element, x,y,z,occ=entry

    #print(x,y,x)
    print("%s %s %s %s %s %s %s %s" % (site.ljust(col_width),str(mult).ljust(col_width),str(stoich).ljust(col_width),
                                    element.ljust(col_width),str(x).ljust(col_width),
                                    str(y).ljust(col_width),str(z).ljust(col_width),str(occ).ljust(col_width)))