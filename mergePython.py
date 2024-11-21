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

# Função para ordenar o array com merge_sort
def merge_sort(arr):
    # Caso base: se o array tem 1 ou 0 elementos, já está ordenado
    if len(arr) <= 1:
        return arr
    
    # Dividir o array ao meio
    meio = len(arr) // 2
    esquerda = arr[:meio]  # Primeira metade
    direita = arr[meio:]   # Segunda metade
    
    # Ordenar recursivamente as duas metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    # Unir as duas metades ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []  # Lista para armazenar o array ordenado
    i = j = 0  # Índices para percorrer as duas listas

    # Enquanto houver elementos em ambas as listas, compare e adicione o menor
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adicionar os elementos restantes de qualquer lista
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado


# Função para ler o arquivo e ordenar os números
def ler_arquivo(nome_arquivo):
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

# Função para escrever o array ordenado em um txt
def escreve_resposta(array):
    with open("Resultados/respostasPythonMerge.txt", "w") as arquivo:
        for i in array:
            # Escreve cada número em uma nova linha
            arquivo.write(str(int(i)) + " ")

# Lê o arquivo, ordena os números e escreve o resultado no arquivo
array = ler_arquivo("arquivoteste.txt")
arrayOrdem = merge_sort(array)
escreve_resposta(arrayOrdem)
"""

# Define o timer por meio do timeit
timer = tm.Timer(stmt=code)
timer.timeit(number=1)  # Execução inicial para "aquecimento"

# Definir o número de execuções e medir o tempo de cada uma, colocando cada tempo em um array.
n_exec = 10
tempos = timer.repeat(repeat=n_exec, number=1) # O "number" serve para delimitar quantas vezes o código será executado em cada medição (que ocorrerá 10 vezes), é definido como 1 para poder obter o tempo individual de cada código.


# Exibir os tempos individuais 
for i, tempo in enumerate(tempos, 1):
    print(f"Execução {i}: {tempo*1000: .5f} milisegundos")
obter_informacoes()