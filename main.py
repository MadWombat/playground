from kivy.config import Config

from world import World
from agent import Agent

from minds import PassiveMind

from render.app import RenderApp


if __name__ == '__main__':
    # setup world and add an agent
    world = World(800, 600)
    mind = PassiveMind()
    agent = Agent(mind)
    world.add(agent)

    # do the kivy thing
    Config.set('kivy', 'desktop', 1)
    Config.set('kivy', 'exit_on_escape', 1)
    Config.set('graphics', 'resizable', 0)
    RenderApp(world).run()
