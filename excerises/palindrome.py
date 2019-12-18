def palindrome1(word):
    size = len(word)
    error = 0
    for index in range(size/2):
        if word[index] == word[size-1]:
            print("so far so good")
            continue
        else:
            print("not a palindrome")
            error = 1
            break
    return error


def palindrome2(word):
    size = len(word)
    if size <= 1:
        print("It's a palindrome")
        return 0
    else:
        last_word = word[size-1]
        first_word = word[0]
        if last_word != first_word:
            print("It's not a palindrome")
            return 1
        palindrome2(word[1:size-1])


def is_array_palindrome(array):
    for index in range(len(array)/2):
        if array[index] != array[-1-index]:
            return False
    return True


def is_palindrome(array):
    if len(array) <= 1:
        return True
    else:
        if array[0] != array[-1]:
            return False
    return is_palindrome(array[1:-1])


if __name__ == "__main__":
    # Array of arrays
    word = "aaaaaaaaaaaa1aaaaaaaaaaaa"
    print(palindrome1(word))
    print(palindrome2(word))
