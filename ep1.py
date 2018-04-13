
estoque = {}

while True:
    print('Controle de estoque\n0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - imprimir estoque')
    while True:
        escolha = int(input("Faça sua escolha:"))
        if escolha not in range(5):
            print("Escolha nao definida")
        else:
            break
    if escolha == 0:
        print("Até mais")
        break
    elif escolha == 1:      
        produto = str(input("Nome do produto:"))
        qnt = int(input("Digite a quantidade inicial:"))
        if produto not in estoque.keys() and qnt >= 0:
            estoque[produto]= {'quantidade':qnt}
        else:
            print("Produto já cadastrado\n")
        if qnt < 0:
            print("A quantidade inicial deve ser positiva\n")
    elif escolha == 2:
        remover = str(input("Nome do produto:"))
        if remover in estoque.keys():
            del(estoque[remover])
        else: 
            print("Produto nao encontrado\n")
    elif escolha == 3:
        alterar = str(input("Digite o produto:"))
        alteracao = int(input("Quantidade:"))
        if alterar in estoque.keys():
            estoque[alterar]['quantidade']+=alteracao
    elif escolha == 4:
        print('{0}\n'.format(estoque))
    