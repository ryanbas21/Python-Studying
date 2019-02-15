def sequentialSearch(list, item):
    found = False
    pos = 0
    while pos < len(list) and not found:
        if list[pos] == item:
            found = True
        else:
            pos+= 1

    return found

print(sequentialSearch([1,2,3], 2) == True)
print(sequentialSearch([1,3, 4, 2, 10], 2) == True)
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13) == True)
