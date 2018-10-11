def lcsdp(X,Y):
    l1=len(X)
    l2=len(Y)
    maxsequence=[]
    matrix =[[0 for j in range(l2+1)] for i in range(l1+1)]

    # BUILDING THE TABLE
    for i in range(l1+1):
        for j in range(l2+1):
            if i==0 or j==0:
                matrix[i][j]=0
            elif X[i-1]==Y[j-1]:
                matrix[i][j]=matrix[i-1][j-1]+1
            else:
                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])

    # PRINTING THE LONGEST COMMON SUBSEQUENCE
    i=l1
    j=l2
    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            maxsequence.append(X[i-1])
            i=i-1
            j=j-1

        elif matrix[i][j-1]>matrix[i-1][j]:
            j=j-1
        elif matrix[i][j-1]<matrix[i-1][j]:
            i=i-1
        elif matrix[i][j-1]==matrix[i-1][j]:
            i=i-1

    for i in range((len(maxsequence))-1,-1,-1):
        print maxsequence[i],




lcsdp("abcdefgh","adgh")