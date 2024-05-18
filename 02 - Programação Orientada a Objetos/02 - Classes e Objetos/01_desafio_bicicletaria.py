class Bicicleta:
    # construtor para inicialização
    # self é uma referência para o objeto
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    # métodos
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando Bicicleta.....")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def get_cor(self):
        return self.cor
    
    # def __str__(self):
    #    return f'''Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}'''
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.
        __dict__.items()])}"

# Inicializando com dados pré determinados
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# chamando os métodos
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(b2)  # é o mesmo que dizer : b2.buzinar()

print(b2.get_cor())

print(b2) # chamada da função __str__()