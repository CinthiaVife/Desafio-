#4 -Crie um programa que:
# 1 - Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
# 2 - Exiba a lista completa.
# 3 - Exiba o maior e o menor número da lista.
# 4 - Exiba a soma e a média de todos os números.


#Entrada de dados

numeros = []

#Processamento dos dados
for i in range(3):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)


#Saída dos dados    

print(f'\nLista completa: {numeros}')
print(f'O maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')
print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media:.2f}')









