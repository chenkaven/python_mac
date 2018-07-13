# -*- coding: utf-8 -*-
import random;
import hashlib;
import time,datetime;
import base64;
import re;
import os,sys,shutil;

# 生成一个图形注释 适用于.h .cpp  .mm   .m   .hpp
def addDescimg():
    text = [
    '\n/**                                                                         佛祖保佑必过包',
    '\n*          .,:,,,                                        .::,,,::.          佛祖保佑必过包',
    '\n*        .::::,,;;,                                  .,;;:,,....:i:         佛祖保佑必过包',
    '\n*        :i,.::::,;i:.      ....,,:::::::::,....   .;i:,.  ......;i.        佛祖保佑必过包',
    '\n*        :;..:::;::::i;,,:::;:,,,,,,,,,,..,.,,:::iri:. .,:irsr:,.;i.        佛祖保佑必过包',
    '\n*        ;;..,::::;;;;ri,,,.                    ..,,:;s1s1ssrr;,.;r,        佛祖保佑必过包',
    '\n*        :;. ,::;ii;:,     . ...................     .;iirri;;;,,;i,        佛祖保佑必过包',
    '\n*        ,i. .;ri:.   ... ............................  .,,:;:,,,;i:        佛祖保佑必过包',
    '\n*        :s,.;r:... ....................................... .::;::s;        佛祖保佑必过包',
    '\n*        ,1r::. .............,,,.,,:,,........................,;iir;        佛祖保佑必过包',
    '\n*        ,s;...........     ..::.,;:,,.          ...............,;1s        佛祖保佑必过包',
    '\n*       :i,..,.              .,:,,::,.          .......... .......;1,       佛祖保佑必过包',
    '\n*      ir,....:rrssr;:,       ,,.,::.     .r5S9989398G95hr;. ....,.:s,      佛祖保佑必过包',
    '\n*     ;r,..,s9855513XHAG3i   .,,,,,,,.  ,S931,.,,.;s;s&BHHA8s.,..,..:r:     佛祖保佑必过包',
    '\n*    :r;..rGGh,  :SAG;;G@BS:.,,,,,,,,,.r83:      hHH1sXMBHHHM3..,,,,.ir.    佛祖保佑必过包',
    '\n*   ,si,.1GS,   sBMAAX&MBMB5,,,,,,:,,.:&8       3@HXHBMBHBBH#X,.,,,,,,rr    佛祖保佑必过包',
    '\n*   ;1:,,SH:   .A@&&B#&8H#BS,,,,,,,,,.,5XS,     3@MHABM&59M#As..,,,,:,is,   佛祖保佑必过包',
    '\n*  .rr,,,;9&1   hBHHBB&8AMGr,,,,,,,,,,,:h&&9s;   r9&BMHBHMB9:  . .,,,,;ri.  佛祖保佑必过包',
    '\n*  :1:....:5&XSi;r8BMBHHA9r:,......,,,,:ii19GG88899XHHH&GSr.      ...,:rs.  佛祖保佑必过包',
    '\n*  ;s.     .:sS8G8GG889hi.        ....,,:;:,.:irssrriii:,.        ...,,i1,  佛祖保佑必过包',
    '\n*  ;1,         ..,....,,isssi;,        .,,.                      ....,.i1,  佛祖保佑必过包',
    '\n*  ;h:               i9HHBMBBHAX9:         .                     ...,,,rs,  佛祖保佑必过包',
    '\n*  ,1i..            :A#MBBBBMHB##s                             ....,,,;si.  佛祖保佑必过包',
    '\n*  .r1,..        ,..;3BMBBBHBB#Bh.     ..                    ....,,,,,i1;   佛祖保佑必过包',
    '\n*   :h;..       .,..;,1XBMMMMBXs,.,, .. :: ,.               ....,,,,,,ss.   佛祖保佑必过包',
    '\n*    ih: ..    .;;;, ;;:s58A3i,..    ,. ,.:,,.             ...,,,,,:,s1,    佛祖保佑必过包',
    '\n*    .s1,....   .,;sh,  ,iSAXs;.    ,.  ,,.i85            ...,,,,,,:i1;     佛祖保佑必过包',
    '\n*     .rh: ...     rXG9XBBM#M#MHAX3hss13&&HHXr         .....,,,,,,,ih;      佛祖保佑必过包',
    '\n*      .s5: .....    i598X&&A&AAAAAA&XG851r:       ........,,,,:,,sh;       佛祖保佑必过包',
    '\n*      . ihr, ...  .         ..                    ........,,,,,;11:.       佛祖保佑必过包',
    '\n*         ,s1i. ...  ..,,,..,,,.,,.,,.,..       ........,,.,,.;s5i.         佛祖保佑必过包',
    '\n*          .:s1r,......................       ..............;shs,           佛祖保佑必过包',
    '\n*          . .:shr:.  ....                 ..............,ishs.             佛祖保佑必过包',
    '\n*              .,issr;,... ...........................,is1s;.               佛祖保佑必过包',
    '\n*                 .,is1si;:,....................,:;ir1sr;,                  佛祖保佑必过包',
    '\n*                    ..:isssssrrii;::::::;;iirsssssr;:..                    佛祖保佑必过包',
    '\n*                         .,::iiirsssssssssrri;;:.                          佛祖保佑必过包',
    '\n*/\n'
    ]
    return text
########宏定义开始####################
msg_descrpt ='\n//  Game-MJSGZ\n//  Created  Created by Kaven on 2018/06/01.\n//  Copyright ©  2017年 .骄傲的你^终究还是我的 All rights reserved.\n//\n\n';
# 获取桌面路径：
target_desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop/target_ios');

#随机选择字符串的数值；
first = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
second = "abcdefghijklmnopqrstuvwxyz";
third='1234567890';


#文件夹数组；
fold_min = 4;
fold_max = 7;
foldArray = [];

#创建垃圾文件的个数
file_Count=10;
projectArray=[];
file_list=[];

#method的数组
methodArray=[];
method_min = 10;
method_max = 100;
#文件class数组
#定义类数组
classArray = ['NSString','UIImageView',
              'UILabel','NSDictionary',
              'NSData','UIScrollView',
              'NSArray','UIView',
              'UIColor',
              'UITextView','UITableView',
              'UIWebView','UIButton',
              'UITextField','UIPageControl',
              'UIImage','UIProgressView',
              'UIPickerView','UIActivityIndicatorView'];
#颜色数组
colorArray = ['blackColor','darkGrayColor',
              'lightGrayColor','whiteColor',
              'grayColor','redColor',
              'greenColor','blueColor',
              'cyanColor','yellowColor',
              'magentaColor','orangeColor',
              'purpleColor','brownColor',
              'clearColor'];

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
    #先base64加密，然后获取以=替换字符
    index = random.randint(0, 2);
    if (index == 1):
        rStr = random.choice(first);
    elif(index == 2):
        rStr = random.choice(second);
    else:
        rStr =  random.choice(third);
    sign = sign.replace('=', 'rStr');
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
       sign = sy_encoding_base64(nStr);
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
    #print("sNows:", str(sNows));
    return str(sNows);


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
#####################################################################################
#创建文件夹数组
def getFoldArray():
    global foldArray,fold_min,fold_min,first,second;
    proNumber = random.randint(fold_min, fold_max);
    #遍历循环
    for i in range(proNumber):
        final = (random.choice(first));
        index = random.randint(3, 5);
        now = sy_getTimeNow();
        final += sy_randomSign(now);
        for i in range(index):
            final += (random.choice(second));
            final = os.path.join(target_desktop_path, final);
        foldArray.append(final);
        update_ImgPath(final);
    foldArray = list(set(foldArray));  # 数组去重
    print("foldArray:",str(len(foldArray)));
    return foldArray;


def getProjectArray():
    global projectArray,file_Count,first,second;
    #遍历循环
    for i in range(file_Count):
        final = (random.choice(first));
        index = random.randint(3, 5);
        now = sy_getTimeNow();
        final += sy_randomSign(now);
        for i in range(index):
            final += (random.choice(second))
        projectArray.append(final);
    projectArray = list(set(projectArray));  # 数组去重
    print("projectArray:",projectArray);
    return projectArray;

def getMethodNameArray():
    global methodArray;

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
   return sline_data;

#创建.h文件
def text_createH(outpath,fileNmae,msg1,propertyNumber,kmethodArray,kclassNameArray,msg3):
    global projectArray;
    full_path = outpath + os.path.sep + fileNmae + '.h';
    file = open(full_path, 'w');
    file.write('//%s.h'%(fileNmae)+msg_descrpt);
    msg = '#import <UIKit/UIKit.h>\n#import <Foundation/Foundation.h>\n';
    file.write(msg);
    file.write(msg1);
    #创建propryNameArray；
    propryNameArray = [];
    for index in range(1,propertyNumber):
        propryNameArray.append(random.choice(projectArray));
    #print "获取拼接后的数据:propryNameArray:", propryNameArray;
    propryNameArray = list(set(propryNameArray));
   # print "去除重复的propryNameArray:", propryNameArray;
    for propertyName in propryNameArray:
        file.write('@property(nonatomic,strong)'+random.choice(classArray)+' * '+propertyName+';\n');
    file.write('\n');
    # 创建methodNameArray；
    for methodName, className in zip(kmethodArray, kclassNameArray):
        aline = '- (nonnull %s *)hsd_%s:(nonnull %s *)info%s;\n'%(className,methodName,className,methodName);
        file.write(aline);
    for methodName, className in zip(kmethodArray, kclassNameArray):
        bline = '- (nonnull %s *)fus_%s:(nonnull %s *)for%s;\n'%(className,methodName,className,methodName);
        file.write(bline);
    for methodName, className in zip(kmethodArray, kclassNameArray):
        cline = '- (nonnull %s *)yhs_%s:(nonnull %s *)into%s;\n'%(className,methodName,className,methodName);
        file.write(cline);
    # 写入尾部@end；
    file.write(msg3);
    file.close();
    print('Done注意：%s.h 完成'%fileNmae);


#创建.m文件
def text_createM(outpath,fileNmae,msg,msg1,kmethodArray,kclassNameArray,msg3):
    full_path = outpath + os.path.sep + fileNmae + '.m';
    file = open(full_path, 'w');
    file.write('//  %s.h'%(fileNmae)+msg_descrpt);
    file.write(msg);
    file.write(msg1);

    for methodName, className in zip(kmethodArray, kclassNameArray):
        #print 'methodName:',methodName;
        #print 'className:',className;
        funcMehthod = getMehtodNameFunc(className,methodName);
        aline = '\n - (nonnull %s *)hsd_%s:(nonnull %s *)info%s {\n%s'%(className,methodName,className,methodName,funcMehthod);
        file.write(aline);
        file.write('\n\treturn %s;\n}\n' % (methodName));

    for methodName, className in zip(kmethodArray, kclassNameArray):
        # print 'methodName:',methodName;
        # print 'className:',className;
        funcMehthod = getMehtodNameFunc(className, methodName);
        bline = '\n - (nonnull %s *)fus_%s:(nonnull %s *)for%s {\n%s'%(className,methodName,className,methodName,funcMehthod);
        file.write(bline);
        file.write('\n\treturn %s;\n}\n' % (methodName));

    for methodName, className in zip(kmethodArray, kclassNameArray):
        # print 'methodName:',methodName;
        # print 'className:',className;
        funcMehthod = getMehtodNameFunc(className, methodName);
        cline = '\n - (nonnull %s *)yhs_%s:(nonnull %s *)into%s {\n%s'%(className,methodName,className,methodName,funcMehthod);
        file.write(cline);
        file.write('\n\treturn %s;\n}\n' % (methodName));

    file.write(msg3);
    file.close();
    print('Done注意：%s.m 完成'%fileNmae);

#####################################################################################
def creatModelFile():
    # 1.创建控制器的模型;
    global projectArray, file_list,foldArray;
    for file_name in projectArray:
        proNumber = random.randint(method_min, method_max);
        #print "初始化：proNumber:", number;
        methodNameArray = []
        for i in range(method_min, method_max):
            methodNameArray.append(random.choice(methodArray));
        methodNameArray = list(set(methodNameArray))  # 数组去重
        #print "初始化:methodNameArray:", methodNameArray;

        classNameArray = [];
        for i in range(method_min, method_max):
            classNameArray.append(random.choice(classArray));
        classNameArray = list(set(classNameArray))  # 数组去重
        #print "初始化:classNameArray:", classNameArray;
        file_list.append("#import \"" + file_name + ".h\"");
        target_iOS_folder = random.choice(foldArray);
        # 创建控制器的模型;
        text_createH(target_iOS_folder,file_name ,
                     '@interface ' + file_name + ':' + 'NSObject\n' \
                     + '\n+(' + file_name + '*)sharedInstance;\n',
                     proNumber,
                     methodNameArray,
                     classNameArray,
                     '\n\n@end');

        text_createM(target_iOS_folder,file_name,
                     '#import "' + file_name + '.h"\n\n' '@interface ' + file_name + '()\n\n @end\n\n',
                     '@implementation ' + file_name + '\n' + '\n+(' + file_name + ' *)sharedInstance {\n' \
                     + '\tstatic\t' + file_name + '  *sharedInstance = nil;' \
                     + '\n\tstatic dispatch_once_t predicate;' \
                     + '\n\tdispatch_once(&predicate, ^{' \
                     + '\n\t\t sharedInstance = [[self alloc] init];' \
                     + '\n\t});' \
                     + '\n\treturn sharedInstance;\n' \
                     + '}',

                     methodNameArray,
                     classNameArray,
                     '\n\n@end');

if __name__ == '__main__':
    update_ImgPath(target_desktop_path);
    getFoldArray();
    getProjectArray();
    creatModelFile();
    print('--开始创建ZZTrash.h--');
    all_header_text = "\n".join(file_list);
    target_iOS_folder = random.choice(foldArray);
    with open(os.path.join(target_iOS_folder, "ZZTrash.h"), "w") as fileObj:
        fileObj.write(all_header_text);
        fileObj.close();
    print('--共创建%s个项目--' % (len(projectArray) * 6));