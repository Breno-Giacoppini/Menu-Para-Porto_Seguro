tipo_problemas = input("Selecione o tipo de problema:\n"
                       "1 - Acidentes de trânsito\n"
                       "2 - Roubo ou furto\n"
                       "3 - Problema elétrico\n"
                       "4 - Problema mecânico\n"
                       "5 - Danos causados por fenômenos naturais\n"
                       "6 - Sair\n")

if tipo_problemas == "1":
    solucao1 = input("Selecione uma opção:\n"
                     "1 - Verificar se há vítimas e prestar socorro\n"
                     "2 - Registrar o acidente junto às autoridades\n"
                     "3 - Acionar o seguro\n")

if tipo_problemas == "2":
    solucao2 = input("Selecione uma opção:\n"
                     "1 - Registrar o roubo ou furto junto às autoridades\n"
                     "2 - Acionar o seguro\n"
                     "3 - Tomar medidas de segurança para evitar futuros roubos ou furtos\n")

if tipo_problemas == "3":
    solucao3 = input("Selecione uma opção:\n"
                     "1 - Verificar se há problemas na bateria ou no alternador\n"
                     "2 - Verificar se há fusíveis queimados\n"
                     "3 - Levar o veículo a um mecânico especializado\n")

if tipo_problemas == "4":
    solucao4 = input("Selecione uma opção:\n"
                     "1 - Verificar se há problemas com o motor\n"
                     "2 - Verificar se há problemas com a transmissão\n"
                     "3 - Levar o veículo a um mecânico especializado\n")

if tipo_problemas == "5":
    solucao5 = input("Selecione uma opção:\n"
                     "1 - Verificar se há danos estruturais no veículo\n"
                     "2 - Acionar o seguro\n"
                     "3 - Levar o veículo a um mecânico especializado\n")

if tipo_problemas == "6":
    print("Saindo...")

