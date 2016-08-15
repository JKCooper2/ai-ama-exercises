import bisect


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
        self.evaluation_cost = 0

    @property
    def total_cost(self):
        return self.path_cost + self.evaluation_cost

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
            print i, "-", round(node.total_cost, 3), ":", len(self.queue.items)

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


class AStarSearch(GeneralSearch):
    def __init__(self, initial_state, expand_node, goal_test, heuristic):
        GeneralSearch.__init__(self, initial_state, expand_node, goal_test)
        self.heuristic = heuristic
        self.queue.items.sort(key=lambda x: x.path_cost + self.heuristic(x.state))

    def queuing_function(self, nodes):
        # Store evaluation cost to massively improve sort performance
        for node in nodes:
            node.evaluation_cost = self.heuristic(node.state)

        self.queue.items.extend(nodes)
        self.queue.items.sort(key=lambda x: x.total_cost)
