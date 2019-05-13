import arcade
import serverclient

class Vindue (serverclient.ClientWindow):
	textOnScreen = "";
	textPostion = [];

	def __init__(self, width, height):
		super().__init__("localhost", "EnterYourName", width, height)
	
	def on_draw(self):
		arcade.start_render();
		arcade.draw_text(self.textOnScreen, 100, 100, arcade.color.WHITE, 20)


	def on_key_press(self, key, modifier):
		
		#if on_key_press == true:
		self.textOnScreen = chr(key)
		self.send(self.textOnScreen);

	def on_key_release(self, key, modifier):

		self.textOnScreen = "o"
		self.send(self.textOnScreen);
				







if __name__ == "__main__":
	vindue = Vindue(800, 600)
	arcade.run()