import tkinter


# root = tkinter.Tk()
# bt = tkinter.Button(root, text="windows")
# bt.config(print("你好呀"))
# bt.pack(padx=200, pady=100)
# root.title("TK窗口")
# root.mainloop()
class TKwondows(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("operation")
        self.mainWin()

    def mainWin(self):
        self.bt = tkinter.Button(self, text="按键1")
        self.bt.pack(padx=200, pady=100)
        self.bt.config(command=self.tellYou)

    def tellYou(self):
        print("nihao")


if __name__ == "__main__":
    app = TKwondows()
    app.mainloop()
