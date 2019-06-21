fig,ax=plt.subplots(figsize=(15,15))
mnt=1
crt=1
cromium_diss=np.arange(0,crt,0.1)
data=[]
data2=[]
data3=[]
data4=[]
for i in cromium_diss:
    cr_s=i
    ricp=[]
    rcomp=[]
    ricp_rcomp=[]
    rcomp_ricp=[]
    #colors.append(cm.plasma(int(0+i*255/len(cromium_diss))))
    mn_diss=np.arange(0,mnt+0.01,0.01)
    for j in mn_diss :
        mn_s=j
        mn_c=mnt-mn_s
        cr_c=crt-cr_s
        Rtot=crt/mnt
        Ricp=cr_s/mn_s
        Rcomp=cr_c/mn_c
        ricp.append(Ricp)
        rcomp.append(Rcomp)
        ricp_rcomp.append(10**((Ricp+Rcomp)/2))
        rcomp_ricp.append(Rcomp/Ricp)
    data.append(ricp)
    data2.append(rcomp)
    data3.append(ricp_rcomp)
    data4.append(rcomp_ricp)
    ax.plot(mn_diss,ricp,linestyle='--',alpha=0.8,color=cm.plasma(int(0+i*10*255/len(cromium_diss))),label=str(round(i,2)))
    ax.plot(mn_diss,rcomp,linestyle='-',alpha=0.8,color=cm.plasma(int(0+i*10*255/len(cromium_diss))))
    #ax.plot(mn_diss,ricp_rcomp,linestyle='-',color=cm.plasma(int(0+i*125/len(cromium_diss))))
    
    ax.plot(mn_diss,rcomp_ricp,linestyle=':',color=cm.plasma(int(0+i*10*255/len(cromium_diss))))
    ax.axhline(Rtot,xmin=-2, xmax=12,linestyle='-',color='k')
    ax.set_xlabel('Moles of Mn in solution')
    ax.semilogy()
    ax.set_xlim(0,1)
    ax.legend(title='Ricp: Cr moles in solution',ncol=3)
df=pd.DataFrame(data)
df2=pd.DataFrame(data2)
df3=pd.DataFrame(data3)
df4=pd.DataFrame(data4)
import seaborn as sns
sns.set()

#Load the example flights dataset and conver to long-form
#flights_long = sns.load_dataset(df)
#flights = flights_long.pivot("month", "year", "passengers")

#Draw a heatmap with the numeric values in each cell
nota=True
heat=False
if heat:
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(df, annot=nota,  linewidths=0, ax=ax)
    ax.set_title('Ricp')
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(df2, annot=nota,  linewidths=0, ax=ax)
    ax.set_title('Rcomp')
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(df3, annot=nota,  linewidths=0, ax=ax)
    ax.set_title('data3')
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(df4, annot=nota,  linewidths=0, ax=ax)
    ax.set_title('logRcomp/logRicp')