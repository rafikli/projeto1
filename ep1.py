import json

arquivo_in = open("ep1.json", "r")
json1 = arquivo_in.read()

if len(json1) == 0:
    estoques = {}#add sub estrutura
    print("Sem lojas disponíveis\n")
else:
    estoques = json.loads(json1)#add sub estrutura
    print("Lojas disponíveis:\n")   
    for e in estoques.keys():
        print(e)
    
while True:
    print("\n1 - Escolher uma loja\n2 - Criar nova loja\n3 - Deletar loja")
    escolha_1 = int(input("Digite a sua escolha:"))
    if escolha_1 == 1:
        loja = str(input("Digite o nome da loja:"))
        if loja in estoques.keys():
            estoque = estoques[loja]
            break
        else:
            print("Loja nao encontrada\n")
            
    if escolha_1 == 2:
        nova_loja = str(input("Digite o nome da nova loja:\n"))
        if nova_loja not in estoques.keys():
            estoques[nova_loja] = {}
            estoque = estoques[nova_loja]
            break
        else:
            print("Loja já existente\n")
    
    if escolha_1 == 3:
        deletar_loja = str(input("Digite a loja que deseja deletar:"))
        if deletar_loja in estoques.keys():
            del(estoques[deletar_loja])#add sub estrutura
            print('\nA loja {} foi removida\n'.format(deletar_loja))
        else:
            print("\nLoja nao encontrada")
            
    if escolha_1 not in range(4):
        print("Escolha inválida")
            
    if len(estoques) == 0:
            estoques = {}#add sub estrutura
            print("Sem lojas disponíveis\n")
    else:
        print("Lojas disponíveis:\n")   
        for e in estoques.keys():
            print(e)
        
for k, v in estoque.items():#add sub estrutura
     if 'preco' not in v.keys():#add sub estrutura
         estoque[k]['preco'] = int(input("Valor do produto {0} nao definido, digite o preço:".format(k)))#add sub estrutura


arquivo_out = open("ep1.json", "w")

if escolha_1 == 1:
    print("\nBem vindo à loja {}\n".format(loja))
if escolha_1 == 2:
    print("\nBem vindo à loja {}\n".format(nova_loja))

while True:
    print('Controle de estoque\n\n0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - alterar preço\n5 - informações sobre estoque\n')
    while True:
        escolha = int(input("Faça sua escolha:"))
        if escolha not in range(6):
            print("Escolha nao definida")
        else:
            break
    if escolha == 0:
        print("Até mais")
        arquivo_out.write(json.dumps(estoques))#add sub estrutura
        break
    
    elif escolha == 1:  
        try:    
            produto = str(input("Nome do produto:"))
            qnt = int(input("Digite a quantidade inicial:"))
            preco = float(input('Digite o valor unitário do produto:'))
            if produto not in estoque.keys() and qnt >= 0 and preco > 0:#add sub estrutura
                estoque[produto]= {'quantidade':qnt, 'preco': preco} #add sub estrutura
                print('\n{} unidades de {} foram adicionadas ao estoque com preço unitario de R${}\n'.format(qnt,produto,preco))
            else:
                if produto in estoque.keys():#add sub estrutura
                    print("\nProduto já cadastrado\n")
                if preco <= 0:
                    print('o valor do produto deve ser positivo\n')

                if qnt < 0:
                    print("A quantidade inicial deve ser positiva\n")
        except:
            print("\nEscolha invalida\n") 

    elif escolha == 2:
        try:
            remover = str(input("Nome do produto:"))
            if remover in estoque.keys():#add sub estrutura
                del(estoque[remover])#add sub estrutura
                print('\n{} foi removido do estoque\n'.format(remover))
            else: 
                print("Produto nao encontrado\n")
        except:
            print("\nEscolha invalida\n")
    elif escolha == 3:
        try:
            alterar = str(input("Digite o produto:"))
            alteracao = int(input("Quantidade:"))
            if alterar in estoque.keys():#add sub estrutura
                estoque[alterar]['quantidade'] += alteracao#add sub estrutura
                print('\nA nova quantidade de {} é {} unidades\n'.format(alterar,(alteracao+estoque[alterar]['quantidade'])))
            else:
                print("\nProduto nao encontrado\n")
        except:
            print("\nEscolha invalida\n")
    elif escolha == 5:
        try:
            print('Informações do estoque \n\n0 - sair\n1 - imprimir estoque\n2 - imprimir estoque negativo\n3 - imprimir valor monetario no estoque')
            sub_escolha = int(input("Digite um numero:"))
            if sub_escolha == 1:
                print(json.dumps(estoque, sort_keys=True, indent=4))#add sub estrutura
            
            elif sub_escolha == 2:
                for k,v in estoque.items():#add sub estrutura
                    for c in v.values():#add sub estrutura
                        if c < 0:#add sub estrutura
                            print("\nO produto {} esta com etoque negativo de {} unidades\n".format(k,c))

            elif sub_escolha == 3:
                total = 0
                for k in estoque.keys():#add sub estrutura
                    total += estoque[k]['preco']*estoque[k]['quantidade']#add sub estrutura
                print("\nValor monetario total é de R${}\n".format(total))
        except:
            print("\nEscolha invalida\n")
    elif escolha == 4:
        try:
            alterar = str(input("Digite o produto:"))
            novo_preco = float(input("Novo preco:"))
            if alterar in estoque.keys() and novo_preco > 0:#add sub estrutura
                
                
                estoque[alterar]['preco'] = novo_preco#add sub estrutura
                print('\nO novo preço de {} é R${}\n'.format(alterar,novo_preco))
            else:
                if alterar not in estoque.keys():#add sub estrutura
                    print('Produto não encontrado\n')
                if novo_preco <= 0:
                    print('O valor deve ser positivo\n')
        except:        
            print("\nEscolha invalida\n")
  

arquivo_in.close()
arquivo_out.close()