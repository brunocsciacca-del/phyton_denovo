NUM_FILEIRAS = 5
NUM_COLUNAS = 6
COLUNAS = ["A", "B", "C", "D", "E", "F"]

assentos = [["L" for _ in range(NUM_COLUNAS)] for _ in range(NUM_FILEIRAS)]
passageiros = []  # cada item: {"nome", "documento", "assento", "categoria", "valor"}


def mostrarAssentos():
    print("\n     " + "   ".join(COLUNAS))
    for i in range(NUM_FILEIRAS):
        linha = f"{i + 1}   "
        for j in range(NUM_COLUNAS):
            linha += f" {assentos[i][j]}  "
        print(linha)
    print()


def validarAssento(assento):
    assento = assento.strip().upper()
    if len(assento) < 2:
        return None

    letra = assento[-1]
    numero = assento[:-1]

    if not numero.isdigit() or letra not in COLUNAS:
        return None

    fileira = int(numero)
    if fileira < 1 or fileira > NUM_FILEIRAS:
        return None

    linha = fileira - 1
    coluna = COLUNAS.index(letra)
    return linha, coluna


def verificarDisponibilidade(linha, coluna):
    return assentos[linha][coluna] == "L"


def calcularPreco(linha):
    fileira = linha + 1
    if fileira == 1:
        return "Executiva", 850.00
    elif fileira in (2, 3):
        return "Espaco extra", 600.00
    else:
        return "Economica", 400.00


def buscarPassageiroPorDocumento(documento):
    for p in passageiros:
        if p["documento"] == documento:
            return p
    return None


def buscarPassageiroPorAssento(assento):
    for p in passageiros:
        if p["assento"] == assento:
            return p
    return None


def comprarAssento():
    entrada = input("Assento desejado (ex: 2C): ")
    resultado = validarAssento(entrada)

    if resultado is None:
        print("Assento invalido! Verifique a fileira e a coluna.")
        return

    linha, coluna = resultado
    codigo = f"{linha + 1}{COLUNAS[coluna]}"

    if not verificarDisponibilidade(linha, coluna):
        print(f"O assento {codigo} ja esta ocupado.")
        print("Escolha outro assento.")
        return

    categoria, preco = calcularPreco(linha)
    print(f"\nAssento: {codigo}")
    print(f"Categoria: {categoria}")
    print(f"Valor: R$ {preco:.2f}")

    confirmacao = input("Confirmar compra? S/N: ").strip().upper()
    if confirmacao != "S":
        print("Compra cancelada.")
        return

    nome = input("Nome do passageiro: ")
    documento = input("Documento: ")

    assentos[linha][coluna] = "O"
    passageiros.append({
        "nome": nome,
        "documento": documento,
        "assento": codigo,
        "categoria": categoria,
        "valor": preco
    })

    print("\nCompra realizada com sucesso.")
    print(f"O assento {codigo} agora esta indisponivel.")


def consultarPassageiro():
    documento = input("Digite o documento do passageiro: ")
    passageiro = buscarPassageiroPorDocumento(documento)

    if passageiro is None:
        print("Passageiro nao encontrado.")
        return

    print(f"\nNome: {passageiro['nome']}")
    print(f"Documento: {passageiro['documento']}")
    print(f"Assento: {passageiro['assento']}")
    print(f"Categoria: {passageiro['categoria']}")
    print(f"Valor pago: R$ {passageiro['valor']:.2f}")


def alterarAssento():
    documento = input("Digite o documento do passageiro: ")
    passageiro = buscarPassageiroPorDocumento(documento)

    if passageiro is None:
        print("Passageiro nao encontrado.")
        return

    novo = input("Novo assento desejado (ex: 3D): ")
    resultado = validarAssento(novo)

    if resultado is None:
        print("Assento invalido!")
        return

    linha, coluna = resultado
    novoCodigo = f"{linha + 1}{COLUNAS[coluna]}"

    if not verificarDisponibilidade(linha, coluna):
        print(f"O assento {novoCodigo} ja esta ocupado.")
        return

    # libera o assento antigo
    antigo = passageiro["assento"]
    linhaAntiga = int(antigo[:-1]) - 1
    colunaAntiga = COLUNAS.index(antigo[-1])
    assentos[linhaAntiga][colunaAntiga] = "L"

    # ocupa o novo assento
    assentos[linha][coluna] = "O"
    categoria, preco = calcularPreco(linha)

    passageiro["assento"] = novoCodigo
    passageiro["categoria"] = categoria
    passageiro["valor"] = preco

    print(f"Assento alterado com sucesso para {novoCodigo}.")
    print(f"Nova categoria: {categoria} - R$ {preco:.2f}")


def cancelarPassagem():
    documento = input("Digite o documento do passageiro: ")
    passageiro = buscarPassageiroPorDocumento(documento)

    if passageiro is None:
        print("Passageiro nao encontrado.")
        return

    confirmacao = input(f"Confirma cancelamento da passagem de {passageiro['nome']}? S/N: ").strip().upper()
    if confirmacao != "S":
        print("Operacao cancelada.")
        return

    codigo = passageiro["assento"]
    linha = int(codigo[:-1]) - 1
    coluna = COLUNAS.index(codigo[-1])
    assentos[linha][coluna] = "L"

    passageiros.remove(passageiro)
    print(f"Passagem de {passageiro['nome']} cancelada. Assento {codigo} liberado.")


def mostrarListaPassageiros():
    if not passageiros:
        print("\nNenhum passageiro registrado.")
        return

    print("\n===== LISTA DE PASSAGEIROS =====")
    for p in passageiros:
        print(f"{p['nome']:<20} | Doc: {p['documento']:<12} | Assento: {p['assento']:<4} | "
              f"{p['categoria']:<14} | R$ {p['valor']:.2f}")


def mostrarResumo():
    livres = sum(linha.count("L") for linha in assentos)
    ocupados = sum(linha.count("O") for linha in assentos)
    total = livres + ocupados
    percentualOcupacao = (ocupados / total) * 100

    faturamento = sum(p["valor"] for p in passageiros)

    vendasPorCategoria = {"Executiva": 0, "Espaco extra": 0, "Economica": 0}
    for p in passageiros:
        vendasPorCategoria[p["categoria"]] += 1

    print("\n===== RESUMO DO VOO =====")
    print(f"Assentos livres: {livres}")
    print(f"Assentos ocupados: {ocupados}")
    print(f"Percentual de ocupacao: {percentualOcupacao:.1f}%")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print("Vendas por categoria:")
    for categoria, quantidade in vendasPorCategoria.items():
        print(f"  {categoria}: {quantidade}")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Mostrar mapa de assentos")
        print("2 - Comprar passagem")
        print("3 - Consultar passageiro")
        print("4 - Alterar assento")
        print("5 - Cancelar passagem")
        print("6 - Mostrar lista de passageiros")
        print("7 - Mostrar relatorio do voo")
        print("8 - Encerrar")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            mostrarAssentos()
        elif opcao == "2":
            comprarAssento()
        elif opcao == "3":
            consultarPassageiro()
        elif opcao == "4":
            alterarAssento()
        elif opcao == "5":
            cancelarPassagem()
        elif opcao == "6":
            mostrarListaPassageiros()
        elif opcao == "7":
            mostrarResumo()
        elif opcao == "8":
            print("Encerrando o sistema. Ate mais!")
            break
        else:
            print("Opcao invalida! Tente novamente.")


if __name__ == "__main__":
    menu()