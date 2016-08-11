import numpy as np
import copy
from search import BreadthFirstSearch, BidirectionalSearch
from immediate_search import BreadthFirstSearchImmediateCheck


class MissionaryCannibalEnv(object):
    """
    Three missionaries and cannibals need to cross a river with a boat only big enough for two of them

    Rules:
     - At no points can a member of one group be alone with more than one member of the other group
     - Maximum two people can be transferred by the boat at any point in time
     - Boat cannot switch banks without someone in it
    """
    def __init__(self):
        self.initial_state = np.array([[3, 3, 1], [0, 0, 0]])    # Missionaries, cannibals, and boat on each bank

    @staticmethod
    def is_goal_state(node):
        if node.state[1][0] == 3 and node.state[1][1] == 3:
            return True

        return False

    @staticmethod
    def expand_node(node):
        """
        Returns a list of possible states to reach from the provided node
        """

        bank = int(node.state[0][2] != 1)  # 1 means boat on the starting bank, 0 means on the finishing bank

        expanded = []  # Holds the actions that are allowed
        if node.state[bank][0] >= 1:
            expanded.append((1, 0))
        if node.state[bank][1] >= 1:
            expanded.append((0, 1))
        if node.state[bank][0] >= 2:
            expanded.append((2, 0))
        if node.state[bank][1] >= 2:
            expanded.append((0, 2))
        if node.state[bank][0] >= 1 and node.state[bank][1] >= 1:
            expanded.append((1, 1))

        new_nodes = []

        for operator in expanded:
            n = copy.deepcopy(node)

            n.parent = node
            n.depth = node.depth + 1
            n.path_cost = node.path_cost + 1

            # Swap boat banks
            n.state[bank][2] = 0
            n.state[1 - bank][2] = 1

            n.state[bank][0] -= operator[0]
            n.state[1 - bank][0] += operator[0]

            n.state[bank][1] -= operator[1]
            n.state[1 - bank][1] += operator[1]

            add_node = True

            # Check for only adding valid states
            for bank_side in n.state:
                if (bank_side[0] == 1 and bank_side[1] > 1) or (bank_side[1] == 1 and bank_side[0] > 1):
                    add_node = False

            if add_node:
                new_nodes.append(n)

        return new_nodes


def main():
    env = MissionaryCannibalEnv()
    goal_state = np.array([[0, 0, 0], [3, 3, 1]])
    search = BidirectionalSearch(env.initial_state, goal_state, env.expand_node)

    path = search.find_path()

    if path is False:
        print "No solution possible"
    else:
        print "Solution found that achieves: ", path.state

if __name__ == "__main__":
    main()
