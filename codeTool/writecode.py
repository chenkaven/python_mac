# -*- coding: utf-8 -*-
import random;
import hashlib;
import time,datetime;
import base64;
import re;
import os,sys,shutil;
reload(sys);
sys.setdefaultencoding("utf8");

#随机选择字符串的数值；
first = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
second = "abcdefghijklmnopqrstuvwxyz";
third='1234567890';
#垃圾变量方法个数
method_min = 30;
method_max = 100;
#要修改的文件所在的文件夹路径
file_floadPath = '/Users/admin/Desktop/Payment1/GMPlatform/Class';#要修还得文件所在的文件夹路径
methodArray = ['HwxrFvrj', 'QnzduQbtdd', 'PvcrwLtqhf',
         'UvdhDbjn', 'SuntmyTxvyzg', 'CvlxwBipbp',
         'GzrdyzIbimvz', 'CqsjqMmgsp', 'OxaaeuWjhasc',
         'NjiardRvwgbi', 'NcculmLtpljq', 'ApoqQrll',
         'GkgokDyvjb', 'EblldkVouplj', 'KfdrFvnw',
         'SfhyhObftc', 'SmruByoc', 'YzcccvXmpmit',
         'OmqvaHpxat', 'XzytsUyvyd', 'MjforNnnyi',
         'ZvjhuIdogs', 'BzfrxzSeahxc', 'PycycwFjtpny',
         'XvngtoSedljr', 'DktiaCbucd', 'AqbplNuodc',
         'MzkvgZuala', 'KdwzIoej', 'AaynatUpqcfd',
         'IyvwhZvtjc', 'UmijGmsy', 'AoayndXxghym',
         'Diwbszoshz','KuaNhqpgys','kSzBMjpdct'];

classArray = ['NSString','UIImageView',
              'UILabel','NSDictionary',
              'NSData','UIScrollView',
              'NSArray','UIView',
              'UIColor',
              'UITextView','UITableView',
              'UIWebView','UIButton',
              'UITextField','UIPageControl',
              'UIImage','UIProgressView',
              'UIPickerView','UIActivityIndicatorView',
              'UIFont'];

#颜色数组
colorArray = ['blackColor','darkGrayColor',
              'lightGrayColor','whiteColor',
              'grayColor','redColor',
              'greenColor','blueColor',
              'cyanColor','yellowColor',
              'magentaColor','orangeColor',
              'purpleColor','brownColor',
              'clearColor'];

#########################################
#prama --MD5加密
def sy_encoding_md5(nStr):
    sl = hashlib.md5();
    sl.update(nStr);
    sign = sl.hexdigest();
    return sign;

def sy_md5andBase64(nStr):
    sign = sy_encoding_base64(nStr);
    sign = sy_encoding_md5(sign);
    return sign;

#prama --base64加密
def sy_encoding_base64(nStr):
    sign = base64.b64encode(nStr.encode('utf-8'));
    return sign;

#prama --base64解码
def sy_decoding_base64(nStr):
    sign = base64.b64decode(nStr);
    return sign;

#prama 随机选择加密方式(base64/md5加密)
def sy_randomSign(nStr):
    index = random.randint(0, 1);
    if (index == 1):
       sign = sy_encoding_md5(nStr);
    else:
       arrList = [first, second,third,methodArray];
       rStr = (random.choice(random.choice(arrList)));
       sign = sy_encoding_base64(nStr);
       # 先base64加密，然后获取以=替换字符
       #print("rStr:", rStr);
       sign = sign.replace('=', rStr);
    return sign;


#判断字符串存在数字,则替换
def sy_replaceLine(nStr):
    pattern = re.compile('[0-9]+');
    index = random.randint(0, 1);
    if index == 1:
        rStr = random.choice(first);
    else:
        rStr = random.choice(second);
    strinfo = pattern.sub(rStr, nStr);
    print("strinfo",strinfo);
    return strinfo;

#prama --获取时间
def sy_getTimeNow():
    # 2018-07-01 00:47:08.505520
    sNows = datetime.datetime.now();
    #datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # 日期格式化
    #print("sNows:", str(sNows ));
    return str(sNows);


#########start 获取文件路径、文件名、后缀名############
def  get_filePath_fileName_fileExt(filename):
    (filepath, tempfilename) = os.path.split(filename);
    (shotname, extension) = os.path.splitext(tempfilename);
    # print "\nfilepath:",filepath;
    #print "\nshotname:", shotname;
    # print "\nextension:", extension;
    return  shotname;



##########################################################

def getMethodArrList():
    #获取methodArrList
    global method_min,method_max,methodArray;
    #数组临时容器
    methodArrList = [];
    methodCount = random.randint(method_min, method_max);
    print("AllCount:",methodCount);
    # 包装所有字符串；
    arrList = [first, second, methodArray];
    for i in range(methodCount):
        final = '';
        #挑选随机的字符串
        rStr = (random.choice(random.choice(arrList)));
        #头部包装
        final += rStr;
        #中间包装时间戳加密方式
        sTime = sy_randomSign(sy_getTimeNow())
        final += sTime;
        #尾部包装
        final += (random.choice(rStr));
        #拼接所有字符串
        methodArrList.append(final);
    #######################################;
    # 数组去重
    methodArrList = list(set(methodArrList));
    print("methodArrList:",methodArrList);
    return methodArrList;


classNameArray = [];
funcNameArray = [];
methodNameArray = [];
########---所有逻辑处理模板---##########
#获取方法名
def getMehtodNameFunc(kclassName,knameStr):
   sline_data ='';
   content_Color = random.choice(colorArray);
   if kclassName =="UILabel" \
       or kclassName=='UIImageView'\
       or kclassName == "UIScrollView"\
       or kclassName == 'UIView'\
       or kclassName == "UITextView"\
       or kclassName == 'UITableView'\
       or kclassName == "UIWebView"\
       or kclassName == 'UIButton'\
       or kclassName == "UITextField"\
       or kclassName == 'UIProgressView'\
       or kclassName == 'UIPickerView'\
       or kclassName == 'UIActivityIndicatorView'\
       or kclassName == 'UIPageControl':
       #遍历控件结束则开启输入写法
       sline_data =  '\n\t/*********mjbwenjian**********/\n' \
                   + '\t' + kclassName + ' * ' + knameStr + ' = ' + '[[' + kclassName + ' alloc]init];\n' \
                   + '\t' + knameStr +'.frame=CGRectMake(' + str(random.randint(0, 100)) + ',' + str(
           random.randint(0, 100)) + ',' + str(random.randint(0, 100)) + ',' \
                   + str(random.randint(0, 100)) + ');\n' \
                   + '\t' + knameStr + '.tag = ' + str(random.randint(5, 10)) + ';\n' \
                   + '\t' + knameStr + '.backgroundColor = [UIColor %s] ;\n'%(content_Color) \
                   + '\t' + knameStr + '.layer.cornerRadius = ' + str(random.randint(5, 10)) + ';\n' \
                   + '\t' + knameStr + '.userInteractionEnabled = YES;\n' \
                   + '\t' + knameStr + '.layer.masksToBounds = YES;\n' \
                   + '\t/*********mjbwenjian**********/';
   elif kclassName =='NSString':
       sline_data += (random.choice(methodArray));
       sline_data = '\n\t/*********mjbwenjian**********/\n' \
                    + '\t' + kclassName + ' * ' + knameStr + ' = ' + '[NSString stringWithFormat:@"%@",'+'@"%s"];' \
                     '\n\t/*********mjbwenjian**********/'%(sline_data);

   elif kclassName == 'NSData':
       sline_data += (random.choice(methodArray));
       sline_data = '\n\t/*********mjbwenjian**********/\n' \
                    + '\t' + kclassName + ' * ' + knameStr + ' = [' + '@"%s" dataUsingEncoding:NSUTF8StringEncoding];\n' \
                     '\n\t/*********mjbwenjian**********/' % (sline_data);

   elif kclassName == 'NSArray':
           sline_data += (random.choice(methodArray));
           sline_data = '\n\t/*********mjbwenjian**********/\n' \
                        + '\t' + kclassName + ' * ' + knameStr + ' = @[' + '@"%s"];' \
                        '\n\t/*********mjbwenjian**********/' % (sline_data);
   elif kclassName == 'NSDictionary':
        sline_data += (random.choice(methodArray));
        sline_data = '\n\t/*********mjbwenjian**********/\n' \
                +'\t'+'NSString *JSONString = [NSString stringWithFormat:@"%@",'+'@{@"%sax":@"%sek"}];'% (sline_data,sline_data)\
                +'\n\tNSData '+'*'+knameStr+'Data'+'\t= [JSONString dataUsingEncoding:NSUTF8StringEncoding];'\
                + '\n\t' + kclassName + ' * ' + knameStr + ' = [NSJSONSerialization JSONObjectWithData:%s options:NSJSONReadingMutableLeaves error:nil];' \
                '\n\t/*********mjbwenjian**********/' % (knameStr+'Data');

   elif kclassName == 'UIImage':
       sline_data += (random.choice(methodArray));
       sline_data = '\n\t/*********mjbwenjian**********/\n' \
                +'\t NSData *imgData = [@"%s" dataUsingEncoding:NSUTF8StringEncoding];\n'%(sline_data)\
                + '\t' + kclassName + ' * ' + knameStr + ' = [UIImage imageWithData:imgData];\n' \
                '\n\t/*********mjbwenjian**********/';
   elif kclassName == 'UIColor':
        sline_data += (random.choice(methodArray));
        sline_data = '\n\t/*********mjbwenjian**********/\n' \
                + '\t' + kclassName + ' * ' + knameStr + ' = [UIColor %s];\n' \
                '\n\t/*********mjbwenjian**********/'%(content_Color);
   elif kclassName == 'UIFont':
        sline_data += (random.choice(methodArray));
        sline_data = '\n\t/*********mjbwenjian**********/\n' \
                + '\t' + kclassName + ' * ' + knameStr + ' = [UIFont systemFontOfSize: %s];\n' \
                '\n\t/*********mjbwenjian**********/'%(random.randint(12, 26));
   return sline_data;
#要修改的文件所在的文件夹路径
def text_createH(sPath,sMsg1,sMethodArr,sClassArr,sFuncArr):
    file_data = "";
    result = [];
    for line in open(sPath, 'r'):
        result.append(line);

    #模拟头部标题；
    result.append(sMsg1);
    # 创建body函数方法
    for methodName, className,funNamec in zip(sMethodArr, sClassArr,sFuncArr):
        aLine = '- (nonnull %s *)hsd_%s:(nonnull %s *)%s;\n'%(className,methodName,className,funNamec);
        file_data += aLine;
    result.append(file_data);
    #写入@end结束
    result.append('\n@end');
    open(sPath,'wb').writelines(result);
    pass;

def text_createM(sPath,sMsg1,sMethodArr,sClassArr,sFuncArr):

    file_data = "";
    result = [];
    if os.path.exists(sPath)==False:
        (filepath, tempfilename) = os.path.split(sPath);
        sPath = filepath+'.mm';
    ############################
    for line in open(sPath, 'r'):
        result.append(line);
        # 模拟头部标题；
    result.append(sMsg1);
    # 创建methodNameArray；
    for methodName, className, funNamec in zip(sMethodArr, sClassArr, sFuncArr):
        funcMehthod = getMehtodNameFunc(className,methodName);
        aline = '\n - (nonnull %s *)hsd_%s:(nonnull %s *)%s {\n%s'%(className,methodName,className,funNamec,funcMehthod);
        aline += '\n\treturn %s;\n}\n' % (methodName);
        file_data += aline;
    result.append(file_data);
    # 写入@end结束
    result.append('\n@end');
    open(sPath, 'wb').writelines(result);
    pass;


def read_fileName(file_dir):
    OCfFunFile = [];
    print "file_dir:",file_dir
    for root, dirs, files in os.walk(file_dir):
        print("root:",root) #当前目录路径
        print("dirs:",dirs) #当前路径下所有子目录
        print("files:",files); #当前路径下所有非目录子文件
        #遍历文件夹下的.h和.m文件并添加废代码
        for file in files:
            if file.endswith('.h')or file.endswith('.m')or file.endswith('.mm'):
                shotname = get_filePath_fileName_fileExt(file);
                filePath = root+'/'+shotname;
                OCfFunFile.append(filePath);
    OCfFunFile  = list(set(OCfFunFile));
    print "OCfFunFile:",OCfFunFile;

    # #去除重复
    for file_name in OCfFunFile:
        isHfile = os.path.exists(file_name+'.h');
        isMfile = os.path.exists(file_name+'.m');
        isMMfile = os.path.exists(file_name + '.mm');
        if isHfile == False:
            OCfFunFile.remove(file_name);
        if isMfile ==  False and isMMfile == False:
            OCfFunFile.remove(file_name);
    print "OCfFunFile:",OCfFunFile;
    return OCfFunFile;


def  mainInfoZhixing():
    #读取所有文件
    global  file_floadPath;
    proFileList = [];
    proFileList = read_fileName(file_floadPath)
    for file_name in proFileList:
        #构造oc函数方法
        methodNameArray = getMethodArrList();
        # 获取classArrlist
        for i in range(method_min, method_max):
            classNameArray.append(random.choice(classArray));
        # funcNameList
        for i in range(method_min, method_max):
            funcNameArray.append(random.choice(methodArray));
        #获取文件名；
        shotname = get_filePath_fileName_fileExt(file_name);
        sTitle = (random.choice(methodNameArray));
        msg1 = '\n@interface '+shotname+' (%s)\n\n'%(sTitle);
        msg2 = '\n@implementation '+shotname+' (%s)\n\n'%(sTitle);
        text_createH(file_name+'.h',msg1,methodNameArray,classNameArray,funcNameArray);
        text_createM(file_name+'.m',msg2,methodNameArray,classNameArray,funcNameArray);
        pass;





##############################
if __name__ == '__main__':
    mainInfoZhixing();


