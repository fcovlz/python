"""
Search algorithms
Elastic search
Built in JavaScript and Json objects from JS. Need front end experience.
Read about projects Lucene, compass, elasticsearch
Hoodsine and notch search, appaching hood
Kibana -> elastic search -> Logstash / Beats
Some API already exist, look what could be related to
Define rules: must, should and each one of them will have more weight
"""


class Search():
    def __init__(self, data, key, verbose=True):
        self.data = data
        self.key = key
        self.verbose = verbose

    def sequential(self):
        for element in self.data:
            if self.verbose:
                print("DEBUG: ", element)
            if element == self.key:
                return True
        print("Item not found")
        return False

    def interpolar(self):
        idx0 = 0
        idxn = len(self.data) - 1
        while idx0 <= idxn and self.data[idxn] > self.key > self.data[idx0]:
            # Set mid point
            mid = idx0 + (((idxn - idx0)/(self.data[idxn] - self.data[idx0]) *
                           (self.key - self.data[idx0])))
            if self.data[mid] == self.key:
                return "Found {} at index {}".format(self.key, mid)
            if self.data[mid] < self.key:
                idx0 = mid + 1
        return False

    def binary_search(self):
        first = 0
        last = len(self.data) - 1
        while first <= last:
            midpoint = (first + last) / 2
            if self.verbose:
                print(self.data[midpoint])
            if self.data[midpoint] == self.key:
                return True
            else:
                if self.key < self.data[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return False

    def binary_search_recursive0(self, first=None, last=None):
        if not first <= last:
            return False
        else:
            if first is None or last is None:
                first = 0
                last = len(self.data) - 1
                return self.binary_search_recursive0(first, last)
            else:
                midpoint = (first + last) / 2
                if self.verbose:
                    print(self.data[midpoint])
                if self.data[midpoint] == self.key:
                    return True
                else:
                    if self.key < self.data[midpoint]:
                        last = midpoint - 1
                    else:
                        first = midpoint + 1
                    return self.binary_search_recursive0(first, last)

    def binary_search_recursive1(self, list):
        if len(list) == 0:
            return False
        else:
            midpoint = len(list) / 2
            if self.verbose:
                print(list)
            if list[midpoint] == self.key:
                return True
            else:
                if list[midpoint] > self.key:
                    new_list = list[:midpoint]
                else:
                    new_list = list[midpoint+1:]
                return self.binary_search_recursive1(new_list)


if __name__ == "__main__":
    # list = [1, 3, -1, 4, -2, -3, 10, 2, 5, -4, 0]
    list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    key = -2
    search = Search(list, key)
    # result = search.busqueda_seq()
    # print result
    #
    # result = search.interpolar()
    # print result

    # result = search.binary_search()
    # print result

    # TODO fix boundary errors
    # result = search.binary_search_recursive0(list)
    # print result

    # TODO fix boundary errors
    result = search.binary_search_recursive1(list)
    print(result)
