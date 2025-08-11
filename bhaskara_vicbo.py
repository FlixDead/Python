def bhaskara(a, b, c):
  delta = b**2 - 4*a*c
  if delta < 0:
    return "Raiz negativa"
  x1 = (-b + delta**(1/2)) / (2*a)
  x2 = (-b - delta**(1/2)) / (2*a)
  return (x1, x2)

while True:
  try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
  except ValueError:
    print("Insira um valor válido, gay.")
    continue
  
  resultado = bhaskara(a, b, c)
  
  if resultado == "Raiz negativa":
    print("Não existem raízes reais.")
    continue
  print("As raízes da função quadrática são:", bhaskara(a, b, c))
  end = input("Insira 'fim' para finalizar, ou qualquer coisa para continuar.")
  if end.lower() == "fim":
    break