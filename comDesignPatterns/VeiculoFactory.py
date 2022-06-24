from Carro import Carro

class VeiculoFactory:
    def criar_veiculo(self,nome):
        if nome == 'CARRO':
            marca = input('Qual a marca do seu carro? ')
            modelo = input('Qual o modelo do seu carro? ')
            ano = input('Qual o ano do seu carro? ')
            return Carro(marca, modelo, ano)

    
