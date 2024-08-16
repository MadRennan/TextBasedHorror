import os
import sys
import random
from time import sleep
from player import Human
import deaths

#Limpar a tela

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Primeira Fase

def main():
    player = Human()
    Room = "Dormitório"

    clear_screen()

    #Mensagem Inicial

    sleep(2.0)
    print("\nSua cabeça está latejando enquanto lentamente abre seus olhos.")
    sleep(2.0)
    print("\nApós um tempo, seus olhos fixam no teto mofado e sujo.")
    sleep(2.0)
    print("\nVocê se sente como se tivesse afundando.")
    sleep(2.5)

    #Enquanto estiver nesta sala

    while Room == "Dormitório":
        print("\n1 - LEVANTAR\n2 - OLHAR AO REDOR\n3 - NÃO FAZER NADA\n")
        sleep(1)
        try:
            escolha = int(input("O que pretende fazer?: "))
        except ValueError:
            print("\nPor favor, insira um número válido.")
            continue

        if escolha == 1:
            clear_screen()
            sleep(2)
            print("\nApós uma leve dificuldade, você consegue se levantar.")
            sleep(2)
            print("\nÉ como se você nem se lembrasse de como usar suas pernas.")
            sleep(2)
            print("\nVocê sente um frio na espinha ao pisar no chão frio e sujo.")
            sleep(2)
            print("\n1 - OLHAR AO REDOR\n2 - CHECAR SEUS BOLSOS")
            sleep(1)
            try:
                subescolha = int(input("\nO que pretende fazer?: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if subescolha == 1:
                clear_screen()
                sleep(2)
                print("\nVocê olha ao redor e percebe que está em uma espécie de dormitório.")
                sleep(2)
                print("\nHá camas de ferro sem um colchão, e aqueles que têm, estão em situação precária.")
                sleep(2)
                print("\nHá três armários, dois deles parecem ter sido revirados por completo, mas o terceiro está intacto")
                sleep(2)
                print("\nHá uma porta aberta a sua esquerda, mas não é possível ver o que há do outro lado.\n")
                sleep(2)
                print("Você sente que sua percepção está melhor\n")
                sleep(3)
                deaths.typing("Algo está te observando\n")
                sleep(1)
                player.atualizar_atributo("Per", 1)  # Atualizando a percepção
                print("\n1 - IR PARA A PORTA \n2 - CHECAR OS ARMÁRIOS\n")
                sleep(1)
                try:
                    subescolha = int(input("O que pretende fazer?: "))
                except ValueError:
                    print("Por favor, insira um número válido.")
                    continue
                if subescolha == 1:
                    clear_screen()
                    sleep(2)
                    print("\nVocê anda até a porta.. sem saber onde isso te levará..")
                    sleep(3)
                    Room = "Hallway"  # Atualizando a sala
                    break  # Sai do loop
                elif subescolha == 2:
                    clear_screen()
                    sleep(2)
                    print("\nVocê checa o primeiro armário, e não há nada além de trapos. Pegar?\n")
                    sleep(1)
                    escolhaitem = input("Y/N: ").strip().lower()
                    if escolhaitem == 'y':
                        clear_screen()
                        sleep(1)
                        print("\nVocê pegou trapos(x3)")
                        player.bolsa['Trapos'] = 3
                        sleep(2.5)
                        print("\nVocê vai para o segundo armário, mas não havia nada")
                        sleep(2)
                        print("\nVocê tenta abrir o terceiro, mas está trancado")
                        sleep(3)
                        deaths.typing("\nO armário, estranhamente, está bem conservado")
                        sleep(3)
                        print("\n1 - IR PARA A PORTA\n2 - OLHAR OS BOLSOS\n")
                        sleep(1)
                        subescolha = input("O que pretende fazer?: ")
                        if subescolha == '1':
                            clear_screen()
                            sleep(2)
                            print("Você vai para a porta, sem saber o que te espera..")
                            sleep(3)
                            Room = "Hallway"  # Atualizando a sala
                            break  # Sai do loop
                        elif subescolha == '2':
                            sleep(1)
                            print(player.bolsa)
                            sleep(1.5)
                            clear_screen()
                            continue
                    elif escolhaitem == 'n':
                        clear_screen()
                        print("\nVocê vai para o próximo armário, onde não havia nada.\n")
                        sleep(2)
                        print("Você vasculha o segundo armário, mas estava vazio\n")
                        sleep(2)
                        print("Você tenta abrir o terceiro, mas está trancado\n")
                        sleep(3)
                        deaths.typing("O armário, estranhamente, está bem conservado.\n")
                        sleep(3)
                        print("Você não possui a chave.\n")
                        sleep(2.0)
                        print("1 - IR PARA A PORTA\n2 - OLHAR SEUS BOLSOS\n")
                        sub = int(input("O que vai fazer?: "))
                        if sub == 1:
                            clear_screen()
                            sleep(2)
                            print("\nVocê anda até a porta.. sem saber onde isso te levará..")
                            sleep(3)
                            Room = "Hallway"  # Atualizando a sala
                            break  # Sai do loop
                        elif sub == 2:
                            clear_screen()
                            print("Você checa seus bolsos, mas não há nada.\n")
                            sleep(2)
                            deaths.typing("Ele te chama\n")
                            sleep(1)
                            clear_screen()
                            print("1 - IR PARA A PORTA\n")
                            sub = int(input(": "))
                            if sub == 1:
                                clear_screen()
                                sleep(1)
                                print("\nVocê anda até a porta.. sem saber onde isso te levará..\n")
                                sleep(2)
                                Room = "Hallway"  # Atualizando a sala
                                break  # Sai do loop
                            else:
                                clear_screen()
                                deaths.DeathbyError()
                    else:
                        print("Escolha uma opção válida\n")
                        continue
            elif subescolha == 2:
                clear_screen()
                print("Você checa seus bolsos, mas não há nada...")
                print("\n1 - IR PARA A PORTA \n2 - CHECAR OS ARMÁRIOS")
            else:
                print("Opção inválida.")
                continue
        elif escolha == 2:
            clear_screen()
            sleep(2)
            print("\nVocê olha ao redor, e você está em uma espécie de dormitório.")
            sleep(2)
            print("\nHá camas de ferro sem um colchão, e aqueles que têm, estão em situação precária como o seu colchão.")
            sleep(2)
            print("\nSeu colchão parece estar te engolindo cada vez mais.\n")
            sleep(1.5)
            player.atualizar_atributo("Per", 1)  # Atualizando a percepção
            print("Você sente que sua percepção está melhor\n")
            sleep(1.5)
            print("1 - LEVANTAR\n2 - CONTINUAR DEITADO\n")
            try:
                subescolha = int(input("O que pretende fazer?: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if subescolha == 1:
                clear_screen()
                print("\nVocê decide levantar, mas sente uma dificuldade extrema ao fazer isso.")
                sleep(3)
                deaths.typing("\nHá algo te puxando para baixo\n")
                sleep(2)
                sucesso, rolagem = player.rolar_dado("Força")
                if sucesso:
                    print(f"\nVocê conseguiu se levantar com sucesso! (Rolagem: {rolagem})")
                else:
                    clear_screen()
                    deaths.DeathbyBelow()
            elif subescolha == 2:
                clear_screen()
                sleep(1)
                print("\nVocê decide continuar deitado...\n")
                sleep(2)
                clear_screen()
                deaths.DeathbyBelow
            else:
                print("\nOpção inválida.")
                continue
        elif escolha == 3:
            clear_screen()
            sleep(2)
            print("\nVocê decide não fazer nada.\n")
            sleep(2)
            print("O colchão está lhe engolindo ainda mais do que deveria, te puxando pra baixo.\n")
            sleep(1.5)
            print("1 - LEVANTAR\n2 - OLHAR AO REDOR\n3 - CONTINUAR DEITADO\n")
            sleep(1)
            try:
                subescolha = int(input("O que pretende fazer?: "))
            except ValueError:
                print("\nPor favor, insira um número válido.")
                continue

            if subescolha == 1:
                clear_screen()
                sleep(1)
                print("\nVocê decide levantar, mas sente uma dificuldade extrema ao fazer isso, como se há algo te puxando para baixo.")
                sucesso, rolagem = player.rolar_dado("Força")
                if sucesso:
                    print(f"Com muito esforço, você se levanta. (Rolagem: {rolagem})")
                else:
                    sleep(1)
                    clear_screen()
                    deaths.DeathbyBelow()
            elif subescolha == 2:
                clear_screen()
                sleep(2)
                print("\nVocê olha ao redor, e você está em uma espécie de dormitório.\n")
                sleep(2)
                print("\nHá várias camas de ferro, que estão em situação precária como o seu.")
                sleep(2)
                print("\nSeu colchão parece estar te engolindo cada vez mais.")
                sleep(2)
                player.atualizar_atributo("Per", 1)  # Atualizando a percepção
                print("Você sente que sua percepção está melhor\n")
            elif subescolha == 3:
                clear_screen()
                sleep(1)
                print("\nVocê decide continuar deitado...")
                sleep(1)
                deaths.DeathbyNothing()
            else:
                print("\nOpção inválida.")
        else:
            print("\nIsto não é uma opção válida.")

# Após sair do loop, chamar a próxima fase do jogo
    main2()

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
            clear_screen()
            sleep(1)
            print("\nVocê olha pela janela")
            sleep(1)
            print("\nA janela, fechada por algumas barras de metal, ainda dava para ver o exterior")
            sleep(1)
            print("\nA lua iluminava a floresta adiante, recheada de pinheiros.")
            sleep(2)
            deaths.typing("\nVocê sente que há alguém lhe observando..")
            sleep(1)
            print("\nVocê percebe, pela luz da lua, uma pequena comoda em sua frente")
            sleep(2)
            deaths.typing("Você jura ter visto alguém passando entre as árvores lá fora.")
            sleep(2)
            print("\n1 - OLHAR O COMODO\n2 - OLHAR A JANELA\n2 - DAR MEIA VOLTA\n")
            sleep(1)
            subescolha = int(input("Sua escolha: "))
            if subescolha == 1:
                sleep(1)
                print("Você abre o comodo, e nele havia uma lanterna.")

        elif escolha == 2:
            print("Você avança pelo corredor...")
            print("")
        else:
            print("Opção inválida. Escolha 1 ou 2.")


if __name__ == "__main__":
    main()
