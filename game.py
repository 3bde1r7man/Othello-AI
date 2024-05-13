from board import Board


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



