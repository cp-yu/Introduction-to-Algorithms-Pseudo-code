def MERGE(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(n1):
        L[i]=A[p+i]
    for i in range(n2):
        R[i]=A[q+i+1]
    L[n1]=float("inf")
    R[n2]=float("inf")
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
    return A

def MERGE_SORT(A,p,r):
    if p<r:
        q=(p+r)//2
        A=MERGE_SORT(A,p,q)
        A=MERGE_SORT(A,q+1,r)
        A=MERGE(A,p,q,r)
    return A

# A=MERGE_SORT(A,0,len(A)-1)