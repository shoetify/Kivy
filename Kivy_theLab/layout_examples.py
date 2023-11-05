from tkinter import Button

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

Builder.load_file("layout_examples.kv")
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0,100):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None,None), size=(size,size))
            self.add_widget(b)


class GridLayoutExample(GridLayout):
    pass


class AuchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass