O intuito deste exercício é validar o máximo de conhecimento que você possui.

Antes de mais nada, crie um repositório no git e cole o conteúdo desse texto no readme.

Você precisará construir um sistema para uma agência de veículos, ele será composto por uma api e um frontend (Desktop ou Mobile).

Sinta-se à vontade para usar a linguagem que achar melhor e pode usar templates prontos, frameworks e/ou outras coisas que possam facilitar a sua vida.

Crie um arquivo readme falando um pouco sobre quais as decisões que você tomou para a resolução do exercício, e, caso não tenha feito algo, explique o motivo. Também informe os passos para fazer sua aplicação rodar, e caso tenha, o processo de deploy.

Precisamos que nosso sistema seja capaz de:

Cadastrar a compra de um veículo, modelo, marca, ano de fabricação, placa, cor, chassi, data da compra e valor da compra.

Registrar a venda de um veículo, com data da venda, valor da venda e comissão do vendedor (10% sobre o lucro da venda).

Deverá ser possível listar todos os veículos, veículos disponíveis e histórico de veículos vendidos.

Listar o valor total em compras e vendas, lucro/prejuízo do mês e o valor pago em comissões.

Caso queira criar mais funcionalidades fique à vontade, apenas se lembre de mencionar sobre elas no readme.

Qualquer dúvida entre em contato comigo pelo linkedin, estarei à disposição para esclarecer quaisquer dúvidas que surgirem.

Ao finalizar a prova basta enviar o link do repositório no linkedin.

#
# Instruções de uso:
#### Abra o terminal na pastar sistemaVeiculos, e execute o comando:
``` 
source env/bin/activate
````
#### A máquina virtual "(env)" deverá ser ativada, após isso basta executar o comando:
``` 
python3 api/sistemaVeiculos.py
````

#
# Experiências vivenciadas

## Decisões tomadas para resolução do exercício

#### 1. Conhecimentos necessários.
Eu não tinha nenhuma experiência com desenvolvimento web, minha primeira decisão foi sintetizar quais os conhecimentos que eu precisaria para conseguir realizar o desafio, chegando a 3 pontos: Front-end, API e Banco de Dados.

#### 2. Tecnologias:
Eu optei por tecnologias acessíveis, simples e rápidas, sendo elas: Bootstrap, Flask e SQLite.

## Desafios.

#### 1. Tempo.
Precisando aprender do zero cada tecnologia, conciliando com a época de provas da faculdade, eu não tive tempo de me aprofundar nos estudos, fazendo com que por vários momentos eu sentisse que estava complicando algo que não devia ser tão complicado.
Também gostaria de ter caprichado mais no front-end, eu fiz um esboço e fui estudar o back, acabou que não não sobrou tempo para melhorar o front. 

#### 2. Relatório mensal.
Essa foi a etapa que eu mais demorei para progredir, e no fim não consegui fazer da forma que eu queria (o usuário seleciona o mês dentre os disponíveis e os gráficos são exibidos na mesma página). Acredito que essa parte poderia ser feita de forma muito mais simples com JavaScript, mas por falta de tempo eu optei por fazer toda a lógica em Python. 

## Conquistas.
#### 1. Oportunidade.
Por coincidência eu tinha acabado de organizar uma série de conteúdos para estudar em paralelo com a faculdade, sendo eles: HTML,  CSS, JavaScript, Banco de Dados, React, Docker, API’s com Python e metodologia SOLID.
O desafio funcionou como um incentivo e ao mesmo tempo possibilitando uma sensação de estar implementando algo concreto. Durante todo o processo me senti muito empolgado e ansioso para superar cada obstáculo. 

#
# Sobre o desenvolvimento da API
#### A API foi desenvolvida usando o Flask framework. O armazenamento é feito em um banco de dados SQLite.
# Sobre o funcionamento da API
#### A api sistemaVeiculos.py define todas as rotas do site, ela está diretamente ligada ao banco de dados e envia para o front arquivos do tipo lista, solicitados através dos métodos GET e POST.

## Funções criadas:
```Python
def mesesUnicos(list):
````
Recebe uma lista, e remove todos os elementos com mês e ano iguais. É usada para definir quais os meses estarão presentes no relatório mensal.

```Python
def gerarDict(listaKeys, listaValues):
````
Recebe duas listas, e retorna um dicionário. É para separar os veículos por meses únicos.
```Python
def toTuple(string):
````
transforma uma string em uma tupla de inteiros. É usada para que seja possível passar o request.form como chave no dicionário.

#
# Sobre desenvolvimento dos Templates
Para todos os templates foi usado Bootstrap 5 e Jinja2, e no relatorioMes.html também foi usado Chart.js

## Funções:
Basicamente em todos os templates que precisaram de alguma função, eu usei do Jinja2 para fazer um laço for, para manipular as strings recebidas do back e convertê-las no dado necessário para o funcionamento do front-end.



