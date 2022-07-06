def SQUARE_MATRIX_MULTIPLY(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for  i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]=C[i][j]+A[i][k]*B[k][j]
    return C

#below from https://www.freesion.com/article/71351270819/
def square_matrix_multiply_recursive(A,B):
    n = len(A)
    C = [[0 for col in range(n)] for row in range(n)]
    if n == 1:
        C[0][0] = A[0][0]*B[0][0]
    else:
        (A11,A12,A21,A22) = partition_matrix(A)
        (B11,B12,B21,B22) = partition_matrix(B)
        (C11,C12,C21,C22) = partition_matrix(C)
        C11 = add_matrix(square_matrix_multiply_recursive(A11,B11),square_matrix_multiply_recursive(A12,B21))
        C12 = add_matrix(square_matrix_multiply_recursive(A11,B12),square_matrix_multiply_recursive(A12,B22))
        C21 = add_matrix(square_matrix_multiply_recursive(A21,B11),square_matrix_multiply_recursive(A22,B21))
        C22 = add_matrix(square_matrix_multiply_recursive(A21,B12),square_matrix_multiply_recursive(A22,B22))
        C = merge_matrix(C11,C12,C21,C22)
    return C
 
 
 
def partition_matrix(A):
    n = len(A)
    n2 =  int(n/2)
    A11 = [[0 for col in range(n2)] for row in range(n2)]
    A12 = [[0 for col in range(n2)] for row in range(n2)]
    A21 = [[0 for col in range(n2)] for row in range(n2)]
    A22 = [[0 for col in range(n2)] for row in range(n2)]
    for i in range(0,n2):
        for j in range(0,n2):
            A11[i][j] = A[i][j]
            A12[i][j] = A[i][j+n2]
            A21[i][j] = A[i+n2][j]
            A22[i][j] = A[i+n2][j+n2]
    return (A11,A12,A21,A22)
    
def merge_matrix(A11,A12,A21,A22):
    n2 = len(A11)
    n = 2*n2
    A = [[0 for col in range(n)] for row in range(n)]
    for i in range (0,n):
        for j in range (0,n):
            if i <= (n2-1) and j <= (n2-1):
                A[i][j] = A11[i][j]
                
            elif i <= (n2-1) and j > (n2-1):
                     A[i][j] = A12[i][j-n2]
            elif i > (n2-1) and j <= (n2-1):
                     A[i][j] = A21[i-n2][j]
            else:
                     A[i][j] = A22[i-n2][j-n2]
    return A
                     
 
def add_matrix(A,B):
    n = len(A)
    C = [[0 for col in range(n)] for row in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            C[i][j] = A[i][j]+B[i][j]
    return C