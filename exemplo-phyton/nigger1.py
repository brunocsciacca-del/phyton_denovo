def calcularMedia(notas):
    soma=0
    for nota in notas:
        soma+= nota
    return soma / len(notas)

notas = [8, 9, 6]
media = calcularMedia(notas) 

if (media >= 7):
    print("Você foi aprovado.")
elif (media >= 5):
    print("Você está de recuperação")
else:
    print("Você foi reprovado.")
