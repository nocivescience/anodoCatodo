from manim import *
class ColorScene(Scene):
    diccionario={
        'color':10,
        'constant':0.01
    }
    def construct(self):
        dot= Dot(radius=0.5).move_to(ORIGIN)
        def getting_color(mob,dt):
            self.diccionario['constant']+=dt*.5
            if self.diccionario['constant'] > 1:
                self.diccionario['constant'] = 0.01
            mob.set_color(interpolate_color(RED,BLUE, self.diccionario['constant']))
        dot.add_updater(getting_color)
        self.add(dot)
        self.wait(3)