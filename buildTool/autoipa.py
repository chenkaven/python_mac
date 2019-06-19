import os, shutil
import zipfile
import sys
import time

#xcode bulid 生成的文件
SCRAPP = r'/Users/zhu/Library/Developer/Xcode/DerivedData/JingBanYun-cfwznllnatfulnbcpaeqivottcvc/Build/Products/Debug-iphoneos/JingBanYun.app'
#存放ipa文件的目录
Dir = r'/Users/zhu/Music/iTunes/iTunes Media/Mobile Applications'

DESdir = os.path.join(Dir,'APP/Payload/JingBanYun.app')

def moveFile(scrdir,desdir):
    print('*' * 50)
    if not os.path.isdir(scrdir):
        print("%s not exist" % scrdir)
    else:
        if os.path.isdir(desdir):
            shutil.rmtree(desdir)
            print('JingBanYun.app文件存在删除')

        shutil.copytree(scrdir, desdir)
        print('复制文件成功%s' % desdir)

def zipDir():
    print('*' * 50)
    global Dir
    if not os.path.isdir(Dir):
        print('压缩的文件夹不存在')
    else:
        print('压缩开始')
        os.chdir('%s/APP'%Dir)
        os.system('zip -r myfile.zip ./*')
        print('压缩完成')
        os.rename('myfile.zip','myfile.ipa')

def changeName(typeInt=0):
    print('*' * 50)
    print('重命名开始')
    typeStr = 'devJingBanYun.ipa'
    if typeInt == 2:
        typeStr = 'disJingBanYun.ipa'
    elif typeInt == 1:
        typeStr = 'ydevJingBanYun.ipa'

    desPath = os.path.join(Dir,typeStr)
    if os.path.exists(desPath):
        os.remove(desPath)
        print('删除：%s'%desPath)
        
    shutil.move('%s/APP/myfile.ipa'%Dir,desPath)
    print('重命名完成')
    ipapath = desPath
    res = os.path.getctime(ipapath)
    size = os.path.getsize(ipapath)

    time_local = time.localtime(res)
    dt = time.strftime('%Y-%m-%d %H:%M:%S', time_local)
    print('%s' % ipapath)
    print ('IPA文件大小：%.2f'%float(size))
    print(dt)

def main(typeInt=0):
    moveFile(SCRAPP,DESdir)
    zipDir()
    changeName(typeInt)

if __name__ == '__main__':
    '''
    1:预发布     (cmd: python3 build 1)
    2：正式      (cmd: python3 build 2)
    3:测试        (cmd: python3 build )
   使用用例：
  
    '''
    print('开始执行...')

    if (len(sys.argv) == 2):
        typeInt = sys.argv[1]
        main(int(typeInt))
    else:
        main()
