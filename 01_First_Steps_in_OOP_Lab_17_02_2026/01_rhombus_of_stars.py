def print_line(size: int, stars: int):
    print(" " * (size - stars) + "* " * stars)

def print_lines_up(size: int):
    for row in range(1, size):
        print_line(size, row)

def print_lines_down(size: int):
    for row in range(size, 0, -1):
        print_line(size, row)

def print_rhombus(size: int):
    print_lines_up(size)
    print_lines_down(size)


n = int(input())

print_rhombus(n)