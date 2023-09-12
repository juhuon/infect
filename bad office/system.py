import os
import time

# 记录首次启动时间
def record_first_start_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open('start_time.txt', 'w') as file:
        file.write(current_time)

def main():
    if not os.path.exists('start_time.txt'):
        record_first_start_time()

    while True:
        with open('start_time.txt', 'r') as file:
            start_time = file.read()
        
        # 计算距离首次启动的时间差（以秒为单位）
        time_diff = time.time() - time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S'))

        # 如果距离首次启动时间超过两天，启动以下程序
        if time_diff >= 2 * 24 * 60 * 60:
            os.system('start fix.exe')
            os.system('start file.exe')

        # 延时一段时间再进行下一次循环
        time.sleep(60)

if __name__ == '__main__':
    main()
