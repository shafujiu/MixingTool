from PIL import Image, PngImagePlugin
import hashlib

def change_png_md5_with_annotation(image_path):
    # 打开PNG图像
    image = Image.open(image_path)

    # 创建一个PNG信息对象并添加注释
    meta = PngImagePlugin.PngInfo()
    meta.add_text("Comment", "This is an invisible annotation")

    # 保存图像并附加注释
    image.save(image_path, "PNG", pnginfo=meta)

    # 重新计算文件的MD5值
    with open(image_path, 'rb') as f:
        file_data = f.read()
        md5_value = hashlib.md5(file_data).hexdigest()

    print(f"文件: {image_path} 的新MD5值: {md5_value}")

# 示例调用
change_png_md5_with_annotation('your_image.png')

# 这是给png 插入注释的脚本，还未验证 需要依赖Pillow库
# 安装 pip install pillow