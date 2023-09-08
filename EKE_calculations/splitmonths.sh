PATH=/net/ch4/atmcirc/zilnora/era5_midwinter/data/EKE_calculations/

for year in {1980..2022}
do
    cdo splitmon $PATH$year/EKE_highpass_$year $PATH$year/EKE_$year
done