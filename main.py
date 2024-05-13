from game import Game
from gui_display import GUIDisplay

def main():
    game = Game()
    game.add_observer(GUIDisplay())  # Switch to GUIDisplay() for GUI version

if __name__ == "__main__":
    main()
