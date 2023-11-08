# Import necessary modules from Kivy and KivyMD
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

# Define your main application class
class MainApp(MDApp):
    # The build method is where the application interface is constructed
    def build(self):
        # Set the primary color palette to "DeepPurple"
        self.theme_cls.primary_palette = "DeepPurple"
        # Load the user interface layout defined in 'login.kv' file
        return Builder.load_file('login.kv')
    
    # Function to handle the "Log In" button press
    def logger(self):
        # Update the welcome label 
        self.root.ids.welcome_label.text = f'Hii {self.root.ids.user.text}!'

    # Function to handle the "Clear" button press
    def clear(self):
        # Reset the welcome label to its initial state
        self.root.ids.welcome_label.text = "WELCOME"
        # Clear the user and password input fields
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""


MainApp().run()
