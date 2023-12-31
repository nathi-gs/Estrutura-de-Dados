# -*- coding: utf-8 -*-
"""Cópia_de_Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/nathi-gs/AULA/blob/main/C%C3%B3pia_de_Untitled0.ipynb

#                        Exercicio 1

> **LIST**



 * Usada para armazenar vários item em uma variável.
 * Um dos quatro tipos de dados intregados em Python.
 * São criadas usando colchetes "[ ]".
 * Os itens são ordenados, tem uma ordem definida e não mudará.  
 * Os item são mutáveis, podemos adicionar ou remover itens de uma lista após ter sido criada.
 * As listas são indexadas, o primeiro item possui index [0], o segundo item possui index [1].
 * Permitem valores duplicados.
 * Um item da lista pode ser de qualquer tipo de dado.
"""

list = ["Dipirona", "Buscopan", "Amato"]
print(list)

"""> **SET**



*   Conjuntos são usados para armazenar vários itens em uma única variável.
*   Um dos quatro tipos de dados integrados em Python.
*   Os itens não são indexados.
*   Não ordenado, ou seja, não possuem uma ordem definida.
*   O item é imutável, não podemos alterá-lo após a criação do conjunto.
*   O item apenas pode ser adicionado ou removido.
*   Não permite duplicatas.
*   O item da lista pode ser de qualquer tipo de dado.
"""

thisset = {"Dipirona", "Buscopan", "Amato"}
print(thisset)

"""> **MAP**

* Executa uma função especificada para cada item da lista.
"""

def myfunc(n):
  return len(n)

x = map(myfunc, ('Dipirona', 'Buscopan', 'Amato'))

"""# Exercicio 2"""

listPaises = []

while True:
    nomePaises = input("Digite o nome de um país:")
    listPaises.append(nomePaises)
    add = input("Adicionar outro País (1) ou ir para o Menu (2): ")
    if add == '2':
        print("*****************************")
        print("LISTAS DOS PAISES")
        break

for item in range(len(listPaises)):

   print(f"{item}",listPaises[item])

while True:
    print("\nMENU:")
    print("1 - Criar país")
    print("2 - Listar países")
    print("3 - Modificar país")
    print("4 - Deletar país")
    print("5 - Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "1":
        nomePaises = input("Digite o nome do país que deseja adicionar: ")
        listPaises.append(nomePaises)
    elif opcao == "2":
        print("Lista de países:")
        for indice, nome in enumerate(listPaises):
            print(f"{indice} - {nome}")
    elif opcao == "3":
        indice = int(input("Digite o índice do país que deseja modificar: "))
        if 0 <= indice < len(listPaises):
            novo_nome = input("Digite o novo nome para o país: ")
            listPaises[indice] = novo_nome
            print(f'O país na posição {indice} foi modificado para {novo_nome}')
        else:
            print('Índice inválido')
    elif opcao == "4":
        indice = int(input("Digite o índice do país que deseja deletar: "))
        if 0 <= indice < len(listPaises):
            pais_removido = listPaises.pop(indice)
            print(f'O país na posição {indice} ({pais_removido}) foi removido')
        else:
            print('Índice inválido')
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

"""# Exercicio 3

"""

jogadores = {}

while True:
    print("\nMENU:")
    print("1 - Adicionar jogador")
    print("2 - Listar jogadores (Máximo 20)")
    print("3 - Atualizar jogador")
    print("4 - Deletar jogador")
    print("5 - Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "1":
        if len(jogadores) < 20:
            camisa = input("Digite o número da camisa do jogador: ")
            nome = input("Digite o nome do jogador: ")
            jogadores[camisa] = nome
            print(f"Jogador {nome} adicionado com sucesso.")
        else:
            print("Limite de 20 jogadores atingido. Não é possível adicionar mais jogadores.")

    elif opcao == "2":
        if jogadores:
            print("Lista de jogadores:")
            for camisa, nome in jogadores.items():
                print(f"Número da camisa: {camisa}, Nome: {nome}")
        else:
            print("A lista de jogadores está vazia.")

    elif opcao == "3":
        camisa = input("Digite o número da camisa do jogador que deseja atualizar: ")
        if camisa in jogadores:
            nome = input("Digite o novo nome do jogador: ")
            jogadores[camisa] = nome
            print(f"O jogador com número da camisa {camisa} foi atualizado para {nome}.")
        else:
            print("Número da camisa não encontrado.")

    elif opcao == "4":
        camisa = input("Digite o número da camisa do jogador que deseja deletar: ")
        if camisa in jogadores:
            del jogadores[camisa]
            print(f"O jogador com número da camisa {camisa} foi removido.")
        else:
            print("Número da camisa não encontrado.")

    elif opcao == "5":
        print("Obrigado por usar o CRUD de jogadores. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

"""# Exercicio 4"""

def adicionar_item(arquivo, item):
    with open(arquivo, 'a') as file:
        file.write(item + '\n')

def listar_itens(arquivo):
    try:
        with open(arquivo, 'r') as file:
            itens = file.readlines()
            if itens:
                for i, item in enumerate(itens, start=1):
                    print(f"{i}. {item.strip()}")
            else:
                print("A lista está vazia.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def alterar_item(arquivo, numero_item, novo_valor):
    try:
        with open(arquivo, 'r') as file:
            itens = file.readlines()
            if 1 <= numero_item <= len(itens):
                itens[numero_item - 1] = novo_valor + '\n'
                with open(arquivo, 'w') as file:
                    file.writelines(itens)
                print(f"Item {numero_item} alterado para: {novo_valor}")
            else:
                print("Número de item inválido.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def excluir_item(arquivo, numero_item):
    try:
        with open(arquivo, 'r') as file:
            itens = file.readlines()
            if 1 <= numero_item <= len(itens):
                item_removido = itens.pop(numero_item - 1)
                with open(arquivo, 'w') as file:
                    file.writelines(itens)
                print(f"Item removido: {item_removido.strip()}")
            else:
                print("Número de item inválido.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

# Teste das funções
arquivo = "lista_itens.txt"

while True:
    print("\nOpções disponíveis:")
    print("1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Alterar item")
    print("4 - Excluir item")
    print("5 - Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "1":
        novo_item = input("Digite o novo item: ")
        adicionar_item(arquivo, novo_item)
    elif opcao == "2":
        listar_itens(arquivo)
    elif opcao == "3":
        listar_itens(arquivo)
        numero_item = int(input("Digite o número do item que deseja alterar: "))
        novo_valor = input("Digite o novo valor para o item: ")
        alterar_item(arquivo, numero_item, novo_valor)
    elif opcao == "4":
        listar_itens(arquivo)
        numero_item = int(input("Digite o número do item que deseja excluir: "))
        excluir_item(arquivo, numero_item)
    elif opcao == "5":
        print("Obrigado por usar o programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

"""# Exercicio 5

> Bubble Sort

* Classificação por bolha.
* Algortimo básico, para organizar uma sequência de números ou outros elementos na ordem correta.
* Compara repetidamente pares de elementos adjacentes e, em seguida, troca as suas posições se existirem na ordem errada.
"""

def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

list1 = [5, 3, 8, 6, 7, 2]
print("A lista não é ordenada: ", list1)
# Calling the bubble sort function
print("A lista é ordenada: ", bubble_sort(list1))

"""# Exercicio 6"""

import os

# Função para autenticar o usuário
def autenticar_usuario(nome,senha):
        with open('usuario.txt', 'a') as file:
            file.write(f"Nome: {nome}, Senha: {senha}\n")


# Função para listar todos os produtos
def listar_produtos(produtos):
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print("Nenhum produto cadastrado.")

# Função para listar um produto pelo ID
def listar_produto_por_id(produtos, id_produto):
    for produto in produtos:
        if produto['id'] == id_produto:
            print(produto)
            return
    print(f"Produto com ID {id_produto} não encontrado.")

# Função para ordenar a lista de produtos por descrição (A/Z)
def ordenar_produtos(produtos, ordem_crescente=True):
    return sorted(produtos, key=lambda x: x['descricao'], reverse=not ordem_crescente)

# Função para cadastrar um novo produto
def cadastrar_produto(produtos):
    id_produto = len(produtos) + 1
    descricao = input("Digite a descrição do produto: ")
    peso = input("Digite o peso do produto: ")
    valor = input("Digite o valor do produto: ")
    fornecedor = input("Digite o fornecedor do produto: ")

    novo_produto = {
        'id': id_produto,
        'descricao': descricao,
        'peso': peso,
        'valor': valor,
        'fornecedor': fornecedor
    }

    produtos.append(novo_produto)
    print("Produto cadastrado com sucesso!")

# Função para editar um produto pelo ID
def editar_produto(produtos, id_produto):
    for produto in produtos:
        if produto['id'] == id_produto:
            print(f"Produto atual: {produto}")
            descricao = input("Digite a nova descrição do produto: ")
            peso = input("Digite o novo peso do produto: ")
            valor = input("Digite o novo valor do produto: ")
            fornecedor = input("Digite o novo fornecedor do produto: ")

            produto['descricao'] = descricao
            produto['peso'] = peso
            produto['valor'] = valor
            produto['fornecedor'] = fornecedor

            print(f"Produto com ID {id_produto} foi atualizado.")
            return

    print(f"Produto com ID {id_produto} não encontrado.")

# Função para excluir um produto pelo ID
def excluir_produto(produtos, id_produto):
    for produto in produtos:
        if produto['id'] == id_produto:
            produtos.remove(produto)
            print(f"Produto com ID {id_produto} foi removido.")
            return

    print(f"Produto com ID {id_produto} não encontrado.")

# Função para salvar os produtos em um arquivo
def salvar_produtos_em_arquivo(produtos):
    with open("produtos.txt", "w") as arquivo_produtos:
        for produto in produtos:
            arquivo_produtos.write(f"ID: {produto['id']},DescriCao: {produto['descricao']},Peso: {produto['peso']},Valor: {produto['valor']},Fornecedor: {produto['fornecedor']}\n")

# Função principal
def main():
    # Autenticar o usuário
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    autenticar_usuario(nome, senha)

    # Carregar os produtos do arquivo
    produtos = []
    if os.path.isfile("produtos.txt"):
        with open("produtos.txt", "r") as arquivo_produtos:
            for linha in arquivo_produtos:
                id_produto, descricao, peso, valor, fornecedor = linha.strip().split(",")
                produtos.append({
                    'id': int(id_produto),
                    'descricao': descricao,
                    'peso': peso,
                    'valor': valor,
                    'fornecedor': fornecedor
                })

    while True:
        print("\n=== MENU ===")
        print("(1) Listar todos os produtos")
        print("(2) Listar produto pelo ID")
        print("(3) Listar todos os produtos ordenados (A/Z)")
        print("(4) Cadastrar novo produto")
        print("(5) Editar produto")
        print("(6) Excluir produto")
        print("(7) Sair do programa")
        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            listar_produtos(produtos)
        elif opcao == "2":
            id_produto = int(input("Digite o ID do produto: "))
            listar_produto_por_id(produtos, id_produto)
        elif opcao == "3":
            ordem = input("Listar em ordem crescente (A) ou decrescente (Z): ").upper()
            if ordem == "A":
                produtos_ordenados = ordenar_produtos(produtos, ordem_crescente=True)
            elif ordem == "Z":
                produtos_ordenados = ordenar_produtos(produtos, ordem_crescente=False)
            else:
                print("Opção inválida.")
                continue
            listar_produtos(produtos_ordenados)
        elif opcao == "4":
            cadastrar_produto(produtos)
        elif opcao == "5":
            id_produto = int(input("Digite o ID do produto que deseja editar: "))
            editar_produto(produtos, id_produto)
        elif opcao == "6":
            id_produto = int(input("Digite o ID do produto que deseja excluir: "))
            excluir_produto(produtos, id_produto)
        elif opcao == "7":
            salvar_produtos_em_arquivo(produtos)
            print("Obrigado por usar o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()