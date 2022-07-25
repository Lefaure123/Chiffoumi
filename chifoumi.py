import random

woch = "W"
sizo = "S"
papye = "P"

print()
print('** Byenvini nan jwet Chifoumi osinon woch, papye, sizo **\n')


chans = 10
while chans > 0:
    antre = input("tanpri chwazi youn nan opsyon sa yo W,P,S : ")
    if str(antre) != woch and str(antre) != sizo and str(antre) != papye:
        print("Reeseye, chwazi ant W, S, P ")
    elif str(antre) == woch or str(antre) == sizo or str(antre) == papye:
        break
    chans -= 1






