abc = 'String'

print(abc[-1])

pessoas = ['Jorge', 'Tom', 'Jerry', 'Brutus']
pessoas[0] = 'Mike'
print(*pessoas)  # mostra todos os ementos dentro de pessoas
pessoas.append('Toby')  # adiciona 'Toby' no final da pessoas

lista1 = ['John', 'Leon']
pessoas.extend(lista1)  # adiciona os elementos de lista1 no final de pessoas
pessoas.insert(0, 'Ana')  # adiciona "Ana" na posição indicada e empurra pra frente todos os elementos posteriores
pessoas.remove('Tom')  # remove os elementos que tem o valor "Tom"
print(*pessoas)

# pessoas.clear() # apaga todos os elementos de pessoas
# pessoas.pop() # se usado assim, apaga o último elemento, se for especificado um número dentro do método, esse 
# número aponta qual item será apagado, por exemplo: pessoas.pop(0) apaga o elemento de posição 0
print(pessoas.index('Leon'))  # imprime a localização na lista de 'Leon'
print(pessoas.count('Jerry'))  # imprime quantos elementos de valor "Jerry" existem na lista
pessoas.sort()  # organiza a lista em ordem crescente ou alfabética
pessoas.reverse()  # inverte a ordem dos elementos da lista

pessoas2 = pessoas.copy() # faz uma cópia de todos os elementos de pessoas e as guarda em 
pessoas2.insert(0, 'Karen') 

print('people = ' + str(pessoas))
print('people2 = ' + str(pessoas2))

coordinates = (1, 2)  # isso é a forma de se declarar uma 'tuple', que é uma lista imutável