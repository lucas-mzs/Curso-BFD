# Como funcionam as classes e para que servem?

# vendedor ='João'
# vendas = 1000
# meta = 500

# if vendas >= meta:
#     print('Parabéns, você bateu sua meta!')
# else:
#     print('Infelizmente você não bateu sua meta.')

class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0
    
    def vendeu(self, vendas):
        self.vendas = vendas
    
    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(f'Parabéns, {self.nome} bateu sua meta!')
        else:
            print(f'Infelizmente {self.nome} não bateu sua meta.')

vendedor1 = Vendedor('João')
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)