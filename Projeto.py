saldo = 2000
limite = 500
quantSaque = 0
quantDeposito = 0
opc = 0


menu =  """
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [4] Sair
    """

while opc != 4:
    opc = int(input(menu))
    if opc == 1:
        saque = float(input("Digite o valor a ser sacado: \n"))
        if saque <= saldo and saque <= limite and quantSaque < 3:
            print("Saque altorizado \n")
            saldo -= saque
            quantSaque += 1
        else:
            print("Saque não altorizado \n")

    elif opc == 2:
        deposito = float(input("Digite o valor a ser depositado: \n"))
        saldo += deposito
        quantDeposito += 1

    elif opc == 3:
        print(f"""
        Saldo atual: {saldo}
        Quantidade de saques efetuados: {quantSaque}
        Quantidade de depositos efetuados: {quantDeposito}
        """)

else:
    print("Saindo...")