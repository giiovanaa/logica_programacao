print ('Hello, World! Eu sou Giovana Blank e este é meu primeiro programa em Python.')

valorDoPedido = float(input('Digite o valor do pedido: '))
quantidadeDeParcelas = float(input('Digite a quantidade de parcelas: '))

if quantidadeDeParcelas <= 4:
    juros = 0/100
elif quantidadeDeParcelas <= 6:
    juros = 4/100
elif quantidadeDeParcelas <= 9:
    juros = 8/100
elif quantidadeDeParcelas <= 13:
    juros = 16/100
else:
    juros = 32/100

print(f'O valor das parcelas é de: {(valorDoPedido + (valorDoPedido * juros)) / quantidadeDeParcelas:.2f}')
print(f'O valor total parcelado é: {valorDoPedido + (valorDoPedido * juros):.2f}')

