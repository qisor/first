import tkinter as tk

class CaluTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("计算器")
        self.caleMainWindow()

    def caleMainWindow(self):
        # self.initWindowName.title("计算器 v0.1")
        self.initWindowName=tk.Grid()
        self.inputNumLable=tk.Label(text="请输入数据：")
        self.inputNumLable.grid(row=0, column=0)
        self.result_data_label = tk.Label( text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = tk.Label( text="日志")
        self.log_label.grid(row=12, column=0)


numl = [1, 4, 6, 7, 8, 9, 3]
app = CaluTk()
app.mainloop()
