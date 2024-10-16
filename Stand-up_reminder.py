import time
import tkinter as tk
from tkinter import messagebox
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

def remind_to_stand():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo("站立提醒", "该站起来活动一下了！")
    root.destroy()

def create_image():
    # 为系统托盘图标生成图像
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2 - 10, height // 2 - 10, width // 2 + 10, height // 2 + 10),
        fill=(0, 0, 0))
    return image

def on_exit(icon, item):
    icon.stop()
    global running
    running = False

def main():
    global running
    running = True
    reminder_interval = 30 * 60  # 以秒为单位

    icon = pystray.Icon("站立提醒")
    icon.icon = create_image()
    icon.menu = pystray.Menu(item('退出', on_exit))
    icon.run_detached()

    while running:
        time.sleep(reminder_interval)
        if running:
            remind_to_stand()

if __name__ == "__main__":
    main()