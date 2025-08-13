user = "socorram me subi no onibus em marrocos"
comeco = 0
fim = len(user)-1
certo = True

while comeco <= fim:
    if user[comeco] == " ":
        comeco = comeco +1
        continue
    elif user[fim] == " ":
        fim = fim-1
        continue
    if user[comeco] == user[fim]:
        comeco = comeco+1
        fim = fim-1
    else:
        certo = False
        break
if certo == True:
    print("certo")
else:
    print("Erradao")