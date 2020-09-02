## o for, é a primeira estrutura de repetição que veremos.

## vamos pelo mais simples, para visualizarmos seu funcionamento.

for numero in range(10):
    print(numero)
    
## ------------- EXECUTE O CÓDIGO -------------------

## o que aconteceu? nossa função range() gera números de 0 até 10,
## da forma que a usamos. Há outras formas de usar essa função, 
## mas deixaremos para depois, para não complicarmos.

## para cada número que foi gerado o for executou uma vez seu
## loop, fazendo um print() no número que foi gerado. Usamos aqui
## o nome 'numero' na estrutura do for, mas poderia ser qualquer
## outro. E essa estrutura é uma das bases das linguagens de
## programação.

## se nós quisermos, por exemplo, repetir uma mesma ação mais de
## uma vez, usamos o for, assim:

# ---------- DESCOMENTE AS TRÊS LINHAS ABAIXO E EXECUTE -------------
# for i in range(3):
    # animal = input('Digite o nome de um animal: ')
    # print(animal)
    
## veja que o for rodou três vezes, uma para cada número gerado
## pelo range(). Nós não precisamos obrigatoriamente usar nosso 'i',
## o utilizamos apenas para controlar quantos loops nosso for deve
## fazer.

## podemos também utilizar o for para percorrer os elementos de
## uma lista, exemplo:

letras = ['a','b','c','d','e']

## ------- DESCOMENTE AS DUAS LINHAS ABAIXO E EXECUTE ----------
# for letra in letras:
    # print(letra)

## percorremos nossa lista, e imprimimos cada um de nossos elementos.

## vamos agora fazer uma lista de dez elementos, os números de 1 a 10.

numeros  = [1,2,3,4,5,6,7,8,9,10]

## e façamos um código que percorra nossa lista, e some os números
## ímpares e pares, separadamente.

## ------- ESCREVA SEU CÓDIGO AQUI ABAIXO E EXECUTE ---------



















## ------- APÓS EXECUTADO COM SUCESSO, COMENTE O CÓDIGO ---------

## vamos agora para um novo desafio: faça um código que possibilite
## ao usuário cadastrar três produtos, com nome, preço e quantidade,
## e guarde esses produtos. Ao fim de cada cadastro, deve-se 
## imprimir na tela 'NOME- PREÇO - QUANTIDADE'. Use o for.

## ------- ESCREVA SEU CÓDIGO AQUI ABAIXO E EXECUTE ---------



















## -------------------------------------------------------------

## agora, crie um código que imprima o nome dos itens que tem preço
## superior a 30. Crie itens com valor acima e abaixo deste para
## verificar a funcionalidade do código.

## ------- ESCREVA SEU CÓDIGO AQUI ABAIXO E EXECUTE ---------



















## -------------------------------------------------------------

## conseguiu? Então vamos ver o funcionamento do while no arquivo 09.