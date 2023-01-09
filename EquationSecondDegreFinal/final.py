import math


def get_user_input():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    return a, b, c


def equation1(a, b):
    solution = (-b) / a

    print("Equation du premier degre avec la solution: ", solution)


def equation2(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("PAS DE NOMBRE REELLE")

    elif delta == 0:
        solution = (-b) / (2 * a)
        print("Le resultat est:", solution)

    else:
        solution1 = ((-b) + math.sqrt(delta)) / (2 * a)
        solution2 = ((-b) - math.sqrt(delta)) / (2 * a)
        print("Les resultat sont: ", solution1, solution2)


a, b, c = get_user_input()

if a == 0:
    equation1(b, c)
else:
    equation2(a, b, c)
