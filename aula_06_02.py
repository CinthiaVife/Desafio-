#2- Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00.
# Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.


#Entrada de dados

area = float(input('Informe em metros quadrados a área a ser pintada:'))

#Processamento dos dados

cobertura_por_lata = 18*3
preço_tinta_lata = 130
qtd_lata = area/cobertura_por_lata



if qtd_lata != int(qtd_lata):
   qtd_lata = int(qtd_lata) + 1
else:
    qtd_lata = int(qtd_lata)
compra = qtd_lata*preço_tinta_lata
  

#Saída dos dados

print (f'A quantidade de latas de tinta a ser comprada é de {qtd_lata} unidades, e o valor a ser desembolsado é de R$ {compra}')
