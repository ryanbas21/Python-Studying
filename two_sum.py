def two_sum (list, k):
    seen = set()
    output = set()

    for num in list:
        if k - num in seen:
            output.add((k - num, num))
        else:
            seen.add(num)
    print(output)

two_sum([1,2,3,4], 5)
two_sum([1,2,2,3], 4)
