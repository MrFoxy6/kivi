from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

class clickerApp(App):
    i = -1
    def build(self):
        fl = FloatLayout()
        self.label = Label(text="Нажато: 0", size_hint=(.9, .9), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        btn = fl.add_widget( Button(text="Нажать", size_hint=(.3, .2),pos=(660 / 1.5 - 140, 480 / 1.5 - (480 * .25 / 2)), on_press=self.on_button_press) )
        fl.add_widget(self.label)
        return fl

    def on_button_press(self, instance):
        self.i += 1
        self.label.text = "Нажато: " + str(self.i + 1)


if __name__ == "__main__":
    clickerApp().run()
