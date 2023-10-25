import numpy as np
M=np.random.randint(0,51,50)
M1=M.reshape(5,10)
N=np.random.randint(0,51,50)
M2=N.reshape(10,5)
print(M1,M2)
def Matrix_multip(M1,M2):
    a,b=M1.shape
    b,c=M2.shape
    C=np.zeros((a,c))
    for i in range(a):
        for j in range(c):
            for k in range(b):
                C[i,j]+=M1[i,k]*M2[k,j]
    return C
Matrix_multip(M1, M2)
print(Matrix_multip(M1, M2))