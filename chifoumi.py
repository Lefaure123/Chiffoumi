import random
import pickle

woch = "W"
sizo = "S"
papye = "P"

lis_chwa = ['W', 'S', 'P']

print()
print('**** Byenvini nan jwet Chifoumi osinon woch(W), papye(P), sizo(S) ****\n')

name = input("Se kiyes kap jwe a svp : ")
print()

sko_computer_a = 0
sko_jwe_a = 0

chwa_odinate_a = random.choice(lis_chwa)


#  fonksyon ke nap bezwen nan pwogram nan
def noChange():
    if sko_jwe_a <= 0:
        return 0
    print(0)


def egalityGame():
    if chwa_odinate_a == antre:
        print("Computer a chwazi ==> ", chwa_odinate_a)
        print('Match nul, rejwe svp___\n')


#  Nan ka ke se computer a kp genyen
chans = 10
while chans > 0:
    antre = input("chwazi oubyen rechwazi youn nan opsyon sa yo W,P,S : ")
    if chwa_odinate_a == woch and antre == sizo:
        if sko_jwe_a == 0:
            noChange()
        else:
            sko_jwe_a -= 50
        print("Computer a chwazi ==> ", chwa_odinate_a)
        print('Computer win', ',' f'{name} loose', ',' f'==> score = {sko_jwe_a}\n')
    elif chwa_odinate_a == sizo and antre == papye:
        if sko_jwe_a == 0:
            noChange()
        else:
            sko_jwe_a -= 50
        print("Computer a chwazi ==> ", chwa_odinate_a)
        print('Computer win', ',' f'{name} loose', ',' f'==> score = {sko_jwe_a}\n')
    elif chwa_odinate_a == papye and antre == woch:
        if sko_jwe_a == 0:
            noChange()
        else:
            sko_jwe_a -= 50
        print("Computer a chwazi ==> ", chwa_odinate_a)
        print('computer win', ',' f'{name} loose', f'==> score = {sko_jwe_a}\n')

        print()

    # Nan ka ke se jwe a kap genyen

    if antre == woch and chwa_odinate_a == sizo:
        sko_jwe_a += 50
        print("Computer a chwazi ==> ", chwa_odinate_a)
        print(f'{name} win ', f' ==> score = {sko_jwe_a}\n')

    elif antre == sizo and chwa_odinate_a == papye:
        sko_jwe_a += 50
        print("Computer a chwazi ==> ", chwa_odinate_a)
        print(f'{name} win ', f' ==> score = {sko_jwe_a}\n')

    elif antre == papye and chwa_odinate_a == woch:
        sko_jwe_a += 50
        print("Computer a chwazi ==> ", chwa_odinate_a)
        print(f'{name} win ', f' ==> score = {sko_jwe_a}\n')

    if antre == chwa_odinate_a:
        egalityGame()
    if str(antre) == 'K' or str(antre) == 'k':
        fichye_mwen = open("file.txt", "ab")
        score_dict = {f'{name}': f'{sko_jwe_a}'}
        pickle.dump(score_dict, fichye_mwen)
        fichye_mwen.close()

        fichye_mwen = open("file.txt", "rb")
        score_dict = pickle.load(fichye_mwen)
        print({f'{name}': f'{sko_jwe_a}'})
        fichye_mwen.close()
        exit()
    elif str(antre) == 'H' or str(antre) == 'h':
        print("Byenvini nan jwet Woch, Papye, Sizo : \n"
              "Men komanl jwe => wap gen pou chwazi ant woch(W), sizo(S), ou byen papye(P) .\n"
              "konprann sa : Woch bat sizo - Sizo bat papye - Papye bat woch\n"
              "Wap gen pou antre yon epsedo ew pral jwe kont kompite a\n"
              "Bon chans, epi Byen chwazi\n")
    elif str(antre) == 'Z' or str(antre) == 'z':
        for el in {f'{name}': f'{sko_jwe_a}'}:
            for i in {f'{name}': f'{sko_jwe_a}'}:
                if el > i:
                    print(i)
        print('Meye sko a se : sk')
        exit()
    else:
        if str(antre) != woch and str(antre) != sizo and str(antre) != papye:
            print()
            print("__Reeseye__")

    chans += 1

# def dataBase():
#     global anrejistre
#     score_dict = {f'{name}': f'{sko_jwe_a}'}
#     with open("file.txt", "rb") as f:
#         while True:
#             try:
#                 anrejistre = pickle.load(score_dict)
#             except EOFError:
#                 break
#             else:
#                 score_dict.update()
# dataBase()
