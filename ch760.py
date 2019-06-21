
# coding: utf-8




import pandas as pd
import numpy as np
import scipy as sp
import matplotlib
import matplotlib.pyplot as plt
from pylab import *  ##### in order to use the MATLAB-like API
import os
#get_ipython().magic('matplotlib inline')


def ch760_impi(rfi='', rs='txt',rfo='',cfi='', cs='ch760',cfo='',pr_ph=False, pr_fdl=False):  
    '''INPUT: ch760_gen(
    
    rfi='raw filename' 
    
    rs='extension of the file (txt default)'
    
    rfo='raw file folder path',cfi='converted filename'
    
    cs='extension of the converted file (txt default)'
    
    cfo='converted file folder'
    
    pr_ph= if True print the path of the converted file (default false)
    
    pr_fdl= Print the number of the line with the first data and prints the first row values
    
    )
    The script takes as input the path and the name we want to give to the file, 
    produces a new file with only the columns and
    the column headers as the 1st row;
    If 'Scan rate' is present in the file, adds a new column on the right called 'Time/s' and the time in second per line
    gives the first data line and the headers and the path of the created file as an input'''   
    raw_path=os.path.join(rfo, rfi + '.' + rs)
    raw_open=open(raw_path)####the file needs to be open
    raw_lines=raw_open.readlines()
    scan_rate=False
    for i in range(len(raw_lines)):
        juice=raw_lines[i]
        if 'Scan Rate (V/s)' in juice:
            scn=float(juice.replace("Scan Rate (V/s) = ",""))
            scan_rate=True ####Triggers the cycle for affing the time line
        else:
            if 'Sample Interval (V)' in juice:
                sdff=float(juice.replace("Sample Interval (V) = ",""))
            else:
                if 'Freq/'  in juice or 'Potential/V' in juice or 'Time/sec' in juice:  #### finds the line in which are the headers in CH EIS and CV files files
                    c=i+2
                    j=i
                    if pr_fdl==True:
                        print('First daTta line: '+str(c))#### lns[i] con i maggiore di first_data_line = data
                        print(raw_lines[c])#### lns[i] con i minore di first data = headers               
                else:
                    continue    
    
            
    if scan_rate: ####activates the insertion of the Time column only if scan_rate has been turned to True by the presence of the 'Scan rate' row
        a=raw_lines[j].replace("\n","")+'\tTime/s\n'
        b=raw_lines[c:]
        b.append(a)#inserts the headers at the end of the rows
        b.insert(0, b[len(b)-1])#copies the header row as first row
        del[b[len(b)-1]]#delete the original header row (last row)
        for i in range(len(b)):
            if i>0:
                b[i]=b[i].replace("\n","")
                b[i]= b[i]+'\t'+str(str(0+(i-1)*(sdff/scn))+'\n')
    else:
        a=raw_lines[j] 
        if 'Time/sec' in a:
            a=a.replace("Time/sec","Time/s")
        b=raw_lines[c:]
        b.append(a)
        b.insert(0, b[len(b)-1])
        del[b[len(b)-1]]   
        
    conv_path=os.path.join(cfo, cfi + '.'+ cs)
    if pr_ph==True:
        print(str(conv_path))       
    
    with open(conv_path,'w') as cav:         
        for i in range(len(b)):
            cav.write(b[i])
            

path='C:/M_drive_docs/Lab/RDE/180303'
make=os.listdir(path)
for file in make:  
    if file.endswith('.txt'):   
        name=str(file).replace('.txt','')
        ch760_impi(rfi=name,rfo=path,cfi=name,cfo=path)
        
 
ciao=False  
if ciao:
    print('Cr%at', 'MN%at','Cr/Mn', 'single point composition')
    print()
    aV,bV,ratV,xMnV,xCrV=[],[],[],[],[]# containers for single point values as a list, to be averaged later
    for i in range(len(NiCr2bef)):
        a,b,c=MnCu25bef[i]['C_atom_atperc']['Cr'],MnCu25bef[i]['C_atom_atperc']['Mn'],MnCu25bef[i]['C_atom_atperc']['Cu'] # %at of Cr and Ni and CU
        rat=a/b #ratio Cr/Mn
        rat2=c/b #ratio Cu/Mn
        cMn,qMn,cCr,qCr,cCu,qCu=1,2,rat,3,rat2,2#coefficient 'c' (and ionic charges 'q')of a formula where Mn is unitary
        oxy=(cMn*qMn+cCr*qCr+cCu*qCu)/2 #number of oxygen atoms(charge 2) necessary to compensate the cationic charges from formula
        coeff=4/oxy # coefficient to refer the formula to 4 oxygen atoms (spinel structure)
        sep,xMn,xCr,xCu=' ',round(coeff*cMn,2),round(coeff*cCr,2),round(coeff*cCu,2) #separator, and coefficeint for a spinel formula
        form=['Mn',str(xMn),'Cu',str(xCu),'Cr',str(xCr),'O',str(round(coeff*oxy,2))]
        composition=sep.join(form)
        aV.append(a)
        bV.append(b)
        ratV.append(rat)
        xMnV.append(xMn)
        xCrV.append(xCr)
        print(a,b,c,round(rat,3),composition)
    print()
    fCu=round(np.mean(xMnV),2)# averaged coefficient NI
    fCr=round(np.mean(xCrV),2)# averaged coefficient Cr
    print()
    print(' if Mn=2+ AVERAGE COMPOSITION: Ni',fNi,'Cr',fCr,'O',str(round(coeff*oxy,2)))

