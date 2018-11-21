import tkinter as tk
from tkinter import *

# 创建一个主窗口，用于容纳整个GUI程序
root = tk.Tk()
# 设置主窗口对象的标题栏
root.title('NEW')
# 添加一个Lable组件，Lable组件是GUI程序中最常用的组件之一
# Lable组件可以显示文本、图标或图片
thelable = tk.Label(root,text = '就是体验一下')
# 然后调用Lable组件的pack()方法，用于自动调节组建自身的尺寸
thelable.pack()
# 开启窗口
root.mainloop()

