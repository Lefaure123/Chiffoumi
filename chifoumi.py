import random
import time

woch = "W"
sizo = "S"
papye = "P"

lis_chwa = ['W', 'S', 'P']

print()
print('** Byenvini nan jwet Chifoumi osinon woch (W), papye(P), sizo(S) **\n')

name = input("Se kiyes kap jwe a svp : ")
sko_jwe_a = 0
sko_computer_a = 0

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


# def gameException():
#     global sko_jwe_a
#     sko_jwe_a = 0
#     if antre == papye and chwa_odinate_a == woch:
#         print(f'{name} ou genyen\n')
#         sko_jwe_a += 50
#     elif antre == woch and chwa_odinate_a == papye:
#         print(f'{name} ou pedi\n')
#         sko_jwe_a -= 50








