import os
import random

dictionary = {'jovenel': 'li se yon prezidan ayisyen ki mouri asasine lakay li.',
              'balon': 'Li gen fom ron, ou itilizel pou w jwe boul.',
              'telefon': 'yo itlizel pou kontakte moun a distans',
              'bib': 'Se yon liv sakre pou kretyen yo'}
print()

print("Byenvini nan jwet Hangman osinon 'Le jeu du pendu',\n"
      "Se yon jwèt kote sistèm nan ap chwazi yon mo aleyatwa,\n"
      "epi li ap baw yon deskripsyon sou mo sa, epi ou menm ou pral devine\n"
      "ki mo ki kache deye deskripsyon sa, Bon chans epi Byen chwazi")
print('-------------------------------------------------------------------------')

print()

# storing dict keys in a list
key = []
for x in dictionary:
    key.append(x)
name = random.choice(key)

length = int(len(name))
asterix = '*' * length

while name != asterix:
    os.system('cls')

    print(dictionary[name])
    print("\nSa se mo wap verifye a: ", asterix)
    print('----------------------------------------')
    a = input("antre ou byen fin antre let ki manke yo pou konplete mo a:\n>>> ")
    a = a.lower()
    count = name.count(a)

    position = [pos for pos, char in enumerate(name) if char == a]

    if a in name and len(a) == 1:

        index = name.find(a)

        if count == 2:
            position = [pos for pos, char in enumerate(name) if char == a]

            position1 = position[0]
            position2 = position[1]

            asterix = asterix[:position1] + a + asterix[position1 + 1:]
            asterix = asterix[:position2] + a + asterix[position2 + 1:]

        elif count > 2:
            position1 = position[0]
            position2 = position[1]
            position3 = position[2]

            asterix = asterix[:position1] + a + asterix[position1 + 1:]
            asterix = asterix[:position2] + a + asterix[position2 + 1:]
            asterix = asterix[:position3] + a + asterix[position3 + 1:]
        else:
            asterix = asterix[:index] + a + asterix[index + 1:]

print(asterix)
