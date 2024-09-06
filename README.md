# MixingTool
混淆工具

## image 的 混淆
使用python 实现修改图片md5的脚本，注意我们是针对png图片，png图片适合添加看不见的注释的方式

当前支持2种方式：
1. annotation 通过添加看不见的注释
2. empty_byte 通过在末尾添加空字节

使用之前需要确保电脑上有python环境，如果需要支持 annotation 还使用到了工具库Pillow库（安装： pip3 install pillow）

> 使用方法： 
> - 打开terminal，
> -  cd到我们的脚本位置，
> - 输入 python3 change_img_md5.py， enter 
> - 根据提示数据文件路径（注意是绝对路径），这里需要注意拖入terminal 的路径后面会多一个空格，需要我们去掉
> - 输入我们混淆的方式，现在提供了2种方式 'annotation' 或 'empty_byte'
>    - 如果输入的是 annotation（这是通过添加看见的注释 改变md5）值得注意的是，同一张图，添加同样的注释md5是相同的，默认我们是添加长度为16的随机字符串
> - 最后就可以看到输出新的md5值了

### 补充：

关于文件路径，脚本会遍历路径下面所有的png 图片

安装工具库 Pillow 容易遇到 SSL 证书验证的问题，这是国内环境容易出现，
```
Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)'))': /simple/pillow/
```
有2个方案 应该比较有效其中第1个已经尝试有效：
1. 使用 --trusted-host 忽略 SSL 验证
```
pip install pillow --trusted-host pypi.org --trusted-host files.pythonhosted.org
```
2. 配置国内的 PyPI 镜像源(需要自己验证)：
```
pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
```
当然你如果并非国内环境，那上诉问题您应该遇不到


