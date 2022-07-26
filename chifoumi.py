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

sko_computer_a = 0
sko_jwe_a = 0
chwa_odinate_a = random.choice(lis_chwa)


def noChange():
    if sko_jwe_a < 0:
        return 0


def egalityGame():
    if chwa_odinate_a == antre:
        print('Match nul, rejwe svp')


chans = 10
while chans > 0:
    antre = input("chwazi oubyen rechwazi youn nan opsyon sa yo W,P,S : ")
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
        print()

    if antre == woch and chwa_odinate_a == sizo:
        sko_jwe_a += 50
        print(f'{name} win ', f' ==> score = {sko_jwe_a}')
    elif antre == woch.lower() and chwa_odinate_a == sizo.lower():
        sko_jwe_a += 50
        print(f'{name} win ', f' ==> score = {sko_jwe_a}')

    elif antre == sizo and chwa_odinate_a == papye:
        sko_jwe_a += 50
        print(f'{name} win ', f' ==> score = {sko_jwe_a}')
    elif antre == sizo.lower() and chwa_odinate_a == papye.lower():
        sko_jwe_a += 50
        print(f'{name} win ', f' ==> score = {sko_jwe_a}')

    elif antre == papye and chwa_odinate_a == woch:
        sko_jwe_a += 50
        print(f'{name} win ', f' ==> score = {sko_jwe_a}')
    elif antre == papye.lower() and chwa_odinate_a == woch.lower():
        sko_jwe_a += 50
        print(f'{name} win ', f' ==> score = {sko_jwe_a}')

    if antre == chwa_odinate_a:
        egalityGame()

    # if str(antre) == woch or str(antre) == sizo or str(antre) == papye:
    #     break
    # elif str(antre) == woch.lower() or str(antre) == sizo.lower() or str(antre) == papye.lower():
    #     break
    if str(antre) == 'K' or str(antre) == 'k':
        exit()
    elif str(antre) == 'H' or str(antre) == 'h':
        print("Byenvini nan jwet Woch, Papye, Sizo : \n"
              "Men komanl jwe => wap gen pou chwazi ant woch(W), sizo(S), ou byen papye(P) .\n"
              "konprann sa : Woch bat sizo - Sizo bat papye - Papye bat woch\n"
              "Wap gen pou antre yon epsedo ew pral jwe kont kompite a\n"
              "Bon chans, epi Byen chwazi\n")
    else:
        if str(antre) != woch and str(antre) != sizo and str(antre) != papye:
            print()
            print("__Reeseye__")

    chans -= 1

print("Computer a chwazi ==> ", chwa_odinate_a)

# def playAgain():
#     if antre and chwa_odinate_a:
#         return antre


# Le se Computer a ki genyen


# Le se jwe a ki genyen


# while antre != 'K' or antre != 'k':
#     playAgain()
