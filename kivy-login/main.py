from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import *
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import *
import webbrowser

#inverts hex color
def inv_hex(color):
    # strip the # from the beginning
    color = color[1:]
 
    # convert the string into hex
    color = int(color, 16)
    comp_color = 0xFFFFFF ^ color
 
    # convert the color back to hex by prefixing a #
    comp_color = "#%06X" % comp_color
 
    return comp_color

class LoginScreen(Screen):
	
    #theme_cls can be Dark, Light or leave blank for system
    def __init__(self, theme_cls, **kw):
        super().__init__(**kw)
        self.theme_cls = theme_cls
        
       
    def show_alert_dialog(self, after_accepting):
        def _rejected(_=None): toast("We are sorry but to keep our community safe you have to agree to our TOS and PP.");self.dialog.dismiss()
        def _aggred(_=None): after_accepting(); self.dialog.dismiss()
        def _read(_=None): webbrowser.open("https://google.com/tos")

        self.dialog = MDDialog(
            text="We want to keep our community safe, please take a moment and read our privacy policy and terms of service.",
            buttons=[
                MDFlatButton(
                    text="I AGREE",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=_aggred
                ),
                MDFlatButton(
                    text="DISAGREE",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=_rejected
                ),
                MDFlatButton(
                    text="READ",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=_read
                ),
            ],
        )
        self.dialog.open(animation=True)


    def do_login(self, *args):
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        toast(email + " " + password)

    def do_google_login(self, *args):
        toast("Google login!")
        
    
    def do_facebook_login(self, *args):
        toast("Facebook login!")

    def do_apple_login(self, *args):
        toast("Apple login!")

class LayoutApp(MDApp):
    def build(self):
		#by using a manager you can add multiple screens and switch around them easly
        manager = ScreenManager(transition=NoTransition())
        self.theme_cls.theme_style = "Dark"
        manager.add_widget(LoginScreen('self.theme_cls'))

        return manager
    #this makes sure that the label wll be white on dark theme and black on light theme
    def get_color_for_theme(self, color):
        if self.theme_cls.theme_style == "Dark": 
            return inv_hex(color)
        return color

if __name__ == '__main__':
    LayoutApp().run()