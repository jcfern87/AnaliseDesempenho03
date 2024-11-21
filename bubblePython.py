import timeit as tm
import sys
import platform
import psutil



def obter_informacoes():
    versao_python = sys.version
    so = platform.system()
    versao_so = platform.version()
    arquitetura = platform.architecture()
    processador = platform.processor()
    maquina = platform.machine()

    print("=== Informações do Sistema ===")
    print(f"Versão do Python: {versao_python}")
    print(f"Sistema Operacional: {so}")
    print(f"Versão do SO: {versao_so}")
    print(f"Arquitetura: {arquitetura[0]}")
    print(f"Processador: {processador}")
    print(f"Tipo de Máquina: {maquina}")


# Código que será medido
code = """
import numpy as np
import os

def bubble_sort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ler_e_ordenar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            numeros = [float(linha.strip()) for linha in arquivo]
        return numeros  # Retorna uma lista para o bubble_sort
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return []
    except ValueError:
        print("Erro: O arquivo contém dados inválidos.")
        return []

def escreve_resposta(array):
    os.makedirs("Resultados", exist_ok=True)  # Cria o diretório se não existir
    with open("Resultados/respostasPythonBubble.txt", "w") as arquivo:
        for num in array:
            arquivo.write(f"{int(num)} ")

array = ler_e_ordenar_arquivo("arquivoteste.txt")
array_ordenado = bubble_sort(array)
escreve_resposta(array_ordenado)
"""

# RAM utilizada antes da execução (em KB)
memoria = psutil.virtual_memory()
ram_utilizada = memoria.used / 1024  # Convertendo para KB

# Mede o tempo com timeit
timer = tm.Timer(stmt=code)
n_exec = 10 
tempos = timer.repeat(repeat=n_exec, number=1)

# Exibir os tempos
for i, tempo in enumerate(tempos, 1):
    print(f"Execução {i}: {tempo * 1000:.5f} ms")
    print(f"RAM Utilizada: {ram_utilizada:.2f} KB")

obter_informacoes()
