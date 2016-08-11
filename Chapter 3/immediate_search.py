from search import Queue, Node


class GeneralSearchImmediateCheck(object):
    def __init__(self, initial_state, expand_node, goal_test):
        self.nodes = [Node(initial_state, None, None, 1, 1)]  # Root Node
        self.expand_node = expand_node  # Function that returns expansion of inputted node
        self.goal_test = goal_test
        self.hashes = {self.nodes[0].state_hash: True}

        self.queue = Queue()
        self.queue.make_queue(self.expand_node(self.nodes[0]))

    def queuing_function(self, nodes):
        raise NotImplementedError

    def find_path(self):
        i = 1

        # Test goal for initial node
        if self.goal_test(self.nodes[0]):
            return self.nodes[0]

        while not self.queue.is_empty():
            node = self.queue.remove_front()
            print i, "-", node.depth, ":", len(self.queue.items)

            print "EXPANDING NODE:", node.state_hash

            # Check for repeated states
            expanded_nodes = [new_node for new_node in self.expand_node(node) if new_node.state_hash not in self.hashes]

            if len(expanded_nodes) == 0:
                print "No expansion possible"

            for new_node in expanded_nodes:
                # If node is goal then immediately return
                if self.goal_test(new_node):
                    return new_node

                print "Adding hash:", new_node.state_hash
                self.hashes[new_node.state_hash] = True

            self.queuing_function(expanded_nodes)

            i += 1

        return None


class BreadthFirstSearchImmediateCheck(GeneralSearchImmediateCheck):
    def __init__(self, initial_state, expand_node, goal_test):
        GeneralSearchImmediateCheck.__init__(self, initial_state, expand_node, goal_test)

    def queuing_function(self, nodes):
        self.queue.items.extend(nodes)
