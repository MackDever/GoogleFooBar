# https://gist.github.com/algomaster99/782b898177ca37bfbf955cec416bb6a4?permalink_comment_id=3827248#gistcomment-3827248
# The most efficient solution I was able to find, I cleaned up the detect_states function

import numpy as np

# returns active / terminal states
def detect_states(matrix):
    active = [i for i, row in enumerate(matrix) if np.any(row)]
    terminal = [i for i, row in enumerate(matrix) if not np.any(row)]
    return active, terminal
  
# converts array elements to simplest form
def simplest_form(B):
    B = B.round().astype(int).A1
    gcd = np.gcd.reduce(B)
    B = np.append(B, B.sum()) / gcd                     
    return B.astype(int)

# calculates absorbing probabilities
def solution(m):
    active, terminal = detect_states(m)
    # if s0 is terminal
    if 0 in terminal:                              
        return [1] + [0]*len(terminal[1:]) + [1]
    m = np.matrix(m, dtype=float)[active, :]       # list --> np.matrix (active states only)
    comm_denom = np.prod(m.sum(1))                 # product of sum of all active rows (used later)
    P = m / m.sum(1)                               # divide by sum of row to convert to probability matrix
    Q, R = P[:, active], P[:, terminal]            # separate Q & R
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)                            # calc fundamental matrix
    B = N[0] * R * comm_denom / np.linalg.det(N)   # get absorbing probs & get them close to some integer
    return simplest_form(B)
