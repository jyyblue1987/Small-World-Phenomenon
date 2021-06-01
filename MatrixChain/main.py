def printMatrix(m):
    for row in m:
        print(row)

def parenStr(track, row, col):
    n = len(track)
    
    pos = track[row][col]
    if pos < 0 or row == col:
        return "(A" + str(row) + ")"

    if row == 0 and col == n - 1:
        return parenStr(track, row, pos) + parenStr(track, pos + 1, col)
    else:
        return "(" + parenStr(track, row, pos) + parenStr(track, pos + 1, col) + ")" 



def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]
    track = [[-1 for i in range(n)] for j in range(n)]
    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0

    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1): 
        for i in range(n+1-chainLength):
            j = i + chainLength - 1
            # Fill in m[i][j] with the best of the recursive options
            m[i][j] = float("inf")
            for k in range(i,j):
                # Two previous table values plus
                # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    track[i][j] = k

    printMatrix(m)
    printMatrix(track)

    print(parenStr(track, 0, n - 1))
    return m[0][n-1]

dims = [30,35,15,5,10,20,25]
print(chainMatrix(dims))


# dims = [40, 20, 30, 10, 30]
# print(chainMatrix(dims))


dims = [4, 10, 3, 12, 20, 7]
print(chainMatrix(dims))