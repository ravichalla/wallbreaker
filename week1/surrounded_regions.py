import  collections

# BFS
def solve(self, board):
    if not board:
        return
    r, c = len(board), len(board[0])
    for i in range(r):
        self.bfs(board, i, 0);
        self.bfs(board, i, c - 1)
    for j in range(1, c - 1):
        self.bfs(board, 0, j);
        self.bfs(board, r - 1, j)
    # recover the board at second time
    for i in range(r):
        for j in range(c):
            if board[i][j] == "D":
                board[i][j] = "O"
            else:
                board[i][j] = "X"


def bfs(self, board, i, j):
    queue = collections.deque()
    if board[i][j] == "O":
        queue.append((i, j));
        board[i][j] = "D"
    while queue:
        r, c = queue.popleft()
        if r > 0 and board[r - 1][c] == "O":  # up
            queue.append((r - 1, c));
            board[r - 1][c] = "D"
        if r < len(board) - 1 and board[r + 1][c] == "O":  # down
            queue.append((r + 1, c));
            board[r + 1][c] = "D"
        if c > 0 and board[r][c - 1] == "O":  # left
            queue.append((r, c - 1));
            board[r][c - 1] = "D"
        if c < len(board[0]) - 1 and board[r][c + 1] == "O":  # right
            queue.append((r, c + 1));
            board[r][c + 1] = "D"


'''
Ideas/thoughts:

Any o on border are not flipped to x.
and any o not on border and connected to some o will be flipped.
And correpsonding movement up,left,right,down

'''