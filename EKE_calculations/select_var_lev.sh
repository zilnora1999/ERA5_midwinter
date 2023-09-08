#prepare data to high-pass filter U and V   
PATH=/net/ch4/atmcirc/zilnora/era5_midwinter/data/EKE_calculations/

for year in {1996..2022}
do
    for month in {01,02,03,04,05,06,07,08,09,10,11,12} 
    do 
        for file in /net/thermo/atmosdyn/era5/cdf/$year/$month/Z*00
        do
            cdo selname,U,V $file $PATH$year/UV${file: -11}
    
        done
        echo $month
    done
    echo $year
    cdo mergetime $PATH$year/UV* $PATH$year/UV_$year
    rm $PATH$year/UV1*
    rm $PATH$year/UV2*
done
