class Sorting(object):

    def __init__(self):
        pass

    def ord_inserccion(self):
        lista = [1,-6,2,7,0,4,5,6,8,-4,-2,-1]
        for n in range(len(lista)-1):
            if lista[n] > lista[n+1]:
                v = lista[n+1]
                j = n+1
                while j > 0 and v < lista[j-1]:
                    print lista 
                    lista[j] = lista[j-1]
                    j -= 1
                lista[j] = v
            print "DEBUG: ", lista

    def ord_seleccion(self):
        lista = [1,-6,2,7,0,4,5,6,8,-4,-2,-1]
        for i in range(0,len(lista)-1):
            min=i
            for j in range(i+1,len(lista)):
                if lista[min] > lista[j]:
                    min=j
            aux=lista[min]
            lista[min]=lista[i]
            lista[i]=aux
            print "DEBUG: ", lista

    def ord_burbuja(self):
        lista = [1,-6,2,7,0,4,5,6,8,-4,-2,-1]
        for n in range(0,len(lista)-1):
            j = n+1
            for i in range(len(lista)-n):
                if(lista[n] > lista[j]):
                    temp = lista[n]
                    lista[n] = lista[j]
                    lista[j] = temp
                j+=1
                print "DEBUG0: ", lista
            print "DEBUG1: ", lista

    def ord_mezcla(self, lista=[]):
        left = []
        right = []
        if(len(lista)<=1):
            return lista
        else:
            middle = len(lista)/2
            left=lista[:middle]
            right=lista[middle:]
            self.ord_mezcla(left)
            self.ord_mezcla(right)
            i=0
            j=0
            k=0
            while i<len(left) and j <len(right):
                if left[i] < right[j]:
                    lista[k] = left[i]
                    i = i+1
                else:
                    lista[k] = right[j]
                    j = j+1
                k = k+1
            while i < len(left):
                lista[k] = left[i]
                i = i+1
                k = k+1
            while j < len(right):
                lista[k] = right[j]
                j = j+1
                k = k+1
            print "DEBUG: ", lista

    def ord_rapido(self, lista=[]):
        equal = []
        greater = []
        less = []
        if len(lista) < 1:
            return lista
        else: 
            pivot = lista[0]
            for x in lista:
                if x < pivot:
                    less.append(x)
                if x == pivot:
                    equal.append(x)
                if x > pivot:
                    greater.append(x)
            return  self.ord_rapido(less)+equal+self.ord_rapido(greater)

    def ord_original(self):
        lista = [1,-6,2,7,0,4,5,6,8,-4,-2,-1]
        n=0
        while(n<len(lista)-1):
            if(lista[n]>lista[n+1]):
                tmp= lista[n]
                lista[n]= lista[n+1]
                lista[n+1]=tmp
                if(n!=0):
                    n-=1
            else:
                n+=1
            print "DEBUG: ", lista
