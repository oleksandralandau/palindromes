def palindrome(str):
    rev = ''.join(reversed(str))
    if (str == rev):
        return True
    return False
str = "wow"
answer = palindrome(str)
print(palindrome(str))