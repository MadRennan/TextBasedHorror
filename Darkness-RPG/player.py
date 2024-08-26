import sys, random

# Definindo uma classe Human
class Human:
    def __init__(self):
        self.vida = {"Vida": 5} #Só há como aumentar via itens de cura
        self.bleeding = False
        self.bolsa = {}
        # Inicializa o dicionário de atributos com valores padrão
        self.atributos = {
            'PER': 5,  # Percepção
            'FOR': 5,  # Força
            'AGI': 5,  # Agilidade
            'INT': 5,  # Inteligência
            'SAN': 5   # Sanidade
        }

    def atualizar_atributo(self, atributo, valor):
        if atributo in self.atributos:
            self.atributos[atributo] += valor
        else:
            print(f"Atributo '{atributo}' não encontrado.")

    def rolar_dado(self, atributo):
        # Rolagem de um dado de 1 a 20
        rolagem = random.randint(1, 20)
        # Compara a rolagem com o atributo para determinar o sucesso ou fracasso
        sucesso = rolagem <= self.atributos.get(atributo, 0)
        return sucesso, rolagem

    def bleeding():
        bleeding = True
        if bleeding == True:
            typing("Você está sangrando..")
            vida -= 1
            while bleeding == True:
                if bolsa not in ['Trapos', 'Bandagem', 'Kit-Médico', 'Frasco-Vermelho']:
                    typing("Você não possui nenhum item para curar-se. .")
                    break
                else:
                    print(bolsa)
                    cura = string(input("Qual item desejas usar?: ")).capitalize()
                    if cura not in ['Trapos', 'Bandagem', 'Kit-Médico', 'Frasco-Vermelho']:
                        print("Opção inválida")
                        continue
                    else:
                        print(f"Você usou {cura} em você.")
                        print("Você não está mais sangrando..")
                        bleeding = False
                        break
        else:
            typing("Seu corpo, está intacto.. por agora.")

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.1)
