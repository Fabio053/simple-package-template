opcao = -1

while opcao != 0:
    print("Escolha a função desejada:")
    opcao = int(input("[1] Adição \n[2] Subtração \n[3] Multiplicação \n[4] Divisão \n[0] Sair\n"))

    if opcao in [1, 2, 3, 4]:
        simbolos = {1: 'Adição', 2: 'Subtração', 3: 'Multiplicação', 4: 'Divisão'}
        simbolo_matematico = simbolos[opcao]

        primeiro_valor = float(input(f"Digite o primeiro valor da {simbolo_matematico}: "))
        segundo_valor = float(input(f"Digite o segundo valor da {simbolo_matematico}: "))

        if opcao == 1:
            valor_total = primeiro_valor + segundo_valor
        elif opcao == 2:
            valor_total = primeiro_valor - segundo_valor
        elif opcao == 3:
            valor_total = primeiro_valor * segundo_valor
        elif opcao == 4:
            if segundo_valor != 0:
                valor_total = primeiro_valor / segundo_valor
            else:
                print("Erro: Divisão por zero não é permitida.")
                continue

        print(f"O resultado de sua {simbolo_matematico} é de {valor_total}")

    elif opcao == 0:
        print("Saindo da calculadora...")
    else:
        print("Valor incorreto! Por favor insira uma opção válida.")