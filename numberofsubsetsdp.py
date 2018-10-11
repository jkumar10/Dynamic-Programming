def subsets(n):
    matrix = [[0 for x in range(n+1)] for y in range(n+1)]
    matrix[0][0]=1
    for i in range(1,n+1):
        matrix[i][0]=matrix[i-1][i-1]
        for j in range(1,i+1):
            matrix[i][j]=matrix[i][j-1]+matrix[i-1][j-1]
    return (matrix[n][0])


print subsets(5)