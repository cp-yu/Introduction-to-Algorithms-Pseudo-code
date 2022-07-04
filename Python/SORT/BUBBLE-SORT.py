def BUBBLE_SORT(A):
    for i in range(len(A)-2):
        for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
    return A