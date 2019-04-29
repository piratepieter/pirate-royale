import arcade
import serverclient

class Vindue (serverclient.ServerWindow):
	def __init__(self, width, height):
		super().__init__("localhost",width, height)

if __name__ == "__main__":
	vindue = Vindue(800, 600)
	arcade.run()