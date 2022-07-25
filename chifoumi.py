import random

woch = "W"
sizo = "S"
papye = "P"

print()
print('** Byenvini nan jwet Chifoumi osinon woch, papye, sizo **\n')


chans = 10
while chans > 0:
    antre = input("tanpri chwazi youn nan opsyon sa yo W,P,S : ")
    if str(antre) == woch or str(antre) == sizo or str(antre) == papye:
        break
    elif str(antre) == woch.lower() or str(antre) == sizo.lower() or str(antre) == papye.lower():
        break
    else:
        if str(antre) != woch and str(antre) != sizo and str(antre) != papye:
            print("Reeseye, chwazi ant W, S, P ")
    chans -= 1






