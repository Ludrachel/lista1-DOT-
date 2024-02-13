def contar_divisores(numero):
        if numero <= 0:
            raise ValueError("O número deve ser inteiro e positivo.")

        contador = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                contador += 1

        return contador
        
while True:
    try:
        numero = int(input("Digite um número inteiro e positivo (ou digite 0 para sair): "))
        if numero == 0:
            break
        
        divisores = contar_divisores(numero)
        print(f"O número {numero} possui {divisores} divisores.")
    
    except ValueError:
        print("Erro: Digite um número inteiro e positivo.")