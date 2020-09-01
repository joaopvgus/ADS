peso = float(input('Digite o seu peso: '))

altura = float(input('DIgite a sua altura: '))

if (peso > 200):
    resposta_peso = 'acima do peso'
    
else:
    print('Seu peso está tranquilo')
    
if (altura > 2.5):
    print('Abaixa a cabeça')
    
else:
    print('Anão')
    
print('Você está ' + resposta_peso)