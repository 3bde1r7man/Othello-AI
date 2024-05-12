from helper import Helper

class GUI_Helper:
    @staticmethod
    def updateGUI(board,buttons,whiteScore,blackScore,whiteScore_label, blackScore_label ,params=None):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    buttons[i][j].config(text="", bg="black")
                    blackScore += 1
                    blackScore_label.config(text=f"{blackScore}")
                elif board[i][j] == 2:
                    buttons[i][j].config(text="", bg="white")
                    whiteScore += 1
                    whiteScore_label.config(text=f"{whiteScore}")
                elif board[i][j] == 0:
                    buttons[i][j].config(text="", bg="#009067")
        print("GUI should update now")
        for i in range(8):
            for j in range(8):
                if not (Helper.validMove(self.board.grid, i, j, 1)):
                    self.buttons[i][j].config(state=tk.DISABLED)




    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")


    @staticmethod
    def button_click(x, y, board,buttons,whiteScore,blackScore,whiteScore_label, blackScore_label, player_turn):
        if Helper.validMove(board, x, y, 1) and player_turn == True:
            print(f"Button clicked at ({x}, {y})")
            board = Helper.getMove(board, x, y, 1)
            GUI_Helper.updateGUI(board,buttons,whiteScore,blackScore,whiteScore_label, blackScore_label)
            player_turn = False
