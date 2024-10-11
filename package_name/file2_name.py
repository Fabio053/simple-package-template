import datetime

saldo = 2000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10
d = datetime.datetime.now()
usuarios = []
contas = []
proximo_numero_conta = 1

def deposito(saldo, extrato):  # Define a função 'deposito', que recebe saldo e extrato como argumentos
    print("Deposito")  # Informa ao usuário que a operação é um depósito

    data_formatada = d.strftime("%d/%m/%Y %H:%M %a")  # Formata a data e hora atuais para um formato legível
    print(data_formatada)  # Imprime a data formatada

    valor = float(input("Digite o valor a depositado: "))  # Solicita ao usuário o valor a ser depositado

    if valor > 0:  # Verifica se o valor depositado é maior que zero
        saldo += valor  # Atualiza o saldo, adicionando o valor depositado
        extrato += f"Deposito: R$ {valor:.2f}\n{data_formatada}"  # Adiciona a transação ao extrato formatado
        print(f"Deposito concluido!")  # Confirma que o depósito foi concluído
    else:  # Se o valor não for válido
        print("Valor não permitido, operação cancelada...")  # Informa que a operação foi cancelada
    
    return saldo, extrato  # Retorna o saldo e o extrato atualizados

def saque(*, valor, saldo, extrato, numero_saques):  # Define a função 'saque' com argumentos nomeados obrigatórios
    print("Saque")  # Informa ao usuário que a operação é um saque

    data_formatada = d.strftime("%d/%m/%Y %H:%M %a")  # Formata a data e hora atuais para um formato legível
    print(data_formatada)  # Imprime a data formatada

    # Verifica se o valor do saque excede o saldo disponível
    excedeu_saldo = valor > saldo  
    
    # Verifica se o valor do saque excede o limite máximo permitido por operação
    excedeu_limite = valor > limite  
    
    # Verifica se o número máximo de saques permitidos foi atingido
    excedeu_saques = numero_saques >= LIMITE_SAQUES  

    # Se o número de saques excedeu o limite
    if excedeu_saques:
        print("Limite de saques alcançado, tente novamente em 24h")  # Informa ao usuário sobre o limite

    # Se o valor do saque exceder o limite máximo
    elif excedeu_limite:
        print(f"Valor digitado maior que o limite maximo por saque, digite um valor menor que R$ {limite:.2f}")  # Informa sobre o limite do saque
        
    # Se o valor do saque exceder o saldo disponível
    elif excedeu_saldo:
        print("Saldo insuficiente, digite um valor dentro do saldo atual de sua conta.")  # Informa sobre saldo insuficiente
        
    # Se o valor do saque é válido
    elif valor > 0:
        saldo -= valor  # Atualiza o saldo subtraindo o valor do saque
        extrato += f"Saque: -R$ {valor:.2f}\n{data_formatada}"  # Adiciona a transação ao extrato formatado
        print("Saque concluído!")  # Confirma que o saque foi realizado
        numero_saques += 1  # Incrementa o contador de saques
        
    else:  # Se o valor não é válido
        print("Valor não permitido, operação cancelada...")  # Informa que a operação foi cancelada
    
    return saldo, extrato, numero_saques  # Retorna o saldo, o extrato e o número de saques realizados

def mostrar_extrato(saldo, *, extrato):  # Define a função 'mostrar_extrato' com 'saldo' como argumento posicional e 'extrato' como argumento nomeado
    print("Extrato")  # Informa ao usuário que está prestes a mostrar o extrato

    data_formatada = d.strftime("%d/%m/%Y %H:%M %a")  # Formata a data e hora atuais para um formato legível

    # Verifica se não há transações no extrato
    if not extrato:
        print(f"Não foram realizadas transações \n Saldo atual: R${saldo}")  # Informa que não há transações e mostra o saldo atual
    else:  # Se houver transações no extrato
        print("Extrato")  # Exibe o título do extrato
        print(f"{extrato}\nSaldo atual: R${saldo:.2f}\n{data_formatada} ")  # Imprime o extrato das transações e o saldo atual formatado
    
    return saldo, extrato  # Retorna o saldo e o extrato

def criar_usuario():
    global usuarios  # Usando a lista de usuários globalmente para acessar e modificar

    nome = input("Digite o nome do usuário: ")  # Solicita ao usuário o nome do novo usuário
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")  # Solicita a data de nascimento

    cpf = input("Digite o CPF (apenas os números): ")  # Solicita o CPF do usuário

    # Verificar se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:  # Compara o CPF fornecido com os existentes
            print("CPF já cadastrado. Tente novamente.")  # Informa que o CPF já existe
            return  # Sai da função se o CPF já estiver cadastrado

    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")  # Solicita o endereço do usuário

    # Criar dicionário para o novo usuário com a chave 'contas'
    novo_usuario = {
        'nome': nome,  # Armazena o nome
        'data_nascimento': data_nascimento,  # Armazena a data de nascimento
        'cpf': cpf,  # Armazena o CPF
        'endereco': endereco,  # Armazena o endereço
        'contas': []  # Adiciona uma lista vazia de contas ao usuário
    }

    usuarios.append(novo_usuario)  # Adiciona o novo usuário à lista de usuários
    print("Usuário criado com sucesso!")  # Confirma a criação do usuário

def criar_conta():
    global contas, proximo_numero_conta  # Usando as listas de contas e a variável globalmente
    agencia = "0001"  # Definindo o número da agência como fixo
    
    cpf_usuario = input("Digite o CPF do usuário que deseja criar a conta: ")  # Solicita o CPF do usuário

    # Verificar se o usuário existe
    usuario_encontrado = None  # Inicializa a variável para armazenar o usuário encontrado
    for usuario in usuarios:  # Itera sobre a lista de usuários
        if usuario['cpf'] == cpf_usuario:  # Verifica se o CPF corresponde a um usuário existente
            usuario_encontrado = usuario  # Armazena o usuário encontrado
            break  # Sai do loop ao encontrar o usuário
    
    if not usuario_encontrado:  # Se nenhum usuário foi encontrado
        print("Usuário não encontrado. Crie o usuário primeiro.")  # Informa que o usuário não existe
        return  # Sai da função

    # Criar dicionário para a nova conta
    nova_conta = {
        'agencia': agencia,  # Armazena o número da agência
        'numero_conta': proximo_numero_conta,  # Armazena o número da conta
        'usuario': usuario_encontrado  # Armazena o usuário associado à conta
    }

    # Adicionar a nova conta à lista de contas
    contas.append(nova_conta)  # Adiciona a nova conta à lista de contas

    # Adicionar a conta à lista de contas do usuário
    usuario_encontrado['contas'].append(nova_conta)  # Adiciona a conta à lista de contas do usuário

    print(f"Conta criada com sucesso! Número da conta: {proximo_numero_conta}")  # Confirma a criação da conta

    # Incrementar o número da conta para a próxima criação
    proximo_numero_conta += 1  # Aumenta o número da conta para a próxima criação

def menu_principal():
    # Define o menu de opções
    menu = """ 

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuario
    [5] Criar Conta
    [0] Sair

    => """ 

    while True:  # Inicia um loop infinito para mostrar o menu
        opcao = int(input(menu))  # Solicita que o usuário escolha uma opção do menu

        if opcao == 1:  # Se a opção escolhida for 1 (Depositar)
            global saldo, extrato  # Declara que as variáveis saldo e extrato são globais
            saldo, extrato = deposito(saldo, extrato)  # Chama a função deposito e atualiza saldo e extrato

        elif opcao == 2:  # Se a opção escolhida for 2 (Sacar)
            valor = float(input("Digite o valor a ser sacado: "))  # Solicita o valor a ser sacado
            global numero_saques  # Declara que a variável numero_saques é global
            saldo, extrato, numero_saques = saque(valor=valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques)  # Chama a função saque

        elif opcao == 3:  # Se a opção escolhida for 3 (Extrato)
            mostrar_extrato(saldo, extrato=extrato)  # Chama a função mostrar_extrato

        elif opcao == 4:  # Se a opção escolhida for 4 (Criar Usuário)
            criar_usuario()  # Chama a função criar_usuario

        elif opcao == 5:  # Se a opção escolhida for 5 (Criar Conta)
            criar_conta()  # Chama a função criar_conta

        elif opcao == 0:  # Se a opção escolhida for 0 (Sair)
            break  # Sai do loop e termina o programa

        else:  # Se a opção não for válida
            print("Digite uma opção válida...")  # Informa que a opção não é válida

# Chama a função menu_principal para iniciar o programa
menu_principal()