numeros = [1, 2, 3, 4, 5]

print(numeros) #imprime a lista
print(numeros[0]) #imprime o primeiro elemento da lista
print(numeros[4]) #imprime o último item dessa lista
print(numeros[-1]) #garante a impressão do último elemento da lista

#removendo um elemento da lista
numeros.remove(3)
print(numeros)

#exibir elemento por elemento
for numero in numeros:
    print(numero)

#Adiciona valor na lista
numeros.append(6)
print(numeros)

#verificando se o valor 2 e 3 estão na lista
if 2 in numeros:
    print("O número 2 está na lista")
else:
    print("O número 2 não está na lista")

if 3 in numeros:
    print("O número 3 está na lista")
else:
    print("O número 3 não está na lista")
