print('Olá, mundo! Eu sou Giovana Blank e desejo-lhes as boas vindas à Fábrica de Camisetas Python!')

def escolha_modelo():

    #definição dos modelos e preços
    modelos = {
        'MCS': 1.80, 
        'MLS': 2.10,  
        'MCE': 2.90, 
        'MLE': 3.20 
    }

    # escolha do modelo
    while True :
        print('Escolha o modelo de camiseta: \n MCS - Camiseta Manga Curta Simples \n MLS - Camiseta Manga Longa Simples \n MCE - Camiseta Manga Curta Estampada \n MLE - Camiseta Manga Longa Estampada')
        modelo = input('>> ').upper()
        if modelo in modelos:
            return modelos[modelo]
        else:
            print('Modelo inválido. Tente novamente.')

def numero_camisetas():
    while True:
        try:
            qtd = int(input('Quantas camisetas?'))
            if qtd > 2000:
                print('Não aceitamos tantas camisetas.')
                continue
            elif qtd <= 2000:
                desconto = 12/100
            elif qtd >= 200:
                desconto = 7/100
            elif qtd >= 20:
                desconto = 5/100
            else:
                desconto = 0.00
            return qtd, desconto
        except ValueError:
            print('Por favor, insira um número válido.')
       

def frete():
    while True:
        print('Escolha o frete: \n 1 - Transportadora (R$ 100.00) \n 2- Sedes (R$ 200.00) \n 0- Returada na fábrica (R$ 0.00)') 
        opcao = input('>> ')
        if opcao == '1':
            return 100.00
        elif opcao == '2':
            return 200.00
        elif opcao == '0':
            return 0.00
        else:
            print('Opção inválida. Tente novamente.')


#chamada das funções
try:
    valor_modelo = escolha_modelo() #define como variável o input da função
    quantidade, desconto = numero_camisetas()
    valor_frete = frete()

    valor_total = (valor_modelo * quantidade * (1 - desconto)) + valor_frete #define o valor da variáel a partir dos inputs das outras variáveis

    print(f"Valor total: R$ {valor_total:.2f}")
  
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")