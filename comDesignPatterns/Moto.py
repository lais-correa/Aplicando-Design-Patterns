from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade = self.velocidade + valor
        return self.velocidade

    def frear(self, valor):
        if self.velocidade > 0:
            self.velocidade = self.velocidade - valor
        else:
            print(f'\nO veículo já está parado, portanto não há como frear.')
        return self.velocidade
    
    def printVeiculo(self):
        print(f"""
            A marca da moto é: {self.__marca}
            O modelo é: {self.__modelo}
            O ano é: {self.__ano}
            A velocidade é: {self.velocidade} km/h""")