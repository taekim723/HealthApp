from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton, Button, MDRoundFlatButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from base import DataBase
from kivy_garden.zbarcam import ZBarCam

screen_helper = """
ScreenManager :
    Login:
    MenuScreen:
    ProfileScreen:
    Text:
    Drawer:
    Name:
    Upload:
    Great:
    Good:
    Mid:
    Low:
    Worse:
    Color_Dark:
    Color_Medium:
    Color_Good:
    Color_Best:
    Database:
    Result:
    QR_Check:
"""
class Login(Screen):
    pass

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class Text(Screen):
    pass

class Drawer(Screen):
    pass

class Name(Screen):
    pass

class Upload(Screen):
    pass

class Great(Screen):
    pass
class Good(Screen):
    pass
class Mid(Screen):
    pass
class Low(Screen):
    pass

class Worse(Screen):
    pass

class Color_Dark(Screen):
    pass

class Color_Medium(Screen):
    pass

class Color_Good(Screen):
    pass

class Color_Best(Screen):
    pass

class Database(Screen):
    color = ObjectProperty(None)
    second = ObjectProperty(None)

    def submit(self):
        if self.color.text != "" and self.second.text != "" :
            db.add_user(self.second.text, self.color.text)
            self.reset()
        else :
            invalidForm()
    
    def reset(self):
        self.color.text = ""
        self.second.text = ""

    
class Result(Screen):
    pass

class QR_Check(Screen):
    pass

    
    

    


sm = ScreenManager()
sm.add_widget(Text(name = "password"))
sm.add_widget(Login(name = "login"))
sm.add_widget(MenuScreen(name = "menu"))
sm.add_widget(ProfileScreen(name = "Profile"))
sm.add_widget(Drawer(name = "drawer"))
sm.add_widget(Name(name = "name"))
sm.add_widget(Upload(name = "upload"))
sm.add_widget(Great(name = "great"))
sm.add_widget(Good(name = "good"))
sm.add_widget(Mid(name = "mid"))
sm.add_widget(Low(name = "low"))
sm.add_widget(Worse(name = "worse"))
sm.add_widget(Color_Dark(name = "color_dark"))
sm.add_widget(Color_Medium(name = "color_medium"))
sm.add_widget(Color_Good(name = "color_good"))
sm.add_widget(Color_Best(name = "color_best"))
sm.add_widget(Database(name = "database"))
sm.add_widget(Result(name = "result"))
sm.add_widget(QR_Check(name = "qr"))

db = DataBase("users.txt")

class HealthApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
    
      
        changescreen = Builder.load_string(screen_helper)
        screen.add_widget(changescreen)
        return screen
HealthApp().run()
