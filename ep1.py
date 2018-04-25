from firebase import firebase       #importa o firebase
firebase = firebase.FirebaseApplication('https://ep1-design-de-software.firebaseio.com/', None) #puxa o URL da nuvem do firebase para lançar o código
estoques = firebase.get('', None) #lê o json do firebase e transforma num dicionario atribuindo a variavel estoques

lista_del_itens = [] #criação da lista que deleta os itens das lojas

print("Lojas disponíveis:\n")   
for e in estoques.keys():
    print(e)
    
while True:
    print("\n1 - Escolher uma loja\n2 - Criar nova loja\n")#mostrar menu para adicionar e alterar loja
    escolha_1 = int(input("Digite a sua escolha:"))
    if escolha_1 == 1:
        loja = str(input("Digite o nome da loja:"))
        if loja in estoques.keys():       #se a loja esta no dicionario
            estoque = estoques[loja]     # estoque recebe a loja
            break
        else:
            print("Loja nao encontrada\n")
            
    if escolha_1 == 2:
        nova_loja = str(input("Digite o nome da nova loja:\n"))
        if nova_loja not in estoques.keys():#se a loja nao existe no dicionario
            estoques[nova_loja] = {} #cria um nova loja
            estoque = estoques[nova_loja]#estoque recebe nova loja
            break
        else:
            print("Loja já existente\n")
            
    if escolha_1 not in range(4):
        print("Escolha inválida")
            
    if len(estoques) == 0:    #se o estoque esta vazio 
            estoques = {}#adiciona dicionario vazio ao estoque
            print("Sem lojas disponíveis\n")
    else:
        print("Lojas disponíveis:\n")   
        for e in estoques.keys():
            print(e)
        
for k, v in estoque.items():
     if 'preco' not in v.keys():# verifica se o produto no estoque tem um preço
         estoque[k]['preco'] = int(input("Valor do produto {0} nao definido, digite o preço:".format(k)))

if escolha_1 == 1:
    print("\nBem vindo à loja {}\n".format(loja))
if escolha_1 == 2:
    print("\nBem vindo à loja {}\n".format(nova_loja))

while True:
    print('Controle de estoque\n\n0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - alterar preço\n5 - informações sobre estoque\n')#mostra o menu para altera estoque
    while True:
        escolha = int(input("Faça sua escolha:"))
        if escolha not in range(6):
            print("Escolha nao definida")
        else:
            break
    if escolha == 0:
        print("Até mais")
        break
    
    elif escolha == 1:  
        try:    
            produto = str(input("Nome do produto:"))
            qnt = int(input("Digite a quantidade inicial:"))
            preco = float(input('Digite o valor unitário do produto:'))
            if produto not in estoque.keys() and qnt >= 0 and preco > 0:
                estoque[produto]= {'quantidade':qnt, 'preco': preco} #adiciona o produto, quantidade e preço no estoque
                print('\n{} unidades de {} foram adicionadas ao estoque com preço unitario de R${}\n'.format(qnt,produto,preco))
            else:
                if produto in estoque.keys():
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
            if remover in estoque.keys():
                lista_del_itens.append(remover)
                del(estoque[remover])    #deleta um produto da loja
                print('\n{} foi removido do estoque\n'.format(remover))
            else: 
                print("Produto nao encontrado\n")
        except:
            print("\nEscolha invalida\n")
    elif escolha == 3:
        try:
            alterar = str(input("Digite o produto:"))
            alteracao = int(input("Quantidade:"))
            if alterar in estoque.keys():
                estoque[alterar]['quantidade'] += alteracao #altera quantidade de um produto
                print('\nA nova quantidade de {} é {} unidades\n'.format(alterar,(alteracao+estoque[alterar]['quantidade'])))
            else:
                print("\nProduto nao encontrado\n")
        except:
            print("\nEscolha invalida\n")
    elif escolha == 5:
        try:
            print('Informações do estoque \n\n0 - sair\n1 - imprimir estoque\n2 - imprimir estoque negativo\n3 - imprimir valor monetario no estoque')#mostra menu de informaçoes do estoque
            sub_escolha = int(input("Digite um numero:"))
            if sub_escolha == 1:
                for x in estoque:
                    print("\n")
                    print (x)
                    for y in estoque[x]:
                        print ('\t{} : {}'.format(y,estoque[x][y]))#imprime o estoque
                print("\n")
            elif sub_escolha == 2:
                for k,v in estoque.items():
                    for c in v.values():
                        if c < 0:
                            print("\nO produto {} esta com etoque negativo de {} unidades\n".format(k,c))#imprime os valores negativos

            elif sub_escolha == 3:
                total = 0
                for k in estoque.keys():
                    total += estoque[k]['preco']*estoque[k]['quantidade'] #calcula o valor monetario total
                print("\nValor monetario total é de R${}\n".format(total))#imprime o valro monetario total
        except:
            print("\nEscolha invalida\n")
    elif escolha == 4:
        try:
            alterar = str(input("Digite o produto:"))
            novo_preco = float(input("Novo preco:"))
            if alterar in estoque.keys() and novo_preco > 0:
                
                
                estoque[alterar]['preco'] = novo_preco #altera o preço do produto
                print('\nO novo preço de {} é R${}\n'.format(alterar,novo_preco))
            else:
                if alterar not in estoque.keys():
                    print('Produto não encontrado\n')
                if novo_preco <= 0:
                    print('O valor deve ser positivo\n')
        except:        
            print("\nEscolha invalida\n")
            
if len(lista_del_itens) > 0: #se o tamanho da lista de deletar os itens for maior que 0 o programa realiza o que está digitado abaixo
    for i in lista_del_itens:
        firebase.delete(nova_loja, i) #deletar os itens da nova loja no firebase

if escolha_1 == 1:        
    firebase.patch(loja, estoques[loja]) #aqui as informações são atializadas no firebase
       
if escolha_1 == 2:
    firebase.patch(nova_loja, estoques[nova_loja])  #aqui também as informações são atribuidas na nuvem do firebase