import tkinter as tk
from tkinter import *

# root=Tk()
# 创建一个文本lable对象，justify函数让下图中的两行文字左对齐
# textLable = Label(root,text='您所下载的影片含有未成年限制内容，\n请满18岁后再点击观看',justify=LEFT,padx = 20)
# textLable.pack(side=LEFT)
# photo = PhotoImage(file = 'C:/Users/84607/Desktop/381Z463RoZEgKG1vdPvQKHy8eXI0Yp0L.gif_s400x0')
# img_Lable = Label(root,image = photo)
# img_Lable.pack(side=RIGHT)
#
# mainloop()

# root = Tk()
#
# photo = PhotoImage(file = 'C:/Users/84607/Desktop/VPoglUAJP0vneTJTsgl8u5Cc8exmBlC0.gif_s400x0')
# theLable = Label(root,text = 'Python来啦！！',justify=LEFT,image=photo,
#                  compound=CENTER,fg='white',font=("幼圆",30))
# theLable.pack(padx=100,pady=100)
# mainloop()

# def callback():
# #     var.set('吹吧就')
# #
# # root = Tk()
# # frame1 = Frame(root)
# # frame2 = Frame(root)
# # # 创建一个文本lable对象
# # var= StringVar()
# # var.set('您所下载的影片含有未成年限制，\n请满18岁后再来观看！')
# # textLable = Label(frame1,textvariable = var,justify=LEFT,fg='blue',font=('幼圆',20))
# # textLable.pack(side=LEFT)
# # #创建一个图形lable对象
# # # 用PhotoImage实例化一个图片对象（支持gif格式文件）
# # photo = PhotoImage(file='C:/Users/84607/Desktop/ZbWYbiLEI1Uod0ledrMue28CNCf1U3lS.gif_s400x0')
# # ImgLabel= Label(frame1,image=photo)
# # ImgLabel.pack(side=RIGHT)
# # # 添加按钮
# # theButton = Button(frame2,text='已满18岁',command=callback,fg='blue')
# # theButton.pack()
# # frame1.pack(padx=20,pady=20)
# # frame2.pack(padx=20,pady=20)
# #
# # mainloop()

# root = Tk()
# # # GIRLS = ['西施','王昭君','貂蝉','杨玉环']
# # # v = []
# # # for girl in GIRLS:
# # #     v.append(IntVar())
# # #     # CheckButton组件(多选)
# # #     b = Checkbutton(root,text=girl,variable=v[-1])
# # #     # anchor选项是用于置顶显示位置，可以设置为N, NE, E, SE, S, SW, W, NW, CENTER九个不同的值
# # #     b.pack(anchor=W)
# # #
# # # mainloop()

# root = Tk()
# v = IntVar()
#
# # Radiobutton单选(value 必写)
# Radiobutton(root,text='One',variable=v,value=1).pack(anchor = W)
# Radiobutton(root,text="Tow",variable=v,value=2).pack(anchor=W)
# Radiobutton(root,text='Three',variable=v,value=3).pack(anchor=W)
#
# mainloop()
# import numbers
# root = Tk()
#
# LANGS = [('Python' ,1),("Flask",2),("Java",3),("Web",4)]
# v = IntVar()
# v.set(1)
# for lang ,num in LANGS:
#
#     # b = Radiobutton(root,text=lang,variable=v,value=num)
#     # b.pack(anchor=W)
#     b = Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False)
#       横向平铺
#     b.pack(fill=X)
# mainloop()

# root = Tk()
# #
# # group = LabelFrame(root,text='最好的脚本语言？',padx= 5,pady=5)
# # group.pack(padx=10,pady=10)
# # LANGS = [('Python' ,1),("Flask",2),("Java",3),("Web",4)]
# # v = IntVar()
# # v.set(1)
# # for lang,num in LANGS:
# #     b = Radiobutton(group,text=lang,variable = v,value=num)
# #     b.pack(anchor = W)
# #
# # mainloop()

# # Entry 输入框
# root = Tk()
# e = Entry(root)
# e.pack(padx = 30,pady = 30)
# e.delete(0,END)
# e.insert(0,'啊哈哈')
# mainloop()

# root= Tk()
# # Thinker总共提供了三种布局组件的方法：pack(),grid()和place()
# # grid()方法允许你用表格的形式来管理组件的位置
# # row选项代表行，column选项表示列
# # 例如:row=1，column=2表示第二行第三列（0表示第一行）
# Label(root,text='作品：').grid(row=0)
# Label(root,text='作者：').grid(row=1)
# e1 = Entry(root)
# e2 = Entry(root)
# # show='*' 当密码需要保密时，填入
# # 例如：e2= Entry(root,show='*')
#
# e1.grid(row=0,column=1,padx= 10,pady =5)
# e2.grid(row=1,column=1,padx =10,pady =5)
#
# def show():
#     print('作品:<< %s >>' % e1.get())
#     print('作者:<< %s >>' % e2.get())
#     e1.delete(0,END)
#     e2.delete(0,END)
#
#
# # 如果表格大于组件，那么可以使用sticky选项来设置组件的位置
# # 同样你需要使用N，E，S，W以及他们的组合NE，SE，SW，NW来表示方位
# Button(root,text='获取信息',width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
# Button(root,text='退出',width=5,command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)
#
# mainloop()

# root =Tk()
#
# def test():
#     if e1.get() == '啊啊啊':
#         print('正确')
#         return True
#     else:
#         print('错误')
#         e1.delete(0,END)
#         return False
#
# v = StringVar()
# e1 = Entry(root,textvariable=v,validate='focusout',validatecommand=test)
# e1.pack(padx=10,pady=10)
# mainloop()

# root = Tk()
#
# e = Entry(root)
# e.pack(padx=20, pady=20)
#
# # 创建一个空列表
# theLB = Listbox(root,setgrid=True)
# theLB.pack()
#
# # 往列表里添加数据
# def insert_content():
#     theLB.insert(END,e.get())
#     e.delete(0,END)
# # for item in ['篮球','足球','乒乓球','羽毛球']:
# #     theLB.insert(END,item)
# a = Button(root,text='添加',command=insert_content)
# a.pack(anchor=W)
# theButton = Button(root,text='删除',command=lambda x=theLB:x.delete(ACTIVE))
# theButton.pack(anchor=E)
#
# mainloop()

# root = Tk()
# # 创建一个空列表
# theLB = Listbox(root,setgrid=True)
# theLB.pack()
# # 添加数据
# for item in range(11):
#     theLB.insert(END,item)
#
# mainloop()

# root = Tk()
# sb = Scrollbar(root)
# sb.pack(side=RIGHT,fill=Y)
# lb = Listbox(root,yscrollcommand=sb.set)
# for i in range(1000):
#     lb.insert(END,i)
# lb.pack(side=LEFT,fill=BOTH)
# sb.config(command=lb.yview)
# mainloop()

# root = Tk()
#
# Scale(root,from_=0,to=42).pack()
# # HORIZONTAL 水平的
# Scale(root,from_=0,to=200,orient=HORIZONTAL).pack()
# mainloop()

# root = Tk()
# s1 = Scale(root,from_=0,to=42)
# s1.pack()
# s2 = Scale(root,from_=0,to=200,orient=HORIZONTAL)
# s2.pack()
# def show():
#     print(s1.get(),s2.get())
#
# Button (root,text="获取位置",command=show).pack()
# mainloop()


root = Tk()
Scale(root,from_=0,to=42,tickinterval=5,length=200,resolution=5,orient=VERTICAL).pack()
Scale(root,from_=0,to=200,tickinterval=10,length=600,orient=HORIZONTAL).pack()
mainloop()

