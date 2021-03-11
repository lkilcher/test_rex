from rex import MultiYearWaveX
import pandas as pd


lat_lon = (37.541, -123.365) # ~50 miles offshore of the Golden Gate

wavepath = '/nrel/US_wave/West_Coast/' # All years
years = list(range(1980, 2011))

parameters = ['significant_wave_height', 'peak_period', 'energy_period']
tmp = []
with MultiYearWaveX(wavepath, years=years, hsds=True) as mYears:
    for p in parameters:
        tmp.append(mYears.get_lat_lon_df(p, lat_lon))

df = pd.DataFrame({p: d.values[:, 0] for p, d in zip(parameters, tmp)}, index=tmp[0].index)

