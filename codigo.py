while True:   
    escolha_usuario = input("Selecione o tipo de problema:\n"
                        "1 - Acidentes de trânsito\n"
                        "2 - Roubo ou furto\n"
                        "3 - Problema elétrico\n"
                        "4 - Problema mecânico\n"
                        "5 - Danos causados por fenômenos naturais\n"
                        "6 - Sair\n\n")                                
    
    if escolha_usuario == "1":
        while True:
            tipo_problemas = input("Selecione uma opção:\n"
                                "1 - Verificar se há vítimas e prestar socorro\n"
                                "2 - Registrar o acidente junto às autoridades\n"
                                "3 - Acionar o seguro\n"
                                "4 - retornar para página anterior\n")
            if tipo_problemas == "1":
                print("Verifique se há vítimas e preste socorro imediatamente.")
            elif tipo_problemas == "2":
                print("Registre o acidente junto às autoridades competentes.")
            elif tipo_problemas == "3":
                print("Acione o seu seguro e siga as instruções para receber assistência.")
            elif tipo_problemas == "4":
                break
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")

    elif escolha_usuario == "2":
        while True:
            tipo_problemas = input("Selecione uma opção:\n"
                                "1 - Registrar o roubo ou furto junto às autoridades\n"
                                "2 - Acionar o seguro\n"
                                "3 - Tomar medidas de segurança para evitar futuros roubos ou furtos\n"
                                "4 - retornar para página anterior\n")
            if tipo_problemas == "1":
                print("Registre o roubo ou furto junto às autoridades competentes.")
            elif tipo_problemas == "2":
                print("Acione o seu seguro e siga as instruções para receber assistência.")
            elif tipo_problemas == "3":
                print("Tome medidas para aumentar a segurança do seu veículo, como instalar alarmes e rastreadores.")
            elif tipo_problemas == "4":
                break
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")
    elif escolha_usuario == "3":
        while True:
            tipo_problemas = input("Selecione uma opção:\n"
                                "1 - Verificar se há problemas na bateria ou no alternador\n"
                                "2 - Verificar se há fusíveis queimados\n"
                                "3 - Levar o veículo a um mecânico especializado\n"
                                "4 - retornar para página anterior\n")
            if tipo_problemas == "1":
                print("Verifique se a bateria ou o alternador estão apresentando problemas e tome as medidas necessárias.")
            elif tipo_problemas == "2":
                print("Verifique se há fusíveis queimados e substitua-os, se necessário.")
            elif tipo_problemas == "3":
                print("Leve o veículo a um mecânico especializado para avaliar e reparar o problema elétrico.")
            elif tipo_problemas == "4":
                break
            else:
                print("Opção inválida. Por favor, selecione uma opção válida")
    elif escolha_usuario == "4":
        while True:
            tipo_problemas = input("Selecione uma opção:\n"
                                "1 - Verificar se há problemas no motor\n"
                                "2 - Verificar se há problemas nos freios\n"
                                "3 - Levar o veículo a um mecânico especializado\n"
                                "4 - retornar para página anterior\n")
            if tipo_problemas == "1":
                print("Verifique se há problemas no motor e tome as medidas necessárias.")
            elif tipo_problemas == "2":
                print("Verifique se há problemas nos freios e tome as medidas necessárias.")
            elif tipo_problemas == "3":
                print("Leve o veículo a um mecânico especializado para avaliar e reparar o problema mecânico.")
            elif tipo_problemas == "4":
                break
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")
    elif escolha_usuario == "5":
        while True:
            tipo_problemas = input("Selecione uma opção:\n"
                                "1 - Verificar se há danos visíveis no veículo\n"
                                "2 - Verificar se há problemas no vidro ou na lataria\n"
                                "3 - Acionar o seguro\n"
                                "4 - retornar para página anterior\n")
            if tipo_problemas == "1":
                print("Verifique se há danos visíveis no veículo e tome as medidas necessárias.")
            elif tipo_problemas == "2":
                print("Verifique se há problemas no vidro ou na lataria e tome as medidas necessárias.")
            elif tipo_problemas == "3":
                print("Acione o seu seguro e siga as instruções para receber assistência.")
            elif tipo_problemas == "4":
                break
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")
    elif escolha_usuario == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

