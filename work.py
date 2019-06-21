#only selecting the files with a specific extension
def list_files1(directory, extension):
    return [f for f in os.listdir(directory) if f.endswith('.' + extension)]
# reading .ras files from Rigaku Smartlab
source='C:/M_drive_docs/Lab/MaterialsSynth/XRD/SnO2/BsnO2_new_samples/fixed/'
#bisno=os.listdir(source)
bisno=list_files1(source,'xy')
cucro=[31.33,36.27,40.73,55.75,65.37]
fig,ax=plt.subplots(figsize=(10,5))
colors=[]
for g in bisno: 
    sg=bisno.index(g)
    colors.append(cm.copper(int(70+sg*125/len(bisno))))
    path=source+g
    #peaks position taken from the patter of CuCrO2
    test=pd.read_csv(path, delimiter=' ',names=['2theta', 'Intensity','Error'],skiprows=1)
    x=test['2theta']
    y=test['Intensity']/max(test['Intensity'])
    labby=g[0]+'.'+g[1]+' %at'
    if g==bisno[0]:
        labby='pure SnO$_2$'
    ax.plot(x,y+0.2*sg,label=labby,color=colors[sg])
    #plotting arrpws fpr CuCrO2 peaks
  #  xstr = [str(i) for i in x] 
  #  for j in cucro:
  #      for t in range(len(xstr)):
  #          if xstr[t].startswith(str(j)) and i==samples[0]:
  #              ax.annotate('',xy=(j,y[t]+0.02),xytext=(j,y[t]+0.12),arrowprops=dict(arrowstyle="->"))
ax.set_xlim(10,140)
ax.set_xlabel(2 )
#ax.set_ylim(0,0.4)
ax.legend(title='Bi content:', ncol=3,frameon=False)