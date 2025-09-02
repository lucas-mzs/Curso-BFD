def somando_impares():
    soma = 0

    print('=== Ímpares multiplos de 3 entre 1 e 500 ===')

    for i in range(1, 501):
        if i % 2 != 0 and i % 3 == 0:
            soma += i
            print(i, end=' ')

    print(f'\n\n🔢 Soma total: {soma}')

somando_impares()