#mkdir
PATH=/net/ch4/atmcirc/zilnora/era5_midwinter/data/EKE_calculations/

mkdir monthdir
for month in {01,02,03,04,05,06,07,08,09,10,11,12}
    do
        mkdir ${PATH}monthdir/$month
    done
    