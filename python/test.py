import torch
import GenerateTable
import CalculateError

f = lambda x: x*1.2
start = 1.
n = 5

addTable, mulTable, numbers = GenerateTable.generateTables(f, start, n)
addError, mulError = CalculateError.calculateErrors(addTable, mulTable, numbers, lambda x, y: abs(x-y))

print(numbers)
print(addError/n**2)
print(mulError/n**2)
