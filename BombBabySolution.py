# the easiest one so far? not complaining lol

def solution(M, F):
    m, f = int(M), int(F)
    generations = 0

    while m > 1 or f > 1:
        if m <= 0 or f <= 0:
            return "impossible"

        if m == 1 and f != 1:
            generations += f - 1
            break
        elif f == 1 and m != 1:
            generations += m - 1
            break

        if m > f:
            generations += m // f
            m %= f
        else:
            generations += f // m
            f %= m

    return str(generations)
