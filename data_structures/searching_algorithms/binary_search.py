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

def binarySearch(list, item):
    while len(list) > 1:
        middle = len(list) // 2

        if list[middle] == item:
            return True
        else:
            if list[middle] > item:
                list = list[:middle]
                middle = len(list)// 2
            else:
                list = list[middle:]
                middle = len(list) // 2

    if list[0] == item:
        return True

    return False




print(binarySearch(testlist, 3) == False)
print(binarySearch(testlist, 13) == True)
print(binarySearch(testlist, 32) == True)
print(binarySearch(testlist, 0) == True)

