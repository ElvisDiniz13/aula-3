taxa_euro = 0.16
taxa_iene = 26.79

valor_real = float(input("Digite o valor em real:\n"))

print(f'Euro: {valor_real * taxa_euro}')
print(f'Iene: {valor_real * taxa_iene}')

#ou

print(f'Euro: {valor_real: * taxa_euro} | Iene: {valor_real * taxa_iene}')

