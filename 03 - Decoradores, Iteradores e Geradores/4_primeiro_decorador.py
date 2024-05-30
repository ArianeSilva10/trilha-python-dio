def meu_decorador(funcao):
    def envelope():
        print("Faz algo aantes de executar")
        funcao()
        print("Faz algo depois de executar")

    return envelope


def ola_mundo():
    print("Olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

# Colocar um comportamento nesta função