import arcade
import serverclient

class Vindue (serverclient.ServerWindow):
	textOnServer = "message";
	playerX = 200;
	playerY = 200;
	speed = 15;
	def __init__(self, width, height):
		super().__init__("localhost",width, height)


	def on_message_received (self, client, message):
		self.textOnServer = message;

		

	def on_draw(self):
		arcade.start_render()
		# arcade.draw_text(self.textOnServer, 100, 100, arcade.color.WHITE, 20)


		arcade.draw_circle_filled(self.playerX, self.playerY, 20, arcade.color.WHITE)

		if self.textOnServer == "w":
			self.playerY = self.playerY + self.speed

		if self.textOnServer == "a":
			self.playerX = self.playerX - self.speed

		if self.textOnServer == "s":
			self.playerY = self.playerY - self.speed

		if self.textOnServer == "d":
			self.playerX = self.playerX + self.speed

if __name__ == "__main__":
	vindue = Vindue(800, 600)
	arcade.run()