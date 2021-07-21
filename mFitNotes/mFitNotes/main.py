
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.togglebutton import ToggleButtonBehavior, ToggleButton
from kivy.uix.image import Image    
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,ObjectProperty

class MenuWindow(Screen):
    pass
class SelectionWindow(Screen):
    pass
class ExerciseWindow(Screen):
    pass
class StatisticsWindow(Screen):
    pass


kv = Builder.load_file("main.kv")

class MyMainApp(App):
    selected_body_parts = []

    def build(self):
        return kv

    def on_start(self):
        body_part_layout = self.root.ids.selection_window.ids.selection_window_layout

    def change_window(self,window_name):
        window_manager = self.root.ids.window_manager
        window_manager.current = window_name

    def load_image(self,image_name, image_source):
        image_name = Image(source="C:/Users/Matej/Source/Repos/mFitNotes/mFitNotes/Pictures/"+image_source)
        image_path = self.root.ids.selection_window.ids.selection_window_layout
        image_path.add_widget(image_name)

    def remove_image(self,image_name):
       self.remove = self.root.ids.selection_window.ids.selection_window_layout.children
       for child in self.remove :
           try:
               if child.source == "C:/Users/Matej/Source/Repos/mFitNotes/mFitNotes/Pictures/"+image_name:
                   self.root.ids.selection_window.ids.selection_window_layout.remove_widget(child)
           except:
               continue

    def collect_selected_parts(self):
        
        self.open_buttons = self.root.ids.selection_window.ids.selection_window_layout.children
        for child in self.open_buttons :
            try:
                if child.state == "down":
                    print(child.text)


            except:
                continue
    def display_exercises(self,body_part):







if __name__ == "__main__":
    MyMainApp().run()
