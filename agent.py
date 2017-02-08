class Agent(object):
    def __init__(self, mind, traits=[]):
        self.pos = (0, 0)
        self.world = None
        self._actions = {}
        self.traits = traits
        self.alive = True
        self.mind = mind
        for trait in self.traits:
            for action in trait.actions:
                self._actionmap[action] = trait

    def update(self):
        """ one step in agent life cycle """
        action = self.mind.decide(self)
        if action: # if action is None do nothing
            handler = self._actionmap[action]
            handler.act(self, action)
        for trait in self.traits:
            trait.update(self)

    def actions(self):
        """ return a list of possible actions """
        return [None, ] + list(self._actionmap.keys())

    def state(self):
        state = [self.alive, self.pos] # life and position are the basic state
        for trait in self.trait:
            state.extend(trait.state(self))
        return state
