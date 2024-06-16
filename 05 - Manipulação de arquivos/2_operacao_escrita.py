arquivo = open(r"C:\Users\arian\OneDrive\Área de Trabalho\Estudo_Programação\bootcamp\trilha-python-dio\05 - Manipulação de arquivos/teste.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines("Python") # escreveu uma letra por vez

arquivo.close()