from manim import *
import itertools as it
class UpingDot(Scene):
    diccionario={
        'height': 0
    }
    def construct(self):
        self.get_dot()
    def get_dot(self):
        dot= Dot().move_to(-config['frame_height']*DOWN/2)
        dot.set_color(RED)
        def update_dot(mob,dt):
            self.diccionario['height']+=dt*3
            if mob.get_center()[1]>config['frame_height']/2:
                self.diccionario['height']=-config['frame_height']/2
            mob.move_to(UP*self.diccionario['height'])
        dot.add_updater(update_dot)
        self.add(dot)
        self.wait(10)