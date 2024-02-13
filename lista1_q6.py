def calcular_poligono(num_lados, medida_lado):
    if num_lados == 3:
        perimetro = num_lados * medida_lado
        print("TRIÂNGULO")
        print("Perímetro:", round(perimetro, 2))
    elif num_lados == 4:
        area = medida_lado ** 2
        print("QUADRADO")
        print("Área:", round(area, 2))
    elif num_lados == 5:
        print("PENTÁGONO")
    else:
        raise ValueError("Número de lados inválido. Use 3, 4 ou 5.")

while True:
    try:
        num_lados = int(input("Digite o número de lados do polígono: "))
        medida_lado = float(input("Digite a medida do lado em cm: "))

        calcular_poligono(num_lados, medida_lado)

    except ValueError:
        print("Erro: O valor fornecido não é válido. Digite novamente.")