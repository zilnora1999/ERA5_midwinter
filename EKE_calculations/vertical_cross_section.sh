#calculate vertical cross-section
P=/net/ch4/atmcirc/zilnora/era5_midwinter/data/EKE_calculations/

for year in {1980..2022}
do
    for month in {01,02,03,04,05,06,07,08,09,10,11,12} 
    do 
        cdo ymonmean -zonmean -sellonlatbox,150,180,30,70 $P$year/EKE_$year$month.nc ${P}monthdir/EKE_${month}_mean_cross
    done
done