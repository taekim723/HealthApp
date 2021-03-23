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


screen_helper = """
ScreenManager :
    Login:
    MenuScreen:
    ProfileScreen:
    Text:
    Drawer:
    Name:
#: import utils kivy.utils
#: import MDChips kivymd.uix.chip.MDChip
 

   
<Text>:
    name : "password"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
        
    MDTextField:
    
        hint_text : "Enter the Password"
        helper_text: "click if forgotten"
        helper_text_mode : "on_focus"
        icon_right:"language-python"
        password :True
        icon_right_color: app.theme_cls.primary_color
        pos_hint : {"center_x" : 0.5, "center_y": 0.5}
        size_hint_x : None
        width : 300
        id : passw
     
    MDFloatingActionButton:
        icon : "login"
        theme_text_color : "Custom"
        halign : "center"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.3}
        size_hint: (0.15, 0.1)
        on_press : root.manager.current = "Profile" if passw.text == "tae" else "login"
        
<RoundedButton@Button>:
    background_color : (0,0,0,0)
    background_normal : ""
    canvas.before:
        Color : 
            rgba : (229/255, 194/255, 0, 1)
        RoundedRectangle:
            size : self.size
            pos : self.pos
            radius : [60]
    

<Login>:
    name: "login"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    MDRoundFlatButton:
        text : "Welcome to the Health App"
        pos_hint : {"center_x": 0.5, "center_y": 0.5}
        on_press: root.manager.current = "menu"
<MenuScreen>:
    name: "menu"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    FloatLayout:
        GridLayout : 
            rows : 1
            pos_hint : {"top" : 1, "left": 1}
            size_hint : 1, 0.1
        GridLayout:
            rows : 1
            pos_hint : {"top" : 0.9, "left": 1}
            size_hint : 1, 0.15
            
            
        GridLayout:
            
            rows : 1
            pos_hint : {"top": 0.75 , "left":1}
            size_hint : 1, 0.25
            Image : 
                source : "man.png"

        Label : 
            pos_hint : {"top": 0.5 , "left":1}
            size_hint : 1, 0.1
            color : (1,1,1,1)
            text : "Health Care App"
            font_style : "Button"
            color : (0,1,0,1)
        
        GridLayout:
            
            rows : 1
            pos_hint : {"top": 0.4 , "left":1}
            size_hint : 1, 0.4

        

    MDRoundFlatButton:
        text: "Click to Login"
        pos_hint : {"center_x":0.5, "center_y":0.2}
        on_press : root.manager.current = "password"
<ProfileScreen>:
    name: "Profile"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    MDLabel :
        text: "How are you, Minjeong?"
        font_style : "Button"
        color : (0,1,0,1)
        halign : "center"
    FloatLayout:
        GridLayout : 
            rows : 1
            pos_hint : {"center_x" : 0.6 , "center_y": 0.6}
            size_hint : 1, 0.15
            Image : 
                source : "grandma_1.png"
    MDRoundFlatButton:
        text: "Back"
        pos_hint : {"center_x":0.7, "center_y":0.2}
        on_press: root.manager.current = "menu"
        on_press : print("You have clicked to go to Menu")
    MDRoundFlatButton:
        text: "Menu"
        pos_hint : {"center_x":0.3, "center_y":0.2}
        on_press: root.manager.current = "drawer"
<Name>:
    name: "name"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    BoxLayout:
        orientation: 'vertical'
        spacing: "15dp"
        padding: "15dp"
        MDRoundFlatButton:
            text: "Name:  Tae Kim"
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "Nationality:  South Korea"
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "Date of Birth:  1996.08.20"
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "Blood Type:  B"
            font_stryle : "Subtitle"
            size_hint_y : None
        
        ScrollView
        MDRoundFlatButton:
            text:"Back"
            on_press:   
                root.manager.transition.direction = "right"
                root.manager.current = "drawer"


<Drawer>:
    name : "drawer"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    FloatLayout:
        GridLayout : 
            rows : 1
            pos_hint : {"top" : 0.7, "left": 1}
            size_hint : 1, 0.1
            Image :
                source : "grandma.png"
            Image : 
                source : "senior.png"
            Image : 
                source: "bald.png"
        GridLayout:
            rows : 1
            pos_hint : {"top" : 0.5, "left": 1}
            size_hint : 1, 0.1
            Image : 
                source : "teacher.png"
            Image : 
                source : "grandpa.png"
            Image : 
                source : "grandma_2.png"
            
        GridLayout:
            
            rows : 1
            pos_hint : {"top": 0.3 , "left":1}
            size_hint : 1, 0.1
            Image : 
                source : "grandma_3.png"
            Image : 
                source : "beard.png"
            Image : 
                source : "beard_2.png"

        

    
    Screen:
        NavigationLayout:
            ScreenManager : 
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Health App'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
    
                        Widget:
                        
                        ScrollView
            MDNavigationDrawer: 
                id: nav_drawer
                canvas : 
                    Color: 
                        rgb: utils.get_color_from_hex("#FEFEFE")
                    Rectangle :
                        size : self.size
                        pos : self.pos
                BoxLayout:
                    orientation: 'vertical'
                    spacing: "15dp"
                    padding: "15dp"
                    Image :
                        source : "skku.png"
                    MDLabel : 
                        text : "    App: Health App"
                        color : (1,1,1,1)
                        font_stryle : "Subtitle"
                        size_hint_y : None
                        height: self.texture_size[1]
                    MDLabel : 
                        text : "    Email : taekim723@gmail.com"
                        color : (1,1,1,1)
                        font_stryle : "Caption"
                        size_hint_y : None
                        height: self.texture_size[1]

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Profile'
                                color : (1,1,1,1)
                                on_press : 
                                    root.manager.current = "name"
                                IconLeftWidget:
                                    icon_right_color: app.theme_cls.primary_color
                                    icon : "face-profile"
                          
                            OneLineIconListItem:
                                text: 'Logout'
                                color : (1,1,1,1)
                                on_press :
                                    root.manager.current = "login"
                                IconLeftWidget:
                                    icon : "logout"
                                  

            

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



sm = ScreenManager()
sm.add_widget(Text(name = "password"))
sm.add_widget(Login(name = "login"))
sm.add_widget(MenuScreen(name = "menu"))
sm.add_widget(ProfileScreen(name = "Profile"))
sm.add_widget(Drawer(name = "drawer"))
sm.add_widget(Name(name = "name"))

class HealthApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
    
      
        changescreen = Builder.load_string(screen_helper)
        screen.add_widget(changescreen)
        return screen
HealthApp().run()

