#CALCULATION OF BINOMIAL COEFFICIENT USING DYNAMIC PROGRAMMING
# TOP DOWN APPROACH : BECAUSE WE ARE USING MEMOIZATION INSTEAD OF CREATING THE ENTIRE TABLE AND CALCULATING ALL THE VALUES FROM THE TABLE.



def binomial(n,k):
    A = {}
    if k==0:
        A[0] = 1
        return 1
    if k==1:
        A[1] = n
        return n
    if k not in A:
        A[k] = binomial(n,k - 1) * (n-k+1)/k


    return  A[k]

print binomial(10,5)