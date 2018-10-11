def paths(n,m):
    matrix=[[0 for j in range(m)] for i in range(n)]
    #if n==1 or m==1:
    #    return 1

    for i in range(n):
        matrix[i][0]=1
    for j in range(m):
        matrix[n-1][j]=1

    for i in range(n-2,-1,-1):
        for j in range(1,m):
            matrix[i][j]=matrix[i+1][j]+matrix[i][j-1]

    return matrix[0][m-1]


print paths(5,3)