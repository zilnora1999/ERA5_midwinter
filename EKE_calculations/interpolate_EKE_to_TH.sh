#!/bin/bash
#interpolate EKE_data to TH-levels
PATH=/net/ch4/atmcirc/zilnora/era5_midwinter/data/netcdf_filtering/

for year in {1980..2023}
do  
    for month in {01,02,03,04,05,06,07,08,09,10,11,12}
    do 
        for file in /net/thermo/atmosdyn/era5/cdf/$year/$month/Z*00
        do
            outfile_final=$PATH$year/EKE_${file: -11}_TH
            python /net/ch4/atmcirc/zilnora/era5_midwinter/code/EKE_calculations/interpolate_EKE_to_TH.py -f1 $PATH$year/EKE_$year$month.nc -f2 $file -o $outfile_final

        done
    done
done