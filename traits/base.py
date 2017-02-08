class Trait(object):
    def __init__(self):
        self.actions = []

    def update(self, agent):
        raise NotImplemented

    def state(self, agent):
        raise NotImplemented
