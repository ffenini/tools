from data_importer_script import *
selector = [12, 2]
baseline = [6]  ##data to use as a baseline, only baseline[0] will be used
base_plot = True  # in order to show in the plot the data used as baseline

### this ranges are made when experimetns with different potential ranges are compared
## the same number of cycles is required

########peaks from peak analysis
disk_peaks = []
ring_peaks = []
shoulder_min = 870
shoulder_max = 870
ranges = []
numb_cyc = 10  ####number of cycles in the experiment
if base_plot and len(baseline) > 0:
    selector.append(baseline[0])

for i in range(10):  ####define how many cycles to plot
    a = []
    b = []
    for t in selector:
        aa = int(len(data[t]) / numb_cyc) * i
        bb = aa + int(len(data[t]) / numb_cyc)
        a.append(aa)
        b.append(bb)
    d = str(i + 1) + 'th'
    if i == 0:
        d = str(i + 1) + 'st'
    if i == 1:
        d = str(i + 1) + 'nd'
    if i == 2:
        d = str(i + 1) + 'rd'
    e = i + 1
    c = (a, b, d, e)
    ranges.append(c)
# print(ranges)

fig = plt.figure(figsize=(20, 20))  ## muar be out of ranges to have a single figure
for p in ranges:
    ring = plt.subplot(5, 4, p[3] * 2 - 1)
    zoom = plt.subplot(5, 4, p[3] * 2)
    labz = ['MnCu25 GG \n exchGC U.P.=2.0 V', 'Nicr2 GG  \n oldGC U.P.=2 V', 'baseline', 'MnCU25 GG oldGC',
            'GG2 old', 'GG2 exch', 'NiCr2 old', 'MnCu25 exch', 'MLCI exch']
    colors = []
    # interval=rng_min[selector.index(i)]rng_max[selector.index(i)]
    # ring_disk=plt.subplot(52) #ring_disk=plt.subplot(gs[0:,1])
    for i in selector:
        si = selector.index(i)
        rng_min = p[0][si]
        rng_max = p[1][si]
        Ar = dimen[i][1]  # RING area
        ce = dimen[i][2]  # collection efficiency
        Ad = dimen[i][0]  # DISK area
        colors.append(cm.viridis(int(0 + si * 255 / (len(selector)))))  ##color map divided by the number of files
        time = data[i]['Time/s'].values[rng_min:rng_max]  # time
        potential = data[i]['Potential/V'].values[rng_min:rng_max] + 0.658  # potential vs SHE (V)

        try:
            curr2 = data[i]['i2/A'].values[rng_min:rng_max]  # current  DISK (A )
        except KeyError:
            curr2 = data[i]['Time/s'].values[rng_min:rng_max] * 0  ### in case it is only disk
        try:
            curr1 = data[i]['i1/A'].values[rng_min:rng_max]  ##current  RING (A )
        except KeyError:
            curr = data[i]['Current/A'].values[rng_min:rng_max]  # current  (A )

        if len(baseline) > 0 and i != baseline[0]:  # baseline subtraction script
            try:
                curr2 = data[i]['i2/A'].values[rng_min:rng_max] - data[baseline[0]]['i2/A'].values[
                                                                  rng_min:rng_max]  # current  DISK (A )
            except KeyError:
                curr2 = data[i]['Time/s'].values[rng_min:rng_max] * 0  ### in case it is only disk
            try:
                curr1 = data[i]['i1/A'].values[rng_min:rng_max] - data[baseline[0]]['i1/A'].values[
                                                                  rng_min:rng_max]  ##current  RING (A )
            except KeyError:
                curr = data[i]['Current/A'].values[rng_min:rng_max] - data[baseline[0]]['Current/A'].values[
                                                                      rng_min:rng_max]  # current  (A )
        ##############  RING
        try:
            ring.plot(time - time[0], 1000 * curr2 / Ar / ce, linestyle='-', color=colors[si], label=labz[si])
            zoom.plot(time - time[0], 1000 * curr2 / Ar / ce, linestyle='-', color=colors[si], label=labz[si])
            # ring.plot(time,((1000*curr2)/ce)/Ar,linestyle='-', color = colors[si],label=labz[si])
            for h in disk_peaks:
                ring.plot(time[h], 1000 * curr2[h] / Ar / ce, marker='o', markersize=10, color='r')
            for t in ring_peaks:
                ring.plot(time[t], 1000 * curr2[t] / Ar / ce, marker='+', mew=5, markersize=20, color='b')
        #   ring.plot(data[i]['Time/s'].values[shoulder_min:shoulder_max],
        #            1000*data[i]['i2/A'].values[shoulder_min:shoulder_max]/Ar/ce,
        #            color = 'g', linewidth=4,
        #           label=labz[si])
        except KeyError:
            continue
        ring.set_xlim((0, 150))
        zoom.set_xlim((0, 150))
        ring.set_ylim((-0.35, 0.005))
        ring.set_title(p[2] + ' Cycle', fontsize=25)
        zoom.set_title('- zoom -', fontsize=20)
        ring.set_ylabel('Current density \n (mA cm$^{-2}$)', fontsize=15)
        ring.set_xlabel('Time (s)', fontsize=15)
        #ring.legend(fontsize=15)
        fig.suptitle('Baseline subtraction: RING current', fontsize=35)
        plt.tight_layout()
plt.subplots_adjust(top=0.90)
path = 'C:/M_drive_docs/Lab/RDE/180407/prova' + p[2] + '.png'
fig.savefig(path)
plt.show(block=True)