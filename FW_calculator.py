def FW(form):
    ''' 
    Formula weigth calculator:
        
    REQUIRED MODULES:
        Numpy, Scipy, periodictable
    
    INPUT: Name of element followed by _stoich. coeff_ , 
    stoichiometric coefficient surrounded by '_' on both sides.
    Fractions (a/b), integers and floats are valid inputs
    Input example :
    water: H_2_O_1
    Percloric acid: H_1_Cl_1_O_4
    Chromia: Cr_2_O_3
    
    OUTPUT:
        Dictionary:
           {'formula':chemical formula,'FW': formula weight in g/mol} 
           
    Example:
        input:
            >>water=FW(H_2_O_1)
            >>print(water['formula'])
            >>print(water['FW'])
        output:
            >>H (2.0) O (1.0)  
            >>18.02
    '''
    import scipy as sp
    import numpy as np
    import periodictable as pt
    form=form.split('_')
    formula,weigth,perc,percentages='',[],[],[]
    for i in range(len(form)):
        if i%2==0:
            formula=formula+form[i]
            percentages.append([form[i]])
        else:
            if '/' in form[i]:
                frac=form[i].split('/')
                stoich=float(float(frac[0])/float(frac[1]))
                perc.append(stoich)
                weigth.append(getattr(pt,form[i-1]).mass*stoich)
            else:
                stoich=float(form[i])
                perc.append(stoich)
                weigth.append(getattr(pt,form[i-1]).mass*stoich)
            formula=formula+' ('+str(round(stoich,3))+') '
    tot=sum(perc)
    FW=round(sum(weigth),2)
    for z in range(len(weigth)):       
        percentages[z].insert(1,round(weigth[z]/FW*100,2))
    return {'formula':formula,'FW':FW,'mass %':percentages}
          
