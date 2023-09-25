import os
import getpass

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