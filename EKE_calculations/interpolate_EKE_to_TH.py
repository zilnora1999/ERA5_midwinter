#calculate filtered PV and its gradient along isentropes and interpolate to model levels
#input: PV on model levels, output: filtered PV and its gradient along isen on model levels
from math import nan
import xarray as xr
import argparse
import numpy as np
from pyshtools.expand import MakeGridDH
from pyshtools.expand import SHExpandDH
from metpy.units import units
from metpy.calc import potential_temperature
from metpy.interpolate import interpolate_1d


#read input files
parser = argparse.ArgumentParser()                                               

parser.add_argument("--file1", "-f1", type=str, required=True)
parser.add_argument("--file2", "-f2", type=str, required=True)
parser.add_argument("--output", "-o", type=str, required=True)
args = parser.parse_args()

df1=xr.open_dataset(args.file1)
df2=xr.open_dataset(args.file2)

#df1=xr.open_dataset('/net/ch4/atmcirc/zilnora/era5_midwinter/data/netcdf_filtering/1980/EKE_198001.nc')
#df2=xr.open_dataset('/net/thermo/atmosdyn/era5/cdf/1980/01/Z19800101_00')

levs=df1.plev.values
lats=df1.lat.values
lons=df1.lon.values

#interpolate to TH-levels
EKE=df1.EKE.values[0]
TH_on_p_levels=potential_temperature(np.transpose(np.tile(df2.plev.values,(len(lons),len(lats),1)))*units.Pa,df2.T.values*units.K).magnitude[0]
TH_levels=np.arange(320,342,2)


levs_new=np.reshape(np.repeat(np.repeat(levs,len(lons)),len(lats)),(len(levs),len(lats),len(lons)))


EKE_field = interpolate_1d(TH_levels*units.K,TH_on_p_levels*units.K, EKE*units('m^2/s^2'), axis=0)
levs_interp = interpolate_1d(TH_levels*units.K,TH_on_p_levels*units.K, levs_new, axis=0)


#write netcdf file
EKE_out=xr.DataArray(name='EKE',data=EKE_field,dims=['time','TH','lat','lon'])

data_vars={'EKE':EKE_out}
ds_new=xr.Dataset(coords={'time':df2.time,'lon':lons,'lat':lats,'TH':TH_levels},data_vars=data_vars)

ds_new.to_netcdf(args.output)

