from Carro import Carro
from Moto import Moto
from Bicicleta import Bicicleta
from Cores import Cores

cor = Cores()
    

def registraVeiculo():

    while True:

        marcaVeiculo = input(f'{cor.branco}\nInsira a marca do veículo: ')
        modeloVeiculo = input('Insira o modelo do veículo: ')

        tipoVeiculo = input ('Insira o tipo de veículo que você deseja cadastrar: ').upper()

        if tipoVeiculo == 'CARRO':

            qtdRodas = 4
            potenciaMotor = input('Insira a potencia do motor: ')
            qtdPortas = input('Insira a quantidade de portas do carro: ')
            carro = Carro(marcaVeiculo, qtdRodas, modeloVeiculo, potenciaMotor, qtdPortas)
            print(f'{cor.verde}\nCadastrado com sucesso!')
            carro.imprimirInformacoes()        
            modificaVelocidade(carro)

    ######################################
            
        elif tipoVeiculo == 'MOTO':


            escolha = input('A moto possui partida elétrica? S para Sim, N para não: ').upper()
            if escolha =='S':
                partidaEletrica = True
            elif escolha == 'N':
                partidaEletrica = False
            
            else:
                print(f'{cor.vermelho}\nEscolha algo válido!')         

            qtdRodas = 2
            potenciaMotor = input('Insira a potencia do motor: ')
            moto = Moto(marcaVeiculo, qtdRodas, modeloVeiculo, potenciaMotor, partidaEletrica)
            print(f'{cor.verde}\nCadastrado com sucesso!')
            moto.imprimirInformacoes()
            modificaVelocidade(moto)

    ##########################################
        elif tipoVeiculo =='BICICLETA':
            
            numMarcha = input('Insira o número de marchas que a bicicleta possui: ')
            esc = input('A bicicleta possui bagageiro? S para Sim, N para Não: ').upper()
            if esc =='S':
                bagageiro = True
            elif esc == 'N':
                bagageiro = False
            else:
                print(f'{cor.vermelho}\nEscolha algo válido!') 

            qtdRodas = 2
            bike = Bicicleta(marcaVeiculo, qtdRodas, modeloVeiculo, numMarcha, bagageiro)
            print(f'{cor.verde}\nCadastrado com sucesso!')
            bike.imprimirInformacoes()
            modificaVelocidade(bike)
            
        else:
            print(f'{cor.vermelho}Escolha algum veículo válido! Veículos válidos: Carro, Moto, Bicicleta')

    ########################################## 
        escolha = input('\nDeseja adicionar mais algum veículo? S para Sim, N para Não: ').upper()
        if escolha == 'N':
            print(f'{cor.verde}\nVocê escolheu encerrar.')
            break
   

def modificaVelocidade(veiculo):
    while True:
        escolha = input( f"""\n\n {cor.rosa}          Você gostaria de modificar a velocidade do seu veículo?  
                        ----------------------------------
                        1. Acelerar Veículo
                        2. Frear Veículo   
                        3. Sair       
                        ----------------------------------
                        """)
        if escolha == '1':
            try:
                valor = int(input(f'{cor.branco}Insira um valor para acelerar seu automóvel: '))
                veiculo.acelerar(valor)
                veiculo.imprimirInformacoes()
            except:
                print(f'{cor.vermelho}\nInsira apenas números!')
        elif escolha == '2':
            try:
                valor = int(input(f'{cor.branco}Insira um valor para frear seu automóvel: '))
                veiculo.frear(valor)
                veiculo.imprimirInformacoes()
            except:
                print(f'{cor.vermelho}\nInsira apenas números!')
        else:
            print(f'\n{cor.branco}Você escolheu sair.')
            break


     

registraVeiculo()