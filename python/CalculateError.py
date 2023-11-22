import torch

# use only half a table
def calculateErrors(addTable, mulTable, numbers, f=lambda x,y: (x-y)**2):
    errorAdd = 0.
    errorMul = 0.
    n = len(addTable)
    for i in range(n):
        for j in range(n):
            errorAdd += f(numbers[i]+numbers[j], numbers[addTable[i][j]])
            # print("{} und {} mit Addier-Fehler {}".format(numbers[i], numbers[j], f(numbers[i]+numbers[j], numbers[addTable[i][j]])))
            errorMul += f(numbers[i]*numbers[j], numbers[mulTable[i][j]])
    return errorAdd, errorMul



if __name__ == "__main__":
    print()
