def plotter(i,selector,p):
    rm=p[0][si] #single plot range minimum
    rh=p[4][si]
    rM=p[1][si] #single plot range maximum
    Ar=dimen[i][1] # RING area
    ce=dimen[i][2] # collection efficiency
    Ad=dimen[i][0] # DISK area
    
    time=data[i]['Time/s'].values #time 
    potential=0.658+data[i]['Potential/V'].values #potential vs SHE (V)
    try:
        datD=data[i]['i1/A'].values
        datR=data[i]['i2/A'].values
    except KeyError:
        datD=data[i]['Current/A'].values
        datR=0*data[i]['Current/A'].values
    curr2=datR/Ar/ce #current density RING (A cm-2)
    curr1=datD/Ad ##current density DISK (A cm-2) 


class plotter(self,selector,p):
     def __init__(self):
        self.rm=p[0][si] #single plot range minimum
        self.rh=p[4][si]
        self.rM=p[1][si] #single plot range maximum
        self.Ar=dimen[i][1] # RING area
        self.ce=dimen[i][2] # collection efficiency
        self.Ad=dimen[i][0] # DISK area
        
        self.time=data[i]['Time/s'].values #time 
        self.potential=0.658+data[i]['Potential/V'].values #potential vs SHE (V)
        try:
            self.datD=data[i]['i1/A'].values
            self.datR=data[i]['i2/A'].values
        except KeyError:
            self.datD=data[i]['Current/A'].values
            self.datR=0*data[i]['Current/A'].values
        self.curr2=datR/Ar/ce #current density RING (A cm-2)
        self.curr1=datD/Ad ##current density DISK (A cm-2)
