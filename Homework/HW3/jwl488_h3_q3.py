def print_triangle(n):
    if n == 1:
        print("*")
    if n > 1:
        print_triangle(n - 1)
        print(n * "*")


# print_triangle(5)

def print_opposite_triangle(n):
    if n == 1:
        print("*")
        print("*")
    if n > 1:
        print(n * "*")
        print_opposite_triangle(n - 1)
        print(n * "*")


# print_opposite_triangle(5)