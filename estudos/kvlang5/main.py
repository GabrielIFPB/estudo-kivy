
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.11.1')


def funcSelf(x):
	print("funcSelf")


Button.funcSelf = funcSelf


class MinhaTela(BoxLayout):
	
	def funcRoot(self):
		print("funcRoot")


class EstudoApp(App):
	
	def funcApp(self):
		print("funcApp")


win = EstudoApp()
win.run()
