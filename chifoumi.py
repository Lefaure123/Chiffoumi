import random

woch = "W"
sizo = "S"
papye = "P"

lis_chwa = ['W', 'S', 'P']

print()
print('** Byenvini nan jwet Chifoumi osinon woch (W), papye(P), sizo(S) **\n')

chans = 10
while chans > 0:
    antre = input("chwazi oubyen rechwazi youn nan opsyon sa yo W,P,S : ")
    if str(antre) == woch or str(antre) == sizo or str(antre) == papye:
        break
    elif str(antre) == woch.lower() or str(antre) == sizo.lower() or str(antre) == papye.lower():
        break
    else:
        if str(antre) != woch and str(antre) != sizo and str(antre) != papye:
            print()
            print("__Reeseye__")
    chans -= 1

chwa_odinate_a = random.choice(lis_chwa)
print("Computer a chwazi ==> ", chwa_odinate_a)


