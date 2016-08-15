import numpy as np
import copy
from informed_search import AStarSearch

class NPuzzle(object):
    def __init__(self, size):
        self.size = size
        self.puzzle = self.make_puzzle()

    @staticmethod
    def is_solvable(puzzle):
        # Based on http://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable
        inversions = 0

        for i in range(len(puzzle)):
            for j in range(i+1, len(puzzle)):
                if puzzle[i] > puzzle[j] and puzzle[i] != 0 and puzzle[j] != 0:
                    inversions += 1

        return inversions % 2 == 0

    def make_puzzle(self):
        tiles = range(self.size ** 2)  # 0 is blank
        np.random.shuffle(tiles)

        while not self.is_solvable(tiles):
            np.random.shuffle(tiles)

        return np.array(tiles).reshape((self.size, self.size))

    @staticmethod
    def goal_test(node):
        """Copy of misplaced tiles with boolean response"""
        puzzle = node.state
        size = len(puzzle)

        distance = 0

        for i, row in enumerate(puzzle):
            for j, tile in enumerate(row):
                correct_row = np.floor(tile / size) - (1 if tile % size == 0 else 0)
                correct_col = (tile % size - 1) % size

                if tile == 0:
                    correct_row = size - 1
                    correct_col = size - 1

                distance += int((i - correct_row) + (j - correct_col) != 0)

        return distance == 0

    @staticmethod
    def manhattan_distance(puzzle):
        size = len(puzzle)

        distance = 0

        for i, row in enumerate(puzzle):
            for j, tile in enumerate(row):
                correct_row = np.floor(tile / size) - (1 if tile % size == 0 else 0)
                correct_col = (tile % size - 1) % size

                if tile == 0:
                    correct_row = size - 1
                    correct_col = size - 1

                distance += abs(i-correct_row) + abs(j - correct_col)

        return distance

    @staticmethod
    def euclidean_distance(puzzle):
        size = len(puzzle)

        distance = 0

        for i, row in enumerate(puzzle):
            for j, tile in enumerate(row):
                correct_row = np.floor(tile / size) - (1 if tile % size == 0 else 0)
                correct_col = (tile % size - 1) % size

                if tile == 0:
                    correct_row = size - 1
                    correct_col = size - 1

                distance += np.sqrt((i - correct_row)**2 + (j - correct_col)**2)

        return distance

    @staticmethod
    def misplaced_tiles(puzzle):
        size = len(puzzle)

        distance = 0

        for i, row in enumerate(puzzle):
            for j, tile in enumerate(row):
                correct_row = np.floor(tile / size) - (1 if tile % size == 0 else 0)
                correct_col = (tile % size - 1) % size

                if tile == 0:
                    correct_row = size - 1
                    correct_col = size - 1

                distance += int((i - correct_row) + (j - correct_col) != 0)

        return distance

    @staticmethod
    def sequence_score(puzzle):
        def adjacent_tiles(x, y, state):
            atl = []

            # Append adjacent tiles in order U, R, D, L with -1 for walls
            try:
                atl.append(state[x - 1][y])
            except:
                atl.append(-1)
            try:
                atl.append(state[x][y + 1])
            except:
                atl.append(-1)
            try:
                atl.append(state[x + 1][y])
            except:
                atl.append(-1)
            try:
                atl.append(state[x][y - 1])
            except:
                atl.append(-1)

            return atl

        # From http://www.cse.buffalo.edu/~rapaport/572/S02/nilsson.8puzzle.pdf
        size = len(puzzle)

        solution = np.array([range(1, 9) + [0]]).reshape((3, 3))

        if size != 3:
            raise ValueError("Heuristic only valid for 3x3 problems")

        distance = 0

        for i, row in enumerate(puzzle):
            for j, tile in enumerate(row):
                correct_row = np.floor(tile / size) - (1 if tile % size == 0 else 0)
                correct_col = (tile % size - 1) % size

                actual_adjacent_tiles = adjacent_tiles(i, j, puzzle)
                correct_adjacent_tiles = adjacent_tiles(correct_row, correct_col, solution)

                # For each adjacent square (and wall) add 2 points if square is incorrect and not a center piece
                # and 1 point if the square is incorrect and is a center piece
                for at in range(len(actual_adjacent_tiles)):
                    if actual_adjacent_tiles[at] != correct_adjacent_tiles[at]:
                        # If not center. Can be hardcoded because of restricted solution to 3x3
                        if i == 1 and j == 1:
                            distance += 1
                        else:
                            distance += 2

        return distance

    @staticmethod
    def expand_nodes(node):
        def create_new_node():
            nn = copy.copy(node)
            nn.parent = node
            nn.path_cost = node.path_cost + 1
            nn.depth = node.depth + 1
            nn.state = np.copy(node.state)
            return nn

        # 0 can swap with any tile beside it

        e_x, e_y = np.where(node.state == 0)
        e_x = e_x[0]
        e_y = e_y[0]

        size = len(node.state)

        expanded_nodes = []

        if e_x != 0:
            new_node = create_new_node()
            new_node.operator = "U"
            new_node.state[e_x][e_y] = node.state[e_x-1][e_y]
            new_node.state[e_x-1][e_y] = 0
            expanded_nodes.append(new_node)

        if e_x != size - 1:
            new_node = create_new_node()
            new_node.operator = "D"
            new_node.state[e_x][e_y] = node.state[e_x + 1][e_y]
            new_node.state[e_x + 1][e_y] = 0
            expanded_nodes.append(new_node)

        if e_y != 0:
            new_node = create_new_node()
            new_node.operator = "L"
            new_node.state[e_x][e_y] = node.state[e_x][e_y - 1]
            new_node.state[e_x][e_y - 1] = 0
            expanded_nodes.append(new_node)

        if e_y != size - 1:
            new_node = create_new_node()
            new_node.operator = "R"
            new_node.state[e_x][e_y] = node.state[e_x][e_y + 1]
            new_node.state[e_x][e_y + 1] = 0
            expanded_nodes.append(new_node)

        return expanded_nodes


def main():
    env = NPuzzle(3)

    env.puzzle = np.array([[6, 3, 7], [1, 0, 5], [2, 8, 4]])

    print env.puzzle

    print "Manhattan Error: " + str(env.manhattan_distance(env.puzzle))
    print "Euclidean Error: " + str(env.euclidean_distance(env.puzzle))
    print "Misplaced Tiles: " + str(env.misplaced_tiles(env.puzzle))
    print "Sequence Score: " + str(env.sequence_score(env.puzzle))

    search = AStarSearch(env.puzzle, env.expand_nodes, env.goal_test, env.sequence_score)

    solution, node = search.find_path()

    if solution:
        print "FOUND SOLUTION"
        print len(solution), solution
        print node.state

    else:
        print "No solution found"


if __name__ == "__main__":
    main()
