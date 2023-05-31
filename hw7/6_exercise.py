def min_arrow_rotations(S):
    directions = {'^': 0, 'v': 0, '<': 0, '>': 0}

    for arrow in S:
        directions[arrow] += 1

    max_count = max(directions.values())
    total_arrows = len(S)

    return total_arrows - max_count
print(min_arrow_rotations("^vv<v"))
print(min_arrow_rotations("v>>>vv"))
print(min_arrow_rotations("<<<"))
