for year in {1980..2022}
do
    cdo splitmon $year/EKE_highpass_$year $year/EKE_$year
done