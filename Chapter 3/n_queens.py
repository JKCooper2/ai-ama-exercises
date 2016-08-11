import numpy as np
import copy

from search import BreadthFirstSearch, DepthFirstSearch


class NQueens(object):
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size))

    @property
    def t_board(self):
        # Transpose of board for simpler testing
        return np.transpose(self.board)

    @property
    def f_board(self):
        # Flips LR for simpler diagonal testing
        return np.fliplr(self.board)

    def place_queen(self, x, y):
        self.board[x][y] = 1

    def can_place_queen(self, x, y):
        if self.board[x][y] != 0:
            raise ValueError("Position already contains a queen")

        self.board[x][y] = 1

        if not self.is_position_valid():
            self.board[x][y] = 0
            return False

        self.board[x][y] = 0
        return True

    def is_position_valid(self):

        # Check rows and columns
        for row in self.board:
            if sum(row) > 1:
                return False

        for col in self.t_board:
            if sum(col) > 1:
                return False

        # Check diagonals
        for i in range(-7, 7):
            if sum(self.board.diagonal(i)) > 1:
                return False

            if sum(self.f_board.diagonal(i)) > 1:
                return False

        return True

    def num_attackers(self, x, y):
        point = self.board[x][y]
        row = sum(self.board[x]) - point
        col = sum(self.t_board[y]) - point
        diag1 = sum(self.board.diagonal(x-y)) - point
        diag2 = sum(self.f_board.diagonal(self.size-x-y-1)) - point

        return row + col + diag1 + diag2

    @staticmethod
    def goal_test(node):
        board = node.state
        t_board = np.transpose(board)
        f_board = np.fliplr(board)

        def is_position_valid():
            # Check rows and columns
            for v_row in board:
                if sum(v_row) > 1:
                    return False

            for v_col in t_board:
                if sum(v_col) > 1:
                    return False

            # Check diagonals
            for i in range(-(len(board)-1), (len(board)-1)):
                if sum(board.diagonal(i)) > 1:
                    return False

                if sum(f_board.diagonal(i)) > 1:
                    return False

            return True

        print np.sum(board)

        # if np.sum(board) == len(board)-1:
        #     print board

        if is_position_valid() and np.sum(board) == len(board):
            return True

        return False


# OPERATOR
def most_constrained_variable(node):
    board = node.state
    t_board = np.transpose(board)
    f_board = np.fliplr(board)

    def num_attackers(a_x, a_y):
        point = board[a_x][a_y]
        a_row = sum(board[a_x]) - point
        a_col = sum(t_board[a_y]) - point
        a_diag1 = sum(board.diagonal(a_y - a_x)) - point
        a_diag2 = sum(f_board.diagonal(len(board) - a_x - a_y - 1)) - point

        return a_row + a_col + a_diag1 + a_diag2

    def is_position_valid():
        # Check rows and columns
        for v_row in board:
            if sum(v_row) > 1:
                return False

        for v_col in t_board:
            if sum(v_col) > 1:
                return False

        # Check diagonals
        for i in range(-(len(board)-1), (len(board)-1)):
            if sum(board.diagonal(i)) > 1:
                return False

            if sum(f_board.diagonal(i)) > 1:
                return False

        return True

    def can_place_queen(a_x, a_y):
        if board[a_x][a_y] != 0:
            raise ValueError("Position already contains a queen")

        board[a_x][a_y] = 1

        if not is_position_valid():
            board[a_x][a_y] = 0
            return False

        board[a_x][a_y] = 0
        return True

    least_attacked_cols = []
    times_attacked = None

    for y, col in enumerate(t_board):
        ta = sum(col)
        if times_attacked is None or ta < times_attacked:
            times_attacked = ta
            least_attacked_cols = [y]

        elif ta == times_attacked:
            least_attacked_cols.append(y)

    available_positions = []

    for row in range(len(board)):
        for col in least_attacked_cols:
            if num_attackers(row, col) == 0:
                if can_place_queen(row, col):
                    new_node = copy.deepcopy(node)
                    new_node.state[row][col] = 1
                    new_node.parent = node
                    new_node.depth = node.depth + 1
                    new_node.path_cost = node.path_cost + 1

                    available_positions.append(new_node)

    return available_positions


def main():
    size = 8
    puzzle = NQueens(size)

    search = DepthFirstSearch(puzzle.board, most_constrained_variable, puzzle.goal_test)

    path = search.find_path()

    if path is not False:
        print path.state
    else:
        print "NO SOLUTION FOUND"

if __name__ == "__main__":
    main()