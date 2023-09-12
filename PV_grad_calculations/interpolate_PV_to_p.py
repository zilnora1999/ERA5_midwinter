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

units.define('pvu = 1e-6 m^2 s^-1 K kg^-1')
#read input files
parser = argparse.ArgumentParser()                                               

parser.add_argument("--file1", "-f1", type=str, required=True)
parser.add_argument("--file2", "-f2", type=str, required=True)
parser.add_argument("--output", "-o", type=str, required=True)
args = parser.parse_args()

df1=xr.open_dataset(args.file1)
df2=xr.open_dataset(args.file2)

df1=xr.open_dataset('/net/ch4/atmcirc/zilnora/era5_midwinter/data/PV_gradient_computations/1980/PV19800101_00')
df2=xr.open_dataset('/net/thermo/atmosdyn/era5/cdf/1980/01/Z19800101_00')

levs=df1.TH.values
lats=df1.lat.values
lons=df1.lon.values
plevels=df2.plev.values

#interpolate to TH-levels
PV=df1.PV.values[0]
PV_filtered=df1.PV_filtered.values[0]
dPV_filtered=df1.dPV_filtered.values[0]
TH_on_p_levels=potential_temperature(np.transpose(np.tile(plevels,(len(lons),len(lats),1)))*units.Pa,df2.T.values*units.K).magnitude[0]
p_levels=np.array([100,200,250,300,400,500,600,700,800,850,900])*100

#interpolate p to TH_levels (needed for interpolation of PV to TH)
levs_new=np.reshape(np.repeat(np.repeat(plevels,len(lons)),len(lats)),(len(p_levels),len(lats),len(lons)))

p_on_TH_levels = interpolate_1d(levs*units.K,TH_on_p_levels*units.K, levs_new*units.Pa, axis=0)

#interpolate PV/filtered_PV/grad_filtered_PV to pressure levels
PV_field = interpolate_1d(p_levels*units.Pa,p_on_TH_levels*units.Pa, PV*units.pvu, axis=0)



#write netcdf file
EKE_out=xr.DataArray(name='EKE',data=np.expand_dims(EKE_field,axis=0),dims=['time','TH','lat','lon'])

data_vars={'EKE':EKE_out}
ds_new=xr.Dataset(coords={'time':df2.time,'lon':lons,'lat':lats,'TH':TH_levels},data_vars=data_vars)

ds_new.to_netcdf(args.output)

