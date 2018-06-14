from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

    def on_enter(instance, value):
        print("User pressed enter in", instance)

    textinput = TextInput()
    textinput.bind(text=on_text)

TestApp().run()
