## veremos aqui como funciona a estrutura condicional If
## agora ficaremos mais objetivos

## porém, antes de vermos como funciona um if, precisamos saber
## o que são valores booleanos.

## Resumindo: verdadeiro e falso. Estes são nossos valores.
## Em Python, são True e False.

## agora veremos quais são os operadores lógicos em Python:
## > (maior que)
## < (menor que)
## >= (maior que ou igual a)
## <= (menor que ou igual a)
## == (igual)
## != (diferente)

## agora veremos a estrutura do if:

if (5 > 2):
    print('Cinco é maior do que 2')
    
## esse '5 > 2' é uma operação lógica. Eu estou perguntando ao
## computador se cinco é maior do que dois, e ele responderá que
## sim, portanto, temos como resultado dessa operação lógica um
## valor booleano, que é True, que é verdadeiro.

## temos dentro do if, o print() como um exemplo. Ou seja, temos
## como estrutura:

## Se cinco for maior do que dois, dê print() nessa mensagem
## simples assim
## porém nós sabemos muito bem que 5 é maior do que 2, então de
## que isso nos serve?

## a história muda se nós tivermos na condição, variáveis, porque
## a próxima ação do computador irá depender da escolha do usuário,
## de repente. Por exemplo, se queremos que o nosso usuário escolha
## se vai fazer uma soma ou subtração, podemos fazer assim:

opcao = input('Você quer fazer uma soma ou uma subtração?\n\n1 - soma \n2 - subtração\n\n')

## o '\n' serve para pular uma linha

if (opcao == '1'): ## estamos fazendo a comparação usando áspas porque o resultado do input é sempre texto
    ## aqui, com um TAB de distância, colocamos o que acontecerá se
    ## a condição resultar True, ou seja, se o usuário digitar '1', esse
    ## será o resultado
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    resultado = a + b
    print(resultado)
    ## mas, o que fazer se essa condição não resultar True, é para
    ## isso que servem o else e ou elif. O else significa senão, ou
    ## ou seja, se aquela operação não resultar True, se fará o que
    ## se especifica no else. E o elif é uma abreviação de else if,
    ## que significa "senão, se", ou seja, se a condição do início
    ## do if não resultar True, ele verificará se essa outra condição
    ## resulta
    
    ## mas enfim, se opcao não for igual a '1', temos que ver se é
    ## igual a '2', portanto, fora do if, escrevemos:
    
elif (opcao == '2'):
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    resultado = a - b
    print(resultado)
    
    ## porém, e se o usuário escolher nem '1', nem '2', pq ele é
    ## birrento, temos de ter uma resposta. É aí que entra nosso
    ## else, nosso senão.
else:
    print('Por favor, escolha uma opção válida')
    
## tem mais um recurso interessante para vermos, que são os operadores
## lógicos E e OU, em Python, and e or

## se colocamos por exemplo:

if (5 > 2) and (10 < 4):
    print('oiê')

## simplesmente não teremos o interior do If executado, pois 5 > 2 é True, mas 10 < 4 é False
## e o If só executa o que está em seu corpo se o resultado geral for um True, o que não é 
## o caso. O or designa que ao menos uma daquelas funções deve ser True.

## um if pode ser posto dentre de outro, não há nenhum problema.