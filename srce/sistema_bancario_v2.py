def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        print("""
            _________    
            | SAQUE |
            ---------""")

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.") 
        return saldo, extrato, numero_saques
             
def depositar(saldo, valor, extrato, /):
        print("""
            ____________      
            | DEPÓSITO |
            ------------""")
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato
            
def visualizar_extrato(saldo, /,*, extrato):
        print("""
            ___________    
            | EXTRATO |
            -----------""")
        print("\n========================================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
def novo_usuario(usuarios):
            mensagem_cu = """
            _____________________
            | Cadastrar Usuário |
            ====================="""
            print(mensagem_cu)
            CPF = int(input("Informe CPF:"))
            usuario = filtrar_usuarios(CPF, usuarios)
            if usuario:
                print("Usuário já cadastrado")
            else:
                nome = input("Informe Nome:")
                data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
                logradouro = input("Informe logradouro:")
                bairro = input("Informe bairro:")
                numero = input("Informe número residêncial:")
                cidade = input("Informe cidade:")
                estado = input("Informe Estado em formato de sigla:")
                print("usuário adicionado com sucesso")
                endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
                usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": CPF, "endereço": endereco })
                print("""
        Usuário Criado com Sucesso!""")

def filtrar_usuarios(CPF, usuarios):
    usuarios_filtrados =  [usuario for usuario in usuarios if usuario["cpf"] == CPF]
    return usuarios_filtrados[0] if usuarios_filtrados else None 
    
def nova_conta(AGENCIA, conta_numero, usuarios):
        mensagem_ccc = """
            ________________________
            | Criar Conta Corrente |
            ========================"""
        print(mensagem_ccc)
        mensagem_uccpf = """
            Informe o CPF do Usuário:"""
        CPF = int(input(mensagem_uccpf))
        usuario = filtrar_usuarios(CPF, usuarios)
        
        if usuario:
            conta_numero += 1
            print(f"""
            Informações da conta:
            Agência: {AGENCIA}
            Número da conta: {conta_numero}
            """)
            return {"agência": AGENCIA, "numero_conta": conta_numero, "usuário": usuario}        
        else:
            print("Usuário inexistente.")
        return
            
def exit():
    print("""
===================================================
                    ________
                    | Exit |
                    ========
                            
    Obrigada pela preferência, volte sempre!

===================================================
            """)
    SystemExit

def opcao_invalida():
    print("""
                __________________
                | Opção inválida |
                ==================""")
    
def menu_1():
    menu = """
=================================================
    Olá, seja bem vindo(a), o que você deseja?
        1 = criar conta corrente
        2 = cadastrar usuário
        3 = outra operação
        0 = sair do sistema
================================================
    Informe ao sistema:"""
    return input(menu)

def menu_2():
        menu_2 = """
=================================================
    Qual operação deseja fazer?
        d = depósito
        s = saque
        e = extrato
        o = sair do sistema
================================================
    Informe ao sistema qual operação deseja executar:"""
        return input(menu_2)

def main():
    contas = []
    usuarios = []
    limite = 500.00
    numero_saques = 0
    LIMITE_SAQUES = 3
    saldo = 0
    AGENCIA= "0001"
    extrato= ""
    while True:
        opcao= menu_1()
        if opcao == "1":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                       
        elif opcao == "2":
            novo_usuario(usuarios)
        
        elif opcao == "3": 
            opcao_2 = menu_2()
            if opcao_2 == "d":
                valor = float(input("Informe o valor do depósito: "))
                
                saldo, extrato = depositar(saldo, valor, extrato)
                
            elif opcao_2 == "s":
                valor = float(input("Informe o valor do saque: "))
                
                saldo, extrato = sacar (
                    saldo = saldo,
                    valor = valor,
                    extrato = extrato,
                    limite= limite,
                    numero_saques= numero_saques,
                    limite_saques= LIMITE_SAQUES,
                )
                
                
            elif opcao_2 == "e":
                visualizar_extrato(saldo, extrato=extrato)
                
            elif opcao_2 == "o":
                exit()
            else:
                opcao_invalida()
        
        elif opcao == "0":
            exit()
        
        else:
            opcao_invalida()
                
            
main()