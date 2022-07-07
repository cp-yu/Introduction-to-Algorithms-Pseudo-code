def MAX_HEAPIFY(A, i, heapsize):
    l = LFET(i)
    r = RIGHT(i)
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A, largest, heapsize)


def MAX_HEAPIFY_LOOP(A, i, heapsize):
    while True:
        l = LFET(i)
        r = RIGHT(i)
        if l < heapsize and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < heapsize and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i = largest
        else:
            break


def MIN_HEAPIFY(A, i, heapsize):
    l = LFET(i)
    r = RIGHT(i)
    if l < heapsize and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < heapsize and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        MAX_HEAPIFY(A, smallest, heapsize)


def BUILD_MAX_HEAP(A):
    heapsize = len(A)
    for i in range((heapsize - 1) // 2, -1, -1):
        MAX_HEAPIFY_LOOP(A, i, heapsize)
    return heapsize


def HEAPSORT(A):
    heapsize = BUILD_MAX_HEAP(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize = heapsize - 1
        MAX_HEAPIFY(A, 0, heapsize)
    return A


def LFET(i):
    return 2 * i + 1


def RIGHT(i):
    return 2 * i + 2


def PARENT(i):
    return i // 2