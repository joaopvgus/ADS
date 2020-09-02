# 3 paises - classificacao
# pais (nome, moedas(ouro 3, prata 2, bronze 1))

paises = [
    ['brasil', 50],
    ['russia', 50],
    ['argentina', 20] 
    
]

# for num in range(3):
#     pais = []
#     nome = input('Digite o nome do país: ')
#     ouro = int(input('Quantas moedas de ouro? '))
#     prata = int(input('Quantas moedas de prata? '))
#     bronze = int(input('Quantas moedas de bronze? '))
#     pais.append(nome)
#     total = (ouro*3) + (prata*2) + (bronze)
#     pais.append(total)
#     paises.append(pais)

def pega_pontuação(elemento):
    return elemento[1]

paises.sort(key=pega_pontuação)
paises.reverse()

colocacao = 1

for num in range(3):
    print(str(colocacao) + ' - ' + paises[num][0] + ' - ' + str(paises[num][1]))
    
    if num < 2 and paises[num + 1][1] == paises[num][1]:
        pass
    else:
        colocacao += 1

