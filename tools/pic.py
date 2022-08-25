 
import os
import glob
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter.messagebox
import cv2
 
# 定义总窗口
if True:
    win = tk.Tk()
    # 设置窗体的长和宽
    win_width = 1590
    win_height = 800
 
    # 窗口在屏幕居中
    sw = win.winfo_screenwidth()  # 得到屏幕宽度
    sh = win.winfo_screenheight() - 80  # 得到屏幕高度
    x = (sw-win_width) / 2
    y = (sh-win_height) / 2
 
    #设置窗体的标题或者可以继续选择设置一个logo
    win.title('查看图片')
    win.geometry("%dx%d+%d+%d" % (win_width, win_height, x, y))
 
    bg = tk.Label(win, bg='#3c3f41')
    bg.place(height=win_height, width=win_width, x=0, y=0)
 
# 图片框参数
if True:
    img_box_x = 0
    img_box_y = 0
    img_box_w = win_width
    img_box_h = win_height-50
    img_box_bg = '#313335'
    
    # 选择文件夹
    folder = filedialog.askdirectory(parent=win,
                                     initialdir=os.getcwd(),
                                     title="Please select a folder:")
    # 将文件夹中的所有图片读到数组中，这里是图片路径的集合
    img_files = glob.glob(os.path.join(folder, "*.jpg"))
    if not len(img_files):
        print('文件中没有jpg图片')
        os._exit(0)  # 文件夹中没有jpg图片就退出
 
    img_num = 0  # 当前显示图片的指针
 
# 图片框
if True:
    def front_img():
        """
        点击显示上一张图片
        """
        global img_num
        img_num -= 1
        if img_num < 0:
            img_num = len(img_files) - 1
        img = img_cut(img_files[img_num], img_box_w, img_box_h)
        img_box.configure(image=img)
        img_box.mainloop()
 
 
    def next_img():
        """
        点击显示下一张图片
        """
        global img_num
        img_num += 1
        if img_num == len(img_files):
            img_num = 0
        img = img_cut(img_files[img_num], img_box_w, img_box_h)
        img_box.configure(image=img)
        img_box.mainloop()
 
 
    def img_cut(img, max_w, max_h):
        """
        锁定图片比例，最大化填充图片框
        :param img: 图片路径
        :param max_w: 图片框的宽度
        :param max_h: 图片框的高度
        :return: 图片对象
        """
        img_original = Image.open(img)
        # 获取图像的原始大小,并根据原图片比例，最大化地显示在图片框中
        w, h = img_original.size
        f1 = 1.0 * max_w / w
        f2 = 1.0 * max_h / h
        factor = min([f1, f2])
        img_w = int(w * factor)
        img_h = int(h * factor)
 
        img_open = img_original.resize((img_w, img_h))
        img_png = ImageTk.PhotoImage(img_open)
 
        return img_png
 
    def show_warning(msg):
        tk.messagebox.showwarning("保存",msg)
 
    def del_img():
        """
        图片另存
        """
        global img_num
        print("img_num=", img_num)
        img_file = "D:Desktop/1/"
        img_save = "D:Desktop/1/"
        print("img_file=",img_file)
        all_img = os.listdir(img_file)
        print("all_img[img_num]=",all_img[img_num])
        like_img = Image.open(img_file + all_img[img_num])
        like_img(img_save + all_img[img_num])
        next_img()
        print("success!")
 
        # show_warning("'保存图片成功！'")
 

    
    bt_next = tk.Button(win, text = "向下查看", command = next_img)
    
    bt_next.place(x = img_box_x + img_box_w / 2, y = img_box_y + img_box_h + 20)
 
    bt_front = tk.Button(win, text = "向上查看", command = front_img)
    bt_front.place(x = img_box_x + img_box_w / 2-70, y = img_box_y + img_box_h + 20)
 
    bt_save = tk.Button(win, text = "图片另存", command = del_img)
    bt_save.place(x = img_box_x + img_box_w / 2-140, y = img_box_y + img_box_h + 20)
    img2 = img_cut(img_files[0], img_box_w, img_box_h)
    img_box = tk.Label(win, bg = img_box_bg, width = img_box_w, height = img_box_h, image = img2)
    img_box.place(x = img_box_x, y = img_box_y)
 
# 循环页面
win.mainloop()