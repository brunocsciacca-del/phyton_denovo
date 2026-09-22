def calcular_total_gols(gols):
    total = 0
    for g in gols:
        total += g
    return total


def calcular_media_gols(gols):
    return calcular_total_gols(gols) / len(gols)


def encontrar_artilheiros(jogadores, gols):
    maior = max(gols)
    artilheiros = []
    for i in range(len(jogadores)):
        if gols[i] == maior:
            artilheiros.append(jogadores[i])
    return artilheiros


def mostrar_relatorio(jogadores, gols):
    for i in range(len(jogadores)):
        print(jogadores[i], "-", gols[i], "gols")


jogadores = ["Lucas", "yohan", "Rafael", "uordionario", "André"]
gols = [4, 7, 2, 7, 5]

mostrar_relatorio(jogadores, gols)

total = calcular_total_gols(gols)
print("\nTotal de gols:", total)

media = calcular_media_gols(gols)
print("Média de gols:", media)

print("\nJogadores acima da média:")
for i in range(len(jogadores)):
    if gols[i] > media:
        print(jogadores[i])

artilheiros = encontrar_artilheiros(jogadores, gols)
print("\nArtilheiro(s):", artilheiros)

if len(artilheiros) > 1:
    print("Houve empate na artilharia!")
else:
    print("Não houve empate na artilharia.")