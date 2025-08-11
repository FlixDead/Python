import math 

def bhaskara():
    while True:
        try:
            a = float(input("Digite o valor de A:").replace(',', '.'))
            b = float(input("Digite o valor de B:").replace(',', '.'))
            c = float(input("Digite o valor de C:").replace(',', '.'))
            break
        except ValueError:
           print("Por favor, insira números válidos.")
           
        
    
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Delta negativo")
        return
    
    raiz = math.sqrt(delta)
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    print(f"Resposta: \nx1: {x1} \nx2: {x2}")

while True:
    bhaskara()
    continuar = input("Digite a palavra fim para terminar.\nOu aperte qualquer tecla para continuar:")
    if continuar.lower() == "fim":
        print("Programa encerrado.")
        break