def Max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

def main():
    for _ in range(4):
        try:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))

            maior = Max(a, b)
            print("O maior número é:", maior)
            print("----------------------------------")
        except ValueError:
            print("Erro: Digite apenas valores inteiros!")
            print("----------------------------------")

main()