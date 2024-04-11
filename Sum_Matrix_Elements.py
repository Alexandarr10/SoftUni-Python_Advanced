rows, cols = [int(el) for el in input().split(", ")]

matrix = []
sum_nums = 0

for _ in range (rows):
    numbers = [int(el) for el in input().split(", ")]
    sum_nums += sum(numbers)
    matrix.append(numbers)

print(sum_nums)
print(matrix)

 