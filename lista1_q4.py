def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
while True:
    try:
        nota1 = float(input("Digite a nota da primeira avaliação: "))
        nota2 = float(input("Digite a nota da segunda avaliação: "))

        media = calcular_media(nota1, nota2)
        media_formatada = round(media, 2)

        if media_formatada >= 6.0:
            print("PARABÉNS! Você foi aprovado!")
            print("Média semestral:", media_formatada)
        else:
            print("Infelizmente, você não foi aprovado.")
            print("Média semestral:", media_formatada)

    except ValueError:
        print("Erro: O valor fornecido não é válido. Digite novamente ")