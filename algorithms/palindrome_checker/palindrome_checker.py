from Queue import deque

def palindrome_checker(string):
    string = string.replace(' ', '')
    q = deque()
    reversed = ''

    for letter in string:
        q.append(letter)


    while q:
        reversed += q.pop()

    return reversed == string


print(palindrome_checker('radar') == True)
print(palindrome_checker('ryan') == False)
print(palindrome_checker('race car') == True)
print(palindrome_checker('is that a word') == False)
