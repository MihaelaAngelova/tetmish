import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.text import LabelBase
LabelBase.register(name='Lemonada',
                   fn_regular='Lemonada-SemiBold.ttf')

class Screen(GridLayout):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.label(Label(text="This is my first try with this library, HELP"))
        #label.size = (0.4, 0.3)

        #The size of the window may not change if the minimum_size or minimum_width 
        # and minimum_height properties of the window are set to values that are larger 
        # than the size you specified. These properties determine the minimum size of 
        # the window, and the window will not be able to be resized to a size smaller 
        # than the minimum size.

        #label.minimum_size = None 
        #self.window = GridLayout

class MenuScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        
        title = Label(text="Tetmish", font_name='Lemonada', size_hint=(1, 1.2), font_size=70)
        start_button = Button(text="Choose an account", font_name='Lemonada', font_size=25)
        quit_button = Button(text="Play without an account", font_name='Lemonada', font_size=25)
        
        self.add_widget(title)
        self.add_widget(start_button)
        self.add_widget(quit_button)

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

        
class TetrisApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        menu = MenuScreen()
        field = PlayingField()

        main_layout.add_widget(menu)
        main_layout.add_widget(field)

        return main_layout

if __name__ == "__main__":
    TetrisApp().run()


""" tetris.kv
#:kivy 2.2.0

<PlayingField>:
    count: 0
    orientation: "vertical"
    padding: 10
    Label:
        text: "Hello!"
"""