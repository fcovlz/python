

class Sorting(object):

    def __init__(self):
        self.lista = [1, -6, 2, 7, 0, 4, 5, 6, 8, -4, -2, -1]

    def ord_inserccion(self):
        for n in range(len(self.lista) - 1):
            if self.lista[n] > self.lista[n + 1]:
                v = self.lista[n + 1]
                j = n+1
                while j > 0 and v < self.lista[j - 1]:
                    print self.lista
                    self.lista[j] = self.lista[j - 1]
                    j -= 1
                self.lista[j] = v
            print "DEBUG: ", self.lista

    def ord_seleccion(self):
        for i in range(0,len(self.lista) - 1):
            min = i
            for j in range(i + 1, len(self.lista)):
                if self.lista[min] > self.lista[j]:
                    min = j
            aux = self.lista[min]
            self.lista[min] = self.lista[i]
            self.lista[i] = aux
            print "DEBUG: ", self.lista

    def ord_burbuja(self):
        for n in range(0, len(self.lista) - 1):
            j = n + 1
            for i in range(len(self.lista) - n):
                if self.lista[n] > self.lista[j]:
                    temp = self.lista[n]
                    self.lista[n] = self.lista[j]
                    self.lista[j] = temp
                j += 1
                print "DEBUG0: ", self.lista
            print "DEBUG1: ", self.lista

    def ord_mezcla(self, list):
        lista = list
        left = []
        right = []
        if len(lista) <= 1:
            return lista
        else:
            middle = len(lista) / 2
            left = lista[:middle]
            right = lista[middle:]
            self.ord_mezcla(left)
            self.ord_mezcla(right)
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lista[k] = left[i]
                    i = i + 1
                else:
                    lista[k] = right[j]
                    j = j + 1
                k = k + 1
            while i < len(left):
                lista[k] = left[i]
                i = i + 1
                k = k + 1
            while j < len(right):
                lista[k] = right[j]
                j = j + 1
                k = k + 1
            print "DEBUG: ", lista

    def ord_rapido(self, list):
        lista = list
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
            return  self.ord_rapido(less) + equal + self.ord_rapido(greater)

    def ord_original(self):
        n = 0
        while n < len(self.lista) - 1:
            if self.lista[n] > self.lista[n + 1]:
                tmp = self.lista[n]
                self.lista[n] = self.lista[n + 1]
                self.lista[n + 1] = tmp
                if n != 0:
                    n -= 1
            else:
                n += 1
            print "DEBUG: ", self.lista
