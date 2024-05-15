import tkinter as tk
from GUI_Helper import GUI_Helper
from helper import Helper
from board import Board
import copy

class BoardWindow:
    def __init__(self):
        self.board = Board()
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.blackScore = 0
        self.whiteScore = 0
        self.blackScore_label = None
        self.whiteScore_label = None
        self.level = 0
        self.gameTerminate = 0
        self.result = ""



    def resultWindow(self, window):
        global image1_result, image2_result

        self.result_window = tk.Toplevel(window)
        self.result_window.title("Othello Game")
        board_window_width = 1000
        board_window_height = 500
        GUI_Helper.center_window(self.result_window, board_window_width, board_window_height)

        top_border = tk.Frame(self.result_window, bg="#009067", height=15)
        top_border.pack(fill="x", side="top")
        down_border = tk.Frame(self.result_window, bg="#009067", height=15)
        down_border.pack(fill="x", side="bottom")

        frame1_board = tk.Frame(self.result_window, bg="white", width=board_window_width)
        frame1_board.pack(fill="x")
        frame2_board = tk.Frame(self.result_window, bg="white", width=board_window_width)
        frame2_board.pack(fill="x",expand=True)

        image1_result = tk.PhotoImage(file="Images/logo.png").subsample(7)
        image2_result = tk.PhotoImage(file="Images/image1.png").subsample(2)
        label_image1_board = tk.Label(frame1_board, image=image1_result, bg="white")
        label_image1_board.pack(side="left", padx=(10, 0), pady=(20, 1))
        label_image2_board = tk.Label(frame1_board, image=image2_result, bg="white")
        label_image2_board.pack(side="left", padx=(0, 1), pady=(20, 1))


        label_result = tk.Label(frame2_board, text=f"{self.result}", bg = "white", fg="black", font=("Arial",50,"bold"))
        label_result.pack(padx=50, pady=(90,180))


        self.result_window.grid_rowconfigure(0, weight=1)
        self.result_window.grid_rowconfigure(1, weight=2)
        frame1_board.grid_columnconfigure(0, weight=1)
        frame2_board.grid_columnconfigure(0, weight=1)



    def boardWindow(self,button_id, window):
        global image1_board, image2_board, whiteImage, blackImage
        if(button_id == 1):
            self.level = 1
        elif(button_id == 2):
            self.level = 3
        elif(button_id == 3):
            self.level = 5


        self.board_window = tk.Toplevel(window)
        self.board_window.title("Othello Game")
        board_window_width = 1300
        board_window_height = 750
        GUI_Helper.center_window(self.board_window, board_window_width, board_window_height)

        top_border = tk.Frame(self.board_window, bg="#009067", height=15)
        top_border.pack(fill="x", side="top")
        down_border = tk.Frame(self.board_window, bg="#009067", height=15)
        down_border.pack(fill="x", side="bottom")

        frame1_board = tk.Frame(self.board_window, bg="white", width=board_window_width)
        frame1_board.pack(fill="x")
        frame2_board = tk.Frame(self.board_window, bg="white", width=board_window_width)
        frame2_board.pack(fill="x")
        frame2_board_left = tk.Frame(frame2_board, bg="white", width=board_window_width // 4)
        frame2_board_left.pack(side="left", fill="both", expand=True)
        frame2_board_right = tk.Frame(frame2_board, bg="white", width=3 * (board_window_width // 4))
        frame2_board_right.pack(side="left", fill="both", expand=True)
        frame2_board_left_up = tk.Frame(frame2_board_left, bg="white", width=board_window_width // 4)
        frame2_board_left_up.pack(side="top", fill="both", expand=True)
        frame2_board_left_down = tk.Frame(frame2_board_left, bg="white", width=board_window_width // 4)
        frame2_board_left_down.pack(side="top", fill="both", expand=True)
        image1_board = tk.PhotoImage(file="Images/logo.png").subsample(7)
        image2_board = tk.PhotoImage(file="Images/image1.png").subsample(2)
        label_image1_board = tk.Label(frame1_board, image=image1_board, bg="white")
        label_image1_board.pack(side="left", padx=(10, 0), pady=(20, 1))
        label_image2_board = tk.Label(frame1_board, image=image2_board, bg="white")
        label_image2_board.pack(side="left", padx=(0, 1), pady=(20, 1))
        canvas = tk.Canvas(frame2_board_right, width=600, height=600)
        canvas.pack(side="left", padx=(20, 50), pady=(50, 25))


        whiteImage = tk.PhotoImage(file="Images/white.png").subsample(4)
        blackImage = tk.PhotoImage(file="Images/black.png").subsample(4)
        label_black_board = tk.Label(frame2_board_left_up, image=blackImage, bg="white")
        label_black_board.pack(side="left", padx=(100, 5), pady=(20, 1))
        self.blackScore_label = tk.Label(frame2_board_left_up, text="2", bg="white", fg="black",font=("Arial", 22))
        self.blackScore_label.pack(padx=50, pady=(70, 10), side="left")
        label_white_board = tk.Label(frame2_board_left_down, image=whiteImage, bg="white")
        label_white_board.pack(side="left", padx=(100, 5), pady=(20, 1))
        self.whiteScore_label = tk.Label(frame2_board_left_down, text="2", bg="white", fg="black",font=("Arial", 22))
        self.whiteScore_label.pack(padx=50, pady=(30, 50), side="left")

        for i in range(8):
            for j in range(8):
                button = tk.Button(canvas, bg="#009067", width=8, height=4,
                                   command=lambda x=i, y=j: self.button_click(x, y, window))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
        self.updateGUI()

        self.board_window.grid_rowconfigure(0, weight=1)
        self.board_window.grid_rowconfigure(1, weight=2)
        frame1_board.grid_columnconfigure(0, weight=1)
        frame2_board.grid_columnconfigure(0, weight=1)

    def button_click(self, x, y, window):

        if Helper.validMove(self.board.grid, x, y, 1):
            self.gameTerminate = 0
            print(f"Player move at ({x}, {y})")
            self.board.black -= 1
            self.board.grid = Helper.getMove(self.board.grid, x, y, 1)
            self.updateGUI()
            
            self.board_window.after(500, self.trigger_computer_move, window)  # Delay computer move by 1000ms

    def trigger_computer_move(self,window):
        print("Computer's turn.")
        resultBoard = copy.deepcopy(self.board.grid)
        Helper.AlphaBeta(self.board.grid, self.level, False, Helper.negative_infinity, Helper.infinity, self.board.grid, Helper.infinity, resultBoard)
        if resultBoard == self.board.grid:
            print("Computer has no valid moves.")
            self.gameTerminate += 1
            if self.gameTerminate == 2 or self.board.black == 0 or self.board.white == 0:
                self.result = Helper.check_winner(self.board.grid)
                self.resultWindow(window)
                print(self.result)
                self.board_window.destroy()
                return

        self.board.grid = resultBoard
        self.board.white -= 1
        self.updateGUI()
        list = Helper.getAllMoves(self.board.grid, 1)
        if (len(list) == 0):
            print("Player has no valid moves.")
            self.trigger_computer_move(window)
        print("Computer has made a move.")
        self.gameTerminate = 0

    def updateGUI(self):
        blackScore = whiteScore = 0  # Reset scores before recount
        for i in range(8):
            for j in range(8):
                self.buttons[i][j].config(state=tk.NORMAL if Helper.validMove(self.board.grid, i, j, 1) else tk.DISABLED)
                if self.board.grid[i][j] == 1:
                    self.buttons[i][j].config(text="", bg="black")
                    blackScore += 1
                elif self.board.grid[i][j] == 2:
                    self.buttons[i][j].config(text="", bg="white")
                    whiteScore += 1
                else:
                    self.buttons[i][j].config(text="", bg="#009067")

        self.blackScore_label.config(text=f"{blackScore}")
        self.whiteScore_label.config(text=f"{whiteScore}")
        print("GUI updated.")

