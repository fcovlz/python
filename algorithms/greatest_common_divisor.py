def get_gcd_greatest_to_lowest(nums, arr):
    validate_inputs(nums, arr)
    gcd = 1
    for index in range(1, nums + 1):
        gcd = (min(arr) / index)
        if verify_gcd(gcd, arr):
            break
    return gcd


def get_gcd_lowest_to_greatest(nums, arr):
    validate_inputs(nums, arr)
    gcd_greatest = 1
    gcd_tmp = 1
    while gcd_tmp <= min(arr):
        if verify_gcd(gcd_tmp, arr):
            gcd_greatest = gcd_tmp
        gcd_tmp = gcd_tmp + 1

        # print "gcd tmp", gcd_tmp
        # print "gcd greatest", gcd_greatest
        print arr
    return gcd_greatest


def verify_gcd(gcd, arr):
    for element in arr:
        if element % gcd != 0:
            return False
    return True


def validate_inputs(nums, arr):
    if not isinstance(nums, int):
        raise ValueError("nums is not an integer")
    if not isinstance(arr, list):
        raise ValueError("arr is not a list")
    if nums != len(arr):
        raise ValueError("nums is not the length size of arr")
    for element in arr:
        if not isinstance(element, int):
            raise ValueError("element '%s' in arr is not int" % element)
        if element < 1:
            raise ValueError("please use only natural and positive numbers")
