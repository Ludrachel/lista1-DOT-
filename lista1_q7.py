def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

while True:
    try:
        numero = int(input("Digite um número inteiro: "))

        fatorial = calcular_fatorial(numero)

        print("O fatorial de", numero, "é:", fatorial)

    except ValueError:
        print("Erro: O valor fornecido não é válido. Digite novamente.")