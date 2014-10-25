from kivy.app import App
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.core.window import Window


class Pres(App):
    time = NumericProperty(0)

    def build(self):
        Window.bind(on_key_down=self.handle_key)
        Clock.schedule_interval(self.update_time, 0)
        return super(Pres, self).build()

    def update_time(self, dt):
        self.time += dt

    def handle_key(self, window, code, code2, char, modifier):
        sm = self.root.ids.sm
        if code == 275:
            sm.transition.direction = 'left'
            sm.current = sm.next()
        if code == 276:
            sm.transition.direction = 'right'
            sm.current = sm.previous()

if __name__ == '__main__':
    Pres().run()
