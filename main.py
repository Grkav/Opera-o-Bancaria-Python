
print("Bem vindo a calculadora 1")
saldo = 0
while True:
    print("___________________________________")
    print("Escolha uma opção: ")
    print("Para depositar o dinheiro digite: 1")
    print('Para retirar o dinheiro digite: 2')
    print('Para ver o saldo digite: 3 ')
    print('Para sair digite: 0')
    print('___________________________________')


    opcao = input("Digite a opção: ")
    1
    if opcao == "1":
        valor = float(input("Digite o Valor do deposito: "))
        if valor > 0:
            saldo += valor
            print('Deposito concluido')
            ver_saldo = input("Caso queira, ver seu saldo digite 1: ")
            if ver_saldo == "1":
                print(f"Seu saldo é: {saldo}")
            else:
                print('Obrigado, volte sempre!')
        else:
            print("Valor Invalido")
    elif opcao == "2":
        valor = float(input("Digite o valor de retirada: "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            print("valor retirado")
            ver_saldo = input("Caso queira ver seu saldo digite 1: ")
            if ver_saldo == "1":
                print(f"seu saldo é: {saldo}")
            else:
                print("obrigado volte sempre!")
        else:
            if valor > saldo:
                print("valor indisponivel para retirada!")
    elif opcao == "3":
        print(f"Seu saldo total é: {saldo}")
    elif opcao == "0":
        print("Encerrando por aqui, Obrigado!")
        break
