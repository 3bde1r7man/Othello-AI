from game import Game
from interfaces.console_display import ConsoleDisplay
from interfaces.gui_display import GUIDisplay

def main():
    game = Game()
    game.add_observer(ConsoleDisplay())  # Switch to GUIDisplay() for GUI version
    game.setup_game()
    game.start()

if __name__ == "__main__":
    main()
