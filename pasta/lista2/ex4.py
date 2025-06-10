idade = int(input("Digite sua idade:\n"))
if idade<=10:
    print("O desconto é de 10% \n O produto sairá por R$180")
elif idade>=80:
    print("O desconto é de 80% \n O produto sairá por R$40")
else:
    desc = idade*2
    custo = 200-(idade*2)
    print("O óculos sairá por R$ " , custo, ". E o desconto é de", desc )
