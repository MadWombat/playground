import random

from minds import Mind


class RandomMind(Mind):
    """ pick an action at random """
    def decide(self, agent):
        return random.choice(agent.actions)
