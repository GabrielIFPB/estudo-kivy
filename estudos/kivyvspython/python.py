
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('1.11.1')


class Tela(BoxLayout):
	
	def on_press_bt(self):
		win.root_window.remove_widget(win.root)
		win.root_window.add_widget(Tela2())
	
	def __init__(self, **kwargs):
		super(Tela, self).__init__(**kwargs)
		self.orientation = "vertical"
		bt1 = Button(text='Clique')
		bt1.on_press = self.on_press_bt
		self.add_widget(bt1)
		self.add_widget(Button(text='bt2'))
		self.add_widget(Button(text='bt3'))


class Tela2(BoxLayout):
	
	def on_press_bt(self):
		win.root_window.remove_widget(win.root)
		win.root_window.add_widget(Tela())
	
	def __init__(self, **kwargs):
		super(Tela2, self).__init__(**kwargs)
		self.orientation = "horizontal"
		bt1 = Button(text='Clique')
		bt1.on_press = self.on_press_bt
		self.add_widget(bt1)
		self.add_widget(Button(text='bt2'))
		self.add_widget(Button(text='bt3'))


class Kv(App):

	def build(self):
		return Tela()


win = Kv()
win.run()
