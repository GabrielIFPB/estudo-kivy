
# coding: utf-8

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

kivy.require('1.11.1')


class RootWidget(FloatLayout):
	pass


class MedidaApp(App):
	
	def build(self):
		return RootWidget()


MedidaApp().run()
