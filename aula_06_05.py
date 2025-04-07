#5 - Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletaram os seguintes dados referentes a cada habitante para serem analisados:
#-sexo (masculino e feminino)
#-cor dos olhos ( verdes ou castanhos)
#-cor dos cabelos ( castanhos, pretos)
#-idade
# Faça um programa que determine e escreva:
#a) a maior idade dos habitantes;
#b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
#c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;


#Entrada de dados

maior_idade = 0
fem_18_35_anos = 0
olhos_verde_louros = 0

n = int(input('Quantos habitantes serão analizados nessa pesquisa?'))

#Processamento dos dados
for i in range(n):
    idade = int(input("Idade: "))
    sexo = input("Sexo (masculino/feminino): ")
    olhos = input("Olhos (verdes/castanhos): ")
    cabelos = input("Cabelos (louros/pretos/castanhos): ")

    if idade > maior_idade:
        maior_idade = idade

    if olhos == 'verdes' and cabelos == 'louros':
        olhos_verdes_louros +=1

#Saída dos dados
print(f"A maior idade dos habitantes foi de {maior_idade} anos")
print(f"Existem {fem_18_35_anos} mulheres entre 18 e 35")
print(f"Existem {olhos_verde_louros} indivíduos que tem olhos verdes e cabelos louros")






