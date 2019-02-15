from datetime import datetime

def busca(coluna,aux):
    
    for linha in coluna:
        linha = linha.rstrip()
        
        if aux == 1:
            n = linha
        elif aux == 2:
            t = int(linha) + 2
        else:
            if aux < t:
                if linha == n:
                    return(True, aux -2)
            elif aux == t and linha ==n:
                return(True, aux -2)
            else:
                return(False, -1)

        aux= aux +1



arq = open('dataset-1-c.csv', 'r')
inicio = datetime.now()
dados = busca(arq,1)
fim = datetime.now()
arq.close()

tempo = str((fim-inicio))[8:14] + ' Mircrosegundos'

arq_w = open('resposta-dataset-1-c.txt','w')
arq_w.writelines(str(dados[0])+ "\n")
arq_w.writelines(str(dados[1])+ "\n")
arq_w.writelines(tempo)
arq_w.close()