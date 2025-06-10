nota1 = float(input("Digite sua primeira nota: \n"))
nota2 = float(input("Digite sua segunda nota: \n"))
media = (nota1 + nota2)/2
if media>=7:
    print("Você foi aprovado")
elif media>=5:
    print("Você está de recuperação")
else:
    print("Você foi reprovado")
