"""
Vacuum Cleaner Environment
"""
import numpy as np
import copy
from search import BreadthFirstSearch, UniformCostSearch


class VacuumEnvironment(object):
    def __init__(self, size=(4, 4), dirt=0.25):
        self.size = size
        self.dirt = dirt

        # Layer 0: dirt, layer 1: objects/home, 2: agent position and direction (0-up, 1-right, 2-down, 3-left)
        self.room = np.zeros((3, self.size[0], self.size[1]))

        for row in range(self.size[0]):
            for col in range(self.size[1]):
                if np.random.uniform() < self.dirt:
                    self.room[0][row][col] = 1

        # Set home base
        home_x = np.random.randint(self.size[0])
        home_y = np.random.randint(self.size[1])
        self.room[1][home_x][home_y] = 1

        self.room[2].fill(-1)
        self.room[2][home_x][home_y] = np.random.randint(4)  # Place agent on home square facing random direction

    @staticmethod
    def goal_test(node):
        # Last action must be switch off

        if node.operator != 4:
            return False

        if np.sum(node.state[0]) == 0:
            home_loc = np.where(node.state[1] == 1)
            agent_loc = np.where(node.state[2] > 0)

            if home_loc == agent_loc:
                return True

        return False


def expand_node(node):
    def has_hit_obstacle(state):
        if (facing == 0 and agent_x == 0) or \
                (facing == 1 and agent_y == len(state[0][1]) - 1) or \
                (facing == 2 and agent_x == len(state[0][0]) - 1) or \
                (facing == 3 and agent_y == 0):
            return True

        return False

    def move_forward(state):
        """
        Updates agents position
        :return: Whether agent hit obstacle
        """

        if has_hit_obstacle(state):
            return state

        if facing == 0:
            state[2][agent_x][agent_y] = -1
            state[2][agent_x - 1][agent_y] = facing

        elif facing == 1:
            state[2][agent_x][agent_y] = -1
            state[2][agent_x][agent_y + 1] = facing

        elif facing == 2:
            state[2][agent_x][agent_y] = -1
            state[2][agent_x + 1][agent_y] = facing

        elif facing == 3:
            state[2][agent_x][agent_y] = -1
            state[2][agent_x][agent_y - 1] = facing

        return state

    def take_action(state, action):
        cost = 101  # Default -1 for each action taken

        if action == 0:
            state = move_forward(state)

        elif action == 1:
            state[2][agent_x][agent_y] = (state[2][agent_x][agent_y] + 1) % 4

        elif action == 2:
            state[2][agent_x][agent_y] = (state[2][agent_x][agent_y] - 1) % 4

        elif action == 3:
            # Reward of +100 for sucking up dirt
            if state[0][agent_x][agent_y] == 1:
                state[0][agent_x][agent_y] = 0

        elif action == 4:
            # If not on home base when switching off give reward of -1000
            if state[1][agent_x][agent_y] != 1:
                cost = 1100

        return state, cost

    # Switch Off stops sequence
    if node.operator == 4:
        return []

    agent_x, agent_y = np.where(node.state[2] >= 0)
    agent_x = agent_x[0]
    agent_y = agent_y[0]

    facing = node.state[2][agent_x][agent_y]

    expanded_nodes = []

    for a in range(5):
        new_node = copy.copy(node)
        new_node.parent = node
        new_node.depth = node.depth + 1
        new_state, action_cost = take_action(copy.copy(node.state), a)
        new_node.state = new_state
        new_node.operator = a
        new_node.path_cost = node.path_cost + action_cost
        expanded_nodes.append(new_node)

        # print new_node.operator
        # print new_node.state_hash

    return expanded_nodes


def make_3x3():
    env = VacuumEnvironment((3, 3), 0)
    env.room = np.array([[[1, 0, 0], [0, 1, 0], [0, 0, 0]], [[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, -1, -1], [-1, -1, -1], [-1, -1, -1]]])
    return env


def make_random_3x3():
    env = VacuumEnvironment((3, 3), 0.2)
    env.room[1] = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]  # Set start facing right in top corner
    env.room[2] = [[1, -1, -1], [-1, -1, -1], [-1, -1, -1]]  # Set home as top right
    return env


def main():
    env = VacuumEnvironment((3, 3), 1)
    search = BreadthFirstSearch(env.room, expand_node, env.goal_test)

    print env.room

    solution, node = search.find_path(search_cost=0)

    if solution is False:
        print "No Solution Found"

    else:
        print "FOUND SOLUTION"
        print node.state
        print node.path_cost, node.depth
        print solution


if __name__ == "__main__":
    main()
