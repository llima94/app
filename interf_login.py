from app import App
from kivy.uix.button import button
from kivy.lang import Builder
 
###painel grafico
 
class aplicativo (App):
    def  build (self):
        return Button()

### tela login

class login.app (App):
	def build (self):
		main_widget = buider.load_string (main_widget_kv):
		return main_widget
		
	def login(self):
		usuario = self.root.ids.usuario.text
		senha = self.root.ids.senha.text
###implementa resgras para acesso :

		if usuario == 'admin' and senha == 'admin':
            pass
			
			
login.app().run()		
aplicativo().run()
