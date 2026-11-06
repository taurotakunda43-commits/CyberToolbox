from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class CyberToolbox(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="CYBER TOOLBOX",
            font_size=30,
            color=(0, 1, 0, 1)
        ))

        topics = [
            "Cybersecurity",
            "Networking Basics",
            "Linux Commands",
            "DNS Learning",
            "IP Address Guide"
        ]

        for topic in topics:
            button = Button(
                text=topic,
                size_hint_y=None,
                height=55
            )
            button.bind(
                on_press=lambda instance, t=topic:
                self.show_topic(t)
            )
            layout.add_widget(button)

        return layout

    def show_topic(self, topic):
        popup = Popup(
            title=topic,
            content=Label(
                text="Welcome to " + topic +
                "\nLearn ethical hacking safely!"
            ),
            size_hint=(0.8, 0.4)
        )
        popup.open()

CyberToolbox().run()
