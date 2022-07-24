import random
import pickle
import os


class Jwe:
    def __init__(self, non, score):
        self.score = score
        self.non = non


def vale_Kompite_a(chwa_jwe_a, sa_kompite_a_chwazi, vire_lanve):
    if vire_lanve is False and chwa_jwe_a == 'W':
        return 1
    elif vire_lanve is False and chwa_jwe_a == 'S':
        return 2
    return sa_kompite_a_chwazi


sko_jwe_a = 0
sko_kompite_a = 0
chans = 10
non = input("Se kiyes kap jwe a ?? : ")

jwe_a = Jwe(non, sko_jwe_a)
kompite_a = Jwe('compite', sko_kompite_a)

lis_chwa = ['W', 'S', 'P']
#    ['P','S','W']
vire_lanve = True

while chans > 0:
    sa_kompite_a_chwazi = random.choice([0, len(lis_chwa) - 1])
    chwa_jwe_a = None
    print('Jwet pou ou, chwazi ant W, S, P :')
    chwa_jwe_a = input(f"{non} >").capitalize()
    if (chwa_jwe_a == 'S' and sa_kompite_a_chwazi == 0) or (chwa_jwe_a == 'W' and sa_kompite_a_chwazi == 1):
        vire_lanve = False
    else:
        vire_lanve = True

    if chwa_jwe_a == "H":
        print("Byenvini nan jwet Woch, Papye, Sizo : \n"
              "Men komanl jwe => wap gen pou chwazi ant woch, sizo, ou byen papye .\n"
              "konprann sa : Woch bat sizo - Sizo bat papye - Papye bat woch\n"
              "Wap gen pou antre yon epsedo ew pral jwe kont kompite a\n"
              "Bon chans, epi Byen chwazi\n")

    if chwa_jwe_a == "K":
        print('Ou deside kite jwet la.')
        exit()

    if chwa_jwe_a != 'W' and chwa_jwe_a != 'S' and chwa_jwe_a != 'P':
        print("Pa bliye chwazi inisyal ke nou pwopwoze yo tanpri : W, S, P")
        print('Jwet pou ou, chwazi ant W, S, P :')
        chwa_jwe_a = input(f"{non} >").capitalize()

    if chwa_jwe_a == "Z":
        print()

    for index, chwa in enumerate(sorted(lis_chwa, reverse=vire_lanve)):

        if chwa == chwa_jwe_a:
            print(f'{non}, ou chwazi {chwa_jwe_a}')
            print(f'odinate a chwazi : {lis_chwa[sa_kompite_a_chwazi]}')

            if index < vale_Kompite_a(chwa_jwe_a, sa_kompite_a_chwazi, vire_lanve):
                sko_kompite_a += 50
                print(f'{chwa_jwe_a} > {lis_chwa[sa_kompite_a_chwazi]}')
            if index < vale_Kompite_a(chwa_jwe_a, sa_kompite_a_chwazi, vire_lanve):
                sko_jwe_a -= 50
                if sko_kompite_a < 0:
                    print('none')

            elif index > vale_Kompite_a(chwa_jwe_a, sa_kompite_a_chwazi, vire_lanve):
                sko_jwe_a += 50
                print(f'{lis_chwa[sa_kompite_a_chwazi]} < {chwa_jwe_a}')
            elif index > vale_Kompite_a(chwa_jwe_a, sa_kompite_a_chwazi, vire_lanve):
                sko_kompite_a -= 50
                if sko_kompite_a < 0:
                    print('none')

            if index == sa_kompite_a_chwazi:
                print("Ou menm ak kompite a chwazi menm bagay, li nul rejwe svp")
    print(f'{non}:{sko_jwe_a} : {sko_kompite_a}: kompite ')

    if os.path.isfile('C:\\Users\\Noel\\PycharmProjects\\coding_club\\fichye.txt'):
        print("ok")
    else:
        print('enregistrement')

    fichye_a = open("fichye.txt", "wb")
    done = {f"{non}:{sko_jwe_a}"}
    pickle.dump(done, fichye_a)
    fichye_a.close()

    fichye_a = open("fichye", "rb")
    done = pickle.load(fichye_a)
    fichye_a.close()