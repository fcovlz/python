def palindrome2(word=""):
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


def fibonacci_recursive0(end_number):
    if end_number < 2:
        return end_number
    return fibonacci_recursive0(end_number-2) + \
        fibonacci_recursive0(end_number-1)


if __name__ == "__main__":
    # Array of arrays
    word = "aaaaaaaaaaaa1aaaaaaaaaaaa"
    print(palindrome2(word))
