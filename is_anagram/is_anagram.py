def is_anagram (str1, str2):
    str1 = "".join(str1.split())
    str2 = "".join(str2.split())
    letters = {}

    if not isString(str1) and isString(str2):
        return False
    if not sameLength(str1, str2.strip()):
        return False

    firstLetters = lettersDict(str1)
    secondLetters = lettersDict(str2)

    for key in firstLetters:
        if not key in secondLetters:
           return False

    return True

# Check if string
def isString (string) :
    return isinstance(string, str)

def sameLength (str1, str2):
  return len(str1) == len(str2)

def lettersDict(str1):
  letters = {}
  for i in str1:
        if str1 in letters.itervalues():
            letters[i] += 1
        else:
            letters[i] = 1
  return letters
