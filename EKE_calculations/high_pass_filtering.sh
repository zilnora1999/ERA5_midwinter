#prepare data to high-pass filter U and V   
#cdo highpass,365/10 -del29feb UV_$year UV_highpass_$year
P=/net/ch4/atmcirc/zilnora/era5_midwinter/data/EKE_calculations/

for year in {2016..2022}
do
    cdo highpass,36.5 -del29feb $P$year/UV_$year $P$year/UV_highpass_$year
    cdo expr,'EKE=0.5*U*U+0.5*V*V' $P$year/UV_highpass_$year $P$year/EKE_highpass_$year
    echo $year
done 


