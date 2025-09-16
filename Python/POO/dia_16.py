class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self. largura = largura

controle1 = ControleRemoto('branco', '10cm', '2cm', '3cm')
controle2 = ControleRemoto('preto', '15cm', '5cm', '5cm')

print(f'\nA cor do controle 1 é {controle1.cor} e a sua altura é de {controle1.altura}.')
print(f'A cor do controle 2 é {controle2.cor} e a sua altura é de {controle2.altura}.')