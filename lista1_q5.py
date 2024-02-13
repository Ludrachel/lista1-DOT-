def peso_ideal(altura, sexo):
    if sexo == 1:  # feminino
        peso = (62.1 * altura) - 44.7
    elif sexo == 2:  # masculino
        peso = (72.7 * altura) - 58
    else:
        raise ValueError("Código de sexo inválido. Use 1 para feminino ou 2 para masculino.")
    return peso

while True:
    try:
        altura = float(input("Digite a altura em metros: "))
        sexo = int(input("Digite o sexo (1 para feminino, 2 para masculino): "))

        peso = peso_ideal(altura, sexo)
        peso_formatado = round(peso, 2)

        print("O peso ideal é:", peso_formatado)

    except ValueError:
        print("Erro: O valor fornecido não é válido. Digite novamente")