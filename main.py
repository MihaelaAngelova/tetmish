from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
LabelBase.register(name='Lemonada',
                   fn_regular='Lemonada-SemiBold.ttf')
from kivy.core.window import Window
Window.size = (400, 650)

class BackgroundImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "background_menu.jpg"
        self.size = (Window.width, Window.height)
        self.allow_stretch = True
        self.keep_ratio = True
        self.size_hint = (1, 1)
        #self.size = (Window.width, Window.height)
        
class Choose_An_Account(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.background_color = (1, 1, 1, 0)

        new_account_button = Button(text="Create a new account", background_color=[0, 0, 0, 0], font_name='Lemonada', font_size=20)
        back_button = Button(text="Back", background_color=[0, 0, 0, 0], font_name='Lemonada', font_size=20)
        back_button.bind(on_press=self.change_screen_menu)
        
        self.add_widget(new_account_button)
        self.add_widget(back_button)
        
    def back(self, instance):
        self.clear_widgets()
        self.add_widget(MenuScreen())

    def change_screen_menu(self, instance):
        self.clear_widgets()
        self.add_widget(MenuScreen())

class MenuScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10 #padding
        #self.background_image = BackgroundImage()
        self.background_color = (1, 1, 1, 0)  # transparent background color
        #self.add_widget(BackgroundImage())

        title = Label(text="Tetmish", font_name='Lemonada', size_hint=(1, 1.2), font_size=60)
        start_button = Button(text="Choose an account", background_color=[0, 0, 0, 0], font_name='Lemonada', font_size=20)
        start_button.bind(on_press=self.change_screen_Choose_An_Account)
        quit_button = Button(text="Play without an account", background_color=[0, 0, 0, 0], font_name='Lemonada', font_size=20)
        
        self.add_widget(title)
        self.add_widget(start_button)
        self.add_widget(quit_button)
        
    def choose_account(self, instance):
        self.parent.clear_widgets()
        self.parent.add_widget(MenuScreen())

    def change_screen_Choose_An_Account(self, instance):
        self.clear_widgets()
        self.add_widget(Choose_An_Account())

    def change_screen_Create_An_Account(self, instance):
        self.clear_widgets()
        self.add_widget(AccountCreationScreen())

class AccountCreationScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10 #padding
        self.background_color = (1, 1, 1, 1)  # non-transparent background color

        title = Label(text="Create a new account", font_name='Lemonada', size_hint=(1, 1.2), font_size=60)
        username_input = TextInput(hint_text="Username", font_name='Lemonada', font_size=20)
        create_button = Button(text="Create", background_color=[0, 0, 0, 0], font_name='Lemonada', font_size=20)
        create_button.bind(on_press=self.create_account)

        self.add_widget(title)
        self.add_widget(username_input)
        self.add_widget(create_button)

    def create_account(self, instance):
        username = self.username_input.text
        # Save the username here
        # ...

        # Navigate back to the previous screen
        self.parent.change_screen()



"""
class PlayingField(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 10
        self.rows = 20
        self.tiles = {}
        for i in range(1, 21):
            self.tiles[f"row{i}"] = []
        self.__init_field()
        
    def __init_field(self):
        # Initialize the field with empty tiles
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                tile = Widget(size_hint=(None, None), size=(40, 40))
                self.add_widget(tile)
                row.append(tile)
            self.tiles[f"row{i+1}"] = row
"""

class TetrisApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        menu = MenuScreen()
        #field = PlayingField()

        main_layout.add_widget(menu)
        #main_layout.add_widget(field)

        return main_layout

if __name__ == "__main__":
    TetrisApp().run()
