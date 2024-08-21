menu = '''
          ################## -MENU- ########################


                        [1] - Depositar


                        [2] - Sacar


                        [3] - Extrato


                        [4] - Sair

          ####################################################
                        
                        => '''

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == '1':
    valor = float(input('Informe o valor que você deseja Depositar: '))

    if valor > 0 :
      saldo += valor
      extrato += f"\n{" " *30}Depósito: R$ {valor:.2f}\n"
    else: print('OPERAÇÃO FALHOU! Valor informado não valido!')

  elif opcao == '2':
    valor = float(input('Informe o valor que você deseja Sacar: '))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_de_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("O Sistema não pode concluir essa opção. Excedeu o Saldo da conta!")
    elif excedeu_limite:
      print('O Sistema não pode concluir essa opção. Excedeu o Limite possivel de saque da conta!')
    elif excedeu_saques:
      print('O Sistema não pode concluir essa opção. Excedeu a quantidade diaria de Saques!')
    elif valor > 0:
      saldo -= valor
      extrato += f"{" " *30}Saque: R$ {valor:.2f}\n"
      numero_de_saques += 1
    else: 
      print("OPERAÇÂO INVALIDA! informe um valor valido.")
    
  elif opcao == '3':
    opcao_3 = f"""
        {"=" *20} INFORMAÇÕES DE EXTRATO {'=' *20}

        {"Não foram realizadas movimentações." if not extrato else extrato}

        Saldo: R$ {saldo:.2f}

        {'=' *65}
        """
    print(opcao_3)
    
  elif opcao == '4':
    break

  else:
    print("OPERAÇÃO INVALIDA! por favor selecione novamente a operação desejada.")

