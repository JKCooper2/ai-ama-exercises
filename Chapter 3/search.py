
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
        try:
            return ''.join([str(item) for row in self.state for item in row]) + str(self.operator if self.operator is not None else -1)
        except:
            return ''.join([str(item) for item in self.state]) + self.operator


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

    @staticmethod
    def solution(node):
        order = []

        while node.parent is not None:
            order.append(node.operator)
            node = node.parent

        order = order[::-1]  # Reverse order to go from root to end

        return order

    def find_path(self, steps=None, search_cost=0):
        i = 1

        while not self.queue.is_empty():
            node = self.queue.remove_front()
            print i, "-", node.depth, ":", len(self.queue.items)
            # print "Checking " + node.state_hash

            if self.goal_test(node):
                return self.solution(node), node

            # Check for repeated states
            expanded_nodes = [new_node for new_node in self.expand_node(node) if new_node.state_hash not in self.hashes]

            for new_node in expanded_nodes:
                new_node.path_cost += search_cost  # Add search cost
                self.hashes[new_node.state_hash] = new_node

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


class UniformCostSearch(GeneralSearch):
    def __init__(self, initial_state, expand_node, goal_test):
        GeneralSearch.__init__(self, initial_state, expand_node, goal_test)

    def queuing_function(self, nodes):
        self.queue.items.extend(nodes)
        self.queue.items.sort(key=lambda x: x.path_cost)


class DepthFirstSearch(GeneralSearch):
    def __init__(self, initial_state, expand_node, goal_test):
        GeneralSearch.__init__(self, initial_state, expand_node, goal_test)

    def queuing_function(self, nodes):
        self.queue.items = nodes + self.queue.items


class DepthLimitedSearch(GeneralSearch):
    def __init__(self, initial_state, expand_node, goal_test, depth_limit):
        GeneralSearch.__init__(self, initial_state, expand_node, goal_test)
        self.depth_limit = depth_limit

    def queuing_function(self, nodes):
        nodes = [node for node in nodes if node.depth <= self.depth_limit]
        self.queue.items = nodes + self.queue.items


class IterativeDeepeningSearch(object):
    def __init__(self, initial_state, expand_node, goal_test, starting_depth, depth_limit):
        self.starting_depth = starting_depth
        self.depth_limit = depth_limit
        self.initial_state = initial_state
        self.expand_node = expand_node
        self.goal_test = goal_test
        self.search = None

    def find_path(self, steps=None, search_cost=0):
        solution = None
        state = None

        for d in range(self.starting_depth, self.depth_limit+1):
            print "Search with depth " + str(d)
            self.search = DepthLimitedSearch(self.initial_state, self.expand_node, self.goal_test, d)
            solution, state = self.search.find_path(steps, search_cost=search_cost)

            if solution:
                break

        return solution, state


class BidirectionalSearch(object):
    def __init__(self, start_state, goal_state, expand_node):
        self.start = BreadthFirstSearch(start_state, expand_node, self.goal_test)
        self.goal = BreadthFirstSearch(goal_state, expand_node, self.goal_test)

    def goal_test(self, node):
        return node.state_hash in self.goal.hashes and node.state_hash in self.start.hashes

    def find_path(self, steps=None, search_cost=0):
        solution = None

        while solution is None:
            solution = self.start.find_path(1, search_cost=search_cost)
            solution = self.goal.find_path(1, search_cost=search_cost)

        return solution
