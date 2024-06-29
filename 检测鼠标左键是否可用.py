import tkinter as tk, time as t
from tkinter import messagebox

root = tk.Tk()
root.title("检测鼠标左键是否能用")
root.geometry("800x600")
root.config(bg="white")
root.resizable(width=False, height=False)
root.maxsize(width=800, height=600)


def check():
    l2.place_forget()
    messagebox.showinfo("检测中", "按下‘确定’开始检测")
    t.sleep(2)
    l2.place(x=100, y=400, width=600, height=40)


def e():
    if messagebox.askokcancel("退出程序", "是否退出程序？"):
        root.destroy()


b = tk.Button(root, text="开始检测", command=check, bg="white", fg="black")
b.place(x=350, y=250, width=100, height=50)

ex = tk.Button(root, text="退出程序", command=e, bg="white", fg="black")
ex.place(x=350, y=310, width=100, height=50)

l2 = tk.Label(root, text="检测完成！您的鼠标左键可用。", bg="white", fg="black", font=("consolas", 20))
l2.place_forget()

root.mainloop()
