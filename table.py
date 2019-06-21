import imgkit
corrtest=pd.read_csv('C:/M_drive_docs/Lab/ICP/ICP_ANALYSIS_2run.csv',delimiter = '\;')
df=corrtest.round(3)
#df=corrtest.loc[[6,13,14,15,16],['sample','Cr [ppb]','La [ppb]','Cu [ppb]','Ni [ppb]','Mn [ppb]']].round(3)
#print(cor2)
#html = cor2.style.render()
#imgkit.from_url('http://google.com', 'out.jpg')
#imgkit.from_string(html, 'styled_table.png')

#df = pd.DataFrame()
#df['date'] = ['2016-04-01', '2016-04-02', '2016-04-03']
#df['calories'] = [2200, 2100, 1500]
#df['sleep hours'] = [2200, 2100, 1500]
#df['gym'] = [True, False, False]


def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,tytle=None,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, rowLoc='center', colLoc='center')
    cellDict=mpl_table.get_celld()
    print(cellDict)
    #cellDict[(0,0)].set_width(0.1)
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        #print(type(k),k,cell.get_text())
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
        mn=[2,3]
       # if k[0] in mn:
            #cell.set_facecolor('lightsalmon')
        #ni=[1,4,5]
        #if k[0] in ni:
           # cell.set_facecolor('lightgreen')
        alert=[(1,2),(4,2)]
        celly=k[0],k[1]
        #if celly in alert:
            #cell.set_facecolor('yellow')
    ax.set_title(tytle)
    ax.legend()
    return ax

render_mpl_table(df, header_columns=0, col_width=2.3,tytle='Corrosion tests')