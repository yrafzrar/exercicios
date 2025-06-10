sal = float(input("Digite seu salário atual\n"))
if sal<1500:
    print("Seu salário é R$", sal,". O reajuste é de 25%, reajuste é de R$", (sal*0.25), " e o salário final é R$", (sal+(sal*0.25)) )

elif sal<2000:
    print("Seu salário é R$", sal, ". O reajuste é de 20%, sendo R$", (sal * 0.20), " e o salário final é R$",
          (sal + (sal * 0.20)))

elif sal<3000:
    print("Seu salário é R$", sal, ". O reajuste é de 15%, sendo R$", (sal * 0.15), " e o salário final é R$",
          (sal + (sal * 0.15)))

elif sal<5000:
    print("Seu salário é R$", sal, ". O reajuste é de 10%, sendo R$", (sal * 0.10), " e o salário final é R$",
          (sal + (sal * 0.10)))

elif sal>=5000:
    print("Seu salário é R$", sal, ". O reajuste é de 5%, sendo R$", (sal * 0.5), " e o salário final é R$",
          (sal + (sal * 0.05)))
