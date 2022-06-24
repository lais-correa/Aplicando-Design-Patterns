from Veiculo import Veiculo

class Bicicleta(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro = False):
        super().__init__(marca, qtdRodas, modelo, velocidade = 0)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print ('Número de marchas: ', self.numMarchas)
        print ('Possui bagageiro: ', self.bagageiro)