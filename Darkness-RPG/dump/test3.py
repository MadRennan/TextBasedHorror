import os
import random
from time import sleep
from player import Human
import deaths
from timed_choices import timed_input

class Game:
    def __init__(self):
        self.player = Human()
        self.room = "Dormitório"
        # Dicionário de mapas
        self.mapas = {
            "Right_Hallway": '''\nSegundo Andar\nVocê está aqui\n
                                \n[] [] []
                                \n[] [] []
                                \n[] [] [*]''',
            "Mid_Hallway": '''\nSegundo Andar\nVocê está aqui\n
                              \n[] [] []
                              \n[] [] [*]
                              \n[] [] []'''
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exibir_mensagem(self, mensagem, atraso=2):
        print(mensagem)
        sleep(atraso)

    def atualizar_atributo(self, atributo, valor):
        atributo = atributo.upper()
        if atributo in self.player.atributos:
            self.player.atributos[atributo] += valor
        else:
            print(f"Atributo '{atributo}' não encontrado.")

    def obter_entrada_opcao(self, mensagem, opcoes_validas):
        while True:
            entrada = input(mensagem).strip()
            if entrada in opcoes_validas:
                return entrada
            else:
                self.exibir_mensagem(f"\nOpção inválida. Escolha entre {', '.join(opcoes_validas)}.")

    def run(self):
        while self.room != "Fim":
            if self.room == "Dormitório":
                self.dormitorio()
            elif self.room == "Right_Hallway":
                self.right_hallway()
            elif self.room == "Mid_Hallway":
                self.mid_hallway()

    def dormitorio(self):
        self.clear_screen()
        sleep(1.5)
        self.exibir_mensagem("Você lentamente abre os seus olhos. . .")
        self.exibir_mensagem("\nSua cabeça está latejando de tanta dor.")
        self.exibir_mensagem("\nSeus olhos lentamente focam no teto mofado e sujo, iluminado por uma luz pálida.")
        self.exibir_mensagem("\nVocê está deitado, mas sente que está afundando no colchão.")
        escolha = self.obter_entrada_opcao("\n1 - LEVANTAR\n2 - OLHAR AO REDOR\n3 - NÃO FAZER NADA: ", ['1', '2', '3'])
        if escolha == '1':
            self.levantar()
        elif escolha == '2':
            self.olhar_redor(inicial=True)
        elif escolha == '3':
            self.olhar_midhallway()

    def levantar(self):
        self.clear_screen()
        self.exibir_mensagem("\nApós uma certa dificuldade, você consegue se levantar.")
        self.exibir_mensagem("\nSeu corpo todo dói.")
        self.exibir_mensagem("\nVocê sente um frio na espinha ao pisar no chão sujo e gelado.")
        while True:
            subescolha = self.obter_entrada_opcao("\n1 - OLHAR AO REDOR\n2 - CHECAR SEUS BOLSOS: ", ['1', '2'])
            if subescolha == '1':
                self.olhar_redor(inicial=False)
                break
            elif subescolha == '2':
                self.exibir_mensagem("\nNão há nada em seus bolsos.")
                self.clear_screen()

    def pegar_trapos(self):
        self.clear_screen()
        self.exibir_mensagem("\nVocê pegou Trapos")
        self.player.bolsa['Trapos'] = 1
        self.exibir_mensagem("\nVocê vai para o segundo armário, mas não havia nada")
        self.exibir_mensagem("\nVocê tenta abrir o terceiro, mas está trancado")
        deaths.typing("\nO armário, estranhamente, está bem conservado\n")
        sleep(2)
        self.interagir_armarios()

    def olhar_redor(self, inicial):
        self.clear_screen()
        self.exibir_mensagem("\nVocê olha ao redor e percebe que está em um tipo de dormitório.")
        self.exibir_mensagem("\nA luz pálida vem de uma única janela enorme, se mostrando ser a luz da lua.")
        self.exibir_mensagem("\nHá diversas camas de ferro, quase nenhuma com um colchão a não ser a sua.")
        self.exibir_mensagem("\nHá três armários: um na esquerda, próximo de uma porta aberta, e dois na direita.")
        self.exibir_mensagem("\nOs armários da direita estão revirados. Estranhamente, o da esquerda está intacto.")
        self.exibir_mensagem("\nHá uma porta aberta à sua esquerda, mas não é possível ver o que há do outro lado.")

        if inicial:
            self.exibir_mensagem("\nSeu colchão parece estar te engolindo cada vez mais.")
            self.atualizar_atributo("PER", 1)
            self.interagir_redor_inicial()
        else:
            self.exibir_mensagem("\nVocê dá uma última olhada em seu colchão, que estava em perfeito estado.")
            self.atualizar_atributo("PER", 2)
            self.interagir_redor_levantado()

    def interagir_redor_inicial(self):
        escolha = self.obter_entrada_opcao("\n1 - LEVANTAR\n2 - CONTINUAR DEITADO: ", ['1', '2'])
        if escolha == '1':
            self.levantar_cama()
        elif escolha == '2':
            self.nada()

    def interagir_redor_levantado(self):
        escolha = self.obter_entrada_opcao("\n1 - IR PARA A PORTA\n2 - CHECAR OS ARMÁRIOS: ", ['1', '2'])
        if escolha == '1':
            self.porta_saida_dormitorio()
        elif escolha == '2':
            self.check_armario()

    def porta_saida_dormitorio(self):
        self.clear_screen()
        self.exibir_mensagem("\nVocê anda até a porta... sem saber onde isso te levará...")
        self.room = "Right_Hallway"

    def right_hallway(self):
        self.clear_screen()
        self.exibir_mensagem("\nVocê está em um corredor estreito.")
        self.exibir_mensagem("\nEstá muito escuro para você ver além disso.")
        self.exibir_mensagem("\nA única luz que ilumina um pouco do corredor, vem da janela.")
        self.exibir_mensagem("\nHá uma comoda próxima a janela.")
        escolha = self.obter_entrada_opcao("\n1 - IR ATÉ A JANELA\n2 - IR ADIANTE NO CORREDOR: ", ['1', '2'])
        if escolha == '1':
            self.interagir_janela()
        elif escolha == '2':
            self.avanca_corredor()

    def interagir_janela(self):
        escolha = self.obter_entrada_opcao("\n1 - OLHAR O COMODO\n2 - OLHAR A JANELA\n3 - DAR MEIA VOLTA: ", ['1', '2', '3'])
        if escolha == '1':
            self.atualizar_atributo("PER", 1)
            self.exibir_mensagem("\nVocê encontra uma pequena gaveta.")
            self.exibir_mensagem("\nAo abrir, você encontra uma lanterna, refletindo o brilho da lua em seu rosto.")
            self.exibir_mensagem("\nA lanterna está desgastada, mas ainda pode ser usada.")
            self.pegar_lanterna()
        elif escolha == '2':
            self.exibir_mensagem("\nVocê observa a floresta lá fora, e o brilho da lua a ilumina suavemente.")
            deaths.typing("\nVocê escuta as folhas se mexendo... Há alguma coisa lá fora.")
            self.atualizar_atributo("PER", 1)
        elif escolha == '3':
            self.exibir_mensagem("\nVocê decide voltar ao corredor escuro...")
            self.exibir_mensagem("\nVocê ainda não vê razão para voltar para o Dormitório, então você segue adiante.")
            self.avanca_corredor()

    def pegar_lanterna(self):
        escolha = self.obter_entrada_opcao("Pegar a lanterna? [Y/N]: ", ['y', 'n'])
        if escolha == 'y':
            self.player.bolsa['Lanterna'] = 30
            self.exibir_mensagem("\nVocê pegou a lanterna.")
        elif escolha == 'n':
            self.exibir_mensagem("\nVocê decide deixar a lanterna por lá.")

    def avanca_corredor(self):
        self.exibir_mensagem("\nVocê avança pelo corredor...")
        sucesso, rolagem = self.player.rolar_dado("AGI")
        if sucesso:
            self.clear_screen()
            self.exibir_mensagem(f"Você pisa em uma madeira podre, mas foi ágil o suficiente para não cair. (Rolagem: {rolagem})")
            self.atualizar_atributo("AGI", 1)
            self.room = "Mid_Hallway"
        else:
            deaths.DeathbyCrackingFloor()

    def mid_hallway(self):
        self.room = "Mid_Hallway"
        self.clear_screen()
        sleep(2)
        self.exibir_mensagem("Você para em uma estrutura alta.")
        self.exibir_mensagem("\nAo virar para esquerda, você vê onde era o centro do lugar.")
        self.exibir_mensagem("\nEm sua esquerda e direita em sua frente, há escadas para baixo.")
        self.exibir_mensagem("\nAtrás de você, Há um elevador, mas também ao lado dele, há escadas para subir ainda mais.")
        deaths.typing("\nAtrás de você es")
        self.clear_screen()
        escolha = self.obter_entrada_opcao("1 - OLHAR AO REDOR\n2 - IR PARA ESCADAS DE BAIXO\n3 - IR PARA AS ESCADAS DE CIMA\n4 - IR PARA O ELEVADOR: ", ['1', '2', '3', '4'])
        if escolha == '1':
            self.exibir_mensagem("\nVocê decide olhar ao redor.")
            self.olhar_midhallway()
        elif escolha == '2':
            self.exibir_mensagem("\nVocê decide descer pelas escadas.")
        elif escolha == '3':
            self.exibir_mensagem("\nVocê sobe as escadas.")
        elif escolha == '4':
            self.exibir_mensagem("\nVocê vai até o elevador.")

    def olhar_midhallway(self):
        self.clear_screen()
        sleep(2)
        self.exibir_mensagem("Onde você está agora, no chão, há diversos frascos, folhas e outras coisas jogadas.")
        self.exibir_mensagem("\nEstá uma bagunça..")
        self.exibir_mensagem("\nA baixo das escadas, você vê onde provavelmente seria a recepção")
        self.exibir_mensagem("\nÉ enorme, e há diversas cadeiras para receber pessoas.")
        self.exibir_mensagem("\nVocê também consegue ver o balcão, que está com grades.")
        self.exibir_mensagem("\nHá uma porta no fundo, você assume que pode ser a saída.")
        self.exibir_mensagem("\nHá também dois corredores, pela esquerda e outro pela direita.")
        self.exibir_mensagem("\nAo lado do elevador onde você está, há um tipo de mapa.")
        self.atualizar_atributo("PER", 1)
        escolha = self.obter_entrada_opcao("1 - OLHAR MAPA\n2 - IR PARA ESCADAS DE BAIXO\n3 - IR PARA AS ESCADAS DE CIMA\n4 - IR PARA O ELEVADOR: ", ['1', '2', '3', '4'])
        if escolha == '1':
            self.mostrar_mapa()
        elif escolha == '2':
            self.exibir_mensagem("")
        elif escolha == '3':
            self.exibir_mensagem("")
        elif escolha == '4':
            self.exibir_mensagem("")

    def mostrar_mapa(self):
        if self.room in self.mapas:
            self.exibir_mensagem(self.mapas[self.room])
        else:
            self.exibir_mensagem("Mapa não disponível para esta região.")

    def nada(self):
        self.clear_screen()
        self.exibir_mensagem("\nVocê decide continuar deitado...")
        deaths.DeathbyBelow()

    def levantar_cama(self):
        self.clear_screen()
        self.exibir_mensagem("\nVocê decide levantar, mas sente uma dificuldade extrema ao fazer isso.")
        deaths.typing("\nHá algo te puxando para baixo...")
        sucesso, rolagem = self.player.rolar_dado("FOR")
        if sucesso:
            self.exibir_mensagem(f"\nVocê consegue se desvinciliar da força, conseguindo se levantar. (Rolagem: {rolagem})")
            self.atualizar_atributo("FOR", 1)
            self.interagir_redor_levantado()
        else:
            self.clear_screen()
            deaths.DeathbyBelow()

    def check_armario(self):
        self.clear_screen()
        escolhaitem = self.obter_entrada_opcao("\nVocê checa o primeiro armário, e não há nada além de trapos. Pegar? [Y/N]: ", ['y', 'n'])
        if escolhaitem == 'y':
            self.pegar_trapos()
        elif escolhaitem == 'n':
            self.exibir_mensagem("\nVocê vai para o próximo armário, onde não havia nada.")
            self.exibir_mensagem("\nVocê tenta abrir o terceiro, mas está trancado.")
            deaths.typing("\nO armário, estranhamente, está bem conservado.")
            deaths.typing("\nVocê sente um frio na espinha enquanto decide o que fazer.")
            self.exibir_mensagem("\n1 - IR PARA A PORTA")
            escolha = self.obter_entrada_opcao("Sua escolha: ", ['1'])
            if escolha == '1':
                self.porta_saida_dormitorio()
            elif escolha == '2':
                deaths.DeathbyError()

if __name__ == "__main__":
    game = Game()
    game.run()
