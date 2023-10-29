from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    my_text = StringProperty("You click 0 times!")
    count = 0
    count_enable = BooleanProperty(False)
    slider_value_txt = StringProperty("50")
    switch_enable = BooleanProperty(False)

    def on_button_click(self):
        print("click!")
        if self.count_enable:
            self.count += 1
        self. my_text = "You click " + str(self.count) + " times!"

    def on_toggle_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enable = False
        else:
            widget.text = "ON"
            self.count_enable = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
        self.switch_enable = widget.active

    def on_slider_value(self, widget):
        print("SLider: " + str(int(widget.value)))
        self.slider_value_txt = str(int(widget.value))

class StackLayoutExample(StackLayout):
    pass


class GridLayoutExample(GridLayout):
    pass


class AuchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
