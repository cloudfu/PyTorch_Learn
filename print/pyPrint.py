# coding:utf-8

import time
from hashlib import sha1
import requests

# 说明：
URL = "http://api.feieyun.cn/Api/Open/"  # 不需要修改
USER = "55387938@qq.com"  # *必填*：飞鹅云后台注册账号
UKEY = "HPJtdVP3FZSBnkJ2"  # *必填*: 飞鹅云后台注册账号后生成的UKEY 【备注：这不是填打印机的KEY】
SN = "960800945"  # *必填*：打印机编号，必须要在管理后台里手动添加打印机或者通过API添加之后，才能调用API


# 签名
def signature(STIME):
    s1 = sha1()
    s1.update((USER + UKEY + STIME).encode())
    return s1.hexdigest()


def addprinter(snlist):
    STIME = str(int(time.time()))  # 不需要修改
    params = {
        'user': USER,
        'sig': signature(STIME),
        'stime': STIME,
        'apiname': 'Open_printerAddlist',  # 固定值,不需要修改
        'printerContent': snlist
    }
    response = requests.post(URL, data=params, timeout=30)
    code = response.status_code  # 响应状态码
    if code == 200:
        print(response.content)
    else:
        print("error")


# 小票机打印订单接口
def printMsg(sn):
    # 标签说明：
    # 单标签:
    # "<BR>"为换行,"<CUT>"为切刀指令(主动切纸,仅限切刀打印机使用才有效果)
    # "<LOGO>"为打印LOGO指令(前提是预先在机器内置LOGO图片),"<PLUGIN>"为钱箱或者外置音响指令
    # 成对标签：
    # "<CB></CB>"为居中放大一倍,"<B></B>"为放大一倍,"<C></C>"为居中,<L></L>字体变高一倍
    # <W></W>字体变宽一倍,"<QR></QR>"为二维码,"<BOLD></BOLD>"为字体加粗,"<RIGHT></RIGHT>"为右对齐
    # 条形码标签
    # <BC128_A>123ABCDEF</BC128_A>：数字字母混合条形码, 最多支持14位数字大写字母混合
    # <BC128_C>0123456789</BC128_C>：最多支持22位纯数字
    # 拼凑订单内容时可参考如下格式
    # 根据打印纸张的宽度，自行调整内容的格式，可参考下面的样例格式

    content = "<CB>测试打印</CB><BR>"
    content += "名称　　　　　 单价  数量 金额<BR>"
    content += "--------------------------------<BR>"
    content += "饭　　　　　　 1.0    1   1.0<BR>"
    content += "炒饭　　　　　 10.0   10  10.0<BR>"
    content += "蛋炒饭　　　　 10.0   10  100.0<BR>"
    content += "鸡蛋炒饭　　　 100.0  1   100.0<BR>"
    content += "番茄蛋炒饭　　 1000.0 1   100.0<BR>"
    content += "西红柿蛋炒饭　 1000.0 1   100.0<BR>"
    content += "西红柿鸡蛋炒饭 100.0  10  100.0<BR>"
    content += "备注：加辣<BR>"
    content += "--------------------------------<BR>"
    content += "合计：xx.0元<BR>"
    content += "送货地点：上海市浦东新区xxx路"
    content += "联系电话：13888888888888<BR>"
    content += "订餐时间：2021-12-21 17:59:08<BR>"
    content += "<QR>http://www.baidu.com</QR>"  # 把二维码字符串用标签套上即可自动生成二维码
    STIME = str(int(time.time()))  # 不需要修改
    params = {
        'user': USER,
        'sig': signature(STIME),
        'stime': STIME,
        'apiname': 'Open_printMsg',  # 固定值,不需要修改
        'sn': sn,
        'content': content,
        'times': '1'  # 打印联数
    }
    response = requests.post(URL, data=params, timeout=30)
    code = response.status_code  # 响应状态码
    if code == 200:
        print(response.content)  # 服务器返回的JSON字符串,建议要当做日志记录起来
    else:
        print("error")


# 标签机打印订单接口
def printLabelMsg(sn):
    # 标签说明：
    # 以下标签里面的x，y值参数说明：
    #    x，y值需要按照实际使用的纸规格大小取值。例如标签纸大小为：宽40mm，高度为30mm。
    #    1mm=8dots
    #    x的最大值就是40*8=320，x的取值范围是0-320。
    #    y的最大值就是为30*8=240，y的取值范围是0-240。
    #
    #  <SIZE>width,height</SIZE>：
    #  该设置宽高标签只需要发送设置一次生效即可，无需放在代码每次打印设置
    #  设置卷标纸宽高，width 标签纸的宽度(不含背纸)，height 标签纸的高度(不含背纸)，单位mm，如<SIZE>30,20</SIZE>
    #
    #  <DIRECTION>n</DIRECTION> ：
    #  设定打印时出纸和打印字体的方向，n 0 或 1，每次设备重启后都会初始化为 0 值设置，1：正向出纸，0：反向出纸，
    #  如<DIRECTION>1</DIRECTION>
    #
    #  <QR x="10"  y="100"  e="L"  w="5">二维码内容</QR>：
    #  打印二维码，其中属性x为水平方向起始点坐标（默认为0），属性y为垂直方向起始点坐标（默认为0），属性e为纠错等级：
    #  L 7%M 15%Q 25%H 30%（默认为K），属性w为二维码宽度（默认为5）
    #
    #  <TEXT x="10" y="100" font="12" w="2" h="2" r="0">文本内容</TEXT>：
    #  打印文本，其中属性x为水平方向起始点坐标（默认为0），属性y为垂直方向起始点坐标（默认为0），属性font为字体：
    #  1、 8×12 dot 英数字体
    #  2、 12×20 dot 英数字体
    #  3、 16×24 dot 英数字体
    #  4、 24×32 dot 英数字体
    #  5、 32×48 dot 英数字体
    #  6、 14×19 dot 英数字体 OCR-B
    #  7、 21×27 dot 英数字体 OCR-B
    #  8、 14×25 dot 英数字体 OCR-A
    #  9、 9×17 dot 英数字体
    #  10、 12×24 dot 英数字体
    #  11、 繁体中文 24×24Font(大五码)
    #  12、 简体中文 24×24Font(GB 码)
    #  13、 韩文 24×24Font(KS 码)
    #
    #  默认为12 简体中文 24×24Font(GB 码)，属性w为文字宽度放大倍率1-10（默认为1），属性h为文字高度放大倍率1-10
    #  属性r为文字旋转角度(顺时针方向)：
    #  0     0度
    #  90   90度
    #  180 180度
    #  270 270度
    #  （默认为0）
    #
    #  <BC128 x="10" y="100" h="80" s="1" r="0" n="1" w="1">12345678</BC128>：打印code128一维码，其中属性x为水平
    #  方向起始点坐标（默认为0），属性y为垂直方向起始点坐标（默认为0），属性s是否人眼可识：0 不可识，1 可识（默认为1），
    #  属性n为窄 bar 宽度，以点(dot)表示（默认为1），属性w为宽 bar 宽度（默认为1），以点(dot)表示，属性r为文字旋转角度
    #  (顺时针方向)：
    #  0     0度
    #  90   90度
    #  180 180度
    #  270 270度
    #  （默认为0）

    # 根据打印纸张的宽度，自行调整内容的格式，可参考下面的样例格式
    content = "<DIRECTION>1</DIRECTION>"
    content += "<TEXT x='5' y='10' font='12' w='1' h='2' r='0'>#001       五号桌      1/3</TEXT>"
    content += "<TEXT x='80' y='80' font='12' w='2' h='2' r='0'>可乐鸡翅</TEXT>"
    content += "<TEXT x='5' y='180' font='12' w='1' h='1' r='0'>张三先生       13800138000</TEXT>"

    STIME = str(int(time.time()))  # 不需要修改
    params = {
        'user': USER,
        'sig': signature(STIME),
        'stime': STIME,
        'apiname': 'Open_printLabelMsg',  # 固定值,不需要修改
        'sn': sn,
        'content': content,
        'times': '1'  # 打印联数
    }
    response = requests.post(URL, data=params, timeout=30)
    code = response.status_code  # 响应状态码
    if code == 200:
        print(response.content)  # 服务器返回的JSON字符串,建议要当做日志记录起来
    else:
        print("error")


def queryOrderState(orderid):
    STIME = str(int(time.time()))  # 不需要修改
    params = {
        'user': USER,
        'sig': signature(STIME),
        'stime': STIME,
        'apiname': 'Open_queryOrderState',  # 固定值,不需要修改
        'orderid': orderid
    }
    response = requests.post(URL, data=params, timeout=30)
    code = response.status_code  # 响应状态码
    if code == 200:
        print(response.content)  # 返回的JSON字符串
    else:
        print("error")


def queryOrderInfoByDate(sn, strdata):
    STIME = str(int(time.time()))  # 不需要修改
    params = {
        'user': USER,
        'sig': signature(STIME),
        'stime': STIME,
        'apiname': 'Open_queryOrderInfoByDate',  # 固定值,不需要修改
        'sn': sn,
        'date': strdata,
    }
    response = requests.post(URL, data=params, timeout=30)
    code = response.status_code  # 响应状态码
    if code == 200:
        print(response.content)  # 返回的JSON字符串
    else:
        print("error")


def queryPrinterStatus(sn):
    STIME = str(int(time.time()))  # 不需要修改
    params = {
        'user': USER,
        'sig': signature(STIME),
        'stime': STIME,
        'apiname': 'Open_queryPrinterStatus',  # 固定值,不需要修改
        'sn': sn,
    }
    response = requests.post(URL, data=params, timeout=30)
    code = response.status_code  # 响应状态码
    if code == 200:
        print(response.content)  # 返回的JSON字符串
    else:
        print("error")

    # **********测试时，打开下面注释掉方法的即可,更多接口文档信息,请访问官网开放平台查看**********

def getPrintData():
    log_file = "d:\\lucky.txt"

    str_print_data = "姓名1,手机号1,验光单所属人1,配镜用途1,右眼SPH,右眼SPH,右眼CYL,右眼CYL,右眼AXIS,右眼AXIS,右眼下加光,右眼下加光,右眼瞳距,右眼瞳距,comments"
    print(str_print_data)
    array_print_data = str_print_data.split(",")

    # 用户信息
    userName = array_print_data[0]
    phoneNum = array_print_data[1]
    billOwner = array_print_data[2]
    Purpose = array_print_data[3]

    # 验光信息
    SPH_RightEye = array_print_data[4]
    SPH_LeftEye = array_print_data[5]
    CYL_RightEye = array_print_data[6]
    CYL_LeftEye = array_print_data[7]
    AXIS_RightEye = array_print_data[8]
    AXIS_LeftEye = array_print_data[9]
    DOWN_RightEye = array_print_data[10]
    DOWN_LeftEye = array_print_data[11]
    DIST_RightEye = array_print_data[12]
    DIST_LeftEye = array_print_data[13]

    # 备注
    Comments = array_print_data[14]

    with open(f, "w+") as file:
        for i in range(len(array_print_data)):
            file.write(str(i) + ":" + array_print_data[i] + "\n")

if __name__ == '__main__':
    # ==================添加打印机接口（支持批量）==================
    # ***返回值JSON字符串***
    # 成功：{"msg":"ok","ret":0,"data":"xxxxxxx_xxxxxxxx_xxxxxxxx","serverExecutedTime":5}
    # 失败：{"msg":"错误描述","ret":非0,"data":"null","serverExecutedTime":5}

    # 提示：打印机编号(必填) # 打印机识别码(必填) # 备注名称(选填) # 流量卡号码(选填)，多台打印机请换行（\n）添加新打印机信息，每次最多100行(台)。
    # snlist = "sn1#key1#remark1#carnum1\nsn2#key2#remark2#carnum2"
    # addprinter(snlist)

    # ==================方法1.小票机打印订单==================
    # ***返回值JSON字符串***
    # 成功：{"msg":"ok","ret":0,"data":"xxxxxxx_xxxxxxxx_xxxxxxxx","serverExecutedTime":5}
    # 失败：{"msg":"错误描述","ret":非0,"data":"null","serverExecutedTime":5}
    printMsg(SN)

    # ==================方法2.标签机打印订单==================
    # ***返回值JSON字符串***
    # 成功：{"msg":"ok","ret":0,"data":"xxxxxxx_xxxxxxxx_xxxxxxxx","serverExecutedTime":5}
    # 失败：{"msg":"错误描述","ret":非0,"data":"null","serverExecutedTime":5}
    # printLabelMsg(SN)

    # ===========方法3.查询某订单是否打印成功=============
    # ***返回值JSON字符串***
    # 成功：{"msg":"ok","ret":0,"data":true,"serverExecutedTime":2}//data:true为已打印,false为未打印
    # 失败：{"msg":"错误描述","ret":非0, "data":null,"serverExecutedTime":7}
    # queryOrderState("xxxxxxxx_xxxxxxxx_xxxxxxxx")#订单ID，从方法1返回值data获取

    # ===========方法4.查询指定打印机某天的订单详情============
    # ***返回值JSON字符串***
    # 成功：{"msg":"ok","ret":0,"data":{"print":6,"waiting":1},"serverExecutedTime":9}//print已打印，waiting为打印
    # 失败：{"msg":"错误描述","ret":非0,"data":"null","serverExecutedTime":5}
    # queryOrderInfoByDate(SN,"2017-04-02")#注意时间格式为"yyyy-MM-dd"

    # ===========方法5.查询打印机的状态==========================
    # ***返回的状态有如下几种***
    # 成功：{"msg":"ok","ret":0,"data":"状态","serverExecutedTime":4}
    # 失败：{"msg":"错误描述","ret":非0,"data":"null","serverExecutedTime":5}
    # queryPrinterStatus(SN)

    pass








