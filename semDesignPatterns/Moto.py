from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaMotor, partidaEletrica = False):
        super().__init__(marca, qtdRodas, modelo, potenciaMotor)
        self.partidaEletrica = partidaEletrica
    
    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print('Partida Elétrica: ', self.partidaEletrica)