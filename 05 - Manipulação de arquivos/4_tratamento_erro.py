from pathlib import Path

try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc) # mensagem da exceção

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc) # mensagem da exceção
except IsADirectoryError as exc:
    print(f"\nNão foi possivel abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")