def calcular_preco(fileira):
    if fileira == 1:
        return "Executiva", 850.00
    elif fileira in [2, 3]:
        return "Espaço extra", 600.00
    else:
        return "Econômica", 400.00


def validar_assento(fileira, coluna):
    if fileira < 1 or fileira > 5:
        return False
    if coluna not in "ABCDEF":
        return False
    return True


def validar_documento(documentos, doc):
    if doc in documentos:
        print("Este documento já possui passagem neste voo!")
        return False
    return True


def verificar_assento(assentos, fileira, coluna_idx):
    return assentos[fileira-1][coluna_idx] == "L"


def comprar_passagem(assentos, nomes, documentos, assentos_pass, categorias, valores):
    doc = input("Documento do passageiro: ")
    if not validar_documento(documentos, doc):
        return

    nome = input("Nome do passageiro: ")
    idade = int(input("Idade: "))

    entrada = input("Assento desejado (ex: 2C): ").upper()
    fileira = int(entrada[0])
    coluna = entrada[1]

    if not validar_assento(fileira, coluna):
        print("Assento inválido!")
        return

    coluna_idx = "ABCDEF".index(coluna)

    if not verificar_assento(assentos, fileira, coluna_idx):
        print(f"O assento {entrada} já está ocupado.")
        return

    if idade < 16 and fileira in [2, 3]:
        print("Menores de 16 anos não podem ocupar assentos de saída de emergência!")
        return

    categoria, preco = calcular_preco(fileira)
    print("Assento:", entrada)
    print("Categoria:", categoria)
    print("Valor: R$", preco)

    confirmar = input("Confirmar compra? S/N: ").upper()
    if confirmar == "S":
        assentos[fileira-1][coluna_idx] = "O"
        nomes.append(nome)
        documentos.append(doc)
        assentos_pass.append(entrada)
        categorias.append(categoria)
        valores.append(preco)
        print("Passagem comprada com sucesso!")
    else:
        print("Compra cancelada.")


def consultar_passageiro(nomes, documentos, assentos_pass, categorias, valores):
    doc = input("Documento do passageiro: ")
    if doc in documentos:
        i = documentos.index(doc)
        print("Nome:", nomes[i])
        print("Documento:", documentos[i])
        print("Assento:", assentos_pass[i])
        print("Categoria:", categorias[i])
        print("Valor pago: R$", valores[i])
    else:
        print("Passageiro não encontrado!")


def calcular_diferenca(preco_antigo, preco_novo):
    if preco_novo > preco_antigo:
        return preco_novo - preco_antigo
    return 0


def alterar_assento(assentos, documentos, assentos_pass, categorias, valores):
    doc = input("Documento do passageiro: ")
    if doc not in documentos:
        print("Passageiro não encontrado!")
        return

    i = documentos.index(doc)
    assento_antigo = assentos_pass[i]
    fileira_antiga = int(assento_antigo[0])
    coluna_antiga = assento_antigo[1]
    coluna_antiga_idx = "ABCDEF".index(coluna_antiga)

    entrada = input("Novo assento (ex: 3D): ").upper()
    fileira = int(entrada[0])
    coluna = entrada[1]

    if not validar_assento(fileira, coluna):
        print("Assento inválido!")
        return

    coluna_idx = "ABCDEF".index(coluna)

    if not verificar_assento(assentos, fileira, coluna_idx):
        print(f"O assento {entrada} já está ocupado.")
        return

    categoria_nova, preco_novo = calcular_preco(fileira)
    diferenca = calcular_diferenca(valores[i], preco_novo)

    if diferenca > 0:
        print("Diferença a pagar: R$", diferenca)

    # Libera assento antigo e ocupa o novo
    assentos[fileira_antiga-1][coluna_antiga_idx] = "L"
    assentos[fileira-1][coluna_idx] = "O"

    assentos_pass[i] = entrada
    categorias[i] = categoria_nova
    valores[i] = preco_novo

    print("Assento alterado com sucesso!")


def cancelar_passagem(assentos, nomes, documentos, assentos_pass, categorias, valores):
    doc = input("Documento do passageiro: ")
    if doc not in documentos:
        print("Passageiro não encontrado!")
        return

    i = documentos.index(doc)
    assento = assentos_pass[i]
    fileira = int(assento[0])
    coluna_idx = "ABCDEF".index(assento[1])

    assentos[fileira-1][coluna_idx] = "L"

    nomes.pop(i)
    documentos.pop(i)
    assentos_pass.pop(i)
    categorias.pop(i)
    valores.pop(i)

    print("Passagem cancelada com sucesso!")


def ordenar_passageiros(nomes, documentos, assentos_pass, categorias, valores):
    n = len(assentos_pass)
    indices = list(range(n))

    for i in range(n):
        for j in range(n - 1 - i):
            if assentos_pass[indices[j]] > assentos_pass[indices[j+1]]:
                indices[j], indices[j+1] = indices[j+1], indices[j]

    return indices


def mostrar_lista_passageiros(nomes, documentos, assentos_pass, categorias, valores):
    indices = ordenar_passageiros(nomes, documentos, assentos_pass, categorias, valores)
    print("\n=== Lista de Passageiros ===")
    for i in indices:
        print(assentos_pass[i], "-", nomes[i], "-", documentos[i], "-", categorias[i], "- R$", valores[i])


def gerar_relatorio_voo(assentos, nomes, documentos, assentos_pass, categorias, valores):
    livres = 0
    ocupados = 0
    for fileira in assentos:
        for a in fileira:
            if a == "L":
                livres += 1
            else:
                ocupados += 1

    total = livres + ocupados
    ocupacao = (ocupados / total) * 100

    faturamento = sum(valores)
    executiva = categorias.count("Executiva")
    espaco_extra = categorias.count("Espaço extra")
    economica = categorias.count("Econômica")

    print("\n=== Relatório do Voo ===")
    print("Assentos livres:", livres)
    print("Assentos ocupados:", ocupados)
    print("Percentual de ocupação:", ocupacao, "%")
    print("Faturamento total: R$", faturamento)
    print("Vendas Executiva:", executiva)
    print("Vendas Espaço extra:", espaco_extra)
    print("Vendas Econômica:", economica)

    print("\nPassageiros por assento:")
    mostrar_lista_passageiros(nomes, documentos, assentos_pass, categorias, valores)


def mostrar_assentos(assentos):
    colunas = "ABCDEF"
    print("   ", "  ".join(colunas))
    for i in range(5):
        print(i+1, " ", "   ".join(assentos[i]))


# Dados
assentos = [
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"]
]

nomes = []
documentos = []
assentos_pass = []
categorias = []
valores = []

# Menu
while True:
    print("\n1 - Mostrar mapa de assentos")
    print("2 - Comprar passagem")
    print("3 - Consultar passageiro")
    print("4 - Alterar assento")
    print("5 - Cancelar passagem")
    print("6 - Mostrar lista de passageiros")
    print("7 - Mostrar relatório do voo")
    print("8 - Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        mostrar_assentos(assentos)
    elif opcao == 2:
        comprar_passagem(assentos, nomes, documentos, assentos_pass, categorias, valores)
    elif opcao == 3:
        consultar_passageiro(nomes, documentos, assentos_pass, categorias, valores)
    elif opcao == 4:
        alterar_assento(assentos, documentos, assentos_pass, categorias, valores)
    elif opcao == 5:
        cancelar_passagem(assentos, nomes, documentos, assentos_pass, categorias, valores)
    elif opcao == 6:
        mostrar_lista_passageiros(nomes, documentos, assentos_pass, categorias, valores)
    elif opcao == 7:
        gerar_relatorio_voo(assentos, nomes, documentos, assentos_pass, categorias, valores)
    elif opcao == 8:
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")