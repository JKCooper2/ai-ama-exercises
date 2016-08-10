"""
Vacuum Cleaner Environment
"""
import numpy as np


class VacuumEnvironment(object):
    def __init__(self, size, dirt):
        self.size = size
        self.dirt = dirt

        self.agent_x = np.random.randint(self.size[0])
        self.agent_y = np.random.randint(self.size[1])
        self.agent_facing = np.random.randint(4)    # 0-up, 1-right, 2-down, 3-left

        # Layer 0: dirt, layer 1: objects/home
        self.room = np.zeros((2, self.size[0], self.size[1]))

        for row in range(self.size[0]):
            for col in range(self.size[1]):
                if np.random.uniform() < self.dirt:
                    self.room[0][row][col] = 1

        # Set home base
        home_x = np.random.randint(self.size[0])
        home_y = np.random.randint(self.size[1])
        self.room[1][home_x][home_y] = 1

    def state(self, obstacle=False):
        return {"obstacle": int(obstacle),
                "dirt": self.room[0][self.agent_x][self.agent_y],
                "home": self.room[1][self.agent_x][self.agent_y],
                "agent": (self.agent_x, self.agent_y)}

    def has_hit_obstacle(self):
        if (self.agent_facing == 0 and self.agent_x == 0) or \
           (self.agent_facing == 1 and self.agent_y == self.size[1] - 1) or \
           (self.agent_facing == 2 and self.agent_x == self.size[0] - 1) or \
           (self.agent_facing == 3 and self.agent_y == 0):
            return True

        return False

    def move_forward(self):
        """
        Updates agents position
        :return: Whether agent hit obstacle
        """
        if self.has_hit_obstacle():
            return True

        if self.agent_facing == 0:
            self.agent_x -= 1

        elif self.agent_facing == 1:
            self.agent_y += 1

        elif self.agent_facing == 2:
            self.agent_x += 1

        elif self.agent_facing == 3:
            self.agent_y -= 1

        return False

    def step(self, action):
        obstacle = False
        reward = -1  # Default -1 for each action taken
        done = False

        if action == 0:
            obstacle = self.move_forward()

        elif action == 1:
            self.agent_facing = (self.agent_facing + 1) % 4

        elif action == 2:
            self.agent_facing = (self.agent_facing - 1) % 4

        elif action == 3:
            # Reward of +100 for sucking up dirt
            if self.room[0][self.agent_x][self.agent_y] == 1:
                reward += 100
                self.room[0][self.agent_x][self.agent_y] = 0

        elif action == 4:
            # If not on home base when switching off give reward of -1000
            if self.room[1][self.agent_x][self.agent_y] != 1:
                reward -= 1000

            done = True

        return self.state(obstacle), reward, done








