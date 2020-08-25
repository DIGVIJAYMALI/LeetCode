

def No_Of_Inversions(B):
    inv_count = 0
    for i in range(len(B)-1):
        for j in range(i+1, len(B)):
            if (B[i] > B[j]) and B[i] != 0 and B[j] != 0:
                inv_count += 1

    return inv_count

'''
int findXPosition(int puzzle[N][N]) 
{ 
    // start from bottom-right corner of matrix 
    for (int i = N - 1; i >= 0; i--) 
        for (int j = N - 1; j >= 0; j--) 
            if (puzzle[i][j] == 0) 
                return N - i; 
} 

'''
def Find_Pos_X(A):

    for i in range(len(A)-1,-1,-1):
        for j in range(len(A)-1,-1,-1):
            print("A[i][j]",A[i][j])
            if A[i][j] == 0:
                # manhattan distance
                return abs(len(A)-1-i) + abs(len(A)-1-j)



A =  [
    [6,13,7,10],
    [8,9,11,0],
    [15,2,12,5],
    [14,3,1,4]
]
B = []
for i in A:
    for j in i:
        B.append(j)
inversions = No_Of_Inversions(B)
print("inversion :",inversions)
position_X = Find_Pos_X(A)
print("position_X :",position_X)
X = inversions % 2
Y = position_X % 2
if X == Y:
    print("__SOLVABLE__")
else:
    print("__NOT SOLVABLE__")
