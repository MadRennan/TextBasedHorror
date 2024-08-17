import sys
from time import sleep
from start import clear_screen

def DeathbyBelow():
    sleep(1.5)
    print("\nBraços esguios e sómbrios envolvem seu corpo e tampa sua boca.\n")
    sleep(2)
    print("Sua visão, consumida pela escuridão, enquanto sentia algo rasgando seu estômago\n")
    sleep(2.5)
    print("Você sente o calor de seu sangue sobre sua pele\n")
    sleep(2)
    print("Você quer gritar pela última vez\n")
    sleep(3)
    typing("Mas ele não lhe permite\n")
    sleep(1.5)
    print("\nSeu corpo agora, pertence a ele.")
    quit()

def DeathbyError():
    sleep(2)
    typing("\nYfy ymná ukoc zut gocni nygji\n")
    sleep(1)
    print("Você sente calafrios em sua espinha\n")
    sleep(1.5)
    print("Seu corpo queima, seus olhos sangram\n")
    sleep(2)
    breaking("\nȨ̴̨͕͙͙̖̣̤̞̰̞̫̪̲̗̉̑̆̊̆̑̆́́u̵̬̟̼̫͈͔̺̤̺͚͇̫̖̯̪̒̓̑͆͑̍̈́͛̌̑̊̔̈́̿͂͒͊̍͌͊͝ ̵̨̮͚̪̪͒̎̾͊̅͛̇͒c̵̫̈́ǫ̴̱̗̳̝̬̠͎͍̣͚̙̫̤̫̖͈̑͗͆̿́͂́̇̓̌̍̄͛̃̚ͅṋ̸̨̥̘̭͔̱͗͛͊̓͐́͆́̽͐̓̀͆̍̋̚̚ͅs̵̨̭̩̟͈̜̤̥͇̬͎̠̝̼͖̟̤̰̯͎͕̬͉̔̿̿̃̎̀̂̏͆̆͆̏͋̑͂į̸̛͙͔͚̦͙͓̒̏͋̾g̵̨̢̯̜̤̠̪̦̀̾̅̎̎͒̃̈́́̋͌͆͗͐̃̕̚͝o̴̢͓̗̲͗̌̑̆ ̶̨̡̛̲͈̫̼̞̬̗̗̫̞͕͓̜͎̪͉̊t̸̢̨̬͓̭̞̰͇̯̺͚̘̙͚̻̱̟̘̃̅̅͌̎͗͐̽͆ͅͅe̴̫̅̾̎̕͝ ̸̜̯̠̹̘͖̯̞͖͙͚̣́͑͂̂͒̿͌̂̋͛̒͘͠v̸̨̡̛̭̬͓͇̣̙͉̻̥̒̏̿͛͂̀̐̈́̎͂͛͑̾̇͌͠͝ͅe̶̡̨̛͕͔̯̠̣͖̥̭̖̻͖̟̞͖̜̤͉̣̅̂̄̈̾̈́͑͌̅̄̉̀̎͊͛͑͛̂̾̚̚ͅṛ̶̡̟̹͎͙͚̜͖̀̾͂̾̽̓\n")
    sleep(1)
    clear_screen()
    typing("Você não sente mais nada, além de dor.\n")
    sleep(1)
    typing("Sua visão, escurece\n")
    sleep(2)
    quit()

def DeathbyNothing():
    sleep(3)
    typing("Há uma figura olhando você na janela")
    sleep(3)
    typing("\nUm sorriso macabro se estende, rindo de você, enquanto você afunda.")
    sleep(2)
    print("\nO colchão te engole")
    sleep(3.5)
    clear_screen()
    sleep(1)
    typing("Ele não está satisfeito")
    sleep(1.5)
    clear_screen()
    quit()

def DeathbyCrackingFloor():
    clear_screen()
    sleep(1)
    print("Você pisa em uma madeira podre, mas você não foi ágil o suficiente.\n")
    sleep(2)
    print("Você achou que ia cair no primeiro andar\n")
    sleep(3)
    clear_screen()
    typing("Mas.. por que você continua caindo, em pura escuridão?\n")
    sleep(2)
    clear_screen()
    sleep(2)
    typing("ᕓꝊ𐌂𐌄 𐌍𐌀Ꝋ 𐌔𐌄 𐌋𐌄𐌌𐌁𐌐𐌀, 𐌍𐌀Ꝋ 𐌄?\n")
    sleep(1)
    typing("𐌌𐌀𐌔 𐌔𐌄 𐌋𐌄𐌌𐌁𐌐𐌀𐌐𐌀. . .")
    clear_screen()
    quit()

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.1)

def breaking(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.005)
