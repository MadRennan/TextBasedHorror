import sys, random

# Definindo uma classe Human
class Human:
    def __init__(self):
        self.vida = {"Vida": 5}
        self.bolsa = {}
        self.atributos = {"Força": 5, "Int": 5, "Destreza": 5, "Agi": 5, "Per": 5}

    def atualizar_atributo(self, atributo, valor):
        if atributo in self.atributos:
            self.atributos[atributo] += valor
        else:
            print(f"Atributo '{atributo}' não encontrado.")

    def rolar_dado(self, atributo):
        # Rolagem de um dado de 1 a 10
        rolagem = random.randint(1, 10)
        # Compara a rolagem com o atributo para determinar o sucesso ou fracasso
        sucesso = rolagem <= self.atributos.get(atributo, 0)
        return sucesso, rolagem
