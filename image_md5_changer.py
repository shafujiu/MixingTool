import hashlib

def change_png_md5_with_annotation(image_path, comment="This is an invisible annotation"):
    """为指定的 PNG 图片插入注释并修改其 MD5 值"""
    from PIL import Image, PngImagePlugin

    try:
        # 打开PNG图像
        image = Image.open(image_path)

        # 创建 PNG 信息对象并添加注释
        meta = PngImagePlugin.PngInfo()
        meta.add_text("Comment", comment)

        # 保存图像并附加注释
        image.save(image_path, "PNG", pnginfo=meta)

        # 重新计算文件的 MD5 值
        with open(image_path, 'rb') as f:
            file_data = f.read()
            md5_value = hashlib.md5(file_data).hexdigest()

        print(f"文件: {image_path} 的新MD5值: {md5_value}")
    except Exception as e:
        print(f"处理文件 {image_path} 时出错: {e}")

def change_png_md5_with_empty_byte(image_path):
    """通过在 PNG 文件末尾添加空字节修改其 MD5 值"""
    try:
        # 读取PNG文件的二进制数据
        with open(image_path, 'ab') as f:
            # 在文件末尾添加一个空字节
            f.write(b'\x00')

        # 重新计算文件的 MD5 值
        with open(image_path, 'rb') as f:
            file_data = f.read()
            md5_value = hashlib.md5(file_data).hexdigest()

        print(f"文件: {image_path} 的新MD5值: {md5_value}")
    except Exception as e:
        print(f"处理文件 {image_path} 时出错: {e}")