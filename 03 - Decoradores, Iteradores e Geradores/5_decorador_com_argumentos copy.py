# primeira forma (mais recomendável)
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args, **kwargs)
        print("faz algo depois de executar")

    return envelope


# segunda forma de fazer
def meu_decorador2(funcao):
    def envelope(nome):
        print("faz algo antes de executar")
        funcao(nome)
        print("faz algo depois de executar")

    return envelope



@meu_decorador # açúcar sintático
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")


@meu_decorador2
def ola(nome):
    print(f"Ola {nome}")



ola_mundo("joao")
ola("Joao")