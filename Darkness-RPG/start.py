import sys, random, deaths
from player import Human
from time import sleep

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

    while True:
        print("\n1 - LEVANTAR\n2 - OLHAR AO REDOR\n3 - NÃO FAZER NADA\n")
        try:
            escolha = int(input("O que pretende fazer?: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if escolha == 1:
            sleep(1)
            print('''\nApós uma leve dificuldade, você consegue se levantar.
            \nÉ como se você nem se lembrasse de como usar suas pernas.
            \nVocê sente um frio na espinha ao pisar no chão frio e sujo.''')
            sleep(1)
            print("1 - OLHAR AO REDOR\n2 - CHECAR SEUS BOLSOS\n")
            try:
                subescolha = int(input("O que pretende fazer?: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if subescolha == 1:
                sleep(1)
                print("Você olha ao redor e percebe que está em uma espécie de dormitório. ")
                sleep(1.5)
                print("\nHá camas de ferro sem um colchão, e aqueles que têm, estão em situação precária.")
                sleep(1.5)
                print("\nHá três armários, dois deles parecem ter sido revirados por completo, mas o terceiro está intacto")
                sleep(1.5)
                print("\nHá uma porta aberta a sua esquerda, mas não é possível ver o que há do outro lado.")
                sleep(2)
                deaths.typing("Algo está te observando")
                print("\n1 - IR PARA A PORTA \n2 - CHECAR OS ARMÁRIOS")
                subescolha = int(input("O que pretende fazer?: "))
                if subescolha == 1:
                    print("\nVocê anda até a porta.. sem saber onde isso te levará..")
                elif subescolha == 2:
                    print("\nVocê checa o primeiro ármario, e não há nada além de trapos, pegar?")
                    escolhaitem = print("Y/N: ")
                    if escolhaitem == "Y" or "y":
                        print("Você pegou trapos(x3)")
                        Human.bolsa.append("Trapos")
                    elif escolhaitem == "N" or "n":
                        print("Você vai para o proximo ármario")
                    else:
                        print("Escolha um valor válido")

            elif subescolha == 2:
                print("Você checa seus bolsos, mas não há nada...")
                print("\n1 - IR PARA A PORTA \n2 - CHECAR OS ARMÁRIOS")
            else:
                print("Opção inválida.")

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
            else:
                print("Opção inválida.")

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
            else:
                print("Opção inválida.")

        else:
            print("Isto não é uma opção válida.")

if __name__ == "__main__":
    main()


