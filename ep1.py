import json
from pprint import pprint

arquivo_in = open("ep1.json", "r")
json1 = arquivo_in.read()
estoque = json.loads(json1)

#estoque = {}      

arquivo_out = open("ep1.json", "w")

while True:
    print('Controle de estoque\n\n0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - imprimir estoque')
    while True:
        escolha = int(input("Faça sua escolha:"))
        if escolha not in range(5):
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
        print(json.dumps(estoque, sort_keys=True, indent=4))
  

arquivo_in.close()
arquivo_out.close()