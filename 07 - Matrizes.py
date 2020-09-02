## agora que já temos a base do conhecimento de listas e como manipulá-las,
## vamos complicar um pouco as coisas.

itens = []

## criamos uma lista, se fizermos um lista.append() e colocarmos um novo
## elemento nela, não há maiores problemas de compreensão, mas podemos
## fazer um append() com outra lista.

## vamos imaginar a seguinte situação, temos que criar um sistema que crie
## itens, com nome, valor e quantidade. Vamos, por hora, nos atentar apenas
## a este problema.

## criamos na linha 4 uma lista vazia com nome 'itens', e nela, poderíamos
## fazer append(nome), append(valor) e append(quantidade), porém, conforme
## fôssemos preenchendo a lista, perderíamos organização, e não seria fácil
## manipular esta lista, então faremos o seguinte:

nome = input('Digite o nome do item: ')
valor = float(input('Digite o valor do item: '))
quantiade = float(input('Digite a quantidade do item: '))

## pedimos os atributos que vão constituir nosso item, até aí nenhum problema,
## devemos agora juntar tudo isso, dessa forma:

novo_item = [nome, valor, quantiade]

## e agora, colocamos essa nossa lista (que descreve um item), dentro da nossa
## lista que guarda itens.

itens.append(novo_item)

## mas digamos que queremos outro item. Basta repetirmos o processo:

nome = input('Digite o nome do item: ')
valor = float(input('Digite o valor do item: '))
quantiade = float(input('Digite a quantidade do item: '))

novo_item = [nome, valor, quantiade]

itens.append(novo_item)

## prontinho, para visualizarmos como está nosso conjunto de itens, vamos dar
## um print.

print(*itens)

## se, por exemplo, quisermos pegar o primeiro item, devemos fazer como fizemos
## no arquivo 05:

print(itens[0])

## se quisermos preço desse item, sabendo que o preço é o segundo valor, fazemos:

print(itens[0][1])

## agora, se quisermos que o usuário escolha de qual item quer o preço, basta
## criarmos um variável à qual ele designa sua opção:

opcao = int(input('De qual item você quer ver o preço? '))

## se ele cadastrou 'arroz' primeiro, ele vê o 'arroz' como '1', porém, para nossa
## lista, é o elemento [0], e assim sucessivamente, logo, temos de fazer uma
## subtração para referenciar na nossa lista, assim:

print(itens[opcao - 1][1])

## prontinho, estamos acessando a posição que o usuário designar e resgantando 
## o preço.

## se quisermos mudar o preço:

opcao = int(input('De qual item você quer mudar o preço? '))

novo_valor = float(input('Qual o novo valor? '))

itens[opcao - 1][1] = novo_valor

## agora, para no prepararmos para fazer nosso primeiro sisteminha, vamos
## ver como funcionam, superficialmente o for e o while.