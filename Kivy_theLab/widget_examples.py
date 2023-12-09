from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout

# load .kv file
Builder.load_file("widget_examples.kv")
class WidgetsExample(GridLayout):
    my_text = StringProperty("You click 0 times!")
    count = 0
    count_enable = BooleanProperty(False)
    slider_value_txt = StringProperty("50")
    switch_enable = BooleanProperty(True)
    text_input_str = StringProperty("foo")

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

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

class ImagesExample(GridLayout):
    pass
