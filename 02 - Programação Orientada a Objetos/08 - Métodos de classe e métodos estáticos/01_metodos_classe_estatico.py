class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade


    @classmethod
    def  criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa("Guilherme", 28)
# print(p.nome, p.idade)

p2 = Pessoa().criar_apartir_data_nascimento(1994, 3, 21, "Guilherme")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(28))
print(Pessoa.e_maior_idade(10))