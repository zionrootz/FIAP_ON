#Criar uma estrutura em Python que multiplique apenas os números primos presentes nesta lista, ou seja, 
# NÃO MULTIPLICA o 34 (por ser divisível por 2), multiplica o 3 (que é primo), o 1 (sim, o um vai entrar) e por aí vai … 
# a FLAG é o resultado desta multiplicação.

numeros = [34, 3, 1, 51, 6, 33, 23, 2, 29, 5, 33, 1, 7, 65, 4, 12, 5, 7, 46, 3, 41, 15, 3, 23, 2, 1, 3, 21, 35, 4, 6, 2, 13, 5, 14, 10, 3, 25, 7, 13, 14, 7, 5, 33, 21]

valor=1
ct=0

# Um numero só é primo se for divisivel unica e exclusivamente por 1 e por ele mesmo, totalizando apenas 2 possiveis divisoes
for num in numeros:
    for c in range(1,num + 1):
        if num % c == 0:
            ct +=1

    if ct == 2:
        print('Número', num, 'é primo')
        valor=valor*num
    else:
        print('Número', num, 'não é primo')

    ct = 0

print("Valor final: ", valor)