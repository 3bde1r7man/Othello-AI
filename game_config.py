class GameConfig:
    def __init__(self, player_color="black", play_mode="human_vs_computer", computer_level=1):
        self.player_color = player_color
        self.play_mode = "human_vs_computer"
        self.computer_level = computer_level
        print(player_color,computer_level)
