import arcade
import serverclient

class Vindue (serverclient.ServerWindow):
	textOnServer = "message";
	def __init__(self, width, height):
		super().__init__("localhost",width, height)


	def on_message_received (self, client, message):
		self.textOnServer = message;
	def on_draw(self):
		arcade.start_render()
		arcade.draw_text(self.textOnServer, 100, 100, arcade.color.WHITE, 20)
if __name__ == "__main__":
	vindue = Vindue(800, 600)
	arcade.run()