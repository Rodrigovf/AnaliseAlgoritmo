
class Tratadados(object):

    
    def encontraMaior(self, coluna):
        aux = 0
        for row in coluna:
            if row > aux:
                Nmaior = row
                aux = row
       
        print Nmaior
        return Nmaior
    

