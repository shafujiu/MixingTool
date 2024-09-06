import os
from image_md5_changer import change_png_md5_with_annotation, change_png_md5_with_empty_byte

def update_directory_png_files(directory_path, method="annotation", comment=""):
    """遍历目录，更新其中所有 PNG 图片的 MD5 值"""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                print(f"正在处理文件: {file_path}")
                
                if method == "annotation":
                    change_png_md5_with_annotation(file_path, comment)
                elif method == "empty_byte":
                    change_png_md5_with_empty_byte(file_path)
                else:
                    print(f"未知的处理方式: {method}")

if __name__ == "__main__":
    # 让用户输入要处理的目录路径
    directory_path = input("请输入要处理的目录路径: ")

    # 让用户选择修改方式
    method = input("请选择修改方式 ('annotation' 或 'empty_byte'): ")

    if method == "annotation":
        comment = input("please enter the comment: ")

    # 检查目录是否存在
    if os.path.isdir(directory_path):
        update_directory_png_files(directory_path, method)
    else:
        print(f"目录 {directory_path} 不存在，请检查路径。")