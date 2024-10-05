import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        title = Label(text="Welcome to EcoPals!", font_size=30)
        layout.add_widget(title)

        air_quality_button = Button(text="Air Quality Monitor")
        air_quality_button.bind(on_press=self.go_to_air_quality)
        layout.add_widget(air_quality_button)

        learn_button = Button(text="Learn About the Environment")
        learn_button.bind(on_press=self.go_to_learn)
        layout.add_widget(learn_button)

        explore_button = Button(text="Explore the Ecosystem")
        explore_button.bind(on_press=self.go_to_explore)
        layout.add_widget(explore_button)

        self.add_widget(layout)

    def go_to_air_quality(self, instance):
        self.manager.current = 'air_quality'

    def go_to_learn(self, instance):
        self.manager.current = 'learn'

    def go_to_explore(self, instance):
        self.manager.current = 'explore'


class AirQualityScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Title Label
        self.title = Label(text="EcoPals - Air Quality Monitor", font_size=24)
        layout.add_widget(self.title)

        # Instruction Label
        self.instruction = Label(text="Enter a city name to check air quality:")
        layout.add_widget(self.instruction)

        # Text input for location
        self.location_input = TextInput(hint_text="Enter location", multiline=False)
        layout.add_widget(self.location_input)

        # Display the air quality data
        self.result_label = Label(text="")
        layout.add_widget(self.result_label)

        # Fetch data button
        self.fetch_button = Button(text="Fetch Air Quality Data")
        self.fetch_button.bind(on_press=self.fetch_air_quality)
        layout.add_widget(self.fetch_button)

        # Back button to return to main menu
        back_button = Button(text="Back to Main Menu")
        back_button.bind(on_press=self.go_to_main_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def fetch_air_quality(self, instance):
        location = self.location_input.text
        if location:
            self.result_label.text = "Fetching data..."
            self.get_air_quality_data(location)
        else:
            self.result_label.text = "Please enter a valid location."

    def get_air_quality_data(self, location):
        """Fetch air quality data from OpenWeather API."""
        api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeather API key
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?q={location}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an error for bad responses
            data = response.json()
            # Extracting PM2.5 data
            pm25 = data['list'][0]['components']['pm2_5']
            self.result_label.text = f"Air Quality (PM2.5) in {location}: {pm25} µg/m³"
        except requests.exceptions.HTTPError as http_err:
            self.result_label.text = f"HTTP error: {http_err}"
        except requests.exceptions.RequestException as req_err:
            self.result_label.text = f"Request error: {req_err}"
        except KeyError:
            self.result_label.text = "Could not find air quality data. Try another location."
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'


class LearnScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Title Label
        self.title = Label(text="Learn About the Environment", font_size=24)
        layout.add_widget(self.title)

        # Learning content
        self.content = Label(text="Learn about climate change, biodiversity,\nand ways to protect our planet!")
        layout.add_widget(self.content)

        # Back button to return to main menu
        back_button = Button(text="Back to Main Menu")
        back_button.bind(on_press=self.go_to_main_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'


class ExploreScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Title Label
        self.title = Label(text="Explore the Ecosystem", font_size=24)
        layout.add_widget(self.title)

        # Exploration content
        self.content = Label(text="Explore different ecosystems and learn about\nthe plants and animals that live there!")
        layout.add_widget(self.content)

        # Back button to return to main menu
        back_button = Button(text="Back to Main Menu")
        back_button.bind(on_press=self.go_to_main_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'


class EcoPalsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(AirQualityScreen(name='air_quality'))
        sm.add_widget(LearnScreen(name='learn'))
        sm.add_widget(ExploreScreen(name='explore'))
        return sm


if __name__ == '__main__':
    EcoPalsApp().run()
