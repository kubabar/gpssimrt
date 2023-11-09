from os import system

for i in range(300):
    sek = i%60
    mi = i//60
    system(f"gps-sdr-sim -e brdc.n -d 1.1 -b 8 -t 2023/11/09,05:{mi}:{sek} -o - >> sek11.bin")
    #system(f"gps-sdr-sim -e brdc.n -d 1.1 -b 8 -t 2023/11/09,05:00:00 -o - >> sek11bezczasu.bin")