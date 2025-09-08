import random
escolhapc = random.randint(1,2)
ataquepc = 2
p1 = 0
p2 = 0
vidaj = 10
vidapc = 10
escolha = int(input('Escolha um personagem \n p1 = 1  p2 = 2\n'))
if escolhapc == 1:
    if escolha == 1:
        ataq = int(input("Ataque 1 = 6 de dano \n Ataque 2 = 4 de dano\n"))
        if ataq == 1:
            vidapc -= 6
        elif ataq == 2:
            vidapc -= 4
    elif escolha == 2:
        ataq = int(input("Ataque 1 = 3 de dano \n ataque 2 = 7 de dano\n"))
        if ataq == 1:
            vidapc -= 3
        elif ataq == 2:
            vidapc -= 7
    print(f"Maquina atacou você!! Você tomou {ataquepc} de dano")
    vidaj -= ataquepc
    print(f" Sua vida = {vidaj}\n Vida do Oponente = {vidapc}")

if escolhapc == 2:
    if escolha == 1:
        ataq = int(input("Ataque 1 = 6 de dano \n Ataque 2 = 4 de dano\n"))
        if ataq == 1:
            vidapc -= 6
        elif ataq == 2:
            vidapc -= 4
    elif escolha == 2:
        ataq = int(input("Ataque 1 = 3 de dano \n ataque 2 = 7 de dano\n"))
        if ataq == 1:
            vidapc -= 3
        elif ataq == 2:
            vidapc -= 7
    print(f"Maquina atacou você!! Você tomou {ataquepc} de dano")
    vidaj -= ataquepc
    print(f" Sua vida = {vidaj}\n Vida do Oponente = {vidapc}")

