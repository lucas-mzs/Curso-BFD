for i in range(11):
    print(i, end=' ')

# = = = = = = = = = = 

lista_vendas = [1000, 500, 800, 1500, 2000, 2300]

meta = 1200
percentual_bonus = 0.1

for v in lista_vendas:
    if v >= meta:
        bonus = percentual_bonus * v
    else:
        bonus = 0

    print(bonus)

# = = = = = = = = = = 

for i in range(51):
    if i % 2 == 0:
        print(i)

lista_precos = [1500, 1000, 800, 3000]

# = = = = = = = = = = 

for preco in lista_precos:
    imposto_ir = 0.2 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    print(f'O valor total dos impostos sobre o produto de R${preco} é de R${imposto_total}.')