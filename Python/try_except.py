try:
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    numero3 = int(input('Digite o terceiro número: '))
    print(f'Os números digitados foram : {numero1}, {numero2} e {numero3}')
except ValueError:
    print('Entrada inválida! Por favor digite um número inteiro.')