#1 - Faça um programa que pergunte quanto um funcionário recebe por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a) salário bruto
#b) quanto pagou ao IRRF
#c) quanto pagou ao INSS
#d) quanto pagou ao sindicato
#e) o salário líquido


#Entrada de dados:

salario = float(input('Informe quanto o funcionário recebe por hora:'))
horas = float(input('Informe quantas horas o funcionário trabalhou no mês:'))

#Processamento dos dados:

salario_bruto = salario*horas
irrf = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto-(irrf+inss+sindicato)

#Saída dos dados 

print('**************************************')
print(f'O salário bruto do funcionário é R$ {salario_bruto:.02f}')
print(f'O valor pago ao IRRF é de R$ {irrf:.02f}')
print(f'O valor pago ao INSS é de R$ {inss:.02f}')
print(f'O valor pago ao Sindicato é de R$ {sindicato:.02f}')
print(f'O salário líquido a ser recebido pelo funcionário é R$ {salario_liquido:.02f}')
print('**************************************')


