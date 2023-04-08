def realizar_login():
    print("Para iniciarmos é necessário realizar um login.\n")

    user = ""
    senha = ""

    while True: 
        opcao = input("Digite 1- caso já possua cadastro.\n"
            "Digite 2- para criar um cadastro.\n\n")
        
        if opcao == "1":
            if user == "" or senha == "":
                print()
                print("Você ainda não tem uma conta cadastrada. Selecione a outra opção!\n")
                continue
            input_user = input("Digite seu usuário: \n")
            input_senha = input("Digite sua senha: \n")
            if input_user == user and input_senha == senha:
                print("Login realizado com sucesso!")
                break
            else:
                print("Usuário ou senha incorretos.")

        elif opcao == "2":
            if user != "" or senha != "":
                print("Você já tem uma conta cadastrada.")
                continue
            print()
            user = input("Digite o nome de usuário: ")
            senha = input("Digite uma senha: ")
            senha2 = input("Digite novamente sua senha: ")
            
            while senha != senha2:
                print()
                print("As senhas não se conferem! Digite novamente. \n")
                senha = input("Digite uma senha: ")
                senha2 = input("Digite novamente sua senha: ")
            print()
            print("Conta criada com sucesso!\n")
            print(user + ", Seja bem-vindo à Porto Seguros!")
            print()
            break
        else:
            print("Informação inválida, digite somente 1 ou 2.\n")

    return user, senha

def determinar_tipo_veiculo():
    while True:
        eixos = input("Digite quantos eixos possui seu veículo: ")
        print()
        if not eixos.isdigit():
            print("Informação incorreta. Digite apenas números correspondentes a quantidade de eixos de seu veículo!")
            print()
        else:
            eixos = int(eixos)
            if eixos > 2:
                print("Seu veículo é considerado de grande porte.")
            else:
                print("Seu veículo é considerado de pequeno porte.")
            break
    print()

def lidar_com_problemas():

    localizacao_do_usuario = input("Para que podemos te ajudar, digite sua localização: ")

    while True:   
        print()
        escolha_usuario = input("Selecione o tipo de problema:\n\n"
                            "1 - Acidentes de trânsito\n"
                            "2 - Roubo ou furto\n"
                            "3 - Problema elétrico\n"
                            "4 - Problema mecânico\n"
                            "5 - Danos causados por fenômenos naturais\n"
                            "6 - Sair\n\n")                                
        
        if escolha_usuario == "1":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Verificar se há vítimas e prestar socorro\n"
                                    "2 - Registrar o acidente junto às autoridades\n"
                                    "3 - Acionar o seguro\n"
                                    "4 - retornar para página anterior\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Verifique se há vítimas e preste socorro imediatamente.")
                    raise SystemExit
                elif tipo_problemas == "2":
                    print()
                    print("Registre o acidente junto às autoridades competentes.")
                    raise SystemExit
                elif tipo_problemas == "3":
                    print()
                    print("Acione o seu seguro e siga as instruções para receber assistência.")
                    raise SystemExit
                elif tipo_problemas == "4":
                    break
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")
                    
        elif escolha_usuario == "2":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Registrar o roubo ou furto junto às autoridades\n"
                                    "2 - Acionar o seguro\n"
                                    "3 - Tomar medidas de segurança para evitar futuros roubos ou furtos\n"
                                    "4 - retornar para página anterior\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Registre o roubo ou furto junto às autoridades competentes.")
                    raise SystemExit
                elif tipo_problemas == "2":
                    print()
                    print("Acione o seu seguro e siga as instruções para receber assistência.")
                    raise SystemExit
                elif tipo_problemas == "3":
                    print()
                    print("Tome medidas para aumentar a segurança do seu veículo, como instalar alarmes e rastreadores.")
                    raise SystemExit
                elif tipo_problemas == "4":
                    break
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")

        elif escolha_usuario == "3":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Verificar se há problemas na bateria ou no alternador\n"
                                    "2 - Verificar se há fusíveis queimados\n"
                                    "3 - Levar o veículo a um mecânico especializado\n"
                                    "4 - retornar para página anterior\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Verifique se a bateria ou o alternador estão com problemas e faça os reparos necessários.")
                    raise SystemExit
                elif tipo_problemas == "2":
                    print()
                    print("Verifique se há fusíveis queimados e troque-os, se necessário.")
                    raise SystemExit
                elif tipo_problemas == "3":
                    print()
                    print("Leve o veículo a um mecânico especializado para diagnosticar e reparar o problema elétrico.")
                    raise SystemExit
                elif tipo_problemas == "4":
                    break
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")

        elif escolha_usuario == "4":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Verificar o óleo e o líquido de arrefecimento\n"
                                    "2 - Verificar os pneus e o sistema de suspensão\n"
                                    "3 - Levar o veículo a um mecânico especializado\n"
                                    "4 - retornar para página anterior\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Verifique o nível e a qualidade do óleo e do líquido de arrefecimento e faça as trocas necessárias.")
                    raise SystemExit
                elif tipo_problemas == "2":
                    print()
                    print("Verifique o estado dos pneus e do sistema de suspensão e faça as trocas ou reparos necessários.")
                    raise SystemExit
                elif tipo_problemas == "3":
                    print()
                    print("Leve o veículo a um mecânico especializado para diagnosticar e reparar o problema mecânico.")
                    raise SystemExit
                elif tipo_problemas == "4":
                    break
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")

        elif escolha_usuario == "5":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Verificar se há danos visíveis no veículo\n"
                                    "2 - Acionar o seguro\n"
                                    "3 - Tomar medidas de segurança para evitar futuros danos\n"
                                    "4 - retornar para página anterior\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Verifique se há danos visíveis no veículo e faça os reparos necessários.")
                    raise SystemExit
                elif tipo_problemas == "2":
                    print()
                    print("Acione o seu seguro e siga as instruções para receber assistência.")
                    raise SystemExit
                elif tipo_problemas == "3":
                    print()
                    print("Tome medidas para aumentar a segurança do seu veículo em relação a fenômenos naturais, como estacionar em locais seguros e longe de árvores e postes.")
                    raise SystemExit
                elif tipo_problemas == "4":
                    break
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")

        elif escolha_usuario == "6":
            print()
            print("Obrigado por utilizar nosso sistema de ajuda. Volte sempre!")
            break 

        else:
            print()
            print("Opção inválida. Por favor, selecione uma opção válida.")

realizar_login()
determinar_tipo_veiculo()
lidar_com_problemas()