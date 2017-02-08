from kivy.uix.widget import Widget

from kivy.graphics import Color
from kivy.graphics import Rectangle


class WorldWidget(Widget):
    def __init__(self, world, *args, **kwargs):
        self.world = world
        super().__init__(*args, **kwargs)
        self.pos = (0, 0)
        self.size = (world.width, world.height)
        with self.canvas:
            Color(0, 0.1, 0, 1)
            Rectangle(pos=self.pos, size=self.size)

    def update(self, dt):
        pass
