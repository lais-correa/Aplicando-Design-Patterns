from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaMotor, qtdPortas):
        super().__init__(marca, qtdRodas, modelo, potenciaMotor)
        self.qtdPortas = qtdPortas
    
    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print('Quantidade de Portas: ', self.qtdPortas)