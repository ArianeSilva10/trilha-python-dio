arquivo = open(r"C:\Users\arian\OneDrive\Área de Trabalho\Estudo_Programação\bootcamp\trilha-python-dio\05 - Manipulação de arquivos\lorem.txt", "r")

# print(arquivo.read())

# print(arquivo.readline()) # What is Lorem Ipsum?
# readline imprime uma linha por vez, se eu colocar outro readline, a segunda linnha também será imprimida

# EXEMPLO
# for linha in arquivo.readline(): # vai imprimir caractere por caractere
#    print(linha)


# for linha in arquivo.readlines(): # vai imprimir linha por linha (iterar pelo texto)
#    print(linha)


# DICA PARA TEXTOS GRANDES
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()