def celsius(fahrenheit):
    celsius = ((fahrenheit - 32) / 9) * 5
    return celsius

while True:
    try:
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        grau_celsius = celsius(fahrenheit)
        grau_celsius_format = round(grau_celsius, 2)
        print("A temperatura em graus Celsius é:", grau_celsius_format)

    except ValueError:
        print("Erro: O valor fornecido não é válido.Digite novamente")