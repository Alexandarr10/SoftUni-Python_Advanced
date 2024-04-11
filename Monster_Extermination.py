from collections import deque

total_kills = 0


monster_armor = deque([int(el) for el in input().split(",")])
soldiers_strikes = deque([int(el) for el in input().split(",")])


while monster_armor and soldiers_strikes:
    current_monster_defence = monster_armor.popleft()
    current_soldier_power = soldiers_strikes.pop()

    if current_soldier_power >= current_monster_defence:
        total_kills += 1
        current_soldier_power -= current_monster_defence
        if not soldiers_strikes and current_soldier_power > 0:
            soldiers_strikes.append(current_soldier_power)
        elif soldiers_strikes:
            soldiers_strikes[-1] += current_soldier_power
    else:
        current_monster_defence -= current_soldier_power
        monster_armor.append(current_monster_defence)

if not monster_armor:
    print(f"All monsters have been killed!")
if not soldiers_strikes:
    print(f"The soldier has been defeated.")

print(f"Total monsters killed: {total_kills}")

