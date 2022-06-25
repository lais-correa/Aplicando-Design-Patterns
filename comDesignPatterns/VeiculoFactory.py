from Carro import Carro
from Moto import Moto
from Bicicleta import Bicicleta

class VeiculoFactory:
    def criar_veiculo(self,nome):
        if nome == 'CARRO':
            marca = input('Qual a marca do seu carro? ')
            modelo = input('Qual o modelo do seu carro? ')
            ano = input('Qual o ano do seu carro? ')
            return Carro(marca, modelo, ano)

        elif nome == 'MOTO':
            marca = input('Qual a marca da sua moto? ')
            modelo = input('Qual o modelo da sua moto? ')
            ano = input('Qual o ano da sua moto? ')
            return Moto(marca, modelo, ano)

        elif nome == 'BICICLETA':
            marca = input('Qual a marca da sua bicicleta? ')
            modelo = input('Qual o modelo da sua bicicleta? ')
            ano = input('Qual o ano da sua bicicleta? ')
            return Bicicleta(marca, modelo, ano)
    
