# MixingTool
混淆工具

## image 的 混淆
使用python 实现修改图片md5的脚本，

当前的实现方案是通过在文件末尾添加空字节，这样能保证不改变文件内容的同时修改md5；
同样的图跑一次这样的脚本 不确定他们的md5，是不是一样的，**猜测应该是一样**

使用之前需要确保电脑上有python环境

> 使用方法： 
> - 打开terminal，
> -  cd到我们的脚本位置，
> - 输入 python3 change_img_md5.py， enter 
> - 根据提示数据文件路径（注意是绝对路径），
> - 最后就可以看到输出新的md5值了

- [ ] 考虑添加更复杂的混淆方式，png还可以添加看不见的注释
