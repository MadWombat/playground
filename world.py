class World:
    def __init__(self, width, height, features=[]):
        self.width = width
        self.height = height
        self.agents = []
        self.features = features

    def reset(self):
        self.agents = []

    def update(self):
        for agent in self.agents:
            agent.update()
        for feature in self.features:
            feature.update(self)

    def add(self, agent, pos=None):
        agent.world = self
        if pos:
            agent.pos = pos
        else:
            agent.pos = (self.width // 2, self.height // 2) # center agent by default
        self.agents.append(agent)

    def remove(self, agent):
        self.agents.remove(agent)
