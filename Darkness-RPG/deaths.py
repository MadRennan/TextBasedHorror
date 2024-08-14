import sys
from time import sleep

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

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.1)
