def calcular_valor_s(N):
    
        if N <= 0:
            raise ValueError("O valor de N deve ser inteiro e positivo.")
        
        S = sum(1/i for i in range(1, N+1))      
        return S
        
while True:
    try:
        N = int(input("Digite um número inteiro e positivo (ou digite 0 para sair): "))
        if N == 0:
            break
        
        resultado = calcular_valor_s(N)
        print(f"O valor de S para N = {N} é igual a {resultado:.2f}.")
    
    except ValueError:
        print("Erro: Digite um número inteiro e positivo.")