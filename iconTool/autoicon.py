#!/user/bin/env python3
# -'- coding:utf-8 -'-
#python icon.py -i icon.png  -s schemename

import argparse;
import os,os.path,sys,shutil;
from PIL import Image;


# 输入图片地址
target_Desktop_path = os.path.join(os.path.expanduser("~"),  'Desktop/imageView/Icon-512.png');

#输出图片的地址
target_iconRGB_path = os.path.join(os.path.expanduser("~"),  'Desktop/imageView/icon_RGB/');
target_iconRGBA_path = os.path.join(os.path.expanduser("~"), 'Desktop/imageView/icon_RGBA/');

#Android输出地址：
target_Android_path = os.path.join(os.path.expanduser("~"),  'Desktop/imageView/icon_Android/');
#ios的输出地址：
target_iOS_path = os.path.join(os.path.expanduser("~"),  'Desktop/imageView/icon_ios/');

target_ImageSet_path = os.getcwd()+os.path.sep+'ImagesSet';
#iconName:
iconName = 'icon.png';
#androidImgName = ['ic_launcher.png','ic_launcher_round.png'];


# serchIconPath = '/Users/apple/Desktop/商务需求/三国卡牌-英瓷-6.20日传/ICON.jpg';

def encodeChincese(msg):
	type = sys.getfilesystemencoding();
	return msg.decode('utf-8').encode(type);
	pass

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




    

########################################
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


#查找图片路径;
def check_ImgPath():
	global target_Desktop_path,target_iconRGB_path,iconName;
	if (check_ImgModel(target_Desktop_path)) == 'RGBA':
	    print('透明转为白底');
	    update_ImgPath(target_iconRGB_path);
	    sIconName = target_iconRGB_path + iconName;
	    save_ImgRGBFile(target_Desktop_path,sIconName,0,0);
	else:
	    print('白底转为透明');
	    update_ImgPath(target_iconRGBA_path);
	    sIconName = target_iconRGBA_path + iconName;
	    save_ImgRGBAFile(target_Desktop_path,sIconName,0,0);
	#创建Android图标
	creat_AndroidIcon();


def creat_AndroidIcon():
	update_ImgPath(target_Android_path);
	creat_iOSIcon();


def creat_iOSIcon():
	#创建ios项目
	# update_ImgPath(target_iOS_path);
	isSetExit = os.path.exists(target_ImageSet_path);
	isIosExit = os.path.exists(target_iOS_path);
	if(isIosExit == True):
		#print("判断存在苹果的icon目录，则删除");
		shutil.rmtree(target_iOS_path);

	if (isSetExit == True):
		print("判断存在苹果的icon,则复制到苹果icon目录");
		shutil.copytree(target_ImageSet_path,target_iOS_path);







	    
    		



if __name__ == '__main__':
    #检查图片通道并保存;
	#check_ImgPath();
	global target_Desktop_path,target_iconRGB_path,iconName;
