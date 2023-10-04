def solution(pegs):
    if len(pegs) < 2:
        return (-1, -1)

    ak = 0
    flipper = -1
    max_even, min_odd = -float("inf"), float("inf")

    for i in range(len(pegs) - 1):
        delta = pegs[i + 1] - pegs[i]
        ak -= flipper * delta
        flipper *= -1
        if i % 2 == 0:
            min_odd = min(min_odd, a_n)
        else:
            max_even = max(max_even, a_n)

    numerator, denominator = 2 * ak, abs(1 + 2 * flipper)

    if numerator < denominator * (max_even + 1) or numerator > denominator * (min_odd - 1):
        return (-1, -1)

    if pm_one == 1 and numerator % 3 == 0:
        numerator /= 3
        denominator = 1

    return (numerator, denominator)
