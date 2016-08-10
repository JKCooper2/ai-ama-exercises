from environment import VacuumEnvironment
from agents import RandomAgent, ReflexAgent

ENV_SIZE = (12, 12)


def main():
    env = VacuumEnvironment(ENV_SIZE, 0.05)
    agent = ReflexAgent()

    print env.room[0]
    print env.room[1]

    observation = env.state()
    reward = 0
    done = False
    action = agent.act(observation, reward)

    print observation
    turn = 1

    while not done:

        observation, reward, done = env.step(action[0])

        print done
        print "Step {0}: Action - {1}".format(turn, action[1])
        print observation

        action = agent.act(observation, reward)
        print "Reward {0}   Total Reward {1}".format(reward, agent.reward)
        turn += 1

        if turn > 1000:
            break

    print env.room[0]

if __name__ == "__main__":
    main()