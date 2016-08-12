from search import BreadthFirstSearch, DepthLimitedSearch, Node, IterativeDeepeningSearch
from copy import deepcopy


class Link(object):
    def __init__(self, l_id, left=None, right=None):
        self.id = l_id
        self.left = False
        self.right = False

        self.attach_left(left)
        self.attach_right(right)

    def __str__(self):
        return str(self.left.id if self.left is not None else None) + "<-" + str(self.id) + "->" + str(self.right.id if self.right is not None else None)

    def open_left(self):
        if self.left is not None:
            self.left.right = None

        self.left = None

    def open_right(self):
        if self.right is not None:
            self.right.left = None

        self.right = None

    def attach_left(self, link):
        self.left = link

        if link is not None:
            link.right = self

    def attach_right(self, link):
        self.right = link

        if link is not None:
            link.left = self


class ChainProblem(object):
    def __init__(self, n_chains, chain_length):
        self.n_chains = n_chains
        self.chain_length = chain_length

        self.chains = []

        l_id = 0
        for n in range(self.n_chains):
            self.chains.append(Link(l_id))
            l_id += 1

            for c in range(self.chain_length - 1):
                self.chains.append(Link(l_id, self.chains[l_id-1], None))
                l_id += 1

    @staticmethod
    def goal_test(node):

        # print [str(n) for n in node.state]

        try:
            l = [link.left.id for link in node.state]
            r = [link.right.id for link in node.state]

            if set(r) != set(l) or len(r) != len(node.state):
                return False
        except:
            return False

        connected = []
        n = node.state[0]
        for i in range(len(node.state)):
            connected.append(n.id)
            n = node.state[n.right.id]

        if connected == range(len(node.state)):
            return True

        return False

    def display(self):
        return [str(link) for link in self.chains]


def expand_node(node):

    expanded_nodes = []

    def copy_node(n):
        return Node(parent=n, state=deepcopy(n.state), operator=None, depth=n.depth+1, path_cost=n.path_cost+1)

    for i, link in enumerate(node.state):
        # for each node can open side if side not already open
        if link.left is not None:
            new_node = copy_node(node)
            new_node.state[i].open_left()
            new_node.operator = "Open left for node " + str(node.state[i].id)
            expanded_nodes.append(new_node)

        if link.right is not None:
            new_node = copy_node(node)
            new_node.state[i].open_right()
            new_node.operator = "Open right for node " + str(node.state[i].id)
            expanded_nodes.append(new_node)

        # for each node can close side on other node with an open side
        if link.left is None:
            open_right = [op_r for op_r in node.state if op_r.right is None and op_r is not link]
            for or_n in open_right:
                new_node = copy_node(node)
                new_node.state[i].attach_left(new_node.state[or_n.id])
                new_node.operator = "Attach left of node " + str(node.state[i].id) + " to " + str(or_n.id)
                expanded_nodes.append(new_node)

            open_left = [op_l for op_l in node.state if op_l.left is None and op_l is not link]
            for ol_n in open_left:
                new_node = copy_node(node)
                new_node.state[i].attach_right(new_node.state[ol_n.id])
                new_node.operator = "Attach right of node " + str(node.state[i].id) + " to " + str(ol_n.id)
                expanded_nodes.append(new_node)

    for en in expanded_nodes:
        en.parent = node
        en.depth = node.depth + 1
        en.path_cost = node.path_cost + 1

    return expanded_nodes


def main():
    env = ChainProblem(2, 3)
    print env.display()
    search = BreadthFirstSearch(env.chains, expand_node, env.goal_test)
    search = IterativeDeepeningSearch(env.chains, expand_node, env.goal_test, 4, 6)
    solution, goal_state = search.find_path()

    if solution is not False:
        print solution
        print goal_state
    else:
        print "NO SOLUTION FOUND"

if __name__ == "__main__":
    main()

