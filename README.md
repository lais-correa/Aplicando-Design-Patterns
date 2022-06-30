# 🪄 Aplicando Design Patterns

_Trabalho desenvolvido por Patrícia e Laís_

## 🙈 Problema

O código que havíamos desenvolvido primeiramente é o que esta no diretório semDesignPatterns, nele criamos as classes Veiculo e Automovel, onde a classe bicicleta herdava de veiculo, enquanto a classe automovel também herdava de veiculo, e as classes carro e moto, herdavam de automovel, o que deixava o código bastante confuso.

Além disso, nosso arquivo main.py estava com muita informação e mal otimizado, ficando uma parte importante do código neste arquivo, o que também não era algo bom.

E caso depois nosso código precisasse de manutenção, ou fosse necessário incorporar novos meios de condução, isso seria bastante difícil e levaria muito tempo.

## 🤯 Solução

A solução que encontramos para melhorar nosso código e otimizá-lo foi utilizar o design patterns **Factory Method** que é um padrão de projeto criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.

Então a partir desse pensamento fizemos algumas alterações:

1. Descontinuamos a classe automóvel;
2. Transformamos a classe Veiculo em uma classe abstrata;
3. Criamos a função veiculoCliente onde primeiramente perguntamos qual o tipo de veículo o usuário quer criar;
4. Criamos a classe VeiculoFactory, que é a nossa fábrica de meios de condução, onde podemos adicionar novos veiculos com maior facilidade;
5. Criamos um arquivo especialmente para a função de alterar a velocidade do veículo;
6. Continuamos com as classes Carro, Moto e Bicicleta, porém agora elas herdam da classe abstrata Veiculo;
7. E por fim, apenas chamamos no main o método veiculoCliente();
