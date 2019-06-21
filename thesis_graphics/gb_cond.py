T=340 # Kelvin
R=physical_constants['molar gas constant'][0]
F=physical_constants['Faraday constant'][0]
fig,ax=plt.subplots(figsize=(10,10))
beta=0.7
i0=10e-3 # A cm-2
print(R,F)
i=np.arange(1,100,0.1)
for T in np.arange(300,370,10):#"(0.1,1,0.1):
    eta=(R*T)/(beta*4*F)*(-log(i))
    
    #ax.plot(i,eta)
#ax.axhline(-0.24,0,1)
#ax.axvline(10,0,1)
#ax.axvline(10,0,1)
grain_size=np.arange(0.0001,1,0.0001)
gb=[]
for i in grain_size:
    gb.append(int(1/i)-1)
    
    
ax.plot(grain_size,gb)
ax.set_ylim(0,10e5)
ax.set_yscale('log')