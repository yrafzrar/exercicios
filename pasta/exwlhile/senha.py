senhacerta = 'auau'
tent = 0
while tent < 3:
    senha = input("Digite sua senha: ")
    if senha == senhacerta:
        print('serto')
        break
    else:
        tent += 1
        print('senha errada')
if tent == 3:
    print('Você passou de 3 tentativas')



