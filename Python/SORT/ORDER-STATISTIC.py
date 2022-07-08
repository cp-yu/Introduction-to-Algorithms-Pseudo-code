import random


def MINIMUM(A):
    min = A[0]
    for i in range(1, len(A)):
        if min > A[i]:
            min = A[i]
    return min


def RANDOMIZED_PARTITION(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return PARTITION(A, p, r)


def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def RANDOMIZED_SELECT(A, p, r, i):
    if p == r:
        return A[p]
    q = RANDOMIZED_PARTITION(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return RANDOMIZED_SELECT(A, p, q - 1, i)
    else:
        return RANDOMIZED_SELECT(A, q + 1, r, i - k)