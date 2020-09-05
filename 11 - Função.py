## funções são estruturas que podem ser invocadas a qualquer momento do código,
## que excutam o conjunto de código em seu corpo, e retornam ou não uma informação.
## funções são um dos princípios básicos de programação, e os utilizamos para
## manter o código, limpo, organizado e com trabalhos bem atribuídos a cada parte,
## e por deixar o código organizado, também auxilia a localizar e corrigir proble-
## mas.

## vamos agora declarar uma função, para ser sua sintaxe:

def soma():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    total = num1 + num2
    print(total)
    
## se executarmos o código até a linha 12, veremos que não acontecerá nada. E não
## acontecerá pois apenas declaramos a função, como fazemos com uma variável. Para
## que seja executada, devemos fazer assim:

soma()

## e se executarmos o código até a linha 20, teremos a execução de todo o código
## contido na função soma().

## podemos ainda, por inúmeros fatores, desejar que os inputs() sejam feitos fora
## da função, mas para isso temos de modificar o escopo de nossa função, temos de
## definir parâmetros, os elementos que seram inseridos entre parênteses quando
## chamarmos nossa função.

def soma(numero1, numero2):
    total = numero1 + numero2
    print(total)
    
## e para chamarmos nossa função, faremos assim:

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma(num1, num2)

## perceba que o que importa para a identificação dos parâmetros não é o nome da
## variável, mas sua posição.

## e pronto, teremos o mesmo resultado, porém utilizando caminhos diferentes.

## podemos ainda, por último, fazer com que nossa função não imprima o resultado,
## pois nem sempre será isso que iremos querer. Podemos querer, que, ao invés
## disso, ela nos retorne um valor, nos retorne o resultado, para que o utilizemos
## para imprimir, ou para fazer outras operações. Façamos assim:

def soma(numero1, numero2):
    total = numero1 + numero2
    return total

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

resultado = soma(num1, num2)

print(resultado)

## prontinho, vimos três formas de fazer, a princípio, a mesma coisa, mas veremos
## mas pra frente, que há casos e casos, para utilizarmos uma ou outra forma.