import hashlib
import os
import time
from tkinter import Tk, Label, Text, Button, END, StringVar, W, E
from tkinter.ttk import Combobox

LOG_LINE_NUM = 0

log_file = os.path.join(os.path.dirname(__file__), "log.txt")


def get_current_time():
    """
    :func :  获取当前时间
    :return: current time
    """
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time


def write_logs(msg):
    with open(log_file, mode="a", encoding="utf8", errors="ignore") as fp:
        fp.write(msg + "\n")


class TkWindow(Tk):
    def __init__(self):
        super().__init__()
        self.xVariable = StringVar()
        self.xVariable1 = StringVar()
        self.xVariable2 = StringVar()
        self.xVariable3 = StringVar()
        self.init_data_label = Label(self, text="选项配置")
        self.combox = Combobox(self, textvariable=self.xVariable, width=6)
        self.init_data_label1 = Label(self, text="选项配置1")
        self.combox1 = Combobox(self, textvariable=self.xVariable1, width=6)
        self.init_data_label2 = Label(self, text="选项配置2")
        self.combox2 = Combobox(self, textvariable=self.xVariable2, width=6)
        self.init_data_label3 = Label(self, text="选项配置3")
        self.combox3 = Combobox(self, textvariable=self.xVariable3, width=6)

        self.init_input_label = Label(self, text="输入地址")
        self.init_input_Text = Text(self, width=78, height=8)  # 原始数据录入框
        self.init_input2_label = Label(self, text="输入地址2")
        self.init_input2_Text = Text(self, width=78, height=3)  # 原始数据录入框
        self.log_label = Label(self, text="日志")
        self.log_data_Text = Text(self, width=78, height=7)  # 日志框
        self.clear_button = Button(self, text="清除", bg="DodgerBlue", width=10, command=self.clear_data)
        self.click_button = Button(self, text="开始执行", bg="lightblue", width=10,
                                   command=self.begin_analyse)  # 调用内部方法  加()为直接调用

    def set_init_window(self):
        self.title("日志处理工具_v0.1")  # 窗口名
        self.geometry('551x370+430+350')  # 290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self["bg"] = "Orchid"  # 窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self.attributes("-alpha", 0.85)  # 虚化，值越小虚化程度越高
        self.combox["value"] = ["1", "2", "3"]
        self.combox.current(0)
        self.combox1["value"] = ["4", "5", "6"]
        self.combox1.current(0)
        self.combox2["value"] = ["7", "8", "9"]
        self.combox2.current(0)
        self.combox3["value"] = ["10", "11", "12"]
        self.combox3.current(2)
        # 标签
        self.init_data_label.grid(row=0, column=0, sticky=W)
        self.init_data_label1.grid(row=0, column=2, sticky=W)
        self.init_data_label2.grid(row=0, column=4, sticky=W)
        self.init_data_label3.grid(row=0, column=6, sticky=W)
        self.combox.grid(row=0, column=1, sticky=W)
        self.combox1.grid(row=0, column=3, sticky=W)
        self.combox2.grid(row=0, column=5, sticky=W)
        self.combox3.grid(row=0, column=7, sticky=W)
        self.combox.bind("<<ComboboxSelected>>", self.get_combox)  # #给下拉菜单绑定事件
        self.combox1.bind("<<ComboboxSelected>>", self.get_combox1)  # #给下拉菜单绑定事件
        self.combox2.bind("<<ComboboxSelected>>", self.get_combox2)  # #给下拉菜单绑定事件
        self.combox3.bind("<<ComboboxSelected>>", self.get_combox3)  # #给下拉菜单绑定事件

        self.init_input_label.grid(row=1, column=0, sticky=W)
        self.init_input_Text.grid(row=2, column=0, rowspan=5, columnspan=10, sticky=W)

        self.init_input2_label.grid(row=7, column=0, sticky=W)
        self.init_input2_Text.grid(row=8, column=0, rowspan=3, columnspan=10, sticky=W)

        self.log_label.grid(row=12, column=0, sticky=W)
        # 文本框
        self.log_data_Text.grid(row=13, column=0, rowspan=5, columnspan=10, sticky=W)

        # 按钮
        self.clear_button.grid(row=20, column=2, rowspan=11, sticky=W + E)
        self.click_button.grid(row=20, column=4, rowspan=11, sticky=W + E)

        # 功能函数

    def get_combox(self, event):
        self.combox.get()
        print(self.combox.get())  # #获取选中的值方法1
        print(self.xVariable.get())  # #获取选中的值方法2

    def get_combox1(self, event):
        self.combox1.get()
        print(self.combox1.get())  # #获取选中的值方法1
        print(self.xVariable1.get())  # #获取选中的值方法2

    def get_combox2(self, event):
        self.combox2.get()
        print(self.combox2.get())  # #获取选中的值方法1
        print(self.xVariable2.get())  # #获取选中的值方法2

    def get_combox3(self, event):
        self.combox3.get()
        print(self.combox3.get())  # #获取选中的值方法1
        print(self.xVariable3.get())  # #获取选中的值方法2

    def begin_analyse(self):
        new_location = self.init_input_Text.get(1.0, END).strip().replace("\n", " ").encode()
        nl = self.init_input_Text.get(1.0, END).strip().replace("\n", " ").split()
        print("src =", new_location)
        print(nl)
        if new_location:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(new_location)
                myMd5_Digest = myMd5.hexdigest()
                # print(myMd5_Digest)
                # 输出到界面
                self.init_input2_Text.delete(1.0, END)
                self.init_input2_Text.insert(1.0, myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.init_input2_Text.delete(1.0, END)
                self.init_input2_Text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

    def clear_data(self):
        write_logs(self.init_input_Text.get(1.0, END).strip().replace("\n", " "))
        write_logs(self.init_input2_Text.get(1.0, END).strip().replace("\n", " "))
        self.init_input_Text.delete("1.0", END)
        self.init_input2_Text.delete("1.0", END)
        self.log_data_Text.delete("1.0", END)

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        self.log_data_Text.insert(END, logmsg_in)
        write_logs(logmsg_in)
        # if LOG_LINE_NUM <= 11:
        #     self.log_data_Text.insert(END, logmsg_in)
        #     LOG_LINE_NUM = LOG_LINE_NUM + 1
        # else:
        #     self.log_data_Text.delete(1.0, 2.0)
        #     self.log_data_Text.insert(END, logmsg_in)


def main():
    window = TkWindow()  # 设置根窗口默认属性
    window.set_init_window()
    window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


main()

''' 背景色一览
#FFB6C1 LightPink 浅粉红
#FFC0CB Pink 粉红
#DC143C Crimson 深红/猩红
#FFF0F5 LavenderBlush 淡紫红
#DB7093 PaleVioletRed 弱紫罗兰红
#FF69B4 HotPink 热情的粉红
#FF1493 DeepPink 深粉红
#C71585 MediumVioletRed 中紫罗兰红
#DA70D6 Orchid 暗紫色/兰花紫
#D8BFD8 Thistle 蓟色
#DDA0DD Plum 洋李色/李子紫
#EE82EE Violet 紫罗兰
#FF00FF Magenta 洋红/玫瑰红
#FF00FF Fuchsia 紫红/灯笼海棠
#8B008B DarkMagenta 深洋红
#800080 Purple 紫色
#BA55D3 MediumOrchid 中兰花紫
#9400D3 DarkViolet 暗紫罗兰
#9932CC DarkOrchid 暗兰花紫
#4B0082 Indigo 靛青/紫兰色
#8A2BE2 BlueViolet 蓝紫罗兰
#9370DB MediumPurple 中紫色
#7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝
#6A5ACD SlateBlue 石蓝色/板岩蓝
#483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝
#E6E6FA Lavender 淡紫色/熏衣草淡紫
#F8F8FF GhostWhite 幽灵白
#0000FF Blue 纯蓝
#0000CD MediumBlue 中蓝色
#191970 MidnightBlue 午夜蓝
#00008B DarkBlue 暗蓝色
#000080 Navy 海军蓝
#4169E1 RoyalBlue 皇家蓝/宝蓝
#6495ED CornflowerBlue 矢车菊蓝
#B0C4DE LightSteelBlue 亮钢蓝
#778899 LightSlateGray 亮蓝灰/亮石板灰
#708090 SlateGray 灰石色/石板灰
#1E90FF DodgerBlue 闪兰色/道奇蓝
#F0F8FF AliceBlue 爱丽丝蓝
#4682B4 SteelBlue 钢蓝/铁青
#87CEFA LightSkyBlue 亮天蓝色
#87CEEB SkyBlue 天蓝色
#00BFFF DeepSkyBlue 深天蓝
#ADD8E6 LightBlue 亮蓝
#B0E0E6 PowderBlue 粉蓝色/火药青
#5F9EA0 CadetBlue 军兰色/军服蓝
#F0FFFF Azure 蔚蓝色
#E0FFFF LightCyan 淡青色
#AFEEEE PaleTurquoise 弱绿宝石
#00FFFF Cyan 青色
#00FFFF Aqua 浅绿色/水色
#00CED1 DarkTurquoise 暗绿宝石
#2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰
#008B8B DarkCyan 暗青色
#008080 Teal 水鸭色
#48D1CC MediumTurquoise 中绿宝石
#20B2AA LightSeaGreen 浅海洋绿
#40E0D0 Turquoise 绿宝石
#7FFFD4 Aquamarine 宝石碧绿
#66CDAA MediumAquamarine 中宝石碧绿
#00FA9A MediumSpringGreen 中春绿色
#F5FFFA MintCream 薄荷奶油
#00FF7F SpringGreen 春绿色
#3CB371 MediumSeaGreen 中海洋绿
#2E8B57 SeaGreen 海洋绿
#F0FFF0 Honeydew 蜜色/蜜瓜色
#90EE90 LightGreen 淡绿色
#98FB98 PaleGreen 弱绿色
#8FBC8F DarkSeaGreen 暗海洋绿
#32CD32 LimeGreen 闪光深绿
#00FF00 Lime 闪光绿
#228B22 ForestGreen 森林绿
#008000 Green 纯绿
#006400 DarkGreen 暗绿色
#7FFF00 Chartreuse 黄绿色/查特酒绿
#7CFC00 LawnGreen 草绿色/草坪绿
#ADFF2F GreenYellow 绿黄色
#556B2F DarkOliveGreen 暗橄榄绿
#9ACD32 YellowGreen 黄绿色
#6B8E23 OliveDrab 橄榄褐色
#F5F5DC Beige 米色/灰棕色
#FAFAD2 LightGoldenrodYellow 亮菊黄
#FFFFF0 Ivory 象牙色
#FFFFE0 LightYellow 浅黄色
#FFFF00 Yellow 纯黄
#808000 Olive 橄榄
#BDB76B DarkKhaki 暗黄褐色/深卡叽布
#FFFACD LemonChiffon 柠檬绸
#EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色
#F0E68C Khaki 黄褐色/卡叽布
#FFD700 Gold 金色
#FFF8DC Cornsilk 玉米丝色
#DAA520 Goldenrod 金菊黄
#B8860B DarkGoldenrod 暗金菊黄
#FFFAF0 FloralWhite 花的白色
#FDF5E6 OldLace 老花色/旧蕾丝
#F5DEB3 Wheat 浅黄色/小麦色
#FFE4B5 Moccasin 鹿皮色/鹿皮靴
#FFA500 Orange 橙色
#FFEFD5 PapayaWhip 番木色/番木瓜
#FFEBCD BlanchedAlmond 白杏色
#FFDEAD NavajoWhite 纳瓦白/土著白
#FAEBD7 AntiqueWhite 古董白
#D2B48C Tan 茶色
#DEB887 BurlyWood 硬木色
#FFE4C4 Bisque 陶坯黄
#FF8C00 DarkOrange 深橙色
#FAF0E6 Linen 亚麻布
#CD853F Peru 秘鲁色
#FFDAB9 PeachPuff 桃肉色
#F4A460 SandyBrown 沙棕色
#D2691E Chocolate 巧克力色
#8B4513 SaddleBrown 重褐色/马鞍棕色
#FFF5EE Seashell 海贝壳
#A0522D Sienna 黄土赭色
#FFA07A LightSalmon 浅鲑鱼肉色
#FF7F50 Coral 珊瑚
#FF4500 OrangeRed 橙红色
#E9967A DarkSalmon 深鲜肉/鲑鱼色
#FF6347 Tomato 番茄红
#FFE4E1 MistyRose 浅玫瑰色/薄雾玫瑰
#FA8072 Salmon 鲜肉/鲑鱼色
#FFFAFA Snow 雪白色
#F08080 LightCoral 淡珊瑚色
#BC8F8F RosyBrown 玫瑰棕色
#CD5C5C IndianRed 印度红
#FF0000 Red 纯红
#A52A2A Brown 棕色
#B22222 FireBrick 火砖色/耐火砖
#8B0000 DarkRed 深红色
#800000 Maroon 栗色
#FFFFFF White 纯白
#F5F5F5 WhiteSmoke 白烟
#DCDCDC Gainsboro 淡灰色
#D3D3D3 LightGrey 浅灰色
#C0C0C0 Silver 银灰色
#A9A9A9 DarkGray 深灰色
#808080 Gray 灰色
#696969 DimGray 暗淡灰
#000000 Black 纯黑'''
