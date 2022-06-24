def modificarVelocidade(veiculo):
    while True:
        escolha = input( f"""\n\nVocê gostaria de modificar a velocidade do seu veículo?  
                        ----------------------------------
                        1. Acelerar Veículo
                        2. Frear Veículo   
                        3. Sair       
                        ----------------------------------
                        """)
        if escolha == '1':
           acelerarVeiculo(veiculo)
           veiculo.printVeiculo()
        elif escolha == '2':
            frearVeiculo(veiculo)
            veiculo.printVeiculo()
        else:
            print(f'\nVocê escolheu sair.')
            break

def acelerarVeiculo(veiculo):
    velocidade =int(input('Qual velocidade? ')) 
    veiculo.acelerar(velocidade)
    
def frearVeiculo(veiculo):
    velocidade =int(input('Qual velocidade? ')) 
    veiculo.frear(velocidade)