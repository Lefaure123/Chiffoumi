import random
import time

woch = "W"
sizo = "S"
papye = "P"

lis_chwa = ['W', 'S', 'P']

print()
print('** Byenvini nan jwet Chifoumi osinon woch (W), papye(P), sizo(S) **\n')

name = input("Se kiyes kap jwe a svp : ")
print()
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


def noChange():
    if sko_jwe_a < 0:
        return 0


def egalityGame():
    if chwa_odinate_a == antre:
        print('Match nul, rejwe svp')


if chwa_odinate_a == woch and antre == sizo:
    sko_jwe_a -= 50
    print('Computer win', ',' f'{name} loose')
    if sko_jwe_a < 0:
        noChange()
elif chwa_odinate_a == sizo and antre == papye:
    print('Computer win', ',' f'{name} loose')
    if sko_jwe_a < 0:
        noChange()
elif chwa_odinate_a == papye and antre == woch:
    print('computer win', ',' f'{name} loose')
    if sko_jwe_a < 0:
        noChange()

if antre == woch and chwa_odinate_a == sizo:
    sko_jwe_a += 50
    print(f'{name} win ', f' ==> score = {sko_jwe_a}')
elif antre == sizo and chwa_odinate_a == papye:
    sko_jwe_a += 50
    print(f'{name} win ', f' ==> score = {sko_jwe_a}')
elif antre == papye and chwa_odinate_a == woch:
    sko_jwe_a += 50
    print(f'{name} win ', f' ==> score = {sko_jwe_a}')

if antre == chwa_odinate_a:
    egalityGame()
