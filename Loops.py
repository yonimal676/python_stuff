def basic() -> None:  # 2 3 4
    for i in range(2, 5):
        print(i, end=" ")


def basic_string() -> None:  # N e v e r   G o n n a   G i v e   Y o u   U p
    for i in "Never Gonna Give You Up":
        print(i, end=" ")


def other_basic() -> None:  # 0 1 2 3 4 5
    for i in range(6):
        print(i, end=" ")


def multiple() -> None:  # 2 5 8 11 14  |  from 2 to 15  -> add 3.
    for i in range(2, 15, 3): \
            print(i, end=" ")


def nested() -> None:
    for i in range(6):
        for j in range(i):
            print(j + 1, end=" ")
        print()


'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''


def for_else() -> None:  # 0 1 2 3 4 5 | Done.

    for i in range(6):
        print(i, end=" ")
    else:
        print("| Done. ")


def for_break() -> None:  # 0 1 2
    for x in range(6):
        if x == 3:
            break
        print(x, end=" ")


def for_pass() -> None:
    pass  # will return nothing




