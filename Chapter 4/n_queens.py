import numpy as np
import copy

from iterative_improvement import GradientDescent, SimulatedAnnealing


class NQueens(object):
    def __init__(self, size, initialise=False):
        self.size = size
        self.board = np.zeros((size, size))

        # Randomly initialise queens to positions
        if initialise:
            for i in range(len(self.board)):
                self.board[i][np.random.randint(8)] = 1

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

        if is_position_valid() and np.sum(board) == len(board):
            return True

        return False


def num_attackers(node):
    board = node.state

    t_board = np.transpose(board)
    f_board = np.fliplr(board)

    total_attackers = 0

    q = np.where(board == 1)

    for i in range(len(q[0])):
        a_x = q[0][i]
        a_y = q[1][i]

        point = board[a_x][a_y]
        a_row = sum(board[a_x]) - point
        a_col = sum(t_board[a_y]) - point
        a_diag1 = sum(board.diagonal(a_y - a_x)) - point
        a_diag2 = sum(f_board.diagonal(len(board) - a_x - a_y - 1)) - point

        total_attackers += a_row + a_col + a_diag1 + a_diag2

    return total_attackers


def expand_nodes(node):

    expanded_nodes = []

    for i in range(len(node.state)):
        curr_pos = np.where(node.state[i] == 1)[0][0]

        for j in range(len(node.state[i])):
            if j == curr_pos:
                continue

            new_node = copy.deepcopy(node)
            new_node.state[i].fill(0)
            new_node.state[i][j] = 1
            new_node.depth = node.depth + 1
            new_node.path_cost = node.path_cost + 1
            expanded_nodes.append(new_node)

    return expanded_nodes


def random_move(node):
    row = np.random.randint(len(node.state))

    new_node = copy.deepcopy(node)
    new_node.state[row].fill(0)
    new_node.state[row][np.random.randint(len(node.state[row]))] = 1
    new_node.depth = node.depth + 1
    new_node.path_cost = node.path_cost + 1

    return new_node


def main():
    size = 8
    random_restart = False

    results = []

    for ep in range(100):
        env = NQueens(size, initialise=True)
        ii = GradientDescent(env.board, num_attackers, expand_nodes, env.goal_test)
        # ii = SimulatedAnnealing(env.board, num_attackers, random_move, env.goal_test, temperature=1, alpha=0.90)

        solved = False

        for i in range(100):
            improve = ii.take_step(equal=True)

            if ii.current_best == 0:
                solved = True
                break

            if not improve and random_restart:
                env = NQueens(size, initialise=True)
                ii.random_restart(env.board)

        if solved:
            print str(ep) + " Solved"
            results.append(ii.node.depth)

    print results
    print len(results)
    print sum(results) / float(len(results))


if __name__ == "__main__":
    main()
