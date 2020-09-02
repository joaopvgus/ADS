## vamos agora, por fim, vermos como funciona o while.
## While significa 'enquanto', e trabalha com valores
## booleanos, assim como o if. Vejamos sua estrutura:

a = 5

while (a > 0):
    print(a)
    a -= 1
    
## --------- EXECUTE O CÓDIGO --------------

## nossa estrutura é a seguinte: ENQUANTO ('a' for maior
## do que 0), dê print() em 'a', e faça o operação: 'a' é
## igual a 'a - 1'.

## lembrando que 'a > 0' é uma operação lógica, o que
## resulta dela é True ou False. E quando for False,
## encerra-se o loop. Portanto, se eu quero por exemplo,
## fazer um menu de opções que se repete até o usuário
## desejar encerrar o loop, basta fazer assim:

opcao = 3

while (opcao != '0'):
    
    opcao = input('Qual sua escolha? \n1 - Opção 1 \n2 - Opção 2 \n0 - Sair\n\n')
    
    if (opcao == '1'):
        print('Você escolheu a opção 1')
        
    elif (opcao == '2'):
        print('Você escolheu a opção 2')
        
    elif (opcao != '0'):
        print('Opção inválida')
        
## Agora, um pequeno desafio para exercitar o entendimento:

## escreva um código que funcione como uma calculadora. Tenha um menu com as
## seguintes opções: 1 - soma, 2 - subtração, 3 - divisão, 4 - multiplicação,
## 5 - exponenciação e 0 - sair. Quando o usuário escolher sua opção, deve-se
## pedir dele os dois números para realizar a operação, e no fim de cada
## operação, deve haver um print() do resultado.

## --------------- ESCREVA SEU CÓDIGO AQUI ABAIXO E EXECUTE -----------------

