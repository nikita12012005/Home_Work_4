


def display_box(width: int, height: int, character: str = "*"):
    print(character * width)


    for _ in range(height - 2):
        print(character + " " * (width - 2) + character)


    if height > 1:
        print(character * width)
display_box(10, 9, 'x')

