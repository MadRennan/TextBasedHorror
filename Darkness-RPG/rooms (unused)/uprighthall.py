import os, sys, random, deaths
from time import sleep
from player import Human
from test import clearscreen
import sys

sys.path.insert(1, '/home/rennan/Downloads/Darkness-RPG/')

def main2():
    player = Human()
    Room = "Hallway"

    clear_screen()

    # Mensagem Inicial
    sleep(1)
    print("\nVocê está em um corredor estreito.")
    sleep(2)
    print("\nEm sua esquerda, há uma janela, enquanto a sua direita, o corredor se estende")
    sleep(2)
    print("\nEstá muito escuro, você não consegue ver mais nada, talvez se você tivesse uma lanterna..")
    while Room == "Hallway":
        print("\n1 - IR ATÉ A JANELA\n2 - IR ADIANTE DO CORREDOR")
        try:
            escolha = int(input("Sua decisão: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if escolha == 1:
            sleep(1)
            print("Você olha pela janela")
            deaths.typing("Você sente que há alguém lhe observando..")
        elif escolha == 2:
            print("Você avança pelo corredor...")
            # Aqui você pode adicionar mais lógica para o corredor
        else:
            print("Opção inválida. Escolha 1 ou 2.")

if __name__ == "__main__":
    main2()
