"""
Input:
    * list sorted of integer numbers
    * value to find
Output: True or False

Description:
    Look if 2 elements of the input array can be sum and it's equal to the value
    to find. Input list is sorted, negative values is possible. Can't repeat the
    same index value to sum
"""


def verify_sum_sorted_list(array, value):
    first_item = 0
    last_item = len(array) - 1

    for index in range(len(array) - 1):
        tmp_sum = array[first_item] + array[last_item]

        if tmp_sum == value:
            return True
        else:
            if tmp_sum > value:
                last_item -= 1
            else:
                first_item += 1
    return False


def verify_sum_no_sorted_list(array, value):
    for index in array:
        if array[index] - value in array[index:]:
            return True
    return False


if __name__ == "__main__":
    # array = [1, 2, 3, 4, 5]
    # value = 9
    # result = verify_sum_sorted_list(array, value)
    # print result
    array = [1, 2, 3, 9, 15]
    value = 10
    result = verify_sum_sorted_list(array, value)
    print(result)
