# only work in 0~1
def BUCKET_SORT(A):
    n=len(A)
    B=[[] for _ in range(n)]

    for i in range(n):
        B[int(n*A[i])].append(A[i])
    for i in range(n):
        if B[i]:
            B[i].sort()
    C=[]
    for b in B:
        if b:
            C=C+b
    return C