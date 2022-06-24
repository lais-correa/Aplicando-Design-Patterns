from Cores import Cores

cor = Cores()

class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade = 0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self, valor):
        self.velocidade = self.velocidade + valor
        return self.velocidade

    def frear(self, valor):
        if self.velocidade > 0:
            self.velocidade = self.velocidade - valor
        else:
            print(f'{cor.vermelho}\nO veículo já está parado, portanto não há como frear.')
        return self.velocidade


    def imprimirInformacoes(self):
        print(f'{cor.amarelo}\nMarca: ', self.marca)
        print('Quantidade de rodas: ', self.qtdRodas)
        print('Modelo: ', self.modelo)
        print('Velocidade: ', self.velocidade)