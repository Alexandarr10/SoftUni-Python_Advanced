rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
primary = [matrix [r] [r] for r in range(rows)]
secondary = [matrix[r] [rows - r - 1] for r in range (rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")

