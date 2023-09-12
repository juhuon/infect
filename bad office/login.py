import tkinter as tk
from tkinter import font

def disable_close():
    pass

# 创建窗口
window = tk.Tk()
window.title("提示")
window.attributes("-fullscreen", True)

message = """
你登录了此账户的原因有两点。
1.此设备处于丢失状态。
2.你未经允许动了我的电脑。
快还给我，啊啊啊啊！！！
"""

custom_font = font.Font(size=15)

# 创建淡红色矩形区域
canvas = tk.Canvas(window, bg="lightpink")
canvas.place(relwidth=1, relheight=1)

text = tk.Text(canvas, font=custom_font, wrap="word")
text.insert(tk.END, message)
text.pack(pady=20)
# 禁用关闭按钮
window.protocol("WM_DELETE_WINDOW", disable_close)

# 进入主循环
window.mainloop()
