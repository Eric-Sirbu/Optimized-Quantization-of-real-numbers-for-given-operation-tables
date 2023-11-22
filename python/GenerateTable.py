import math

import torch

# binary search for roundToIndex
# use only half a table since a+b = b+a

def generateTables(f=lambda x: x+1, start=0, n=2**8):

    numbers = generateStarts(f, start, n)
    print("numbers done")
    addTable = generateAdd(numbers)
    print("add done")
    mulTable = generateMul(numbers)
    print("mul done")
    return addTable, mulTable, numbers


def generateStarts(f=lambda x: x+1, start=0, n=2**8):
    x = start
    numbers = torch.tensor([0.]*n)
    for i in range(n):
        numbers[i] = x
        x = f(x)
    return numbers


def generateAdd(numbers=range(2**8)):
    n = len(numbers)
    table = torch.tensor([[0 for i in range(n)] for j in range(n)])
    for i in range(n):
        for j in range(n):
            table[i][j] = roundToIndex(numbers[i] + numbers[j], numbers,n)

    return table


def generateMul(numbers=range(2**8)):
    n = len(numbers)
    table = torch.tensor([[0 for i in range(n)] for j in range(n)])
    for i in range(n):
        for j in range(n):
            table[i][j] = roundToIndex(numbers[i] * numbers[j], numbers,n)

    return table


def roundToIndex(x,numbers,n):
    # O(n)
    # n = len(numbers)
    # error = float('inf')
    # index = -1
    # for i in range(n):
    #     distance = abs(x - numbers[i])
    #     if distance < error:
    #         error = distance
    #         index = i
    # return index


    # falls geordnet O(logn)
    error = float('inf')
    i = n//2
    found = False
    if x <= numbers[0]:
        return 0
    elif x >= numbers[n-1]:
        return n-1
    # effizienter? richtig?
    # old_i = -1
    # not_found = True
    # for k in range(2, int(math.log2(n))+2):
    #     old_i = i
    #     i = i + (-1)**(x-numbers[i] <= 0) * max(1, n // 2**k)
    #     # print(i)
    #     not_found = i != old_i
    #
    #
    # i_bigger = (x-numbers[i] <= 0)
    # j = i + (-1)**i_bigger
    #
    # res = (i_bigger) * (i - ((x-numbers[i]) + (x-numbers[j]) < 0)) + (not i_bigger) * (i + ((x-numbers[j]) + (x-numbers[i]) >= 0))
    # return res

    #wahrscheinlich richtig & O(logn)
    bigger_i = smaller_i = -1
    k = 2
    while True:
        if x-numbers[i] < 0:
            bigger_i = i
            i = i - max(1, n//2**k)
            found = i == smaller_i
            if found: #i smaller
                if (abs(x-numbers[i+1]) <= abs(x-numbers[i]) and x>=0) or (abs(x-numbers[i+1]) < abs(x-numbers[i]) and x<0):
                    return i+1
                else:
                    return i
        else:
            smaller_i = i
            i = i + max(1, n//2**k)
            found = i == bigger_i
            if found: #i bigger
                if (abs(x-numbers[i]) <= abs(x-numbers[i-1]) and x>=0) or (abs(x-numbers[i]) < abs(x-numbers[i-1]) and x<0):
                    return i
                else:
                    return i-1
        k += 1


if __name__ == "__main__":
    n = 2**8
    numbers = [i for i in range(0,n)]
    #
    # for i in range(n-1):
    #     print(numbers[roundToIndex(i+0.2, numbers, n)])
    #     print(numbers[roundToIndex(i+0.7, numbers, n)])
    # index = roundToIndex(235.2, numbers, n)
    # print("found")
    # print(numbers[index])
    addTable, mulTable, numbers = generateTables()
    print(addTable)
    print("-------------------------------")
    print(mulTable)
