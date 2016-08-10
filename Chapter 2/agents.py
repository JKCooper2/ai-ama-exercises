import numpy as np

ACTIONS = ((0, "Go Forward"),
           (1, "Turn Right"),
           (2, "Turn Left"),
           (3, "Suck Dirt"),
           (4, "Turn Off"),
           (-1, "Break"),)


class RandomAgent(object):
    def __init__(self):
        self.reward = 0

    def act(self, observation, reward):
        self.reward += reward

        action = ACTIONS[np.random.randint(len(ACTIONS))]
        return action


class ReflexAgent(object):
    def __init__(self):
        self.reward = 0

    def act(self, observation, reward):
        self.reward += reward

        # If dirt then suck
        if observation['dirt'] == 1:
            return ACTIONS[3]

        # If obstacle then turn
        if observation['obstacle'] == 1:
            return ACTIONS[1]

        # Else randomly choose from first 3 actions (stops infinite loop circling edge)
        return ACTIONS[np.random.randint(3)]


class InternalAgent(object):
    def __init__(self):
        self.reward = 0
        self.map = [[-1, -1], [-1, -1]]  # 0-Empty, 1-Dirt, 2-Obstacle, 3-Home

        # Agent's relative position to map and direction
        self.x = 0
        self.y = 0
        self.facing = 0  # -1-Unknown, 0-Up, 1-Right, 2-Down, 3-Left

    def add_map(self):

        side = self.is_on_edge()

        while side >= 0:
            if side == 0:  # Top
                self.map.insert(0, [-1] * len(self.map[0]))
                self.x += 1

            elif side == 1:  # Right
                for row in self.map:
                    row.append(-1)

            elif side == 2:  # Down
                self.map.append([-1] * len(self.map[0]))

            elif side == 3:  # Left
                for row in self.map:
                    row.insert(0, -1)
                self.y += 1

            side = self.is_on_edge()

    def is_on_edge(self):
        if self.x == 0:
            return 0

        elif self.y == len(self.map[0]) - 1:
            return 1

        elif self.x == len(self.map) - 1:
            return 2

        elif self.y == 0:
            return 3

        return -1

    def move_forward(self):
        if self.facing == 0:
            self.x -= 1

        elif self.facing == 1:
            self.y += 1

        elif self.facing == 2:
            self.x += 1

        elif self.facing == 3:
            self.y -= 1

    # If obstacle in position then move back to previous square
    def move_backwards(self):
        if self.facing == 0:
            self.x += 1

        elif self.facing == 1:
            self.y -= 1

        elif self.facing == 2:
            self.x -= 1

        elif self.facing == 3:
            self.y += 1

    def update_map(self, observation):
        if observation['dirt'] == 1:
            self.map[self.x][self.y] = 1

        elif observation['home'] == 1:
            self.map[self.x][self.y] = 3

        else:
            self.map[self.x][self.y] = 0

        if observation['obstacle'] == 1:
            self.map[self.x][self.y] = 2
            self.move_backwards()

        # Fill in borders
        x_len = len(self.map) - 1
        y_len = len(self.map[0]) - 1

        if self.map[0][1] == 2 and self.map[1][0] == 2:
            self.map[0][0] = 2

        if self.map[0][y_len - 1] == 2 and self.map[1][y_len] == 2:
            self.map[0][y_len] = 2

        if self.map[x_len - 1][0] == 2 and self.map[x_len][1] == 2:
            self.map[x_len][0] = 2

        if self.map[x_len][y_len - 1] == 2 and self.map[x_len - 1][y_len] == 2:
            self.map[x_len][y_len] = 2

    # Determine next action needed to move towards next_square from current position
    def next_step(self, next_square):
        if next_square[0] < self.x and self.facing != 0 and self.map[self.x - 1][self.y] != 2:
            action = ACTIONS[2]

        elif next_square[0] < self.x and self.facing == 0 and self.map[self.x - 1][self.y] != 2:
            action = ACTIONS[0]

        elif next_square[0] > self.x and self.facing != 2 and self.map[self.x + 1][self.y] != 2:
            action = ACTIONS[2]

        elif next_square[0] > self.x and self.facing == 2 and self.map[self.x + 1][self.y] != 2:
            action = ACTIONS[0]

        elif next_square[1] > self.y and self.facing != 1 and self.map[self.x][self.y + 1] != 2:
            action = ACTIONS[2]

        elif next_square[1] > self.y and self.facing == 1 and self.map[self.x][self.y + 1] != 2:
            action = ACTIONS[0]

        elif next_square[1] < self.y and self.facing != 3 and self.map[self.x][self.y - 1] != 2:
            action = ACTIONS[2]

        elif next_square[1] < self.y and self.facing == 3 and self.map[self.x][self.y - 1] != 2:
            action = ACTIONS[0]

        else:
            action = ACTIONS[4]

        # If moving forward check if map needs to be expanded
        if action[0] == 0:
            self.move_forward()

        if action[0] == 2:
            self.facing = (self.facing - 1) % 4

        return action

    def find_nearest(self, square_type):
        # Else move towards nearest unknown
        min_dist = None
        next_square = None

        for i, row in enumerate(self.map):
            for j, square in enumerate(row):
                if square == square_type:
                    dist = (self.x - i) ** 2 + (self.y - j) ** 2
                    if min_dist is None or dist < min_dist:
                        min_dist = dist
                        next_square = (i, j)

        return next_square

    def choose_action(self):
        # If on a patch of dirt then suck it up
        if self.map[self.x][self.y] == 1:
            return ACTIONS[3]

        next_square = self.find_nearest(-1)

        # If no more unknowns then head home
        if next_square is None:
            next_square = self.find_nearest(3)

        return self.next_step(next_square)

    def act(self, observation, reward):
        self.reward += reward

        self.update_map(observation)
        self.add_map()

        # Choose action (based on map)
        return self.choose_action()
