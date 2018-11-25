
class Sorting(object):

    def __init__(self, lista, verbose=True):
        self.lista = lista
        self.verbose = verbose

    def ord_inserccion(self):

        for index0 in range(len(self.lista) - 1):
            current_value = self.lista[index0]
            next_value = self.lista[index0 + 1]

            if current_value > next_value:

                tmp_index0 = index0 + 1

                while tmp_index0 > 0 and \
                        next_value < self.lista[tmp_index0 - 1]:

                    self.lista[tmp_index0] = self.lista[tmp_index0 - 1]
                    tmp_index0 -= 1

                self.lista[tmp_index0] = next_value

            if self.verbose:
                print "DEBUG: ", self.lista

        return self.lista

    def ord_seleccion(self):

        for index0 in range(len(self.lista) - 1):
            minimun_value = index0

            for index1 in range(index0, len(self.lista)):
                if self.lista[minimun_value] > self.lista[index1]:
                    minimun_value = index1

            self.lista[minimun_value], self.lista[index0] = \
                self.lista[index0], self.lista[minimun_value]

            if self.verbose:
                print "DEBUG: ", self.lista

        return self.lista

    def ord_burbuja0(self):
        for index0 in range(len(self.lista)-1):
            for index1 in range(len(self.lista)-1):
                if self.lista[index1] > self.lista[index1 + 1]:
                    self.lista[index1], self.lista[index1+1] = \
                        self.lista[index1+1], self.lista[index1]

                if self.verbose:
                    print "DEBUG: ", self.lista

        return self.lista

    def ord_seleccion_pythonic(self):
        new_list = []
        for index in range(len(self.lista)):

            minimum_value = min(self.lista)
            new_list.append(minimum_value)
            self.lista.remove(minimum_value)

            if self.verbose:
                print "DEBUG: ", self.lista

        self.lista = new_list
        return self.lista

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

    def ord_original(self):
        index = 0

        while index < len(self.lista) - 1:

            if self.lista[index] > self.lista[index + 1]:

                self.lista[index], self.lista[index + 1] = \
                    self.lista[index + 1], self.lista[index]

                if index:
                    index -= 1

            else:
                index += 1

            print "DEBUG: ", self.lista

        return self.lista

    def ord_rapido(self, list):

        equal = []
        greater = []
        less = []

        if len(list) < 1:
            return list

        else: 
            reference = list[0]

            for element in list:
                if element < reference:
                    less.append(element)
                if element == reference:
                    equal.append(element)
                if element > reference:
                    greater.append(element)

                if self.verbose:
                    print "###########################################"
                    print "list :", list
                    print "reference :", reference
                    print "less than reference :", less
                    print "equal to reference :", equal
                    print "higher reference :", greater

            self.list = self.ord_rapido(less) + equal + self.ord_rapido(greater)

            return self.list

    def quick_sort(self, list):
        if len(list) <= 1:
            return list
        else:
            reference = list[0]

            if self.verbose:
                print "###########################################"
                print "list :", list
                print "reference :", reference
                print "lower than elem 0 :", [e for e in list if e < reference]
                print "reference :", reference
                print "higher elemen 0", [e for e in list if e > reference]

            self.list = self.quick_sort([e for e in list if e < reference]) + \
                [reference] + \
                self.quick_sort([e for e in list if e > reference])

            return self.list

    def merge_sort(self, lista):
        if len(lista) <= 1:
            return lista

        # Find the middle point and devide it
        middle = len(lista) // 2
        left_list = lista[:middle]
        right_list = lista[middle:]

        left_list = self.merge_sort(left_list)
        right_list = self.merge_sort(right_list)

        return self._merge(left_list, right_list)

    def _merge(self, left_half, right_half):

        result = []

        while len(left_half) != 0 and len(right_half) != 0:

            if left_half[0] < right_half[0]:
                result.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                result.append(right_half[0])
                right_half.remove(right_half[0])

        if len(left_half):
            result += left_half
        else:
            result += right_half

        if self.verbose:
            print "result :", result

        return result


if __name__ == "__main__":
    list = [1, 3, -1, 4, -2, -3, 10, 2, 5, -4, 0]
    sort = Sorting(list)

    result = sort.ord_burbuja0()
    print result

    result = sort.ord_seleccion()
    print result

    result = sort.ord_seleccion_pythonic()
    print result

    result = sort.ord_inserccion()
    print result

    result = sort.ord_original()
    print result

    result = sort.ord_rapido(list)
    print result

    result = sort.quick_sort(list)
    print result

    result = sort.merge_sort(list)
    print result