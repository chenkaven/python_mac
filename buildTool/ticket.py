# -*- coding:utf-8 -*-
"""
@author Jianxiong Rao
"""
from splinter.browser import Browser
from time import sleep
import traceback
import time, sys
import os
import threading


# --12306用户名 密码--
UserName = u"18359725318"
Passwd = u"848930qaz"
# cookies值自己找
#https://kyfw.12306.cn/otn/leftTicket/init：f12网络(消息头，cookie# )
StartStation = u"%u6CF0%u5B81%2CTNS"#泰宁
EndStation = u"%u53A6%u95E8%2CXMS" #厦门
# 时间格式2018-02-05
DateTime = u"2018-10-06"

# 车次,选择第几趟,0则从上之下依次点击
Order = 0
###乘客姓名
UserList = [u'陈镇华']


class HuoChe(object):
    ##席位
    xb = u"二等座"
    pz = u"成人票"

    """12306网址"""
    # 12306登录URL
    login_url = "https://kyfw.12306.cn/otn/login/init"
    # 12306查询URL
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    # 我的12306URL
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    # 购票URL
    Main_buy = "https://kyfw.12306.cn/otn/confirmPassenger/initDc";

    def __init__(self):
        self.driver_name = 'chrome'
        self.executable_path = os.getcwd()+'/chromedriver'
        print("Welcome To Use The Tool");

    def login(self):
        self.driver.visit(self.login_url)
        # 填充密码
        self.driver.fill("loginUserDTO.user_name", UserName)
        # sleep(1)
        self.driver.fill("userDTO.password", Passwd)
        print("等待验证码，自行输入....");
        while True:
            if self.driver.url != self.initmy_url:
                #print (self.driver.url);
                sleep(1);
            else:
                #print("断开循环");
                break;

    def startBuy(self):
        print("--购票开始：15秒刷新--");
        self.driver.visit(self.ticket_url);
        try:
            self.driver.cookies.add({"_jc_save_fromStation": StartStation}); #订车起点
            self.driver.cookies.add({"_jc_save_toStation": EndStation}); #订车终点
            self.driver.cookies.add({"_jc_save_fromDate": DateTime}); #订车时间
            self.driver.cookies.add({"_jc_save_wfdc_flag": "dc"});  # 订车时间
            self.driver.reload();
            count = 0
            if Order != 0:
                while self.driver.url == self.ticket_url:
                    self.driver.find_bytext(u"查询").click()
                    count += 1
                    print("循环点击查询.... 第 %s 次" % count)
                    # sleep(1)
                    try:
                        self.driver.find_by_text(u'预订')[Order - 1].click()
                    except Exception as e:
                        print("还没开始预订 %s"%(e))
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print("循环点击查询.... 第 %s 次" % count)
                    # sleep(0.8)
                    try:
                        for i in self.driver.find_by_text(u"预订"):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print("还没开始预订 %s"%(e))
                        continue

            print("开始预订....");
            sleep(1);
            print("开始选择用户....");
            for user in UserList:
                self.driver.find_by_text(user).last.click();
            #成人票
            self.driver.find_by_text(self.pz).click();
            self.driver.find_by_id('').select(self.pz);
            sleep(1);
            #选择二等座
            self.driver.find_by_text(self.xb).click();
            sleep(1);
            print("提交订单....");
            self.driver.find_by_id('submitOrder_id').click();
            # self.driver.find_by_id('1D').last.click();
            # self.driver.find_by_id('1F').last.click();
            print("开始选座...");
            sleep(1.5);
            print("确认选座....");
            self.driver.find_by_text('qr_submit_id').click();
        except Exception as e:
            print(e)
        #定义定时器；
        global timer  # 定义变量
        timer = threading.Timer(15, self.startBuy)  # 60秒调用一次函数
        timer.start();


    def start(self):
        self.driver = Browser("chrome")
        self.driver.driver.set_window_size(1400, 1000)
        self.login();
        self.startBuy();





if __name__ == "__main__":
    train = HuoChe()
    train.start();
