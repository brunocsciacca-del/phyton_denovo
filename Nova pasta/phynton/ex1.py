def calcularMedia(notas):
    soma=0
    for nota in notas:
        soma += nota #soma = soma+nota
    return soma / len(notas)
notas = [8,9 , 6]
media = calcularMedia(notas)

if(media >= 7):
    print("Aprovado")
elif(media >=5):
    print("Recuperação")
else:
    print("Reprovado")        
