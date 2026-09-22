NUM_TENTATIVAS = 10


def registrarTentativas():
    tentativas = []
    for i in range(NUM_TENTATIVAS):
        while True:
            valor = input(f"Tentativa {i + 1} (0=erro, 1, 2 ou 3 pontos): ")
            if valor.isdigit() and int(valor) in (0, 1, 2, 3):
                tentativas.append(int(valor))
                break
            else:
                print("Valor invalido! Digite 0, 1, 2 ou 3.")
    return tentativas


def calcularPontuacao(tentativas):
    return sum(tentativas)


def calcularAproveitamento(tentativas):
    convertidos = sum(1 for t in tentativas if t != 0)
    errados = sum(1 for t in tentativas if t == 0)
    percentual = (convertidos / NUM_TENTATIVAS) * 100
    return convertidos, errados, percentual


def encontrarCestaMaisFrequente(tentativas):
    contagem = {1: 0, 2: 0, 3: 0}
    for t in tentativas:
        if t != 0:
            contagem[t] += 1
    return max(contagem, key=contagem.get)


def main():
    tentativas = registrarTentativas()

    pontuacaoTotal = calcularPontuacao(tentativas)
    convertidos, errados, percentual = calcularAproveitamento(tentativas)
    cestaFrequente = encontrarCestaMaisFrequente(tentativas)

    print("\n===== RESULTADO =====")
    print(f"Pontuacao total: {pontuacaoTotal} pontos")
    print(f"Arremessos convertidos: {convertidos}")
    print(f"Arremessos errados: {errados}")
    print(f"Aproveitamento: {percentual:.1f}%")
    print(f"Tipo de cesta mais frequente: {cestaFrequente} ponto(s)")


if __name__ == "__main__":
    main()