
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button

kivy.require('1.11.1')


class Tela(BoxLayout):

	def on_press_bt(self):
		ax = win.root_window.remove_widget(win.root)
		ax = win.root_window.add_widget(Tela2())


class Tela2(BoxLayout):

	def on_press_bt(self):
		ax = win.root_window.remove_widget(win.root)
		ax = win.root_window.add_widget(Tela())


class Kv(App):
	pass
	# def build(self):
	# 	return Tela()


win = Kv()
win.run()
