from search import BreadthFirstSearch
from copy import copy, deepcopy

STATE = [1, 2, 4, 8, 16]
STATE = [1, 2, 3, 4, 5]
STATE = [0.5, 2, 4.5, 8]


def goal_test(node):
    for i in range(len(STATE)):
        calc = node.state_hash.replace("n", str(i))
        # print str(eval(calc)) + " == " + str(STATE[i]) + ": " + str(eval(calc) == STATE[i])

        # Catches /0
        try:
            if eval(calc) != STATE[i]:
                return False
        except:
            return False

    return True


# Much faster than deepcopy
def copy_node(node):
    new_node = copy(node)
    new_node.state = node.state[:]
    new_node.parent = node
    new_node.path_cost = node.path_cost + 1
    new_node.depth = node.depth + 1

    return new_node


def expand_node(node):
    # To get around initial node issues
    if node.state == [None]:
        n1 = deepcopy(node)
        n1.state = ["1"]

        n2 = deepcopy(node)
        n2.state = ["n"]

        return [n1, n2]

    # Actions = [+, -, *, /, ^] x [1, n] x [) x l]
    # State is a list of actions performed in order

    expanded_nodes = []

    for op in ["+", "-", "*", "/", "**"]:
        for val in ["1", "n"]:
            act = op + val + ")"
            for l in range(len(node.state)):
                new_node = copy_node(node)

                if l == 0:
                    new_node.state[l] = "(" + new_node.state[l]
                else:
                    new_node.state[l] = new_node.state[l][0] + "(" + new_node.state[l][1:]
                new_node.state.append(act)
                expanded_nodes.append(new_node)

    return expanded_nodes


def main():
    search = BreadthFirstSearch([None], expand_node, goal_test)

    solution, state = search.find_path()

    if solution is not False and solution is not None:
        # print solution Operators stored in state in this case
        print state

    else:
        print "NO SOLUTION FOUND"


if __name__ == "__main__":
    main()