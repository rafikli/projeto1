import json

arquivo_in = open("ep1.json", "r")
json1 = arquivo_in.read()

if len(json1)==0:
    estoque = {}
else:
    estoque = json.loads(json1)
    
for k, v in estoque.items():
     if 'preco' not in v.keys():
         estoque[k]['preco'] = int(input("Valor do produto {0} nao definido, digite o preço:".format(k)))


arquivo_out = open("ep1.json", "w")

while True:
    print('Controle de estoque\n\n0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - alterar preço\n5 - imprimir estoque\n')
    while True:
        escolha = int(input("Faça sua escolha:"))
        if escolha not in range(6):
            print("Escolha nao definida")
        else:
            break
    if escolha == 0:
        print("Até mais")
        arquivo_out.write(json.dumps(estoque))
        break
    
    elif escolha == 1:      
        produto = str(input("Nome do produto:"))
        qnt = int(input("Digite a quantidade inicial:"))
        preco = float(input('Digite o valor unitário do produto:'))
        if produto not in estoque.keys() and qnt >= 0 and preco > 0:
            estoque[produto]= {'quantidade':qnt, 'preco': preco} 
        if preco <= 0:
            print('o valor do produto deve ser positivo\n')

        if produto in estoque.keys():
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
    elif escolha == 5:
        print(json.dumps(estoque, sort_keys=True, indent=4))
    elif escolha == 4:
        alterar = str(input("Digite o produto:"))
        novo_preco = float(input("Novo preco:"))
        if alterar in estoque.keys() and novo_preco > 0:
            
            estoque[alterar]['preco'] = novo_preco
        else:
            if alterar not in estoque.keys():
                print('Produto não encontrado\n')
            if novo_preco <= 0:
                print('O valor deve ser positivo\n')
                
        
  

arquivo_in.close()
arquivo_out.close()