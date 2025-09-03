
print('Olá! Eu sou Giovana Blank e desejo-lhes as Boas Vindas ao Marmitando!')
print('MENU: \n ' + 'BIFE ACEBOLADO (BA) \n P - R$ 16,00 \n M - R$ 18,00 \n G - R$ 22,00 \n FRANGO (FF) \n P - R$ 15,00 \n M - R$ 17,00 \n G - R$ 21,00') 

valorTotal = 0
while True: #loop para continuar pedindo até que o usuário não queira mais pedir nada
    sabor = input('Digite o sabor desejado: ').upper() #converte o input para maiúculo
    if sabor != 'BA' and sabor != 'FF':
        print('Sabor inválido. Tente novamente.')
        continue

    tamanho = input('Digite o tamanho desejado: ').upper()
    if tamanho not in ['P', 'M', 'G']: #se o input for diferente de P, M ou G, pede para tentar de novo
        tamanho = input('Tamanho inválido. Tente novamente (P, M ou G): ').upper()
        continue

    if sabor == 'BA':
        if tamanho == 'P':
            valor = 16.00
            print(f'Você pediu um bife acebolado no tamanho P: R$  {valor:.2f}')
        elif tamanho == 'M':
            valor = 18.00
            print(f'Você pediu um bife acebolado no tamanho M: R$ {valor:.2f}')
        elif tamanho == 'G':
            valor = 22.00
            print(f'Você pediu um bife acebolado no tamanho G: R$ {valor:.2f}')
    elif sabor == 'FF':
        if tamanho == 'P':
            valor = 15.00
            print(f'Você pediu um frango no tamanho P: R$ {valor:.2f}')
        elif tamanho == 'M':
            valor = 17.00
            print(f'Você pediu um frango no tamanho M: R$ {valor:.2f}')
        elif tamanho == 'G':
            valor = 21.00
            print(f'Você pediu um frango no tamanho G: R$ {valor:.2f}')

    valorTotal += valor #soma o valor ao total em caso de mais de um item no pedido

    resposta = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
    if resposta != 'S': #se a resposta for diferente de S, encerra o loop. Caso contrário, continua.
        print(f'Valor total a ser pago: R$ {valorTotal:.2f}') 
        break
