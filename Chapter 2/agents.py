import numpy as np

ACTIONS = ((0, "Go Forward"),
           (1, "Turn Right"),
           (2, "Turn Left"),
           (3, "Suck Dirt"),
           (4, "Turn Off"))


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

        # # IF home then turn off
        if observation['home'] == 1:
            return ACTIONS[4]

        # If obstacle then turn
        if observation['obstacle'] == 1:
            return ACTIONS[1]

        # Else randomly choose from first 3 actions (stops infinite loop circling edge)
        return ACTIONS[np.random.randint(3)]
