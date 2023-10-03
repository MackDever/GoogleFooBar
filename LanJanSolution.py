def solution(x):
    l = len(x)
    final = []
    for i in range(l):
        c = x[i]
        if 'a' <= c <= 'z':
            pos = ord(c) - ord('a')
            final.append(chr(ord('a') + 25 - pos))
        else:
            final.append(c)
    return ''.join(final)
