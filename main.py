def palindrome(word):
    if word == word[::-1]:
        return True
    return False


word = "wow"
answer = palindrome(word)
print(palindrome(word))
