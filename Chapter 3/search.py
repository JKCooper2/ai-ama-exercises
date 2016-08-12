
class Queue(object):
    def __init__(self):
        self.items = []

    def make_queue(self, elements):
        self.items = elements

    def is_empty(self):
        return len(self.items) == 0

    def remove_front(self):
        return self.items.pop(0)

    def queue_front(self, elements):
        self.items.insert(0, elements)

    def queue_back(self, elements):
        self.items.extend(elements)


class Node(object):
    def __init__(self, state, parent, operator, depth, path_cost):
        self.state = state
        self.parent = parent
        self.operator = operator  # Unused atm
        self.depth = depth
        self.path_cost = path_cost

    @property
    def state_hash(self):
        return ''.join([str(item) for row in self.state for item in row])


class GeneralSearch(object):
    def __init__(self, initial_state, expand_node, goal_test):
        self.nodes = [Node(initial_state, None, None, 1, 1)]  # Root Node
        self.expand_node = expand_node  # Function that returns expansion of inputted node
        self.goal_test = goal_test
        self.hashes = {self.nodes[0].state_hash: self.nodes[0]}

        self.queue = Queue()
        self.queue.make_queue(self.expand_node(self.nodes[0]))

    def queuing_function(self, nodes):
        raise NotImplementedError

    def solution(self, node):
        order = []

        while node.parent is not None:
            order.append(node.operator)
            node = node.parent

        order = order[::-1]  # Reverse order to go from root to end

        return order


    def find_path(self, steps=None):
        i = 1

        while not self.queue.is_empty():
            node = self.queue.remove_front()
            print i, "-", node.depth, ":", len(self.queue.items)
            if self.goal_test(node):
                print "FOUND SOLUTION"
                return self.solution(node), node.state

            # print "EXPANDING NODE:", node.state_hash

            # Check for repeated states
            expanded_nodes = [new_node for new_node in self.expand_node(node) if new_node.state_hash not in self.hashes]

            # if len(expanded_nodes) == 0:
            #     print "No expansion possible"

            for new_node in expanded_nodes:
                # print "Adding hash:", new_node.state_hash
                self.hashes[new_node.state_hash] = new_node

            print len(expanded_nodes)

            self.queuing_function(expanded_nodes)

            if steps is not None and i >= steps:
                return None, None

            i += 1

        return False, None


class BreadthFirstSearch(GeneralSearch):
    def __init__(self, initial_state, expand_node, goal_test):
        GeneralSearch.__init__(self, initial_state, expand_node, goal_test)

    def queuing_function(self, nodes):
        self.queue.items.extend(nodes)


class DepthFirstSearch(GeneralSearch):
    def __init__(self, initial_state, expand_node, goal_test):
        GeneralSearch.__init__(self, initial_state, expand_node, goal_test)

    def queuing_function(self, nodes):
        self.queue.items = nodes + self.queue.items


class BidirectionalSearch(object):
    def __init__(self, start_state, goal_state, expand_node):
        self.start = BreadthFirstSearch(start_state, expand_node, self.goal_test)
        self.goal = BreadthFirstSearch(goal_state, expand_node, self.goal_test)

    def goal_test(self, node):
        return node.state_hash in self.goal.hashes and node.state_hash in self.start.hashes

    def find_path(self):
        solution = None

        while solution is None:
            solution = self.start.find_path(1)
            solution = self.goal.find_path(1)

        return solution
