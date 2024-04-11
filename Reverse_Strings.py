word = list(input())

stack = []

for i in range (len(word)) :
    stack.append(word.pop())



print("".join(stack))



