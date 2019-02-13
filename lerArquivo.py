import csv
from datetime import datetime


def encontraMaior(coluna):
    aux = 0
    for linha in coluna:
        if linha > aux:
            Nmaior = linha
            aux = linha
    return Nmaior   

arquivo = open('dataset-2-e.csv', 'r')
inicio = datetime.now()
print inicio
maiorValor = encontraMaior(arquivo)
arquivo.close()

fim = datetime.now()
print fim
tempo = str((fim-inicio))[8:14] + ' Mircrosegundos'
print tempo


arquivo2 = open('resposta-dataset-2-e.txt', 'w')
arquivo2.writelines(str(maiorValor))
arquivo2.writelines(tempo)
arquivo2.close()