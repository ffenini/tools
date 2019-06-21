'''
The script takes the data from the url of rig 91 and prints 'info.txt' into 'testXXX_info.txt'
and the 'raaadata' into a .txt file with name format path_raa=date_t+'_'+test_num+'_'+name+'_'+dimen+'_'+atm
Folder: GLOSSYraw
The script prints out the name of the tests that cannot convert
'''
import time
import datetime
import urllib.request
for i in [118]:#range(115,113,1):
    try:
        info = urllib.request.urlopen('https://elektrodetest-18.energy.dtu.dk/rig91/91test'+str(i)+'/info.txt')
        data=urllib.request.urlopen('https://elektrodetest-18.energy.dtu.dk/rig91/91test'+str(i)+'/raadata')
        #page = urllib.request.urlopen('https://elektrodetest-18.energy.dtu.dk/rig91/91test90/raadata')
        file_data_path='C:/M_drive_docs//Lab/Conductivity_rig91/GLOSSYraw/' 
        file_info_path='C:/M_drive_docs//Lab/Conductivity_rig91/GLOSSYraw/test'+str(i)+'_info.txt' 
    except urllib.error.HTTPError:
        print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
        print('CANNOT IMPORT!!!',i) ##prints the file that cannot import
        print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
        continue
    except URLError:
        print('NO CONNECTION: established connection failed because connected host has failed to respond')      
    WriteInfo=True # turn it to 'True' if wanted the overwriting of 'testXXX_info.txt' files in folder GLOSSYraw
    if WriteInfo:
        with open(file_info_path,'w+') as cai:  # writes 'info.txt' taking it from the url of rig91, can be deactivated
            l_inf=info.read()
            inf=l_inf.decode("utf-8")
            try:
                cai.write(str(inf))
            except UnicodeEncodeError:
                continue
        print("'testXXX_info.txt' ovewritten!")
        cai.close()
    lines=open(file_info_path).read()
    for i in range(len(lines)-4): #it is not a problem the -4, since all the last bytes are ######## always
        if lines[i]=='L' and lines[i+1]=='A' and lines[i+2]=='N' and lines[i+3]==' ' and lines[i+4]=='#':
            #print('beg',i+5)
            beg=i+5
        if lines[i+1]=='P' and lines[i+2]=='R' and lines[i+3]=='O' and lines[i+4]=='J':
            end=i
            #print('end',i)
    info_box=lines[beg:end]
    info_text=''
    for i in range(len(info_box)):
        if info_box[i]!=' ' and info_box[i]!=',' and info_box[i]!='/' and info_box[i]!='%' and info_box[i]!='.' and info_box[i]!='_' and info_box[i]!='\n' and info_box[i]!=':':
            info_text=info_text+info_box[i]
             
        if '*' in info_box : ### extractor of dimensions in info.txt
            if info_box[i]=='*':
                dimen=''
                for a in range(-5,6,1):
                    if info_box[i+a]!='.' and info_box[i+a]!=',' and info_box[i+a]!='=':
                        dimen=dimen+info_box[i+a]
                dimen = dimen.replace("*", "x")
                dimen = dimen.replace(" ", "")
                if dimen[0]!='0':
                    dimen='0'+dimen
                for d in range(len(dimen)):
                    if dimen[d]=='x' and dimen[d+1]!='0':
                        dimen = dimen.replace("x", "x0")
                #else:
                    #dimen=dimen
        elif 'x' in info_box:
            if info_box[i]=='x':
                dimen=''
                for a in range(-5,6,1):
                    if info_box[i+a]!='.' and info_box[i+a]!=',' and info_box[i+a]!='=':
                        dimen=dimen+info_box[i+a]
                dimen = dimen.replace(" ", "")
                if dimen[0]!='0':
                    dimen='0'+dimen
                for d in range(len(dimen)):
                    if dimen[d]=='x' and dimen[d+1]!='0':
                        dimen = dimen.replace("x", "x0")
                if '\n' in dimen:
                    dimen=dimen.replace('\n','')
                while len(dimen)<9 and dimen[4]=='x': #adds zeros when the cyphers are less than 4 per dimension;
                    dimen=dimen+'0' # adds a zero at the end of second dimension
        else:
            dimen='nodimen'
            #print(file)
    #print('dimen',dimen, len(dimen))
    while len(dimen)<9 and dimen!='nodimen': #adds a zero at the end of first dimension
        dimen = dimen.replace("x", "0x")
         
    if 'air100mlmin' in info_text or '100mlminair' in info_text: #extracts the name of the sampple from info.txt
            try:
                l=info_text.index('air100mlmin')
                name=info_text[:l]
                atm='air100mlmin'
            except ValueError:
                l=info_text.index('100mlminair')
                name=info_text[:l]
                atm='100mlminair'
    else:
        name=info_text[0:8]  
        atm='100mlminair'            
    if '*' in name:
        ast=info_text.index('*')
        name=name[:ast-4]
    if 'Testplan' in name:
        ast=info_text.index('Testplan')
        name=name[ast+8:]
    if 'Information for test ' in lines and ' on rig 91' in lines:
        st=lines.index('Information for test ')
        en=lines.index(' on rig 91')
        test_num='test'+lines[st+21:en]
    if 'Test started ' in lines and '\n\nRignumber' in lines:
        st=lines.index('Test started ')
        en=lines.index('\n\nRignumber')
        date=lines[st+13:en]
    date_t=time.strftime('%y%m%d',time.strptime(date, "%a %b %d %H:%M:%S %Y"))
    path_raa=date_t+'_'+test_num+'_'+name+'_'+dimen+'_'+atm
    
    with open(file_data_path+path_raa+'.txt','w') as cai:  
        l_dat=data.read()
        dati=l_dat.decode("utf-8")
        cai.write(str(dati))
    cai.close()        
    #print('----------------') 
    #print(path_raa)
    #print('date',date,len(date))
    #print('date_t',date_t,len(date_t))
    #print('atm',atm)
    #print('test_num',test_num, len(test_num))
    #print(dimen,len(dimen))
    #print('name',name)        
    
    