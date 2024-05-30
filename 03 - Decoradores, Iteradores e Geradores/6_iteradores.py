class MeuIterador:
    def __init__(self, numeros: list[int]) -> None:
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError: # caso em que o contador for maior que o numero de elementos, parando assim o looping depois de iterar
            raise StopIteration # Condição de parada do looping

for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)