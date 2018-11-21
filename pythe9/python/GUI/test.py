import tkinter as tk

class App:
    def __init__(self,root):
        # 创建一个框架，然后在里面添加Button按钮组件
        # 框架一般使用再复杂的布局中起到将组件分组的作用
        frame = tk.Frame(root)
        frame.pack()
        # 创建一个按钮组件，fg是foreground的缩写，就是设置前景色的意思
        self.hi_there = tk.Button(frame,text = '打招呼',fg = 'blue',command = self.say_hi)
        self.hi_there.pack(pady = 100,padx=100)

    def say_hi(self):
        print('你好，我是初音未来~~')

# 创建一个toplevel的根窗口，并把它作为参数实例化App的对象
root = tk.Tk()
root.title('打招呼')
app = App(root)
# 开始主事件循环
root.mainloop()