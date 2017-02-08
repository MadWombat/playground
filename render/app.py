from kivy.app import App
from kivy.clock import Clock

from render.world import WorldWidget


class RenderApp(App):
    def __init__(self, world, *args):
        self.world = world
        super().__init__(*args)

    def build(self):
        widget = WorldWidget(world=self.world)
        Clock.schedule_interval(widget.update, 1.0/60.0)
        return widget
