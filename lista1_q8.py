def ler_caractere():
    while True:
        caractere = input("Digite 'S' para sim ou 'N' para não: ")
        if caractere == 'S' or caractere == 'N':
            return caractere
        else:
            print("Caractere inválido. Digite novamente.")
            
def main():
    continuar = True
    while continuar:
        numero = float(input("Digite um número: "))
        print("O cubo do número é:", numero ** 3)
        resposta = ler_caractere()
        if resposta == 'N':
            continuar = False

main()
