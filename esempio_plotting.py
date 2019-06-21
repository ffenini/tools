#Tsample_a(o^C)\tstd.dev\tmicro_forward(Ohm)
v_probe=0.753

fig=plt.figure(figsize=(10,10))
colors=[]
marklist=['o','v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','X','D',
          'd','|','_','.',',','o','v','^','<','>','1','2','3','4','8','s','p','P','*','h',
          'H','+','x','X','D','d','|','_','.',',']
zarina=np.arange(19,26,1).tolist()
for i in zarina:
    colors.append(cm.viridis(int(0+zarina.index(i)*255/len(zarina))))#(int(0+i*255/(len(condots)))))
    try:
        cross_sec=float(condexp[i][3])*float(condexp[i][4])
    except ValueError:
        if condexp[i][3]=='nodimen':
            cross_sec=0.666*0.666        
    ax=plt.subplot(111)
    points_for=condata[i]['micro_forward (Ohm)'].values
    points_rev=condata[i]['micro_reverse (Ohm)'].values
    gyt=int(len(points_for)/2)
    print(gyt)
    u_mean=(points_for+points_rev)/2
    if i==22 or i==24 or i==21:
        print(len(condata[i]['micro_forward (Ohm)'].values))
    size=12
    mew_size=2
    mark=marklist[i]
    if mark=='1' or mark=='2' or mark=='3' or mark=='4':
        size=18
        mew_size=5
    labby=str(i)+': '+condexp[i][2]
    if condexp[i][3]=='nodimen':
        labby=str(i)+': '+'?% '+ condexp[i][2]+'_'+condexp[i][3]+' ?%'
    #if math.isnan(gh in condots[i]['Tsample_a(o^C)'].values):
    ax.plot(1000/(condata[i]['T sample a (o^C)'] .values+273.16),
                log10(1/(u_mean*(cross_sec/v_probe))),
                marker=mark,markersize=size,mew=mew_size,
            markevery=10,fillstyle='none',label=labby,color=colors[zarina.index(i)])
    #else:
        #ax.plot(1000/(condots[i]['Tsample_a(o^C)'].values+273.16),
          #      log(1/(u_mean*(cross_sec/v_probe))),
           #     marker=mark,markersize=size,mew=mew_size,fillstyle='none',label=labby,color=colors[i])
    x_range=(0.6,3.5)
    ax4=ax.twiny() # ax2 is responsible for "top" axis and "right" axis
    cel1=int((1000/x_range[0])-273.16)
    cel2=int((1000/x_range[1])-273.16)
    ax4.set_xlim(x_range)
    cels=np.arange(cel2,cel1)
    tticks=[]
    for i in cels:
        if i<200 and i%25==0:
            tticks.append(i)
        elif i<500 and i%50==0:
            tticks.append(i)
        elif i%100==0:
            tticks.append(i)
    if (x_range[1]-x_range[0])<2.5:
        tticks=[0]
        for i in cels:
            if  i%10==0:
                tticks.append(i)        
    ax.set_xlim(x_range)
    ax4.set_xticks( [ 1000/(t+273.16) for t in tticks ])
    ax4.set_xticklabels(tticks,fontsize=15,rotation='45')
    #ax4.tick_param(y,labelrotation=45)
    ax4.set_xlabel('Temperature (°C)')
    ml=MultipleLocator(0.1)# set the distance of the minor thicks,, based on the arugument of the axis
    Ml=MultipleLocator(0.5)# set the distance of the minor thicks, based on the arugument of the axis
    if (x_range[1]-x_range[0])<2.5:
        ml=MultipleLocator(0.01)# set the distance of the minor thicks,, based on the arugument of the axis
        Ml=MultipleLocator(0.1)# set the distance of the minor thicks, based on the arugument of the axis   
    ax.xaxis.set_major_locator(Ml)
    ax.xaxis.set_minor_locator(ml)
    ml1=MultipleLocator(1)# set the distance of the minor thicks,, based on the arugument of the axis
    #Ml1=MultipleLocator(5)# set the distance of the minor thicks, based on the arugument of the axis
    #ax4.xaxis.set_major_locator(Ml1)
    ax4.xaxis.set_minor_locator(ml1)
    ax.set_xlabel('1000/K')
    ax.set_ylabel('log (S cm$^{-2}$)')
    ax.legend(ncol=1,fontsize=12)
    plt.tight_layout()

    
#fig.savefig('C:/M_drive_docs/Lab/Conductivity_rig91/all_measurements.tif')