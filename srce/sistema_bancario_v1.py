menu = """
=================================================
    Olá, seja bem vindo(a), o que você deseja:
        1 = executar uma operação
        0 = sair do sistema
================================================
    Informe ao sistema:"""

operacao1 = input(menu)

quantidade_saque = 3
saldo = 1500
depo = 0
saq = 0
extrat = "=========================================== \n"


while operacao1 != 0:
    operacao2= input("""
=================================================
    Qual operação deseja fazer?
        d = depósito
        s = saque
        e = extrato
        o = sair do sistema
================================================
    Informe ao sistema qual operação deseja executar:""")
    if operacao2 == "d":
        print("""
            ____________      
            | DEPÓSITO |
            ------------""")
        d1 = float(input("""
    Informe valor depositado:"""))
        if d1 <= 0:
                print("""
    ______________________________________________________         
    | Valor inválido, não é possível executar o depósito |
    ------------------------------------------------------""")
        else:
            depo += d1
            extrat += f"Depósito de:R${d1:0.2f}\n"
            print(f"""
    Você executou um depósito de R${depo}
    Obrigada pela confiança nos nossos serviços!""") 
        
    elif operacao2 == "s":
        print("""
            _________    
            | SAQUE |
            ---------""")
        for saque in range(3):
            if quantidade_saque >=1:
                s1= float(input("Informe ao sistema qual o valor do saque:"))
                if s1 > saldo:
                    print("""
    _______________________________________________________         
    | Saldo insuficiente, não é possível executar o saque |
    -------------------------------------------------------""")
                    break
                if s1 > 500.00:
                    print("""
    _____________________________________________________________         
    | Saque negado, saques acima de R$500,00 não são permitidos |
    -------------------------------------------------------------""")
                    mais_saque=input("""
==========================================
    Deseja efetuar um saque?
            s = sim
            n = não
==========================================
Sua resposta:""")
                    if mais_saque == "s":
                        continue
                    else:
                        break
                elif s1 < 0:
                    print("Valor inválido")
                else:
                    saq += s1
                    extrat += f"Saque de:R${s1:0.2f}\n"
                    quantidade_saque 
                    quantidade_saque -= 1
                    print(f"""
    Saque de R${s1} efetuado com sucesso!
    Você tem {quantidade_saque} saque(s) restando por hoje """)
                    mais_saque=input("""
==========================================
    Deseja efetuar mais um saque?
            s = sim
            n = não
==========================================
Sua resposta:""")
                    if mais_saque == "s":
                        continue
                    else:
                        break
        else: 
            print("""
    ______________________________________________        
    | Você escedeu seu limite de saques por hoje. |
    ----------------------------------------------""")
        
    elif operacao2 == "e":
        saldo = saldo + depo - saq
        print("""
            ___________    
            | EXTRATO |
            -----------""")
        extrat += f"Depósito total de:R${depo:0.2f}\n"
        extrat += f"Saque total de:R${saq:0.2f}\n"
        extrat += f"\n"
        extrat += f"Saldo final de:R${saldo:0.2f}\n"
        extrat += f"=============================================="
        print(extrat)
    elif operacao2 == "o":
        print("""
            ________    
            | EXIT |
            --------""")
        print("Obrigada por ser nosso cliente, tenha um bom dia!")
        operacao1 = 0
        SystemExit
        
    else:
        print("""
            ____________________    
            |Operação inválida |
            --------------------
              """)
            
            
