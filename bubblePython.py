import timeit as tm
import sys
import platform
import psutil

# Função que obtém e imprime as informações necessárias fora o tempo.
def obter_informacoes():
    # Versão do Python
    versao_python = sys.version

    # Informações do PC
    so = platform.system()
    versao_so = platform.version()
    arquitetura = platform.architecture()
    processador = platform.processor()
    maquina = platform.machine()

    # RAM utilizada
    memoria = psutil.virtual_memory()
    ram_utilizada = memoria.used / 1024  # Convertendo de bytes para KB

    # Exibir informações
    print("=== Informações do Sistema ===")
    print(f"Versão do Python: {versao_python}")
    print(f"Sistema Operacional: {so}")
    print(f"Versão do SO: {versao_so}")
    print(f"Arquitetura: {arquitetura[0]}")  # 32-bit ou 64-bit
    print(f"Processador: {processador}")
    print(f"Tipo de Máquina: {maquina}")
    print(f"RAM Utilizada: {ram_utilizada:.2f} KB")

# Código que vai ser medido.
code = """
import numpy as np
def bubble_sort(lista): 
    # Outer loop for traverse the entire list 
    for i in range(0,len(lista)-1): 
        for j in range(len(lista)-1): 
            if(lista[j]>lista[j+1]): 
                temp = lista[j] 
                lista[j] = lista[j+1] 
                lista[j+1] = temp 
    return lista 

# Função para ler o arquivo e ordenar os números
def ler_e_ordenar_arquivo(nome_arquivo):
    try:
        # Lê o arquivo e converte cada linha em um número
        with open(nome_arquivo, 'r') as arquivo:
            numeros = [float(linha.strip()) for linha in arquivo]

        # Converte para um array numpy (opcional, pode usar apenas a lista)
        array = np.array(numeros)

        return array
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except ValueError:
        print("Erro: O arquivo contém dados inválidos. Certifique-se de que todas as linhas contêm números.")

array = ler_e_ordenar_arquivo("arquivoteste.txt")
print("Array pré ordenação: ", array)
arrayOrdenado = bubble_sort(array)
print("Array pós ordenação: ", arrayOrdenado)
print("")
"""

# Define o timer por meio do timeit
timer = tm.Timer(stmt=code)

# Definir o número de execuções e medir o tempo de cada uma, colocando cada tempo em um array.
n_exec = 10
tempos = timer.repeat(repeat=n_exec, number=1) # O "number" serve para delimitar quantas vezes o código será executado em cada medição (que ocorrerá 10 vezes), é definido como 1 para poder obter o tempo individual de cada código.


# Exibir os tempos individuais 
for i, tempo in enumerate(tempos, 1):
    print(f"Execução {i}: {tempo: .5f} segundos")
obter_informacoes()

