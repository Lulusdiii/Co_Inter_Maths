import math

def resol_eq_second_degre(a, b, c):
    if a == 0:
        return "erreur", "Ce n'est pas une équation du second degré"

    delta = b**2 - 4 * a * c

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return 2, [x1, x2]

    elif delta == 0:
        x0 = -b / (2 * a)
        return 1, [x0]

    else:
        return 0, []