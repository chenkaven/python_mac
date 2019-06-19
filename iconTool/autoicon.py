#!/user/bin/env python3
# -'- coding:utf-8 -'-
#python icon.py -i icon.png  -s schemename

import argparse;
import os,os.path,sys,shutil;
from PIL import Image;
from PIL import ImageDraw;
import threading
reload(sys);
sys.setdefaultencoding("utf-8");

#iconName:
iconName = 'icon.png';
sIcon_path = os.getcwd()+os.path.sep+'ImageFold';
#模板;
target_ImageSet_path = os.getcwd()+os.path.sep+'ImagesSet';
# 输入图片地址
target_Desktop_path = os.path.join(os.path.expanduser("~"),'Desktop/');


#Android输出地址：
target_Android_path = target_Desktop_path+'imageView/icon_android/';

#ios输出地址：
target_iconRGB_path = target_Desktop_path+ 'imageView/icon_RGB/';
target_iOS_path = target_Desktop_path+ 'imageView/icon_ios/';
target_outFile_path = target_iOS_path+'AppIcon.appiconset/';

def encodeChincese(msg):
    type = sys.getfilesystemencoding();
    return msg.decode('utf-8').encode(type);
    pass
#创建二维数组
def creatiOSList():
    try:
        # 初始化图片数组
        image_DICT = [['20','icon-20-ipad.png'],
                      ['40', 'icon-20@2X-ipad.png'],
                      ['40','icon-20@2x.png'],
                      ['60','icon-20@3x.png'],
                      ['29', 'icon-29-ipad.png'],
                      ['58','icon-29@2x-ipad.png'],
                      ['29', 'icon-29.png'],
                      ['58','icon-29@2x.png'],
                      ['87','icon-29@3x.png'],
                      ['40','icon-40-ipad.png'],
                      ['80', 'icon-40@2x-ipad.png'],
                      ['80','icon-40@2x.png'],
                      ['120','icon-40@3x.png'],
                      ['50', 'icon-50-ipad.png'],
                      ['100', 'icon-50@2x-ipad.png'],
                      ['57', 'icon-57.png'],
                      ['114', 'icon-57@2x.png'],
                      ['120','icon-60@2x.png'],
                      ['180','icon-60@3x.png'],
                      ['72', 'icon-72-ipad.png'],
                      ['144', 'icon-72@2x-ipad.png'],
                      ['76','icon-76-ipad.png'],
                      ['152','icon-76@2x-ipad.png'],
                      ['167','icon-83.5@2x-ipad.png'],
                      ['512','icon-512.png'],                      
                      ['1024','icon-1024.png']];
        return image_DICT;
    except Exception as e:
        print(e);
########################################
#1.打开图片
def	open_imgFile(sFiledir):
    im = Image.open(sFiledir);
    im.load();
    return im;

#2.检查图像通道
def check_ImgModel(sFiledir):
    im = open_imgFile(sFiledir);
    return im.mode;

#3、修改图片尺寸
def modify_ImgSize(sInFile,sWidth,sHeight):
    im = open_imgFile(sInFile);
    (x,y)=im.size;
    if (sWidth != 0 and sHeight !=0):
        x=sWidth;
        y=sHeight;
    im = im.resize((x,y),Image.ANTIALIAS);
    return im;

#4、保存白底转透明;
def save_ImgRGBAFile(sInFile,sOutFile,sWidth,sHeight):
    imgA = modify_ImgSize(sInFile,sWidth,sHeight);
    # 使用白色来填充背景
    # (alpha band as paste mask).
    imgA = imgA.convert("RGBA");
    datas = imgA.getdata();
    newData = list();
    for item in datas:
        if item[0] >220 and item[1] > 220 and item[2] > 220:
            newData.append(( 255, 255, 255, 0))
        else:
            newData.append(item)  
    imgA.putdata(newData)
    imgA.save(sOutFile, 'png', quality=100);
    imgA.close();

#5、保存透明转成白底(不透明)图片
def save_ImgRGBFile(sInFile,sOutFile,sWidth,sHeight):
    img = modify_ImgSize(sInFile,sWidth,sHeight);
    (x,y)=img.size;
    p = Image.new('RGB', img.size, (255,255,255))
    p.paste(img, (0, 0, x, y), img)
    p.save(sOutFile, 'png', quality=100);
    p.close();

 #6、常规保存图片
def sava_ImgNomalFile(sInFile,sOutFile,sWidth,sHeight):
    img = modify_ImgSize(sInFile, sWidth, sHeight);
    img.save(sOutFile, 'png', quality=100);
    img.close();

#7、图片切成圆角
def circle_corder_image(sInFile,sOutFile):
    im = Image.open(sInFile).convert("RGBA");
    rad = 10;  # 设置半径
    circle = Image.new('L', (rad * 2, rad * 2), 0);
    draw = ImageDraw.Draw(circle);
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255);
    alpha = Image.new('L', im.size, 255);
    (w,h)= im.size;
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0));
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h-rad));
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w-rad, 0));
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad));
    im.putalpha(alpha);
    im.save(sOutFile, 'png', quality=100);
    pass;


#创建或更新文件/文件夹
def update_ImgPath(sPath):
    isPath = os.path.exists(sPath);
    isFile = os.path.isfile(sPath);
    isDir = os.path.isdir(sPath);
    if (isPath == True):
        shutil.rmtree(sPath);
    #print("######\n%s\n不存在则删除重建\n######"%(sPath));
    if(isFile ==True):
        #创建单个文件
        os.mknod(sPath);
    else:
        #创建多个目录
        os.makedirs(sPath);
########################################



#搜索当前路径/imageView下的所有图片；
def serach_ImgPath():
    global  sIcon_path;
    image_list = [];
    for root, dirs, files in os.walk(sIcon_path):
        # print("2==", files,dirs);
        for name in files:
            ext = os.path.splitext(name)[1][1:];
            # print("3==", ext);
            if (ext.lower() == 'png'
                or ext.lower() == 'jpg'
                or ext.lower() == 'PNG'):
                # if尾部为.png，...
                sPath = root + os.sep + name;
                image_list.append(sPath);
                new_img = open_imgFile(sPath);
                (w,h)= new_img.size;
                if(h != w):
                   h = w;
                   new_img = new_img.resize((w, h), Image.ANTIALIAS);
                   new_img.save(sPath, 'png', quality=100);
                else:
                   print("图片正常，无须裁剪");
    #print("image_list:",image_list);
    return image_list;

#制作安卓的图片
def markAndroidImgFile():
    global iconName,target_Android_path;
    update_ImgPath(target_Android_path);
    #遍历所有图片
    mackDir = serach_ImgPath();
    if (len(mackDir) == 2):
        base_img = Image.open(mackDir[0]);
        cor_img = Image.open(mackDir[1]);
        source = cor_img.convert('RGB');
        base_img.paste(source, mask=cor_img);
        # 创建桌面安卓文件夹
        sOutFile = target_Android_path+iconName;
        base_img.save(sOutFile, 'png', quality=100);
    else:
        sOutFile = target_Android_path + iconName;
        base_img = Image.open(mackDir[0]);
        base_img.save(sOutFile, 'png', quality=100);
        print("Success：无角标,合成安卓图标");
    pass;

#检查是否透明通道
def translate_ImgModel():
    global  target_Android_path,target_iconRGB_path,iconName;
    update_ImgPath(target_iconRGB_path);
    hImg = target_Android_path +iconName;
    if(check_ImgModel(hImg) == 'RGBA'):
       print("透明转为白底的");
       sIconName = target_iconRGB_path +iconName;
       save_ImgRGBFile(hImg,sIconName,0,0);
    else:
        print("白底的/不透明的");
        sIconName = target_iconRGB_path + iconName;
        sava_ImgNomalFile(hImg,sIconName,0,0);
    pass;


# 创建ios项目
def creat_iOSIcon():
    isSetExit = os.path.exists(target_ImageSet_path);
    isIosExit = os.path.exists(target_iOS_path);
    if(isIosExit == True):
        #print("判断存在苹果的icon目录，则删除");
        shutil.rmtree(target_iOS_path);
    if (isSetExit == True):
        print("复制到苹果icon目录");
        shutil.copytree(target_ImageSet_path,target_iOS_path);
	#开始做操作了；
	print("iOS_Icon开始秀操作了");
	mainiOSIcon();



# 正式开始制作iosIcon
def mainiOSIcon():
    print("****======Start=========***");
    imgDict = creatiOSList();
	# print(i, imgDict[i]);
    threads = []  # 多线程
    for i in range(0, len(imgDict)):
        #遍历参数
        for j in range(0, len(imgDict[i])):
            #print("图片~j",j,imgDict[i][j]);
            if j ==0:
                mWidth= imgDict[i][j];
            else:
                mReName=imgDict[i][j];
        thread1 = threading.Thread(target=convertIcon,args=(i+1,mWidth,mReName));
        thread1.start();
    print("****======End=========***");
    print ("current has %d threads" % (threading.activeCount() - 1));


# icon转换
def convertIcon(i,width, reName):
    try:
        #1、获取安卓的桌面图标
        inPath = target_iconRGB_path + iconName;
        img = Image.open(inPath);
        width = int(width);
        height = width;
        new_img = img.resize((width, height), Image.ANTIALIAS);
        # 2、获取ios图标的桌面文件夹
        outPath = target_outFile_path + reName;
        print('***'+"第"+str(i)+"张图片正在合成...");
        #print ('start waiting:', time.strftime('%H:%M:%S'));
        new_img.save(outPath, quality=100);
      #time.sleep(1);
       #print('stop waiting', time.strftime('%H:%M:%S'));
    except Exception as e:
        print(e);



if __name__ == '__main__':
    # #检查图片通道并保存;
    markAndroidImgFile();
    translate_ImgModel();
    creat_iOSIcon();

