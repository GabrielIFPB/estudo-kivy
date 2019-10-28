
import kivy
from kivy.app import App
from kivy.lang import Builder

kivy.require('1.11.1')

code = """

BoxLayout:
	Button:
		text: "1"
	Button:
		text: "2"
"""

# Builder.load_file("path")


class EstudoApp(App):
	
	def build(self):
		return Builder.load_string(code)


win = EstudoApp()
win.run()
