import os
import sys
import random
from time import sleep
from player import Human
import deaths

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def primeira_fase(player):
    Room = "Dormitório"

    clear_screen()
    print_intro_message()

    while Room == "Dormitório":
        escolha = get_choice("\n1 - LEVANTAR\n2 - OLHAR AO REDOR\n3 - NÃO FAZER NADA\n")

        if escolha == 1:
            handle_levantar(player)
        elif escolha == 2:
            handle_olhar_ao_redor(player)
        elif escolha == 3:
            handle_nao_fazer_nada(player)
        else:
            print("\nIsto não é uma opção válida.")

def print_intro_message():
    sleep(2.0)
    print("\nSua cabeça está latejando enquanto lentamente abre seus olhos.")
    sleep(2.0)
    print("\nApós um tempo, seus olhos fixam no teto mofado e sujo.")
    sleep(2.0)
    print("\nVocê se sente como se tivesse afundando.")
    sleep(2.5)

def get_choice(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("\nPor favor, insira um número válido.")
        return None

def handle_levantar(player):
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
    subescolha = get_choice("\nO que pretende fazer?: ")

    if subescolha == 1:
        handle_olhar_ao_redor(player)
    elif subescolha == 2:
        handle_checar_bolsos(player)
    else:
        print("Opção Inválida")

def handle_olhar_ao_redor(player):
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
    player.atualizar_atributo("Per", 1)
    print("\n1 - IR PARA A PORTA \n2 - CHECAR OS ARMÁRIOS\n")
    sleep(1)
    subescolha = get_choice("O que pretende fazer?: ")

    if subescolha == 1:
        Room = "Hallway"
        return Room
    elif subescolha == 2:
        handle_checar_armarios(player)
    else:
        print("\nOpção Inválida")

def handle_checar_armarios(player):
    clear_screen()
    sleep(2)
    print("\nVocê checa o primeiro armário, e não há nada além de trapos. Pegar?\n")
    sleep(1)
    escolhaitem = input("Y/N: ").strip().lower()

    if escolhaitem == 'y':
        clear_screen()
        sleep(1)
        print("\nVocê pegou trapos")
        player.bolsa['Trapos'] = 1
        sleep(2.5)
        clear_screen()
        sleep(1)
        print("\nVocê vai para o segundo armário, mas não havia nada")
        sleep(2)
        print("\nVocê tenta abrir o terceiro, mas está trancado")
        sleep(3)
        deaths.typing("\nO armário, estranhamente, está bem conservado\n")
        sleep(3)
        while True:
            print("\n1 - IR PARA A PORTA\n2 - OLHAR OS BOLSOS\n")
            sleep(1)
            subescolha = get_choice("O que pretende fazer?: ")
            if subescolha == 1:
                Room = "Hallway"
                return Room
            elif subescolha == 2:
                print(player.bolsa)
                sleep(1.5)
                clear_screen()
            else:
                print("\nOpção Inválida")
    elif escolhaitem == 'n':
        clear_screen()
        sleep(2)
        print("\nVocê vai para o próximo armário, onde não havia nada.")
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
        sub = get_choice("O que vai fazer?: ")
        if sub == 1:
            Room = "Hallway"
            return Room
        elif sub == 2:
            print("Você checa seus bolsos, mas não há nada.\n")
            sleep(2)
            deaths.typing("Ele te chama\n")
            sleep(1)
            clear_screen()
            print("1 - IR PARA A PORTA\n")
            sub = get_choice(": ")
            if sub == 1:
                Room = "Hallway"
                return Room
    else:
        print("Escolha uma opção válida\n")

def handle_olhar_ao_redor(player):
    clear_screen()
    sleep(2)
    print("\nVocê olha ao redor, e você está em uma espécie de dormitório.")
    sleep(2)
    print("\nHá camas de ferro sem um colchão, e aqueles que têm, estão em situação precária como o seu colchão.")
    sleep(2)
    print("\nSeu colchão parece estar te engolindo cada vez mais.\n")
    sleep(1.5)
    player.atualizar_atributo("Per", 1)
    print("Você sente que sua percepção está melhor\n")
    sleep(1.5)
    print("1 - LEVANTAR\n2 - CONTINUAR DEITADO\n")
    subescolha = get_choice("O que pretende fazer?: ")

    if subescolha == 1:
        handle_levantar(player)
    elif subescolha == 2:
        clear_screen()
        sleep(1)
        print("\nVocê decide continuar deitado...\n")
        sleep(2)
        clear_screen()
        deaths.DeathbyBelow()
    else:
        print("\nOpção inválida.")

def handle_nao_fazer_nada(player):
    clear_screen()
    sleep(2)
    print("\nVocê decide não fazer nada.\n")
    sleep(2)
    print("O colchão está lhe engolindo ainda mais do que deveria, te puxando pra baixo.\n")
    sleep(1.5)
    print("1 - LEVANTAR\n2 - OLHAR AO REDOR\n3 - CONTINUAR DEITADO\n")
    sleep(1)
    subescolha = get_choice("O que pretende fazer?: ")

    if subescolha == 1:
        handle_levantar(player)
    elif subescolha == 2:
        handle_olhar_ao_redor(player)
    elif subescolha == 3:
        clear_screen()
        sleep(1)
        print("\nVocê decide continuar deitado...")
        sleep(1)
        deaths.DeathbyNothing()
    else:
        print("\nOpção inválida.")

def segunda_fase(player):
    Room = "Hallway"

    clear_screen()
    sleep(1)
    print("\nVocê está em um corredor estreito.")
    sleep(2)
    print("\nEm sua esquerda, há uma janela, enquanto a sua direita, o corredor se estende")
    sleep(2)
    print("\nEstá muito escuro, você não consegue ver mais nada, talvez se você tivesse uma lanterna..")
    sleep(2)
    print("\nO cheiro da madeira podre, entra em suas narinas, e te causa naúsea")

    while Room == "Hallway":
        escolha = get_choice("\n1 - IR ATÉ A JANELA\n2 - IR ADIANTE DO CORREDOR\n")

        if escolha == 1:
            handle_ir_janela(player)
        elif escolha == 2:
            handle_ir_corredor(player)
        else:
            print("\nOpção inválida. Escolha 1 ou 2.")

def handle_ir_janela(player):
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
    deaths.typing("\nVocê jura ter visto alguém passando entre as árvores lá fora.\n")
    sleep(2)
    subescolha = get_choice("\n1 - OLHAR O COMODO\n2 - OLHAR A JANELA\n3 - DAR MEIA VOLTA\n")

    if subescolha == 1:
        handle_olhar_comodo(player)
    elif subescolha == 2:
        pass  # Adicione a lógica para olhar a janela novamente
    elif subescolha == 3:
        pass  # Adicione a lógica para dar meia volta
    else:
        print("\nOpção inválida.")
        return

def handle_olhar_comodo(player):
    sleep(1)
    print("\nVocê abre o comodo, e nele havia uma lanterna.")
    escolhaitem = input("\nPegar?: ").strip().lower()
    if escolhaitem == 'y':
        player.bolsa['Lanterna'] = 30
        print("\nVocê pegou a lanterna.")
        subescolha = get_choice("\n1 - OLHAR A JANELA\n2 - DAR MEIA VOLTA\n")
        if subescolha == 1:
            handle_olhar_janela(player)
        elif subescolha == 2:
            pass  # Adicione a lógica para dar meia volta
        else:
            print("\nOpção inválida.")
    elif escolhaitem == 'n':
        sleep(3)
        deaths.typing("\nVocê não pega a lanterna")
        sleep(2.5)
        clear_screen()
        sleep(2)
        print("\n1 - IR ADIANTE DO CORREDOR\n")
    else:
        print("\nOpção inválida.")

def handle_olhar_janela(player):
    clear_screen()
    sleep(1)
    print("\nVocê se aproxima ainda mais da janela")
    sleep(2)
    print("\nA janela, está bem trancada.")
    sleep(2)
    print("\nVocê consegue ouvir a forte brisa batendo na janela")
    sleep(3)
    clear_screen()
    deaths.typing("\nVocê me escuta?\n")
    clear_screen()
    print("\n1 - IR ADIANTE DO CORREDOR\n2 - ILUMINAR O CORREDOR")
    subescolha = get_choice(": ")
    if subescolha == 1:
        sleep(1)
        print("\nVocê avança pelo corredor...")
        sucesso, rolagem = player.rolar_dado("Agi")
        if sucesso:
            sleep(2)
            print("Você pisa em uma madeira podre, mas foi ágil o suficiente para não cair")
        else:
            deaths.DeathbyCrackingFloor()
        sleep(2)
    elif subescolha == 2:
        sleep(2)
        print("\nVocê ilumina o corredor com a sua lanterna.")
        player.bolsa["Lanterna"] = 15
        sleep(2)
        print("\nVocê usa metade da carga da lanterna, enquanto iluminava")
        sleep(2)
        print("\nHá duas portas a sua esquerda, uma porta era sofisticada.")
        sleep(2)
        print("\nA outra porta era de metal maciço.")
        sleep(2)
        subescolha = get_choice("\n1 - VER A PORTA SOFISTICADA\n2 - VER A PORTA DE METAL\n3 - AVANÇAR NO CORREDOR\n")
        if subescolha == 1:
            handle_ver_porta_sofisticada(player)
        elif subescolha == 2:
            pass  # Adicione a lógica para ver a porta de metal
        elif subescolha == 3:
            pass  # Adicione a lógica para avançar no corredor
        else:
            print("\nOpção inválida.")
    else:
        print("\nOpção inválida.")

def handle_ver_porta_sofisticada(player):
    clear_screen()
    sleep(2)
    print("\nVocê vai checar a porta sofisticada, e por algum motivo, a porta está intacta.\n")
    sleep(2)
    clear_screen()
    deaths.typing("𐌌𐌄 𐌃𐌄𐌉𐋄𐌀 𐌔𐌀𐌉𐌐")
    clear_screen()
    print("Sua mão está na maçaneta dourada")
    macaneta = input("Girar?: ").strip().lower()
    if macaneta == 'y':
        print("Você abre a porta")
    else:
        print("\nVocê não girou a maçaneta.")

def main():
    player = Human()
    primeira_fase(player)
    segunda_fase(player)

if __name__ == "__main__":
    main()
