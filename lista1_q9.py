def soma_intervalo(n1, n2):
    soma = 0
    for num in range(n1, n2+1):
        soma += num
    return soma

while True:
    try:
        n1 = int(input("\nDigite o primeiro número: "))
        n2 = int(input("\nDigite o segundo número: "))
        if n1 <= n2:
            print("\nA soma do intervalo informado é ", soma_intervalo(n1,n2))
            break
        else:
            print("\nn2 deve ser maior que n1. Digite novamente!")
    except:
        print("\nValor inválido. Digite novamente!")