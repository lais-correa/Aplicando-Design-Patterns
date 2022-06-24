from Veiculo import Veiculo

class Automovel(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, potenciaMotor):
        super().__init__(marca, qtdRodas, modelo)
        self.potenciaMotor = potenciaMotor

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print ('Potencia do Motor:', self.potenciaMotor)