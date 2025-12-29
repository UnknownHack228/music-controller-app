from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MusicControllerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(Label(text='🎵 MUSIC CONTROLLER', font_size=24))
        layout.add_widget(Button(text='Сканировать Bluetooth'))
        layout.add_widget(Button(text='Воспроизвести музыку'))
        layout.add_widget(Button(text='Микрофон на колонку'))
        return layout

if name == 'main':
    MusicControllerApp().run()
