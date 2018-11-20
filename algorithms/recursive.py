

def palindrome2(word=""):
    size = len(word)
    if size <= 1:
        print "It's a palindrome"
        return 0
    else:
        last_word = word[size-1]
        first_word = word[0]
        if last_word != first_word:
            print "It's not a palindrome"
            return 1
        palindrome2(word[1:size-1])


if __name__ == "__main__":
    # Array of arrays
    word = "aaaaaaaaaaaa1aaaaaaaaaaaa"
    print palindrome2(word)
