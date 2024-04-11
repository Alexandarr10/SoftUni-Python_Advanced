from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders and orders[0] <= food_quantity:
    food_quantity -= orders[0]
    orders.popleft()

if orders :
    print("Orders left:", end='')
    while orders:
        print(f"  {orders.popleft()}", end='')
else:
    print("Orders complete")
