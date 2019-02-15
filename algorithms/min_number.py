# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. O(n2). The second function should be linear O(n).

def minNumber (lst):
    min = lst[0]
    for i in range(len(lst)) :
        for j in range(len(lst)) :
            if lst[i] < lst[j] and lst[i] < min:
              min = lst[i]

    print(min)

def minNumber2 (lst):
    min = lst[0]
    for i in range(len(lst)):
      if lst[i] < min:
        min = lst[i]

    print(min)


minNumber([1,2,3])
minNumber([1,0,2])
minNumber([1,2,3,4,0])

