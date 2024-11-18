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

def lerArq(arq):
    with open(arq, "r") as arq:
        lista = []
        lista.append(int(arq.readlines()))
        

lerArq("arquivoteste.txt")