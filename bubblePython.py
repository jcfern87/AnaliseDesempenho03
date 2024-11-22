import sys
import platform
import psutil
import time


# Função para ordenar a lista (Bubble Sort)
def sort(array):
    for final in range(len(array), 0, -1):  # Vai da última posição do array até a posição 0
        exchanging = False  # Variável para verificar se o array já está ordenado

        for current in range(0, final - 1):  # Vai da posição 0 até a posição final menos 1
            if array[current] > array[current + 1]:  # Verifica se o elemento atual é maior que o próximo
                array[current], array[current + 1] = array[current + 1], array[current]  # Troca os elementos
                exchanging = True

        if not exchanging:  # Se não houve troca, o array já está ordenado
            break


# Função para ler números de um arquivo .txt
def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]  # Lê cada linha, converte para int e armazena na lista
    return numbers


# Função para escrever os números ordenados em um novo arquivo
def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")


# Função para pegar informações do sistema
def get_system_info():
    # Informações do sistema
    python_version = sys.version
    system_info = platform.uname()
    cpu_info = psutil.cpu_percent(interval=1)  # Uso de CPU
    memory_info = psutil.virtual_memory()
    
    # Exibindo as informações
    print(f"Linguagem Python: {python_version}")
    print(f"Sistema: {system_info.system} {system_info.release} ({system_info.machine})")
    print(f"Processador: {system_info.processor}")
    print(f"Uso de CPU: {cpu_info}%")
    print(f"Memória Total: {memory_info.total / (1024 ** 2):.2f} MB")
    print(f"Memória Livre: {memory_info.available / (1024 ** 2):.2f} MB")
    print(f"Memória Usada: {memory_info.used / (1024 ** 2):.2f} MB")

def rodarcode():
    # Caminho do arquivo
    input_filename = 'arquivoteste.txt'
    output_filename = 'respostasPythonBubble.txt'

    # Lê os números do arquivo
    numbers = read_numbers_from_file(input_filename)

    # Medir o tempo de execução do algoritmo de ordenação
    start_time = time.time()  # Inicia o contador de tempo
    sort(numbers)             # Chama a função de ordenação
    end_time = time.time()    # Finaliza o contador de tempo
    execution_time = (end_time - start_time) * 1000  # Tempo em milissegundos

    # Escrever os números ordenados em um novo arquivo
    write_numbers_to_file(output_filename, numbers)

    # Exibe as informações do sistema
    get_system_info()

    # Exibe o tempo de execução e a memória RAM utilizada
    process = psutil.Process()
    memory_info = process.memory_info()
    print(f"\nTempo de Execução: {execution_time:.2f} ms")
    print(f"Memória RAM Utilizada: {memory_info.rss / 1024:.2f} KB")

for i in range(10):
    print(f"Execução {i + 1}:")
    rodarcode()
