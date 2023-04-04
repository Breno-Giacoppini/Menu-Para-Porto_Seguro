guinchos = [
    {'nome': 'Guincho de porte pequeno', 'tipo': 'plataforma', 'comprimento': 10},
    {'nome': 'Guincho de porte médio', 'tipo': 'carreta', 'comprimento': 15},
    {'nome': 'Guincho de porte grande', 'tipo': 'caminhão',  'comprimento': 20}
]

carro = input("Qual é o modelo do seu carro? ")
porte = input("Qual o porte do seu carro? (pequeno, médio, grande) ")
tipo_problema = input("Qual é o tipo de problema que você está enfrentando? \n\n" 
                      "Segue problemas: \n\n"
                      "1 -> colisão \n\n"
                      "2 -> problema elétrico \n\n"
                      "3 -> problema na suspensão \n\n")

comprimento = 0

if porte == 'pequeno':
    comprimento = 10
elif porte == 'médio':
    comprimento = 15
elif porte == 'grande':
    comprimento = 20

if tipo_problema == '1':
    for guincho in guinchos:
        if guincho['comprimento'] >= comprimento and guincho['tipo'] == 'caminhão':
            print(f'O guincho mais adequado para o atendimento do {carro} com problema de {tipo_problema} é {guincho["nome"]}.')
            break
elif tipo_problema == '2':
    print("O problema elétrico será avaliado por um profissional especializado em seu local.")
elif tipo_problema == '3':
    print(f"O carro {carro} com problema de suspensão será atendido por um guincho de porte médio.")
else:
    print("Tipo de problema inválido.")
