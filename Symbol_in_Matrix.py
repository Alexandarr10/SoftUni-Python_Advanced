def find_element_in_matrix (matrix, element):
    for row_index in range (n):
        for col_index in range (n):
            if matrix [row_index] [col_index] == element:
                return (row_index, col_index)


n = int(input())

matrix = []


for _ in range(n):
    inner_list = list(input()) # pravim list ot characters
    matrix.append(inner_list)

searched_symbol = input()

for row_index in range(n):
    if position:
        break
    for col_index in range(n):
        if matrix [row_index] [col_index] == searched_symbol:
            position = (row_index, col_index)
            break

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")