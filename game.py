from board import Board
from player import Player
from human_strategy import HumanStrategy
from computer_strategy import ComputerStrategy

class Game:
    def __init__(self):
        # self.board = Board()
        self.observers = []
        self.players = []

    def add_observer(self, observer):
        self.observers.append(observer)
        observer.mainWindow()

    def notify_all(self):
        for observer in self.observers:
            observer.update()

    def setup_game(self):
        # Placeholder - setup based on input
        self.initialize_players()

    def initialize_players(self):
        human = Player("black", HumanStrategy())
        ai = Player("white", ComputerStrategy())
        self.players = [human, ai]  # Customize as needed

    def start(self):
        # Placeholder - main game loop
        pass
