from kivy.app import App
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder

kvcode = """

StackLayout:

	orientation: "bt-rl"

	Button:
		size_hint: .33, .1
		text: "A"
	Button:
		size_hint: .33, .1
		text: "B"
	Button:
		size_hint: .33, .1
		text: "C"
"""


class JanelaApp(App):
	
	def build(self):
		return Builder.load_string(kvcode)


janela = JanelaApp()

ji = InteractiveLauncher(janela)

ji.run()

