#!/usr/bin/env python
# -*- coding:utf-8 -*-

#./buildAPI.py -b bundle 路径   -f framework 路径
import argparse , subprocess;
import os , shutil ;

#会在桌面路径
Desktop_PATH = os.path.join(os.path.expanduser("~"), 'Desktop');
# Python当前路径
Current_PATH = os.getcwd();
print ("Current_PATH: %s" % (Current_PATH));



# -- 截取名称--
def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    # print ("filepath:文件名称前的路径 %s" % (filepath));
    # print ("tempfilename:文件名称 %s" % (tempfilename));
    # print ("shotname:文件名 %s" % (shotname));
    # print ("extension:扩展名 %s" % (extension));
    return filepath,shotname,extension

#判断是目录或是文件则删除--
def deleteFoldOrFilePath(sPath):
    #判断是否存在
    isPath = os.path.exists(sPath);
    if(isPath == True):
        shutil.rmtree(sPath);
    pass;

#判断是目录或是文件则创建--
def creatFoldPath(sPATH):
    deleteFoldOrFilePath(sPATH);
    isFile = os.path.isfile(sPATH);
    # isDir = os.path.isdir(sPATH);
    if(isFile ==True):
        #创建单个文件
        os.mknod(sPATH);
    else:
        #创建多个目录
        os.makedirs(sPATH);

#复制文件到哪个路径下
def copytreePath(infile,outFile):
    isInfile = os.path.exists(infile);
    isOutFile = os.path.exists(outFile);
    #判断两个目录必须存在,才可以复制
    if(isInfile==True and isOutFile == True):
        shutil.copytree(infile,isOutFile);
    else:
        print ("路径有问题,无法复制");
    pass


def buildCmd(sCmd):
    print ("sCmd:(指令) %s" % (sCmd));
    process = subprocess.Popen(sCmd, shell=True)
    process.wait()
    # os.system(sCmd);

#输出bundle方法
def outBundleFile():
    print ("----开始执行编译Bundle----")
    Bundle_Build_Name = Bundle_Dir + os.path.sep + 'build';
    print ("Bundle_Dir:(传值目录) %s" % (Bundle_Dir));
    print ("Bundle_Build_Name: %s" % (Bundle_Build_Name));
    # --遍历文件夹目录--
    for dirpath, dirnames, filenames in os.walk(Bundle_Dir):
        # print ("root: %s" % root);
        for file in dirnames:
            # print ("file: %s" % file);
            if file.endswith('.xcodeproj'):
                Bundle_Proj = Bundle_Dir + os.path.sep + file;
                Bundle_XCodeProj = Bundle_Proj + os.path.sep + 'project.xcworkspace';
                Bundle_XCuserData = Bundle_Proj + os.path.sep + 'xcuserdata'
                filepath, Bundle_Name, extension = jwkj_get_filePath_fileName_fileExt(file);
                print ("Bundle_Name: %s" % (Bundle_Name));
                print ("Bundle_Proj: %s" % (Bundle_Proj));
                # print ("Bundle_XCodeProj: %s" % (Bundle_XCodeProj));
                # print ("Bundle_XCuserData: %s" % (Bundle_XCuserData));

    print ("=========文件目录遍历执行完毕===========");
    Bundle_Release_Path = Bundle_Build_Name + os.path.sep + 'Release-iphoneos' + os.path.sep + "%s.bundle" % (
    Bundle_Name);
    Bundle_Desktop_Path = Desktop_PATH + os.path.sep + "%s.bundle" % (Bundle_Name);
    Bundle_OutPath = Current_PATH + os.path.sep + 'APIDemoTest' + os.path.sep + "%s.bundle" % (Bundle_Name);
    # print ("Bundle_Release_Path: %s" % (Bundle_Release_Path));
    # print ("Bundle_Dev_Path: %s" % (Bundle_Dev_Path));
    # print ("Bundle_Product_Path: %s" % (Bundle_Product_Path));
    # print ("Bundle_Desktop_Path: %s" % (Bundle_Desktop_Path));
    print ("Bundle_OutPath: %s" % (Bundle_OutPath));
    # 删除桌面存在的文件或目录
    # deleteFoldOrFilePath(Bundle_Desktop_Path);
    deleteFoldOrFilePath(Bundle_OutPath);
    # 开始编译
    strCmd = 'xcodebuild -project %s -target %s  -configuration Release -sdk iphoneos  clean build ' % (
    Bundle_Proj, Bundle_Name);
    buildCmd(strCmd);
    # 复制文件到桌面
    # copyCmd = 'ditto  %s  %s' % (Bundle_Release_Path, Bundle_Desktop_Path);
    copyCmd = 'ditto  %s  %s' % (Bundle_Release_Path, Bundle_OutPath);
    buildCmd(copyCmd);
    # 删除缓存
    deleteFoldOrFilePath(Bundle_Build_Name);
    deleteFoldOrFilePath(Bundle_XCodeProj);
    deleteFoldOrFilePath(Bundle_XCuserData);
    pass;



#输出framework方法
def outFrameworkFile():
    Frame_Build_Name = Frame_Dir + os.path.sep + 'build';
    Frame_Product_Nane = Frame_Dir + os.path.sep + 'Product';
    print ("Frame_Build_Name: %s" % (Frame_Build_Name));
    print ("Frame_Product_Nane: %s" % (Frame_Product_Nane));
    # # --遍历文件夹目录--
    for dirpath, dirnames, filenames in os.walk(Frame_Dir):
        # print ("root: %s" % root);
        for file in dirnames:
            # print ("file: %s" % file);
            if file.endswith('.xcodeproj'):
                Frame_Proj = Frame_Dir + os.path.sep + file;
                Frame_XCodeProj = Frame_Proj + os.path.sep + 'project.xcworkspace';
                Frame_XCuserData = Frame_Proj + os.path.sep + 'xcuserdata'
                filepath, Frame_Name, extension = jwkj_get_filePath_fileName_fileExt(file);
                print ("Frame_Name: %s" % (Frame_Name));
                print ("Frame_Proj: %s" % (Frame_Proj));

    print ("=========文件目录遍历执行完毕===========");
    Frame_Release_Path = Frame_Build_Name + os.path.sep + 'Release-iphoneos' + os.path.sep + "%s.framework" % (
        Frame_Name);
    Frame_Dev_Path = Frame_Build_Name + os.path.sep + 'Release-iphonesimulator' + os.path.sep + "%s.framework" % (
        Frame_Name);
    Frame_Product_Path = Frame_Product_Nane + os.path.sep + "%s.framework" % (Frame_Name);
    Frame_OutPath = Current_PATH + os.path.sep + 'APIDemoTest' + os.path.sep + "%s.framework" % (Frame_Name);
    # # 删除桌面存在的文件或目录
    deleteFoldOrFilePath(Frame_OutPath);
    # 开始真机和模拟器编译
    releaseCmd = 'xcodebuild -project %s -target %s  -configuration Release -sdk iphoneos  clean build ' % (
        Frame_Proj, Frame_Name);
    buildCmd(releaseCmd);
    devCmd = 'xcodebuild -project %s -target %s  -configuration Release -sdk iphonesimulator  clean build ' % (
        Frame_Proj, Frame_Name);
    buildCmd(devCmd);
    # #编译完成，开始合并SDK.....
    creatFoldPath(Frame_Product_Path);
    # # 复制文件终端指令
    cpCmd = 'cp -R %s   %s' % (Frame_Release_Path + os.path.sep ,Frame_Product_Path + os.path.sep);
    buildCmd(cpCmd);
    #开始合并SDK
    lipoCmd = 'lipo -create %s'%(Frame_Release_Path) + os.path.sep + Frame_Name
    lipoCmd = lipoCmd + '' + Frame_Dev_Path + os.path.sep + Frame_Name;
    lipoCmd = lipoCmd + '' + '-output %s '%(Frame_Product_Path) + os.path.sep + Frame_Name;
    buildCmd(lipoCmd);
    # 复制文件到桌面
    copyCmd = 'ditto  %s  %s' % (Frame_Product_Path, Frame_OutPath);
    buildCmd(copyCmd);
    #删除缓存
    deleteFoldOrFilePath(Frame_Build_Name);
    deleteFoldOrFilePath(Frame_Product_Nane);
    deleteFoldOrFilePath(Frame_XCodeProj);
    deleteFoldOrFilePath(Frame_XCuserData);
    pass;


# ---执行main函数 ---
if __name__ == '__main__':
    #  -- 传目录名称 --
    parser = argparse.ArgumentParser();
    parser.add_argument("-b", "--bundle", help= "Build the Bundle workspace", metavar = "name");
    parser.add_argument("-f", "--framework", help= "Build the framework workspace", metavar = "name");
    options = parser.parse_args();
    Bundle_Dir = options.bundle;
    Frame_Dir = options.framework;
    print ("传值目录:Bundle_Dir: %s" % (Bundle_Dir));
    print ("传值目录:Frame_Dir: %s" % (Frame_Dir));
    if (Bundle_Dir  is None and Frame_Dir is None):
        pass;
    #如果Bundle_Dir存在则编译bundle
    if (Bundle_Dir is not None):
        print ("----开始执行编译Bundle----");
        outBundleFile();
    #如果Frame_Dir存在则编译framework
    if (Frame_Dir is not None):
        print ("----开始执行编译Framework----");
        outFrameworkFile();
    print ("----编译成功，浪起来----");
    pass;




















