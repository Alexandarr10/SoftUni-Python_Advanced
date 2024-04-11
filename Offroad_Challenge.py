from collections import deque

fuel = deque(map(int, input().split()))
consumption = deque(map(int, input().split()))
altitude = deque(map(int, input().split()))

counter = 0
has_reached_any = False

while fuel and consumption:
    counter += 1
    temp = fuel[-1] - consumption[0]

    if temp >= altitude[0]:
        has_reached_any = True

        fuel.pop()
        consumption.popleft()
        altitude.popleft()

        print(f"John has reached: Altitude {counter}")
    else:
        print(f"John did not reach: Altitude {counter}")
        print("John failed to reach the top.")
        if has_reached_any:
            print("Reached altitudes:", end=" ")
            reached_altitudes = [f"Altitude {i}" for i in range(1, counter)]
            print(", ".join(reached_altitudes))
        else:
            print("John didn't reach any altitude.")
        exit()

if not altitude:
    print("John has reached all the altitudes and managed to reach the top!")
