import os
import hashlib

def change_image_md5(directory):
    # 获取目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # 仅处理图片文件
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            with open(file_path, 'ab') as f:
                f.write(b'\x00')  # 追加一个空字节

            # 重新计算文件的 MD5 值
            with open(file_path, 'rb') as f:
                file_data = f.read()
                md5_value = hashlib.md5(file_data).hexdigest()

            print(f"文件: {filename} 的新MD5值: {md5_value}")

if __name__ == "__main__":
    # 提示用户输入图片目录路径
    directory = input("请输入图片目录的路径: ")

    # 检查路径是否存在
    if os.path.isdir(directory):
        change_image_md5(directory)
    else:
        print("输入的路径无效，请确认路径是否正确。")