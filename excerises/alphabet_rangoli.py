import string


def print_rangoli(size):
    wide = (4 * size) - 3
    abc = string.ascii_lowercase[:size]
    result = []
    row = ""
    
    for index in range(size-1, -1, -1):
        row = abc[:index:-1] + abc[index:] 
        row = '-'.join(list(row))
        row = row.center(wide,'-')
        result.append(row)
    
    for index in range(size-1):
        row  = result[index]
        result.insert(size, row )

    result = '\n'.join(result)
    print(result)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

    # for index in range(size, -size, -1):
        # square = []
        # rangoli = ""
        # if index <= 0:
            # rangoli = result[index*2 - index - 1]
            # result.insert(abs(index), rangoli)
            # # pdb.set_trace()
        # else:
            # square = list(ABC[:index])
            # if len(square) <2:
                # square = square[::-1]
            # else:
                # square = square
                # reverse_square = square[::-1]
                # square.pop(0)
                # square = reverse_square + square

            # rangoli = '-'.join(square)
            # rangoli = rangoli.center(wide,'-')
            # result.append(rangoli)
            # # pdb.set_trace()
