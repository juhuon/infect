import os
import time

def check_cmd_file():
    file_path = "D:\\ProgramData\\startup\\cmd.txt"
    
    # 判断文件是否存在
    if os.path.exists(file_path):
        # 获取文件内容
        with open(file_path, 'r') as file:
            cmd_content = file.read()
        
             
        # 删除文件
        os.remove(file_path)
        # 执行命令
        os.system(cmd_content)
   

while True:
    check_cmd_file()
    
    # 设置检测间隔时间（单位：秒）
    time.sleep(60)
