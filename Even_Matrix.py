rows = int(input())

matrix = []

for row_index in range(rows):
    inner_list = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(inner_list)

print(matrix)