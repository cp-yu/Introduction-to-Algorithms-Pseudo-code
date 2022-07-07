import random


def QUICK_SORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)
        QUICK_SORT(A, p, q - 1)
        QUICK_SORT(A, q + 1, r)
    return A


def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def RANDOMIZED_PARTITION(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return PARTITION(A, p, r)


def RANDOMIZED_QUICK_SORT(A, p, r):
    if p < r:
        q = RANDOMIZED_PARTITION(A, p, r)
        RANDOMIZED_QUICK_SORT(A, p, q - 1)
        RANDOMIZED_QUICK_SORT(A, p + 1, r)
        return A