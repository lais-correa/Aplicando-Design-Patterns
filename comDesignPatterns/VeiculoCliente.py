from VeiculoFactory import VeiculoFactory
from modificarVelocidade import modificarVelocidade


def veiculoCliente():
    veiculo_factory= VeiculoFactory()
    veiculo_nome = input("Qual o tipo do seu veículo? ").upper()
    veiculo = veiculo_factory.criar_veiculo(veiculo_nome)
    modificarVelocidade(veiculo)
    


