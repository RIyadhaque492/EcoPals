import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import json

class ExploreScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Title
        title = Label(text="Explore the Environment", font_size=30, size_hint_y=None, height=50)
        self.add_widget(title)

        # Instructions
        instruction = Label(text="Enter a city name to fetch air quality data:")
        self.add_widget(instruction)

        # Text input for location
        self.location_input = TextInput(hint_text="Enter city name", multiline=False)
        self.add_widget(self.location_input)

        # Fetch data button
        self.fetch_button = Button(text="
