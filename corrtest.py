from  header import *

'''
    
entry (tuple): 
    - entry_[0]=date,str
    - entry_powder[1]='powder' or 'pellet'
    - entry_powder[2]= material name,str
    - entry_powder[3]= weight powder/pellet before in grams, float
    - entry_powder[4]= weight filter before in grams for 'powder'/ 0 for 'pellet' , float
    - entry_powder[5]= weight filter+powder/pellet after in grams, float
    - entry_powder[6]= testing solution available, boolean
    - entry_powder[7]= notes, str
    
    '''
original=pd.read_csv('C:/M_drive_docs/Lab/CorrTest/raw_corrtest.csv',delimiter = ';')
test_list=[]
for i in range(len(original.values)):
    d=[]
    for b in range(len(original.values[i])):
        d.append(original.values[i][b])
    d=tuple(d)
    test_list.append(d)   

with open('C:/M_drive_docs/Lab/CorrTest/CORROSION_TEST_results.txt','w') as cav:
    cav.write('Date \t Test type \t Material \t w% loss \t Solution \t Notes \n')
    entries=[]
    for test in test_list:
        date=str(test[0])
        test_type=test[1]
        mat=test[2]
        corr_loss=str(round((test[3]-(test[5]-test[4]))*100/test[3],3))
        if test[6]=='True':
            solution='***'
        else:
            solution=''
        if test[7]!=None:
            note=str(test[7])
        else:
            note=''
        entry=date+' \t '+test_type+' \t '+mat+' \t '+corr_loss+' \t '+solution+' \t '+note+'\n'
        entries.append(entry)
    for b in entries:
        cav.write(b)
