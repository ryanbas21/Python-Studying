def binary_search(list, item):

    middle = len(list) // 2

    if list[middle] == item:
        return True

    if len(list) <= 1:
        return False

    if list[middle] > item:
        return binary_search(list[:middle], item)
    else:
        return binary_search(list[middle:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3) == False)
print(binary_search(testlist, 13) == True)
print(binary_search(testlist, 32) == True)
print(binary_search(testlist, 0) == True)
