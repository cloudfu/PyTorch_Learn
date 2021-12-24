import time

from texttable import Texttable


class UserVisionData:

    def __init__(self, args):
        """
        打印数据初始化
        :param args:Excel导出参数，通过，进行分割
        """
        # 字符串分割
        array_print_data = args.split(",")

        self.title = "打印测试"
        self.printDateTime = time.strftime("%Y-%m-%d %H:%M:%S")

        # 用户信息
        self.userName = array_print_data[0]
        self.phoneNum = array_print_data[1]
        self.billOwner = array_print_data[2]
        self.Purpose = array_print_data[3]

        # 验光信息
        self.SPH_RightEye = array_print_data[4]
        self.SPH_LeftEye = array_print_data[5]
        self.CYL_RightEye = array_print_data[6]
        self.CYL_LeftEye = array_print_data[7]
        self.AXIS_RightEye = array_print_data[8]
        self.AXIS_LeftEye = array_print_data[9]
        self.DOWN_RightEye = array_print_data[10]
        self.DOWN_LeftEye = array_print_data[11]
        self.DIST_RightEye = array_print_data[12]
        self.DIST_LeftEye = array_print_data[13]

        # 备注
        self.Comments = array_print_data[14]

    def printTextTable(self):
        """
        打印表格数据
        :return:
        """
        table_user_info = Texttable()
        table_user_info.set_deco(Texttable.HEADER)
        table_user_info.set_header_align(["l", "l"])
        table_user_info.set_cols_align(["r", "l"])
        table_user_info.add_rows([["用户信息", ""],
                                  ["姓名:", self.userName, ],
                                  ["手机号:", self.phoneNum],
                                  ["所属人:", self.billOwner],
                                  ["配镜用途:", self.Purpose],
                                  ["打印时间:", self.printDateTime],
                                  ["备注:", self.Comments]])
        print(table_user_info.draw())

        print()

        table_eyes_info = Texttable()
        table_eyes_info.set_deco(Texttable.HEADER)
        table_eyes_info.set_header_align(["c", "c", "c", "c", "c", "c"])
        table_eyes_info.set_cols_align(["c", "c", "c", "c", "c", "c"])
        table_eyes_info.add_rows([["", "度数", "散光", "轴位", "下加光", "瞳距"],
                                  ["右眼:", self.SPH_RightEye, self.CYL_RightEye, self.AXIS_RightEye, self.DOWN_RightEye,
                                   self.DIST_RightEye],
                                  ["左眼:", self.SPH_LeftEye, self.CYL_LeftEye, self.AXIS_LeftEye, self.DOWN_LeftEye,
                                   self.DIST_LeftEye]])

        table = table_eyes_info.draw()
        print(table)

    def getHtmlData(self):
        """
        获取云端打印数据格式
        :return:返回html数据打印格式
        """
        html = "<CB>" + self.title + "</CB>\n"
        html += "用户姓名:" + self.userName + "\n"
        html += "电话号码:" + self.phoneNum + "\n"
        html += "  所属人:" + self.billOwner + "\n"
        html += "配镜用途:" + self.Purpose + "\n"
        html += "--------------------------------\n"
        html += "验光数据:\n"

        table_eyes_info = Texttable()
        table_eyes_info.set_deco(Texttable.HEADER)
        table_eyes_info.set_header_align(["c", "c", "c", "c", "c", "c"])
        table_eyes_info.set_cols_align(["c", "c", "c", "c", "c", "c"])
        table_eyes_info.add_rows([["", "度数", "散光", "轴位", "下加光", "瞳距"],
                                  ["右眼:", self.SPH_RightEye, self.CYL_RightEye, self.AXIS_RightEye, self.DOWN_RightEye,
                                   self.DIST_RightEye],
                                  ["左眼:", self.SPH_LeftEye, self.CYL_LeftEye, self.AXIS_LeftEye, self.DOWN_LeftEye,
                                   self.DIST_LeftEye]])

        html += table_eyes_info.draw().replace("=", "-")
        html += "\n--------------------------------\n"
        html += "备注信息:" + self.Comments + "\n"
        html += "打印时间:" + self.printDateTime + "\n"
        return html


def formatPrintData(data):
    pass
    # # 文件路径
    # filePath = array_print_data[15] + "\\log.txt"
    #
    # with open(filePath, "w+") as file:
    #     for i in range(len(array_print_data)):
    #         file.write(str(i) + ":" + array_print_data[i] + "\n")


def printData():
    data = "姓名1,手机号1,验光单所属人1,配镜用途1,右眼SPH,右眼SPH,右眼CYL,右眼CYL,右眼AXIS,右眼AXIS,右眼下加光,右眼下加光,右眼瞳距,右眼瞳距,comments,D:\\print"
    # data = sys.argv[1]

    userVisionData = UserVisionData(data)
    userVisionData.printTextTable()
    print(userVisionData.getHtmlData())

    #
    # print_localTime = time.local(time.time())
    # print_strTime = time.strftime("%Y-%m-%d %H:%M:%S", print_localTime)
    #
    # print_html = "<CB>5.67眼镜甄选</CB><BR>"
    # print_html += "<CB>您眼镜BUG的修复师</CB><BR>"
    # print_html += "基本信息:" + userName + " " + phoneNum + "<BR>"
    # print_html += "所属人:" + billOwner + "<BR>"
    # print_html += "配镜用途:" + Purpose + "<BR>"
    # print_html += "打印时间:" + print_strTime + "<BR>"
    # print_html += "--------------------------------<BR>"
    #
    # print_html += "验光数据<BR>"
    # print_html += "--------------------------------<BR>"
    # print_html += "--------------------------------<BR>"
    # print_html += "备注信息"
    # print_html += "--------------------------------<BR>"


if __name__ == '__main__':
    printData()
