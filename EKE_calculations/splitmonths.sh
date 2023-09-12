#split into months to later combine every month separately
#-P 8 paralellises
P=/net/ch4/atmcirc/zilnora/era5_midwinter/data/EKE_calculations/

for year in {1980..2022}
do
    cdo -P 8 splitmon $P$year/EKE_highpass_$year $P$year/EKE_$year
done