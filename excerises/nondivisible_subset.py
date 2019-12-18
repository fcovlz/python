

def non_divisible_subset_sol1(k, s):
    result = 0
    length = len(s)
    print(length)
    
    for index1 in range(length - 1):
        element1 = s[index1]
        print("here 1")
        print("element1 ", element1)
        
        for index2 in range(index1 + 1, length):
            print("here 2")
            element2 = s[index2]
            print("elenment2", element2)


def non_divisible_subset_sol2(k, s):
    result = 0
    for index1 in range(len(s) - 1):
        element1 = s[index1]
        print(element1)
        for index2 in range(index1, len(s[index1 + 1:])):
            element2 = s[index2]
            print(element2)
