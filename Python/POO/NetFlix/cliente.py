# Criar uma classe para o cliente da Netflix

class Cliente():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        lista_planos = ['Básico', 'Premium']
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido.')

cliente = Cliente('João', 'joao@gmail.com', 'Super')
print(cliente.plano)