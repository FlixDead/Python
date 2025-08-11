import random


def confirm_again():
    while True:
        again = input("De novo? (s/n)\n").lower()

        if again == "s":
            return True
        elif again == "n":
            return False
        print("Digita apenas 's' ou 'n'.")


while True:
    N = 10
    lucky = str(random.randint(1, N))

    user = input(f"Escolha um número de 1 a {N}\n")

    if lucky == user:
        print("Você acertou!")
    else:
        print(f"Errou! O número era {lucky}")

    if not confirm_again():
        break