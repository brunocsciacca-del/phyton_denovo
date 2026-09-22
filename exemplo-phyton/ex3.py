def listar_medicamentos(nomes, precos, estoques):
    for i in range(len(nomes)):
        print(i+1, "-", nomes[i], "- R$", precos[i], "- Estoque:", estoques[i])


def pesquisar_medicamento(nomes, precos, estoques):
    nome = input("Nome do medicamento: ")
    if nome in nomes:
        i = nomes.index(nome)
        print(nomes[i], "- R$", precos[i], "- Estoque:", estoques[i])
    else:
        print("Medicamento não encontrado!")


def registrar_venda(nomes, estoques):
    nome = input("Nome do medicamento: ")
    if nome in nomes:
        i = nomes.index(nome)
        qtd = int(input("Quantidade a vender: "))
        if qtd <= 0:
            print("Quantidade inválida!")
        elif qtd > estoques[i]:
            print("Estoque insuficiente!")
        else:
            estoques[i] -= qtd
            print("Venda realizada!")
    else:
        print("Medicamento não encontrado!")


def repor_estoque(nomes, estoques):
    nome = input("Nome do medicamento: ")
    if nome in nomes:
        i = nomes.index(nome)
        qtd = int(input("Quantidade a repor: "))
        if qtd <= 0:
            print("Quantidade inválida!")
        else:
            estoques[i] += qtd
            print("Estoque reposto!")
    else:
        print("Medicamento não encontrado!")


def verificar_estoque_baixo(nomes, estoques):
    for i in range(len(nomes)):
        if estoques[i] < 5:
            print(nomes[i], "- Estoque baixo (", estoques[i], ")")


nomes = ["rusovastatina caustica", "acido beratoximol", "hidrocloroolmersantanado"]
precos = [12.50, 9.90, 18.75]
estoques = [20, 15, 8]

while True:
    print("\n1 - Listar medicamentos")
    print("2 - Pesquisar medicamento")
    print("3 - Registrar venda")
    print("4 - Repor estoque")
    print("5 - Mostrar estoque baixo")
    print("6 - Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        listar_medicamentos(nomes, precos, estoques)
    elif opcao == 2:
        pesquisar_medicamento(nomes, precos, estoques)
    elif opcao == 3:
        registrar_venda(nomes, estoques)
    elif opcao == 4:
        repor_estoque(nomes, estoques)
    elif opcao == 5:
        verificar_estoque_baixo(nomes, estoques)
    elif opcao == 6:
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")