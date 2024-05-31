import functools


def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs) # estes argumentos extras faz com que funcione incluindo funções com e sem argumento

    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")


print(ola_mundo.__name__) # nome da funcao ola_mundo sem o nome do decorador
