from rex import MultiYearWaveX
import pandas as pd
from hist_scatter import scat_hist2d
import matplotlib.pyplot as plt
plt.ion()
import numpy as np

# This is the data file we are loading (defined below)
datname = f'west_coast_gg50.csv'

try:
    dat = pd.read_csv(datname, index_col=0)

except FileNotFoundError:
    # This block of code creates the data file.

    # Modify the lat_lon and 'outname' files to create new datasets.
    lat_lon = (37.541, -123.365) # ~50 miles offshore of the Golden Gate
    outname = 'west_coast_gg50.csv'
    
    wavepath = '/nrel/US_wave/West_Coast/'
    years = list(range(1979, 2011)) # All available years

    parameters = ['significant_wave_height', 'peak_period', 'energy_period']
    tmp = []
    with MultiYearWaveX(wavepath, years=years, hsds=True) as mYears:
        for p in parameters:
            tmp.append(mYears.get_lat_lon_df(p, lat_lon))

    dat = pd.DataFrame({p: d.values[:, 0] for p, d in zip(parameters, tmp)}, index=tmp[0].index)

    dat.to_csv(outname)


fignum = 10
fig = plt.figure(fignum)
fig.clf()
fig, ax = plt.subplots(1, 1, num=fignum)

h = scat_hist2d(dat['energy_period'],dat['significant_wave_height'], bins=[np.arange(5, 20, 0.25), np.arange(0, 12, 0.25)], dens_func=None, normed=True)
cbar = plt.colorbar(h)
cbar.set_label('1/(m sec)')
ax.set_xlabel('Energy Period [sec]')
ax.set_ylabel('Significant Wave Height [m]')
ax.set_title('Wave Energy Joint Probability Distribution\n50 miles offshore of the Golden Gate')

fig.savefig('JPD_GoldenGate.png', dpi=300)

