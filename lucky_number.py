import random

while True:
    lucky_number = str(random.randint(1, 2))

    user = input("Chuta ai :p =")

    if user == lucky_number:
        print(f"Você acertou!!\n o BOT escolheu:{lucky_number}")
    elif user != lucky_number:
        print(f"Você errou,\n o BOT escolheu:{lucky_number}")

    while True:    
        continuar = input("\nQuer continuar?(s/n):")
        if continuar.lower() == "s":
            print("Vamos la novamente!")
            break
        elif continuar.lower() == "n":
            print("tchau tchau")
            exit()
        else:
            print("Apenas S ou N")