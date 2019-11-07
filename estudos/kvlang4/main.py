
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.11.1')


class MinhaTela(BoxLayout):
	
	def click(self):
		print("oi")
		self.ids.lb1.text = ""
		self.ids.lb2.text = "10"


class EstudoApp(App):
	pass


win = EstudoApp()
win.run()
