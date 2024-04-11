def reset_col(size, command):
    if command == "left":
        return size - 1
    return 0


def reset_row(size, command):
    if command == "up":
        return size - 1
    return 0


def move_is_out_of_area(size, pos_row, pos_col, command):
    if (command == "up" and pos_row == 0) or \
            (command == "down" and pos_row == size - 1) or \
            (command == "left" and pos_col == 0) or \
            (command == "right" and pos_col == size - 1):
        return True
    return False


def main():
    size = int(input())

    area = [[""] * size for _ in range(size)]

    pos_row = -1
    pos_col = -1

    fish_quantity = 0

    for i in range(size):
        new_row = input()
        for j in range(size):
            if new_row[j] == "S":
                pos_row = i
                pos_col = j
                area[i][j] = "-"
                continue
            area[i][j] = new_row[j]

    while True:
        command = input()
        if command == "collect the nets":
            break

        if move_is_out_of_area(size, pos_row, pos_col, command):
            if command == "up" or command == "down":
                pos_row = reset_row(size, command)
            if command == "left" or command == "right":
                pos_col = reset_col(size, command)
        else:
            if command == "up":
                pos_row -= 1
            elif command == "down":
                pos_row += 1
            elif command == "left":
                pos_col -= 1
            else:
                pos_col += 1

        if area[pos_row][pos_col].isdigit():
            fish_quantity += int(area[pos_row][pos_col])
            area[pos_row][pos_col] = "-"
        elif area[pos_row][pos_col] == "W":
            print(
                f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{pos_row},{pos_col}]")
            exit(0)

    if fish_quantity >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(
            f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_quantity} tons of fish more.")

    if fish_quantity > 0:
        print(f"Amount of fish caught: {fish_quantity} tons.")

    area[pos_row][pos_col] = "S"

    for i in range(size):
        for j in range(size):
            print(area[i][j], end='')
        print()


if __name__ == "__main__":
    main()
