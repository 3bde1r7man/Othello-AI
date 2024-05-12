import tkinter as tk
from GUI_Helper import GUI_Helper
from boardWindow import BoardWindow

class GUIDisplay:
    def __init__(self):
        self.NewBoardWindow = BoardWindow()

    def update(self, params=None):
        GUI_Helper.updateGUI(self.NewBoardWindow.board.grid,self.NewBoardWindow.buttons,self.NewBoardWindow.whiteScore,self.NewBoardWindow.blackScore)
        print("GUI should update now")


    def createBoardWindow(self, level, color, window):
        NewBoardWindow2 = BoardWindow()
        level= level
        color = color
        window = window
        
        NewBoardWindow2.boardWindow(level, color, window)

    def mainWindow(self):
        window = tk.Tk()
        window_width = 1200
        window_height = 750
        window.title("Home page")
        GUI_Helper.center_window(window, window_width, window_height)

        top_border = tk.Frame(window, bg="#009067", height=15)
        top_border.pack(fill="x", side="top")

        down_border = tk.Frame(window, bg="#009067", height=15)
        down_border.pack(fill="x", side="bottom")

        frame1 = tk.Frame(window, bg="white", width=window_width)
        frame1.pack(fill="x")
        frame2 = tk.Frame(window, bg="white", width=window_width)
        frame2.pack(fill="x")
        frame3 = tk.Frame(window, bg="white", width=window_width)
        frame3.pack(fill="both", expand=True)

        image1 = tk.PhotoImage(file="Images/logo.png").subsample(7)
        image2 = tk.PhotoImage(file="Images/image1.png").subsample(2)

        label_image1 = tk.Label(frame1, image=image1, bg="white")
        label_image1.pack(side="left", padx=(10, 0), pady=(20, 1))

        label_image2 = tk.Label(frame1, image=image2, bg="white")
        label_image2.pack(side="left", padx=(0, 1), pady=(20, 1))

        radio_var = tk.StringVar(value="white")
        radio_button1 = tk.Radiobutton(frame2, variable=radio_var, value="white", bg="white", fg="black")
        radio_button1.pack(side="left", padx=(window_width // 2, 0), pady=(50, 100))

        whitePiece = tk.PhotoImage(file="Images/white.png").subsample(8)
        label_white = tk.Label(frame2, image=whitePiece, bg="white")
        label_white.pack(side="left", padx=(0, 40), pady=(20, 60))

        radio_button2 = tk.Radiobutton(frame2, variable=radio_var, value="black", font=("Arial", 14), bg="white",
                                       fg="black")
        radio_button2.pack(side="left", padx=(window_width / 12, 0), pady=(50, 100))

        blackPiece = tk.PhotoImage(file="Images/black.png").subsample(8)
        label_black = tk.Label(frame2, image=blackPiece, bg="white")
        label_black.pack(side="left", padx=(0, 40), pady=(20, 60))

        levels = ["Easy", "Medium", "Hard"]
        for i in range(1, 4):
            button = tk.Button(frame3, text=levels[i - 1] + " Level", bg="#009067", fg="white",
                               font=("Arial", 22, "bold"), relief="raised", borderwidth=10, highlightthickness=0,
                               command=lambda level=i: self.createBoardWindow(level, radio_var.get(), window))
            if i == 3:
                button.pack(side="top", padx=(window_width // 3, window_width // 3), pady=(10, 50), fill="both",
                            expand=True)
            else:
                button.pack(side="top", padx=(window_width // 3, window_width // 3), pady=10, fill="both", expand=True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_rowconfigure(1, weight=1)
        window.grid_rowconfigure(2, weight=2)

        frame1.grid_columnconfigure(0, weight=1)
        frame2.grid_columnconfigure(0, weight=1)
        frame3.grid_columnconfigure(0, weight=1)
        window.mainloop()



