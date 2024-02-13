def verificar_paridade(n):
    try:
        if isinstance(n, int):
            return n % 2 == 0
        else:
            raise ValueError("O valor fornecido não é um número inteiro.")
    except ValueError as ve:
        print(f"Erro: {ve}")
        return False
    
numero1 = 10
numero2 = 15
numero3 = "abc"

print(verificar_paridade(numero1)) 
print(verificar_paridade(numero2))  
print(verificar_paridade(numero3))  