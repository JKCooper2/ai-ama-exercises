import numpy as np
import matplotlib.pyplot as plt
import copy

from mst import compute_mst, mst_distance
from informed_search import AStarSearch


# Structure to make MST simpler
class Point(object):
    def __init__(self, i, x, y):
        self.index = i
        self.x = x
        self.y = y
        self.d = 0
        self.pred = None

    def __str__(self):
        return "{0}: ({1}, {2})".format(self.index, self.x, self.y)


class TravellingSalesman(object):
    def __init__(self, size, points):
        self.size = size
        self.points = points

        points = np.random.uniform(0, self.size, self.points * 2).reshape((self.points, 2))
        self.map = [Point(i, P[0], P[1]) for i, P in enumerate(points)]

        compute_mst(self.map)

        # State is 3 layers array with x pos, y pos, and connected to for each city
        x = [p.x for p in self.map]
        y = [p.y for p in self.map]
        conns = np.full(self.points, -1)

        self.state = np.array([x, y, conns])
        print self.state

    def plot(self, node=None):
        x = [p.x for p in self.map]
        y = [p.y for p in self.map]

        plt.scatter(x, y)

        for p in self.map:
            plt.annotate(p.index, xy=(p.x, p.y), xytext=(-5, -5), textcoords='offset points', ha='right', va='bottom')

            if p.pred is not None:
                plt.plot([p.x, p.pred.x], [p.y, p.pred.y], c='g', linewidth=4)

        for i in range(len(node.state[2])):
            plt.plot([node.state[0][i], node.state[0][node.state[2][i]]], [node.state[1][i], node.state[1][node.state[2][i]]], c='k')

        plt.show()

    @staticmethod
    def mst_cost(state):
        # Points not connected to another city
        remaining_points = [i for i, p in enumerate(state[2]) if p == 0]

        # h(n) is current node path + mst for remaining nodes
        rp = []

        for i in remaining_points:
            rp.append(Point(i, state[0][i], state[1][i]))

        return mst_distance(rp)

    @staticmethod
    def goal_test(node):
        conns = []

        c = node.state[2][0]

        for i in range(len(node.state[2])):
            # Makes list of points connected to the same points as the currently selected one
            indexes = [i for i, x in enumerate(node.state[2]) if x == int(c) and x != -1]

            # Checks current point is only one connected to it's connection (directed graph)
            if len(indexes) > 1:
                return False

            if len(indexes) == 0:
                continue

            conns.append(indexes[0])
            c = node.state[2][c]

        # Is every node connected to every other node once
        if sorted(conns) == range(len(node.state[2])):
            return True

        return False


def expand_node(node):
    def copy_node():
        nn = copy.copy(node)
        nn.parent = node
        nn.depth = node.depth + 1
        nn.state = np.copy(node.state)
        return nn

    expanded_nodes = []

    # Available nodes to connect to (ones that don't have connections yet
    av_i = [i for i, x in enumerate(node.state[2]) if i not in node.state[2]]

    # Each turn a path can be added or modified
    for i in range(len(node.state[2])):
        for j in av_i:
            if i == j:
                continue

            dist = np.sqrt((node.state[0][i] - node.state[0][j]) ** 2 + (node.state[1][i] - node.state[1][j]) ** 2)

            new_node = copy_node()
            new_node.operator = "{0}->{1}".format(i, j)
            new_node.path_cost = node.path_cost + dist
            new_node.state[2][i] = j
            expanded_nodes.append(new_node)

    return expanded_nodes


def main():
    env = TravellingSalesman(10, 5)

    search = AStarSearch(env.state, expand_node, env.goal_test, env.mst_cost)
    solution, node = search.find_path()

    if solution:
        print "FOUND SOLUTION"
        print str(node.total_cost) + ": " + str(solution)
        env.plot(node)

    else:
        print "No Solution Found"

if __name__ == "__main__":
    main()
