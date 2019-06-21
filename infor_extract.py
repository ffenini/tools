
from  header import * 
    
path='C:/M_drive_docs/Lab/Conductivity_rig91/prova/'
make=os.listdir(path)
for file in make:
    if file.endswith('_info.txt'):
        #print(file)
        with open(str(path+file)) as fai:
            lines=open(str(path+file)).read()
            #print(lines[52:72])
           # print(lines)
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
                     
                    
                    #name=info_text.remove()
                if '*' in info_box : ### extraxtor of dimensions in info.txt
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
                        #print(info_text[:l])                
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
            print('----------------') 
            print(path_raa)
            print('date',date,len(date))
            print('date_t',date_t,len(date_t))
            print('atm',atm)
            print('test_num',test_num, len(test_num))
            print(dimen,len(dimen))
            print('name',name)                        
            #print(info_text)


