from random import randint

from kivy.app import App

from kivy.clock import Clock
from kivy.config import Config
from kivy.vector import Vector
from kivy.uix.widget import Widget
from kivy.properties import AliasProperty, ListProperty, NumericProperty, ReferenceListProperty


class Playground(Widget):
    critters = ListProperty([])

    def update(self, dt):
        for critter in self.critters:
            critter.move()
            if (critter.y < 0) or (critter.top > self.height):
                critter.v_y *= -1
            if (critter.x < 0) or (critter.right > self.width):
                critter.v_x *= -1
        self.score.text = "{}".format(len(self.critters))

    def on_touch_down(self, touch):
        critter = Critter()
        critter.pos = touch.x, touch.y
        self.critters.append(critter)
        self.add_widget(critter)


class Critter(Widget):
    angle = NumericProperty(0)
    v_x = NumericProperty(0)
    v_y = NumericProperty(0)
    velocity = ReferenceListProperty(v_x, v_y)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity = Vector(5, 0).rotate(randint(0, 360))
        self.angle = Vector(*self.velocity).angle(Vector(1, 0))

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.angle = Vector(*self.velocity).angle(Vector(1, 0))


class WorldApp(App):
    def build(self):
        game = Playground()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    Config.set('kivy', 'desktop', 1)
    Config.set('kivy', 'exit_on_escape', 1)
    Config.set('graphics', 'resizable', 0)
    WorldApp().run()
