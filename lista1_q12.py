def calcular_somatorio(numero):
    
        if numero <= 0:
            raise ValueError("O número deve ser inteiro e positivo.")
        
        somatorio = sum(range(1, numero + 1))
        return somatorio
        
while True:
    try:
        numero = int(input("Digite um número inteiro e positivo (ou digite 0 para sair): "))
        if numero == 0:
            break
        
        somatorio = calcular_somatorio(numero)
        print(f"O somatório de 1 até {numero} é igual a {somatorio}.")
    
    except ValueError:
        print("Erro: Digite um número inteiro e positivo.")