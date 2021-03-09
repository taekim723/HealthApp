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
#: import utils kivy.utils
#: import MDChips kivymd.uix.chip.MDChip
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
 
<QR_Check>:
    name : "qr"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    BoxLayout:
        orientation: 'vertical'
        ZBarCam:
            id: zbarcam
            # optional, by default checks all types
            code_types: ZBarSymbol.QRCODE, ZBarSymbol.EAN13
        Label:
            size_hint: None, None
            size: self.texture_size[0], 50
            text: ', '.join([str(symbol.data) for symbol in zbarcam.symbols])
    MDRoundFlatButton:
        text: "Back"
        pos_hint : {"center_x":0.7, "center_y":0.1}
        on_press : 
            root.manager.current = "drawer"

    
<Database>:
    name : "database" 
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos

    second : second
    color : color

    MDTextField:
        id : second
        hint_text : "Please input the duration (in sec)"
        icon_right : "language-python"
        helper_text : "example : 14sec"
        helper_text_mode : "on_focus"
        pos_hint : {"center_x": 0.5, "center_y": 0.6}
        size_hint_x:None
        width :400
        font_size : 15    
    MDTextField:
        id : color
        hint_text : "Please input the color (in 1 to 5)"
        icon_right : "language-python"
        helper_text : "example : two"
        helper_text_mode : "on_focus"
        pos_hint : {"center_x": 0.5, "center_y": 0.4}
        size_hint_x:None
        width :400
        font_size : 15   
    

    MDRoundFlatButton:
        text: "Submit"
        font_style : "BUTTON STYLE"
        pos_hint : {"center_x":0.3, "center_y":0.25}
        on_press : 
            root.submit()
            root.manager.current = "result"

    MDRoundFlatButton:
        text: "Back"
        pos_hint : {"center_x":0.7, "center_y":0.25}
        on_press : 
            root.manager.current = "drawer"
            

    
        
<Result>:
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    name : "result"

    MDRectangleFlatButton:
        text : "Please go to the users.txt to see the result."
        pos_hint : {"center_x": 0.5, "center_y": 0.5}

    

    MDRoundFlatButton:
        text: "Back to Menu"
        pos_hint : {"center_x":0.8, "center_y":0.1}
        on_press : 
            root.manager.transition.direction = "right"
            app.root.current = "database"
            root.manager.current = "drawer"
    
 
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

<Color_Dark>:
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    name: "color_dark"
    BoxLayout:
        orientation: 'vertical'
        spacing: "15dp"
        padding: "15dp"
        Image : 
            source : "trimmed.png"
            pos_hint : {"center_x": 0.5, "center_y": 0.3}
            size_hint : None, None
            width : 250
            height : 200
            allow_stretch: True
            keep_ratio : False
        MDFlatButton:
            text: "Color(Scale from 1 to 5 ,   1 being the lightest)?"
        
        MDRoundFlatButton:
            text: "1"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "great"
            on_press :
                print("1")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "2"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "good"
            on_press :
                print("2")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "3"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "mid"
            on_press :
                print("3")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "4"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "low"
            on_press :
                print("4")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "5"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "worse"
            on_press :
                print("5")
            font_stryle : "Subtitle"
            size_hint_y : None
        ScrollView
        MDRoundFlatButton:
            text:"Back"
            pos_hint : {"center_x": 0.7, "center_y": 0.3}
            on_press: 
                root.manager.transition.direction = "right"
                root.manager.current = "drawer"

<Color_Medium>:
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    name: "color_medium"
    BoxLayout:
        orientation: 'vertical'
        spacing: "15dp"
        padding: "15dp"
        Image : 
            source : "trimmed.png"
            pos_hint : {"center_x": 0.5, "center_y": 0.3}
            size_hint : None, None
            width : 250
            height : 200
            allow_stretch: True
            keep_ratio : False
        MDFlatButton:
            text: "Color(Scale from 1 to 5 ,   1 being the lightest)?"
        
        MDRoundFlatButton:
            text: "1"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "great"
            on_press :
                print("1")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "2"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "good"
            on_press :
                print("2")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "3"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "mid"
            on_press :
                print("3")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "4"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "low"
            on_press :
                print("4")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "5"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "worse"
            on_press :
                print("5")
            font_stryle : "Subtitle"
            size_hint_y : None
        ScrollView
        MDRoundFlatButton:
            text:"Back"
            pos_hint : {"center_x": 0.7, "center_y": 0.3}
            on_press: 
                root.manager.transition.direction = "right"
                root.manager.current = "drawer"

<Color_Good>:
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    name: "color_good"
    BoxLayout:
        orientation: 'vertical'
        spacing: "15dp"
        padding: "15dp"
        Image : 
            source : "trimmed.png"
            pos_hint : {"center_x": 0.5, "center_y": 0.3}
            size_hint : None, None
            width : 250
            height : 200
            allow_stretch: True
            keep_ratio : False
        MDFlatButton:
            text: "Color(Scale from 1 to 5 ,   1 being the lightest)?"
        
        MDRoundFlatButton:
            text: "1"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "great"
            on_press :
                print("1")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "2"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "good"
            on_press :
                print("2")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "3"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "mid"
            on_press :
                print("3")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "4"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "low"
            on_press :
                print("4")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "5"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "worse"
            on_press :
                print("5")
            font_stryle : "Subtitle"
            size_hint_y : None
        ScrollView
        MDRoundFlatButton:
            text:"Back"
            pos_hint : {"center_x": 0.7, "center_y": 0.3}
            on_press: 
                root.manager.transition.direction = "right"
                root.manager.current = "drawer"

<Color_Best>:
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    name: "color_best"
    BoxLayout:
        orientation: 'vertical'
        spacing: "15dp"
        padding: "15dp"
        Image : 
            source : "trimmed.png"
            pos_hint : {"center_x": 0.5, "center_y": 0.3}
            size_hint : None, None
            width : 250
            height : 200
            allow_stretch: True
            keep_ratio : False
        MDFlatButton:
            text: "Color(Scale from 1 to 5 ,   1 being the lightest)?"
        
        MDRoundFlatButton:
            text: "1"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "great"
            on_press :
                print("1")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "2"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "good"
            on_press :
                print("2")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "3"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "mid"
            on_press :
                print("3")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "4"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "low"
            on_press :
                print("4")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "5"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "worse"
            on_press :
                print("5")
            font_stryle : "Subtitle"
            size_hint_y : None
        ScrollView
        MDRoundFlatButton:
            text:"Back"
            pos_hint : {"center_x": 0.7, "center_y": 0.3}
            on_press: 
                root.manager.transition.direction = "right"
                root.manager.current = "drawer"

<Upload>:
    name: "upload" 
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
            source : "hourglass.png"
            pos_hint : {"center_x": 0.5, "center_y": 0.3}
            size_hint : None, None
            width : 150
            height : 100
            allow_stretch: True
            keep_ratio : False
        MDFlatButton:
            text: "For How Long?"
        MDRoundFlatButton:
            text: "5 sec"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "color_dark"
            on_press :
                print("5 seconds")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "10 sec"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "color_medium"
            on_press :
                print("10 seconds")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "15 sec"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "color_good"
            on_press :
                print("15 seconds")
            font_stryle : "Subtitle"
            size_hint_y : None
        MDRoundFlatButton:
            text: "more than 15 sec"
            pos_hint : {"center_x": 0.5}
            on_press :
                root.manager.current = "color_best"
            on_press :
                print("15 seconds or more")
            font_stryle : "Subtitle"
            size_hint_y : None
        
        ScrollView
        MDRoundFlatButton:
            text:"Back"
            pos_hint : {"center_x": 0.7 ,"center_y":0.3}
            on_press: 
                root.manager.transition.direction = "right"
                root.manager.current = "drawer"

<Great>:
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    name : "great"
    MDRoundFlatButton:
        text: "Great! You are doing OK. Well Hydrated. Drink water as normal."
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.5}
    MDRoundFlatButton:
        text: "Press Here to go Back"
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.3}
        on_press : root.manager.current = "drawer"

<Good>:
    name : "good"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    MDRoundFlatButton:
        text: "Good!! You are Fine!! You could start to drink a little more water!"
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.5}
    MDRoundFlatButton:
        text: "Press Here to go Back"
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.3}
        on_press : root.manager.current = "drawer"
<Mid>:
    name : "mid"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    MDRoundFlatButton:
        text: "Drink about 1/2 bottle of water (250ml) within an hour!!"
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.5}
    MDRoundFlatButton:
        text: "Press Here to go Back"
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.3}
        on_press : root.manager.current = "drawer"

<Low>:
    name : "low"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    MDRoundFlatButton:
        text: "Drink about 1/2 bottle of water (250ml) right now!! "
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.5}
    MDRoundFlatButton:
        text: "Press Here to go Back"
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.3}
        on_press : root.manager.current = "drawer"

<Worse>:
    name : "worse"
    canvas : 
        Color: 
            rgb: utils.get_color_from_hex("#FEFEFE")
        Rectangle :
            size : self.size
            pos : self.pos
    MDRoundFlatButton:
        text: "Drink 2 bottles of water right now (1,000ml)!!!"
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.5}
    MDRoundFlatButton:
        text: "Press Here to go Back"
        halign : "center"
        pos_hint : {"center_x":0.5, "center_y": 0.3}
        on_press : root.manager.current = "drawer"
        

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
                source : "man.png"
            Image : 
                source : "man.png"
            Image : 
                source: "man.png"
        GridLayout:
            rows : 1
            pos_hint : {"top" : 0.5, "left": 1}
            size_hint : 1, 0.1
            Image : 
                source : "man.png"
            Image : 
                source : "man.png"
            Image : 
                source : "man.png"
            
        GridLayout:
            
            rows : 1
            pos_hint : {"top": 0.3 , "left":1}
            size_hint : 1, 0.1
            Image : 
                source : "man.png"
            Image : 
                source : "man.png"
            Image : 
                source : "man.png"

        

    
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
                        source : "제목 없음.png"
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
                                text: 'Upload'
                                color : (1,1,1,1)
                                on_press :
                                    root.manager.transition.direction = "left"
                                    root.manager.current = "upload"
                                IconLeftWidget:
                                    icon : "cloud-upload"
                            OneLineIconListItem:
                                text: 'Results'
                                color : (1,1,1,1)
                                on_press :
                                    root.manager.current = "database"
                                IconLeftWidget:
                                    icon : "language-python"
                            OneLineIconListItem:
                                text: 'QR_Scan'
                                color : (1,1,1,1)
                                on_press :
                                    root.manager.current = "qr"
                                IconLeftWidget:
                                    icon : "qrcode-scan"
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
