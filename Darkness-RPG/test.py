import sys, random, deaths
from time import sleep
from player import Human

def clear_screen():
    # Verifica o sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Inicializar a instância da classe Human
    player = Human()

    # Mensagens iniciais
    Room = "Dormitório"
    sleep(1.0)
    print("\nSua cabeça está latejando enquanto lentamente abre seus olhos.")
    sleep(2.0)
    print("\nApós um tempo, seus olhos fixam no teto mofado e sujo.")
    sleep(2.0)
    print("\nVocê se sente como se tivesse afundando.")
    sleep(2.5)

    while Room == "Dormitório":
        print("\n1 - LEVANTAR\n2 - OLHAR AO REDOR\n3 - NÃO FAZER NADA\n")
        try:
            escolha = int(input("O que pretende fazer?: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if escolha == 1:
            sleep(1)
            print("\nApós uma leve dificuldade, você consegue se levantar.")
            sleep(2)
            print("\nÉ como se você nem se lembrasse de como usar suas pernas.")
            sleep(2)
            print("\nVocê sente um frio na espinha ao pisar no chão frio e sujo.")
            sleep(2)
            print("\n1 - OLHAR AO REDOR\n2 - CHECAR SEUS BOLSOS")
            try:
                subescolha = int(input("\nO que pretende fazer?: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if subescolha == 1:
                sleep(1)
                print("\nVocê olha ao redor e percebe que está em uma espécie de dormitório. ")
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
                player.atualizar_atributo("Per", 1)  # Atualizando a percepção
                print("\n1 - IR PARA A PORTA \n2 - CHECAR OS ARMÁRIOS\n")
                subescolha = int(input("O que pretende fazer?: "))
                if subescolha == 1:
                    sleep(1)
                    print("\nVocê anda até a porta.. sem saber onde isso te levará..")
                elif subescolha == 2:
                    sleep(1)
                    print("\nVocê checa o primeiro ármario, e não há nada além de trapos, pegar?\n")
                    sleep(1)
                    escolhaitem = input("Y/N: ").strip().lower()
                    if escolhaitem == 'y':
                        print("\nVocê pegou trapos(x3)")
                        player.bolsa['Trapos'] = 3
                        player.bolsa
                        sleep(2.5)
                        print("\nVocê vai para o segundo armário, mas não havia nada")
                        sleep(2)
                        print("\nVocê tenta abrir o terceiro, mas está trancado")
                        sleep(2.5)
                        deaths.typing("\nO armário, estranhamente, está bem conservado")
                        sleep(2)
                        subescolha = input("\n1 - IR PARA A PORTA\n2 - OLHAR OS BOLSOS\n: ")
                        if subescolha == 1:
                            print("Você vai para a porta, sem saber o que te espera..")
                            Room == "Hallway"
                            break
                        elif subescolha == 2:
                            print(player.bolsa)
                            continue
                    elif escolhaitem == 'n':
                        print("\nVocê vai para o proximo ármario, onde não havia nada.\n")
                        sleep(2)
                        print("Você vasculha o segundo armário, mas estava vázio\n")
                        sleep(2)
                        print("Você tenta abrir o terceiro, mas está trancado\n")
                        sleep(1.5)
                        deaths.typing("O armário, estranhamente, está bem conservado.\n")
                        sleep(2)
                        print("Você não possui a chave.\n")
                        sleep(2.0)
                        print("1 - IR PARA A PORTA\n2 - OLHAR SEUS BOLSOS\n")
                        sub = int(input("O que vai fazer?: "))
                        if sub == 1:
                            print("\nVocê anda até a porta.. sem saber onde isso te levará..")
                            break
                        elif sub == 2:
                            print("Você checa seus bolsos, mas não há nada.\n")
                            sleep(2)
                            deaths.typing("Ele te chama\n")
                            sleep(2)
                            print("1 - IR PARA A PORTA\n")
                            sub = int(input(": "))
                            if sub == 1:
                                print("\nVocê anda até a porta.. sem saber onde isso te levará..\n")
                            else:
                                deaths.DeathbyNothing()
                    else:
                        print("Escolha uma opção válida")
                        continue


            elif subescolha == 2:
                print("Você checa seus bolsos, mas não há nada...")
                print("\n1 - IR PARA A PORTA \n2 - CHECAR OS ARMÁRIOS")
            else:
                print("Opção inválida.")
                continue

        elif escolha == 2:
            print('''Você olha ao redor, e você está em uma espécie de dormitório.
            \nHá camas de ferro sem um colchão, e aqueles que têm, estão em situação precária como o seu colchão.
            \nSeu colchão parece estar te engolindo cada vez mais.''')
            player.atualizar_atributo("Per", 1)  # Atualizando a percepção
            print("Você sente que sua percepção está melhor\n")
            input("Pressione Enter para continuar...")
            print("1 - LEVANTAR\n2 - CONTINUAR DEITADO")
            try:
                subescolha = int(input("O que pretende fazer?: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if subescolha == 1:
                print("Você decide levantar, mas sente uma dificuldade extrema ao fazer isso."
                      "\nHá algo te puxando para baixo.")
                sucesso, rolagem = player.rolar_dado("Força")
                if sucesso:
                    print(f"Você conseguiu se levantar com sucesso! (Rolagem: {rolagem})")
                else:
                    deaths.DeathbyBelow()

            elif subescolha == 2:
                print("Você decide continuar deitado...")
                deaths.DeadbyBelow()
            else:
                print("Opção inválida.")
                continue

        elif escolha == 3:
            print('''Você decide não fazer nada.
            \nO colchão está lhe engolindo ainda mais do que deveria, te puxando pra baixo.''')
            print("1 - LEVANTAR\n2 - OLHAR AO REDOR\n3 - CONTINUAR DEITADO")
            try:
                subescolha = int(input("O que pretende fazer?: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if subescolha == 1:
                print("Você decide levantar, mas sente uma dificuldade extrema ao fazer isso, como se há algo te puxando para baixo.")
                sucesso, rolagem = player.rolar_dado("Força")
                if sucesso:
                    print(f"Você conseguiu se levantar com sucesso! (Rolagem: {rolagem})")
                else:
                    deaths.DeathbyBelow()
            elif subescolha == 2:
                print('''Você olha ao redor, e você está em uma espécie de dormitório.
                \nHá camas de ferro sem um colchão, e aqueles que têm, estão em situação precária como o seu colchão.
                \nSeu colchão parece estar te engolindo cada vez mais.''')
                player.atualizar_atributo("Per", 1)  # Atualizando a percepção
                print("Você sente que sua percepção está melhor\n")
            elif subescolha == 3:
                print("Você decide continuar deitado...")
                deaths.DeathbyBelow()
            else:
                print("Opção inválida.")

        else:
            print("Isto não é uma opção válida.")


def main2():
    player = Human()
    Room = "Hallway"

    clearscreen()

    #Mensagem Inicial

    sleep(1)
    print("\nVocê está em um corredor estreito.")
    sleep(2)
    print("\nEm sua esquerda, há uma janela, enquanto a sua direita, o corredor se estende")
    sleep(2)
    print("\nEstá muito escuro, você não consegue ver mais nada, talvez se você tivesse uma lanterna..")
    while Room == "Hallway":
        print("\n1 - IR ATÉ A JANELA\n2 - IR ADIANTE DO CORREDOR")
        escolha = int(input("Sua decisão: "))
        match escolha:
            case 1:
                sleep(1)
                print("Você olha pela janela")
                deaths.typing("Você sente que há alguém lhe observando..")
            case 2:
                print("")






if __name__ == "__main__":
    main()


