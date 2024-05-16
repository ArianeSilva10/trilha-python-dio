# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []
# TODO: Crie um loop para solicita os itens ao usuário:
def entrada_itens(lista):
  for count in range(3):
    lista.append(input())
    
  return lista

# TODO: Solicite o item e armazena na variável "item":
entrada_itens(itens)
# TODO: Adicione o item à lista "itens":


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")