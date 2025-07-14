N=int(input())
chessBoard = [[0 for _ in range(N)] for _ in range(N)]


def isAttacking(i,j):
    for a in range(0,N):
        if chessBoard[a][j]==1 or chessBoard[i][a]==1:
            return True
        
    for a in range(0,N):
        for b in range(0,N):
            if (a+b==i+j or a-b==i-j):
                if chessBoard[a][b]==1:
                    return True
    return False

def nqueens(n):
    if n==0:
        return True
    
    for i in range(0,N):
        for j in range(N):
            if( not isAttacking(i,j) and chessBoard[i][j]!=1):
                    chessBoard[i][j]=1
                    if nqueens(n-1)==True:
                        return True
                    chessBoard[i][j]=0

    return False

print(nqueens(N))