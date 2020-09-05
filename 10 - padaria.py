## menu: 1 - cadastrar produto, 2 - venda de produto, 3 - total de vendas, 4 - ver estoque 0 - sair
## CADASTRAR PRODUTO
##      pedir NOME
##      pedir PRECO
##      pedir QUANTIDADE
##      imprimir NOME - PRECO - QUANTIDADE

## VENDA DE PRODUTO
##      pedir NOME
##      pedir QUANTIDADE
##      imprimir valor total da venda

## TOTAL DE VENDAS
##      imprimir o total de vendas

## VER ESTOQUE
##      imprimir estoque

## SAIR
##      encerra o sistema

lista_de_produtos = []

vendas = 0

opcao = '10'

while (opcao != '0'):
    
    opcao = input(' 1 - cadastrar produto \n 2 - venda de produto \n 3 - total de vendas \n 4 - ver estoque \n 0 - sair \n\n')
    
    if opcao == '1':
        nome = input('Digite o nome do item: ')
        valor = float(input('Digite o valor do item: '))
        quantidade = float(input('Digite a quantidade do item: '))
        
        novo_item = [nome, valor, quantidade]
        
        lista_de_produtos.append(novo_item)
        
        print(f'{nome} - {str(valor)} - {str(quantidade)}')
        
    elif opcao == '2':
        nome = input('Digite o nome do item: ')
        quantidade = float(input('Digite a quantidade do item: '))
        
        nao_tem = True
        
        for produto in lista_de_produtos:
            if produto[0] == nome:
                nao_tem = False
                if quantidade <= produto[2]:
                    total = quantidade * produto[1]
                    produto[2] -= quantidade
                    print(f'total: {total}')
                    vendas += total
                else:
                    print('Ter a gente tem, mas tá em falta')
        
        if nao_tem:
            print('Nunca nem vi')
        
    elif opcao == '3':
        
        print(f'TOTAL DE VENDAS: {vendas}')
        
    elif opcao == '4':
        
        for produto in lista_de_produtos:
            print(f'NOME: {produto[0]} - PREÇO {produto[1]} - QNT.: {produto[2]}')
    
    elif opcao != '0':
        
        print('Escolha uma opção válida')
        
    elif opcao == '0':
        
        print('Encerrando')
        print('Até a próxima')