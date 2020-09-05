## vamos agora criar uma lista que contem 10 listas com a seguinte estutura:
## [nome_pessoal, pontuação(um valor entre 0 e 100)]

candidatos = [ ['João', 82], ['Paulo', 96], ['Fábio', 46], ['Jorge', 54],
               ['Alexandre', 33], ['Artur', 75], ['Pedro', 47], ['Marta', 22],
               ['Luiza', 88], ['Diego', 72]]

## feita nossa lista, vamos criar um método (uma função), que receba um 
## elemento como parâmetro e retorne um de seus elementos. EM seguida
## explicarei o porquê.

def get_pontos(candidato):
    return candidato[1] ## essa é a posição da pontuação, lembre

## agora, queremos organizar nossa lista de candidados de acordo com a
## pontuação de cada um. E para isso que servirá nossa função get_pontos().
## Utilizaremos a função sort() para organizar nossa lista, porém, já que
## nossa lista é formada de listas, não podemos exatamente organizar os
## elementos em ordem crescente ou alfabética. Para fazermos isso, temos
## informar qual elemento das listas deve ser usado como parâmetro para
## que se faça a organização, para isso, dentro do sort() utilizaremos o
## identificador 'key', e apontaremos nosso parâmetro de organização.

candidatos.sort(key=get_pontos)

## vamos imprimir a lista para verificar se funcionou.

print(candidatos)

## e pronto, temos os candidatos organizados com base em seu segundo elemento.

## caso queiramos que a ordem seja decrescente, para termos a melhor pontuação
## no começo e a pior no fim, devemos simplesmente inverter a lista.

candidatos.reverse()

print(candidatos)

## agora entendemos como funciona o 'key' no método sort().