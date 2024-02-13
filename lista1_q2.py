import math

def calcular_area(raio):
    area = math.pi * raio ** 2
    return area

def calcular_perimetro(raio):
    perimetro = 2 * math.pi * raio
    return perimetro

while True:
    try:
        raio = float(input("Digite o raio do círculo: "))
        area = calcular_area(raio)
        perimetro = calcular_perimetro(raio)

        if area is not None:
            area_formatada = round(area, 2)
            print("Área do círculo:", area_formatada)

        if perimetro is not None:
            perimetro_formatado = round(perimetro, 2)
            print("Perímetro do círculo:", perimetro_formatado)

    except ValueError as ve:
        print("O valor fornecido não é numérico.")

