import numpy as np

from informed_search import Node


class GradientDescent(object):
    def __init__(self, state, utility_function, expand_nodes, goal_test):
        self.node = Node(state, None, None, 1, 1)
        self.utility_function = utility_function
        self.expand_nodes = expand_nodes
        self.goal_test = goal_test
        self.current_best = self.utility_function(self.node)

    def random_restart(self, state):
        self.node.state = state
        self.current_best = self.utility_function(self.node)

    def take_step(self, equal=True):
        curr_best = self.current_best

        # Make all available next states and choose the one with the best score
        for n in self.expand_nodes(self.node):
            score = self.utility_function(n)

            if score < self.current_best or \
               (equal and score == self.current_best and np.random.uniform() < 0.5):
                self.node = n
                self.current_best = score

        # If no improvement return false
        if self.current_best == curr_best:
            return False

        return True


class SimulatedAnnealing(object):
    def __init__(self, state, utility_function, random_move, goal_test, temperature=1, alpha=0.99):
        self.node = Node(state, None, None, 1, 1)
        self.utility_function = utility_function
        self.random_move = random_move
        self.goal_test = goal_test

        self.temperature = temperature
        self.alpha = alpha

        self.current_best = self.utility_function(self.node)

    def random_restart(self, board):
        pass

    def take_step(self):
        curr_best = self.current_best

        nn = self.random_move(self.node)

        score = self.utility_function(nn)

        if np.random.uniform() < np.e ** ((self.current_best - score) / self.temperature):
            self.node = nn
            self.current_best = score

        self.temperature *= self.alpha

        # If no improvement return false
        if self.current_best == curr_best:
            return False

        return True
