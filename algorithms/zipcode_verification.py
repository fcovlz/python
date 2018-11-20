"""
inputs
110000 False
101201 True
542361 True
4542867 False
abcdef False
"""


def main():
    p = raw_input()
    try: 
        result = 999999 > int(p) > 100000 and p[0] == p[2] == p[1] == p[3]
    except():
        result = False
    print result
    
    
def matrix():
    temp = raw_input("")
    temp = temp.split()
    rows = int(temp[0])
    col = int(temp[1])
    matrix = []

    for n in range(col):
        matrix.append([])

    for n in range(rows):
        temp = raw_input("")
        for i in range(col):
            matrix[i].append(temp[i])

    matrix_hor = []
    for n in matrix:
        matrix_hor += n

    n = 0
    print matrix_hor

    while check_alpha_digit(matrix_hor[n:]):

        while not (matrix_hor[n].isalpha() or matrix_hor[n].isdigit()):

            while matrix_hor[n-1] == " " or n == 0 :
                del matrix_hor[n]
                break
            while matrix_hor[n-1].isdigit() or matrix_hor[n-1].isalpha():
                matrix_hor[n] = " "
                break
            break
        print matrix_hor
        n += 1
    matrix_final = ""
    for n in matrix_hor:
        matrix_final += n
    print matrix_final


def check_alpha_digit(temp):
    for n in temp:
        while n.isalpha() or n.isdigit():
            return True
    return False
