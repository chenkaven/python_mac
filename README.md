# python_mac
基于python开发
(一、)buildtool: 打包ios



(二、)codetools:添加垃圾代码工具




(三、)icontools:工具
图片裁剪工具：只需要将图片和角标分别放进ImageFold里面即可；
需要安装工具
1、安装pip，使用easy_install
***: sudo easy_install pip
2、安装pip的PIL(Python Imaging Library)库
***: sudo pip install PIL
若是安装正常，那皆大欢喜了。在我电脑安装时，却出现了问题。
could not find a version that satisfies the requirement PIL.(form versions:)
No matching distribution found for PIL.
这个是说明PIL已经找不到，其实现在已经用Pillow代替了PIL，在使用方面没有不同，API都是相同的。
既然如此，咱们就直接安装Pillow模块吧，
执行下一步：
***: sudo pip install Pillow
安装这个模块时，发现它会依赖另外一个模块：multiprocessing
只能先把multiprocessing模块安装好再执行上面的命令了，即可正常安装，非常小的一个模块
执行下一步：
***: sudo pip install multiprocessing
3、接着重新执行第二步
sudo pip install Pillow
4、使用注意：
使用时需要注意的是引入模块要按照下面的方式写（注意大小写）
第一种：from PIL import Image
第二种：from PIL.Image
(用这种方式时，下面使用时也得写成
PIL.Image.open('1.png')，
个人觉得不太好看，可以在引入时修改下模块名，
如from PIL.Image as image)


