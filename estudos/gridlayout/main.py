
from kivy.app import App
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder

kvcode = """
GridLayout:
	cols: 3
	rows: None
	row_default_height: 50
	row_force_default: True
	# col_default_width: 50
	# col_force_default: True
	Button:
		# size_hint: .1, None
		size_hint: None, .1
		text: "A"
	Button:
		# size_hint: .33, .1
		text: "B"
	Button:
		# size_hint: .1, None
		text: "C"
	Button:
		# size_hint: .33, .1
		size_hint: None, .1
		text: "D"
	Button:
		# size_hint: .33, .1
		text: "E"
	Button:
		# size_hint: .33, .1
		text: "F"
	Button:
		# size_hint: .1, None
		size_hint: None, .1
		text: "G"
"""


class JanelaApp(App):
	
	def build(self):
		return Builder.load_string(kvcode)


janela = JanelaApp()

ji = InteractiveLauncher(janela)

ji.run()

