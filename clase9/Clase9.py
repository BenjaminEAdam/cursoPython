class FuncionesConLista(object):

    def listaXEscalar(self, lista, escalar):
        for i in range(len(lista)):
            lista[i] = lista[i] * escalar
        return lista

    def listaMenorAMayor(self, lista):
        ordenada = False
        while (ordenada==False):
            ordenada = True
            for i in range(len(lista)-1):
                aux1 = lista[i]
                aux2 = lista[i+1]
                if(aux1>aux2):
                    lista[i]=aux2
                    lista[i+1]=aux1
                    ordenada = False
        return(lista)

    def listaMayorAMenor(self, lista):
        ordenada = False
        while (ordenada==False):
            ordenada = True
            for i in range(len(lista)-1):
                aux1 = lista[i]
                aux2 = lista[i+1]
                if(aux1<aux2):
                    lista[i]=aux2
                    lista[i+1]=aux1
                    ordenada = False
        return(lista)

    def listaMaxMin(self, lista):
        if(len(lista)>0):
            maximo= lista[0]
            minimo= lista[0]
            for i in lista:
                if (i>maximo):
                    maximo=i
                if (i<minimo):
                    minimo=i
            return(maximo, minimo)
        else:
            return(0, 0)       

## ESto no sé si funciona
##class FuncionesConListas:
##    def __init__(self):
##        print("Esto es el init")