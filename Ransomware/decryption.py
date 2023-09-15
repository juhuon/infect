from Crypto.Cipher import aes
import os

def decrypt_files(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.@juhuon'):
                try:
                    with open(os.path.join(root, filename), 'rb') as f:
                        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
                    cipher = aes.new(key, aes.MODE_EAX, nonce)
                    data = cipher.decrypt_and_verify(ciphertext, tag)
                    new_filename = filename[:-4]
                    with open(os.path.join(root, new_filename), 'wb') as f:
                        f.write(data)
                    os.remove(os.path.join(root, filename))
                except Exception as e:
                    print(f"Error occurred while decrypting {filename}: {str(e)}")

# 解密桌面及其子目录
key = None
key_file_path = 'D:/README.@juhuon'   

# 将密钥写入C盘根目录的README.@juhuon文件
with open(key_file_path, 'rb') as f:
    key = f.read()
if key is not None:
    decrypt_files(os.path.expanduser("~/Desktop"), key)

    # 解密*盘根目录及其子目录
    decrypt_files('D:/', key)
    decrypt_files('E:/', key)
    decrypt_files('F:/', key)
    decrypt_files('G:/', key)
    decrypt_files('X:/', key)
