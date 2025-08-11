"""
if condicao1:
    bloco de código 1
    pula o elif e o else
elif condicao2:
    bloco de codigo 2
    pula todos os elifs a seguir e o else
elif condicao3:
    bloco de codigo 3
elif condicao4:
...
elif condicaoX:
else:  # opcional
    bloco de codigo 3

bloco de codigo final
"""

condicao1 = True
condicao2 = False

if condicao1 and condicao2:
    print(1)
elif condicao1 or condicao2:
    print(2)
else:
    print(3)

valor1 = 5
valor2 = 10

if valor1 == valor2:
    print(valor1 + " é igual a " + valor2)
if valor1 != valor2:
    print(valor1 + " é diferente de " + valor2)
if valor1 >= valor2:
    print(valor1 + " é maior que o " + valor2)
elif valor1 <= valor2:
    print(valor2 + " é maior que o " + valor1)

"""
== SÃO IGUAIS?
!= SÃO DIFERENTES?
> É MAIOR QUE?
< É MENOR QUE?
>= É MAIOR OU IGUAL?
<= É MENOR OU IGUAL?
"""