#!/bin/python
import os


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    abc = get_abc(h)
    max_height = get_max_height(word, abc)
    wide = get_wide(word)
    rectangule_area = get_rectangule_area(max_height, wide)
    print("abc %s"%abc)
    print("max_height %s"%max_height)
    print("wide %s"%wide)
    print("rectangule area %s"%rectangule_area)
    return rectangule_area


def get_abc(h):
    abc_array = 'abcdefghijklmnopqrstuvwxyz'
    abc = {}
    for index in range(len(abc_array)):
        word = abc_array[index]
        height_value = h[index]
        abc[word] = height_value
    return abc


def get_max_height(word, abc):
    max_height = None
    for ele in word:
        if max_height is None:
            max_height = abc[ele]
        elif abc[ele] > max_height:
            max_height = abc[ele]
    return max_height


def get_wide(word):
    return len(word)


def get_rectangule_area(height, wide):
    return height * wide


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = map(int, input().rstrip().split())
    word = input()
    result = designerPdfViewer(h, word)
    fptr.write(str(result) + '\n')
    fptr.close()
