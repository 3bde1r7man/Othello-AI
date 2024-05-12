from game import Game
from console_display import ConsoleDisplay
from gui_display import GUIDisplay
import game_config

def main():
    game = Game()
    game.add_observer(GUIDisplay())  # Switch to GUIDisplay() for GUI version
    game.setup_game()
    game.start()

if __name__ == "__main__":
    main()
