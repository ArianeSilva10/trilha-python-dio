class Animal:
    def __init__(self, nro_patas) -> None:
        self.nro_patas = nro_patas


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join
        ([f'{chave} = {valor}' for chave, valor in self.
        __dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw) -> None:
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self) -> str:
        return 'Mamifero'


class Ave(Animal):
    def __init__(self, cor_bico, **kw) -> None:
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self) -> str:
        return 'ave 42'



class Gato(Mamifero):
    pass



class  Falar_mixim:
    def falar(self):
        return "oi estou falando"



class Ornitorrinco(Mamifero, Ave, Falar_mixim):
    def __init__(self, cor_bico, cor_pelo, nro_patas) -> None:
        print(Ornitorrinco.__mro__)

        print(Ornitorrinco.mro())

        super().__init__(cor_pelo=cor_pelo,
        cor_bico=cor_bico, nro_patas=nro_patas)

    def __str__(self) -> str:
        return "Ornitorrinco"


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)


ornitorrinco = Ornitorrinco(nro_patas=2,
cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
print(ornitorrinco.falar())