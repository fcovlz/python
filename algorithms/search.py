
class Search():

    def __init__(self, data, key, verbose=True):
        self.data = data
        self.key = key
        self.verbose = verbose

    def busqueda_seq(self):

        for element in self.data:
            if self.verbose:
                print "DEBUG: ", element
            if element == self.key:
                return True

        print "Item not found"
        return False

    def busqueda_seq_idx(lista, mul, llave):

        if mul is None or llave is None:
            print "enter a valid mul or llave"
            return -1
        res = len(lista) % mul
        if res < .5:
            div = (len(lista)/mul) - res
        else:
            div = (len(lista)/mul) + (res > 0)
        for n in range(mul):
            if n == 0:
                index = lista[0:div]
            if n == mul:
                index = lista[(n-1)*div:]
            else:
                index = lista[n * div : ( 1 + n ) * div]
            # print "DEBUG: ", n
            # print index
            if max(index) >= llave:
                return busqueda_seq_fast(index, llave)
        print "Item not found"
        return -1


    def busqueda_seq_fast(lista, llave):
        if llave is None or llave < 0:
            return -1

        mid = (max(lista) - min(lista))/2
        mid += min(lista)
        mid = int(round(mid))
        # print "DEBUG: mid = ",mid

        if max(lista) == llave or min(lista) == llave or mid == llave:
            return 1

        elif mid > llave:
            midd = mid - (len(lista) / 4)
            # print "DEBUG midd = ", midd
            if llave >= midd:
                for n in range(1, len(lista)/2):
                    if (lista[(len(lista)/2) - n] == llave):
                        return 1
                    # print "DEBUG: ",n, lista[(len(lista)/2)-n]
            else:
                for n in range(0, len(lista)/2):
                    if lista[n] == llave:
                        return 1
                    # print "DEBUG: ",n, (lista[n])
        else:
            midd = (len(lista) / 4) + mid
            # print "DEBUG midd = ", midd
            if llave>=midd:
                for n in range(1, len(lista)/2):
                    if lista[len(lista)-n] == llave:
                        return 1
                    elif midd == llave:
                        return 1
                    # print "DEBUG: ",n, lista[len(lista)-n]
            else:
                for n in range(0,len(lista)/2):
                    if lista[(len(lista)/2) + n] == llave:
                        # print "DEBUG: ",n, (lista[(len(lista)/2)+n])
                        return 1
           print "Item not found"
        return -1
