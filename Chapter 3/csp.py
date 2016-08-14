import copy


class Variable(object):
    def __init__(self, domain):
        self.domain = domain
        self.value = domain[0]
        self.active_domain = domain

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if v not in self.domain:
            raise ValueError(str(v) + " is not contained within domain " + str(self.domain))

        self._value = v


class ConstraintSatisfactionProblem(object):
    def __init__(self, variables, constraints, goal_test):
        self.variables = variables
        self.constraints = constraints  # List of functions
        self.goal_test = goal_test  # To differentiate valid partial from valid complete solutions

    @staticmethod
    def hash(variables):
        return ''.join([str(variable.value) for variable in variables])

    @staticmethod
    def is_valid(constraints, variables):
        for constraint in constraints:
            if not constraint(variables):
                return False

        return True

    @staticmethod
    def is_solution(goal_test, variables):
        for test in goal_test:
            if not test(variables):
                return False

        return True


class ConstraintSatisfactionSolver(object):
    def __init__(self, csp):
        self.csp = csp
        self.queue = [self.csp.variables]
        self.hash_list = {self.csp.hash(self.csp.variables): True}

    def forward_checking(self, variables):
        test = copy.deepcopy(variables)

        for i, v in enumerate(test):
            test_variable = copy.deepcopy(v)
            test_variable.active_domain = []
            for value in v.active_domain:
                test_variable.value = value
                test[i] = test_variable

                if self.csp.is_valid(self.csp.constraints, test):
                    test_variable.active_domain.append(value)

                test[i].value = v.value  # Reset for next test

            # print "ACTIVE DOMAIN " + str(test_variable.active_domain)

            if len(test_variable.active_domain) == 0:
                return False

        return True

    def solve(self):
        while len(self.queue) > 0:
            variables = self.queue.pop(0)

            print "TESTING: " + self.csp.hash(variables)

            # Back Tracking
            if not self.csp.is_valid(self.csp.constraints, variables):
                continue

            # Forward Checking
            if self.forward_checking(variables) is False:
                continue

            if self.csp.is_valid(self.csp.constraints, variables) and self.csp.is_solution(self.csp.goal_test, variables):
                print "FOUND SOLUTION " + self.csp.hash(variables)
                return

            for v in range(len(variables)):
                for d in range(len(variables[v].domain)):
                    new_variables = copy.deepcopy(variables)
                    new_variables[v].value = new_variables[v].domain[d]

                    if self.csp.hash(new_variables) not in self.hash_list:
                        self.queue.append(new_variables)  # Standard
                        self.queue.insert(0, new_variables)  # Backtracking
                        self.hash_list[self.csp.hash(new_variables)] = True


def first_variable_must_be_0(state):
    return state[0].value == 0


def sum_must_be_1(state):
    return sum([variable.value for variable in state]) == 1


def main():
    variables = [Variable([0, 1]), Variable([0, 1])]
    constraints = [first_variable_must_be_0]
    goal_test = [sum_must_be_1]
    csp = ConstraintSatisfactionProblem(variables, constraints, goal_test)
    csps = ConstraintSatisfactionSolver(csp)
    csps.solve()


if __name__ == "__main__":
    main()


