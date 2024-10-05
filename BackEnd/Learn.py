from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


class LearnScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Title
        title = Label(text="Learn About the Environment", font_size=30, size_hint_y=None, height=50)
        self.add_widget(title)

        # Scrollable area for learning content
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 400))
        content = BoxLayout(orientation='vertical', size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        # Add learning topics
        content.add_widget(Label(text="1. Climate Change\n\n"
                                       "Climate change refers to significant changes in global temperatures and weather patterns over time. "
                                       "While climate change is a natural phenomenon, scientific evidence shows that human activities are accelerating it.\n\n"
                                       "Tips to combat climate change:\n"
                                       "- Reduce, reuse, recycle\n"
                                       "- Use renewable energy sources\n"
                                       "- Conserve water\n"
                                       "- Plant trees", size_hint_y=None, height=300))

        content.add_widget(Label(text="2. Biodiversity\n\n"
                                       "Biodiversity refers to the variety of life on Earth, including the diversity of species, ecosystems, and genetic variation within species. "
                                       "A rich biodiversity contributes to ecosystem services that are essential for human survival.\n\n"
                                       "Ways to promote biodiversity:\n"
                                       "- Support local wildlife\n"
                                       "- Use native plants in landscaping\n"
                                       "- Reduce habitat destruction", size_hint_y=None, height=300))

        content.add_widget(Label(text="3. Conservation\n\n"
                                       "Conservation is the practice of protecting the Earth's natural resources for current and future generations. "
                                       "This can include the protection of endangered species and their habitats.\n\n"
                                       "How to get involved in conservation:\n"
                                       "- Volunteer for local conservation groups\n"
                                       "- Advocate for policies that protect the environment\n"
                                       "- Educate others about the importance of conservation", size_hint_y=None, height=300))

        scroll_view.add_widget(content)
        self.add_widget(scroll_view)

        # Back button to return to main menu
        back_button = Button(text="Back to Main Menu", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_to_main_menu)
        self.add_widget(back_button)

    def go_to_main_menu(self, instance):
        App.get_running_app().root.current = 'main_menu'


class LearnApp(App):
    def build(self):
        return LearnScreen()


if __name__ == '__main__':
    LearnApp().run()
