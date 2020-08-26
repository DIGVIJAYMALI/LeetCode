'''

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]
Output:
[
    [0,0,0],
    [1,0,1],
    [0,1,1],
    [0,1,0]
]
'''



class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        from collections import Counter
        m = len(board)
        n = len(board[0])
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        # to make a board using [[cols] rows]
        life = [[None for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                life[i][j] = 'live' if board[i][j] == 1 else 'die'

        for i in range(m):
            for j in range(n):
                cell = board[i][j]

                # GET NEIGHBORS WITH VALID BOUNDRY CONDITIONS
                neighbors = [board[i+move[0]][j+move[1]] for move in moves if 0 <= i+move[0] < m and 0 <= j + move[1] < n]
                c = Counter(neighbors)

                # IF THE CELL IS LIVING
                if cell == 1:

                    # LIVE CELL WILL DIE IF NUMBER OF NEIGHBORS ARE LESS THAN 2
                    if c[1] < 2:
                        life[i][j] = 'die'

                    # CELL WILL KEEP ON LIVING IF NEIGBORS ARE 2 OR 3
                    elif c[1] in [2, 3]:
                        life[i][j] = 'live'

                    # CELL WILL DIE WITH OVERPOPULATION
                    elif c[1] > 3:
                        life[i][j] = 'die'

                # IF THE CELL IS DEAD
                else:
                    # MAKE IT LIVE WITH EXACT 3 NEIGHBORS
                    if c[1] == 3:
                        life[i][j] = 'live'

        # MODIFY ORIGINAL BOARD
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if life[i][j] == 'live' else 0
        print(board)





