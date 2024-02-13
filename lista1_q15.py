def calcular_valor_s(N):
    try:
        if N <= 0:
            raise ValueError("O valor de N deve ser inteiro e positivo.")
        
        S = sum((t**2 + 1)/(t+3) for t in range(2, N+2))
        
        return S
    
    except ValueError as ve:
        print(f"Erro: {ve}")
        
while True:
    try:
        N = int(input("Digite um número inteiro e positivo (ou digite 0 para sair): "))
        if N == 0:
            break
        
        resultado = calcular_valor_s(N)
        print(f"O valor de S para N = {N} é igual a {resultado:.2f}.")
    
    except ValueError:
        print("Erro: Digite um número inteiro e positivo.")