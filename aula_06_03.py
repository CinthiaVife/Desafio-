#3- O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas.

#Entrada de dados

temperaturas = []

#Processamento dos dados 

for i in range(10):
    temperatura = float(input(f'Informe a temperatura {i + 1}: '))
    temperaturas.append(temperatura)

if temperaturas:
    print(f'A menor temperatura é: {min(temperaturas):.2f}')
    print(f'A maior temperatura é: {max(temperaturas):.2f}') 
    print(f'A média das temperaturas é: {sum(temperaturas)/len(temperaturas):.2f}')


