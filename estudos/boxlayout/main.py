
from kivy.app import App
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder

kvcode = """
BoxLayout:
	orientation: "vertical"
	padding: 20
	spacing: 50

	Button:
		size_hint: 1., 1.
		text: "A"
	Button:
		size_hint: 1., 1.
		text: "B"
	Button:
		size_hint: 1., 1.
		text: "C"
"""


class JanelaApp(App):
	
	def build(self):
		return Builder.load_string(kvcode)


janela = JanelaApp()

ji = InteractiveLauncher(janela)

ji.run()

