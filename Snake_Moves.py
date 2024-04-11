from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())  # abc => ["a", "b", "c"]

word_copy = deque(word)

for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)  # abc => ["a", "b", "c"] => ["a", "b", "c", "a", "b", "c"]

    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep="")
    else:
        print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")

