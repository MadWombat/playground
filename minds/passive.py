from minds import Mind


class PassiveMind(Mind):
    """ do nothing no matter what """
    def decide(self, agent):
        return None
