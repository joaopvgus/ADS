## VOCÊ DEVE COPIAR ESTE ARQUIVO PARA SUA PASTA PESSOAL

## o que são variáveis?
## variáveis são identificadores na memória do computador que nós criamos
## de forma a facilitar nosso relacionamento com ele. Identificadores para
## guardarmos valores que utilizaremos. Vamos fazer uma simples declaração
## de variável.

a = 5 # o símbolo de '=' é utilizado para realizar uma atribuição, ou seja,
## pôr dentro daquela nossa variável referida, o valor que estamos declarando.
## Portanto, a partir de agora, no nosso código, onde quer que chamemos a
## variável 'a', estaremos chamando o valor nela referido, e até o momento,
## este valor é '5'.

## porém, esse valor, como a própria denominação da variável indica, pode variar.
## e como fazemos isso? Fazendo uma simples sobreescrita. Ex.:

a = 10

# pronto, agora a variável 'a' guarda o valor '10'.

b = 5

## agora vamos aos operadores matemáticos: + , - , / (para divisão),
## * (para multiplicação), ** (para potência) e % (para indicar o restante
## da divisão). Vamos aos exemplos:

c = 40/2 # estamos fazendo uma simples operação de divisão, que segundo a santa
## matemática que nunca nos engana, resulta em 20, logo, esse é o valor guardado
## na nossa variável 'c'.

## vamos introduzir agora o método print(), que imprime no terminal o que lhe
## indicamos.

print(c)

## chamamos assim um método. Seu identificador, e entre àspas o valor
## que lhe estamos passando, nesse caso, 'c', e veremos ao executar o código
## que o valor que nos é retornado não é 'c', 'c' é com o que nós vamos trabalhar
## internamente, mas o valor que será imprimido, será o que ele guarda, que é '20'.

## vamos agora pedir ao usuário que nos dê um valor para trabalharmos, e faremos
## isso usando o método input(). E o faremos assim:

entrada = int(input('Digite aqui um número'))

## o que acabamos de fazer? criamos uma
## variável 'entrada', e lhe atribuímos o valor dado pelo usuário através do
## método input(), e o que é esse 'Digite aqui um número' entre parênteses?
## é o texto que nós passamos ao usuário, para lhe informar o que queremos.

## ---------------- EXECUTE O CÓDIGO E DIGITE UM NÚMERO ---------------------------

a = 10 - entrada

print(a)

## agora, se você se atentar ao erro que foi apontado pelo terminal, verá que ele
## indica a linha 46. Estamos fazendo uma simples sobreescrita na variável 'a',
## correto? Porém há um problema, o valor que nos é retornada pelo método input é,
## por padrão, do tipo String, isso é, do tipo texto, então estamos tentando fazer
## o mesmo que '5 - "bolo de pote"', mesmo que o valor digitado tenha sido um
## número, o seu formato é incompatível para operações matemáticas, então temos de
## convertê-lo ao formato numérico, e faremos isso usando o método int().

## perceba que em programação, o computador lê as linhas de trás para frente,
## como assim? é o seguinte: perceba que não há muito sentido em, como fizemos na
## linha 39, criar uma variável e guardar nela um valor que não existe, portanto,
## o que acontece é, primeiro é executado o input(), que guarda um valor e o entrega
## à variável 'entrada'. Então agora transformaremos o valor do input() em um número,
## e o colocaremos na variável entrada, e ficará assim:

## entrada = int(input('Digite aqui um número'))

## segundo a leitura do código feita pelo computador, pedimos através do input() um
## valor e o transformamos em inteiro através do método int() e o atribuímos à
## variável entrada através do '='.

## ------------------- CORRIJA A LINHA 39 e EXECUTE O CÓDIGO ----------------------

## agora entendamos a leitura procedural do código, isto é, a sua execução direta,
## linear. Se escrevemos:

a = 10
a = 15
a = 20

## ao fim, se dermos um print() na variável 'a', veremos '20'. Ou seja, a variável
## foi sobreescrita inúmeras vezes e sua última sobreescrita foi com o valor '20'.
## isso nos evidencia que a execução do código é feita de cima para baixo.

## mais uma última informação: é possivel que se faça isso:

a = a + 1

## o que nós fizemos aqui, foi, somamos o valor de 'a' que é vinte, a 1, e guardamos
## o resultado na variável 'a', logo, 'a' agora guarda '21'. Essa expressão pode ser
## resumida em:

a += 1

## e funciona com todos os outros operadores, sendo -= , *= , /= .

## agora, escreva um código que peça um valor, guarde em uma variável, peça outro
## valor, guarde em outra variável, e que em seguida crie uma terceira variável que
## seja o resultado da primeira variável vezes a segunda. E em seguida, imprima
## esse resultado. Lembrando: a multiplicação é feita com *

## prontinho, agora se proponha outras operações e faça algumas vezes até fixar ^^