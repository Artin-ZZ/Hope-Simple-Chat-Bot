## Import All Global Libs Here ##
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setStyleSheet("*{\n"
"    border:none;\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"#centralwidget{\n"
"    background-image: url(./pics/rt.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"}\n"
"#header{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"}\n"
"#side_menu{\n"
"    background-color: #071e26;\n"
"    border-radius: 25px;\n"
"}\n"
"#btn1{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn2{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn3{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn4{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn5{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn5:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn5:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn1:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn2:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn3:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn4:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 82, 82),            stop:1 rgb(255, 140, 140));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn1:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn2:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn3:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn4:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"#body_dec{\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    background-image: url('./pics/s.jpg');\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"}\n"
"#body{\n"
"    border: none;\n"
"    background-image: url('./pics/df.png');\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border-radius: 25px;\n"
"}\n"
"/*================================================*/\n"
"#p2_header{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"}\n"
"#p2_sidemenu{\n"
"    background-color: #071e26;\n"
"    border-radius: 25px;\n"
"}\n"
"#btn1_2{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn2_2{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn3_2{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn4_2{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"\n"
"#btn1_2:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn2_2:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn3_2:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn4_2:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 82, 82),            stop:1 rgb(255, 140, 140));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn1_2:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn2_2:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn3_2:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn4_2:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"#p2bodydesc{\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    background-color: #333;\n"
"}\n"
"#p2_body{\n"
"    border: none;\n"
"    background-image: url(./pics/dg.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
# "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 195, 255), stop:0.189055 rgba(176, 0, 255, 255), stop:0.422886 rgba(148, 0, 255, 255), stop:0.621891 rgba(0, 255, 186, 255), stop:0.79602 rgba(0, 255, 204, 255), stop:1 rgba(0, 223, 255, 255));\n"
"    border-radius: 25px;\n"
"}\n"
"#sp_tk{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#sp_tk:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#sp_tk:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#head_lbl{\n"
"    color: #fff;\n"
"}\n"
"#result{\n"
"    color: #fff;\n"
"}\n"
"#txt_box{\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    background-color: rgb(176, 176, 176);\n"
"}\n"
"#submit_btn{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#submit_btn:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#submit_btn:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn5_2{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn5_2:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#btn5_2:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"/*======================== Login Page Ui =====================*/\n"
"#main_body{\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    background-image: url('./pics/banner-right.png');\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"}\n"
"#form_cont{\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    background-color: #333;\n"
"}\n"
"#login_btn{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#reg_btn{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245),            stop:1 rgb(240, 53, 218));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#reg_btn:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#login_btn:hover{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 102, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 250, 90),            stop:1 rgb(99, 255, 104));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#login_btn:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#reg_btn:pressed{\n"
"    font: 75 10pt \"Microsoft YaHei UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.338308 rgba(0, 255, 251, 255), stop:0.616915 rgba(0, 255, 93, 255));\n"
"    border-style: solid;\n"
"    border-radius:21px;\n"
"    padding: 10px;\n"
"}\n"
"#label_usernm{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#passw_lbl{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#usernm_txtbox{\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    background-color: rgb(159, 159, 159);\n"
"    color: #000;\n"
"}\n"
"#passw_txtbox{\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    background-color: rgb(159, 159, 159);\n"
"    color: #000;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.main_body = QtWidgets.QFrame(self.page1)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.form_cont = QtWidgets.QFrame(self.main_body)
        self.form_cont.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_cont.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_cont.setObjectName("form_cont")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.form_cont)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_usernm = QtWidgets.QLabel(self.form_cont)
        self.label_usernm.setMinimumSize(QtCore.QSize(600, 70))
        self.label_usernm.setMaximumSize(QtCore.QSize(600, 70))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.label_usernm.setFont(font)
        self.label_usernm.setObjectName("label_usernm")
        self.verticalLayout_10.addWidget(self.label_usernm, 0, QtCore.Qt.AlignTop)
        self.usernm_txtbox = QtWidgets.QLineEdit(self.form_cont)
        self.usernm_txtbox.setMinimumSize(QtCore.QSize(600, 100))
        self.usernm_txtbox.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.usernm_txtbox.setFont(font)
        self.usernm_txtbox.setText("")
        self.usernm_txtbox.setObjectName("usernm_txtbox")
        self.verticalLayout_10.addWidget(self.usernm_txtbox)
        self.passw_lbl = QtWidgets.QLabel(self.form_cont)
        self.passw_lbl.setMinimumSize(QtCore.QSize(600, 70))
        self.passw_lbl.setMaximumSize(QtCore.QSize(600, 70))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.passw_lbl.setFont(font)
        self.passw_lbl.setObjectName("passw_lbl")
        self.verticalLayout_10.addWidget(self.passw_lbl)
        self.passw_txtbox = QtWidgets.QLineEdit(self.form_cont)
        self.passw_txtbox.setMinimumSize(QtCore.QSize(600, 100))
        self.passw_txtbox.setMaximumSize(QtCore.QSize(600, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.passw_txtbox.setFont(font)
        self.passw_txtbox.setText("")
        self.passw_txtbox.setObjectName("passw_txtbox")
        self.verticalLayout_10.addWidget(self.passw_txtbox)
        self.login_btn = QtWidgets.QPushButton(self.form_cont)
        self.login_btn.setMinimumSize(QtCore.QSize(600, 50))
        self.login_btn.setMaximumSize(QtCore.QSize(600, 50))
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout_10.addWidget(self.login_btn)
        self.reg_btn = QtWidgets.QPushButton(self.form_cont)
        self.reg_btn.setMinimumSize(QtCore.QSize(600, 50))
        self.reg_btn.setMaximumSize(QtCore.QSize(600, 50))
        self.reg_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reg_btn.setObjectName("reg_btn")
        self.verticalLayout_10.addWidget(self.reg_btn)
        self.horizontalLayout_3.addWidget(self.form_cont, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_9.addWidget(self.main_body)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header = QtWidgets.QFrame(self.page2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.header)
        self.body = QtWidgets.QFrame(self.page2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QFrame(self.body)
        self.side_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn1 = QtWidgets.QPushButton(self.side_menu)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setObjectName("btn1")
        self.verticalLayout_3.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.side_menu)
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2.setObjectName("btn2")
        self.verticalLayout_3.addWidget(self.btn2)
        self.btn3 = QtWidgets.QPushButton(self.side_menu)
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3.setObjectName("btn3")
        self.verticalLayout_3.addWidget(self.btn3)
        self.btn5 = QtWidgets.QPushButton(self.side_menu)
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn5.setObjectName("btn5")
        self.verticalLayout_3.addWidget(self.btn5)
        self.btn4 = QtWidgets.QPushButton(self.side_menu)
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn4.setStyleSheet("")
        self.btn4.setObjectName("btn4")
        self.verticalLayout_3.addWidget(self.btn4)
        self.horizontalLayout.addWidget(self.side_menu, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.body_dec = QtWidgets.QFrame(self.body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body_dec.sizePolicy().hasHeightForWidth())
        self.body_dec.setSizePolicy(sizePolicy)
        self.body_dec.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_dec.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_dec.setObjectName("body_dec")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.body_dec)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.body_dec)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.body_dec)
        self.verticalLayout_2.addWidget(self.body)
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.p2_header = QtWidgets.QFrame(self.page3)
        self.p2_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.p2_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.p2_header.setObjectName("p2_header")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.p2_header)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.p2_header_lbl = QtWidgets.QLabel(self.p2_header)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.p2_header_lbl.setFont(font)
        self.p2_header_lbl.setObjectName("p2_header_lbl")
        self.verticalLayout_7.addWidget(self.p2_header_lbl, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.p2_header)
        self.p2_body = QtWidgets.QFrame(self.page3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p2_body.sizePolicy().hasHeightForWidth())
        self.p2_body.setSizePolicy(sizePolicy)
        self.p2_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.p2_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.p2_body.setObjectName("p2_body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.p2_body)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.p2_sidemenu = QtWidgets.QFrame(self.p2_body)
        self.p2_sidemenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.p2_sidemenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.p2_sidemenu.setObjectName("p2_sidemenu")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.p2_sidemenu)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn1_2 = QtWidgets.QPushButton(self.p2_sidemenu)
        self.btn1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1_2.setObjectName("btn1_2")
        self.verticalLayout_8.addWidget(self.btn1_2)
        self.btn2_2 = QtWidgets.QPushButton(self.p2_sidemenu)
        self.btn2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2_2.setObjectName("btn2_2")
        self.verticalLayout_8.addWidget(self.btn2_2)
        self.btn3_2 = QtWidgets.QPushButton(self.p2_sidemenu)
        self.btn3_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3_2.setObjectName("btn3_2")
        self.verticalLayout_8.addWidget(self.btn3_2)
        self.btn5_2 = QtWidgets.QPushButton(self.p2_sidemenu)
        self.btn5_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn5_2.setObjectName("btn5_2")
        self.verticalLayout_8.addWidget(self.btn5_2)
        self.btn4_2 = QtWidgets.QPushButton(self.p2_sidemenu)
        self.btn4_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn4_2.setStyleSheet("")
        self.btn4_2.setObjectName("btn4_2")
        self.verticalLayout_8.addWidget(self.btn4_2)
        self.horizontalLayout_2.addWidget(self.p2_sidemenu, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.p2bodydesc = QtWidgets.QFrame(self.p2_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p2bodydesc.sizePolicy().hasHeightForWidth())
        self.p2bodydesc.setSizePolicy(sizePolicy)
        self.p2bodydesc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.p2bodydesc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.p2bodydesc.setObjectName("p2bodydesc")
        self.gridLayout = QtWidgets.QGridLayout(self.p2bodydesc)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_box = QtWidgets.QLineEdit(self.p2bodydesc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_box.sizePolicy().hasHeightForWidth())
        self.txt_box.setSizePolicy(sizePolicy)
        self.txt_box.setMinimumSize(QtCore.QSize(1200, 100))
        self.txt_box.setMaximumSize(QtCore.QSize(1200, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.txt_box.setFont(font)
        self.txt_box.setText("")
        self.txt_box.setObjectName("txt_box")
        self.gridLayout.addWidget(self.txt_box, 3, 0, 1, 1)
        self.submit_btn = QtWidgets.QPushButton(self.p2bodydesc)
        self.submit_btn.setMinimumSize(QtCore.QSize(150, 100))
        self.submit_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_btn.setObjectName("submit_btn")
        self.gridLayout.addWidget(self.submit_btn, 3, 1, 1, 1)
        self.head_lbl = QtWidgets.QLabel(self.p2bodydesc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.head_lbl.sizePolicy().hasHeightForWidth())
        self.head_lbl.setSizePolicy(sizePolicy)
        self.head_lbl.setMinimumSize(QtCore.QSize(500, 150))
        self.head_lbl.setMaximumSize(QtCore.QSize(500, 150))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.head_lbl.setFont(font)
        self.head_lbl.setObjectName("head_lbl")
        self.gridLayout.addWidget(self.head_lbl, 1, 0, 1, 1)
        self.result = QtWidgets.QLabel(self.p2bodydesc)
        self.result.setMinimumSize(QtCore.QSize(1200, 100))
        self.result.setMaximumSize(QtCore.QSize(1200, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 4, 0, 1, 1)
        self.sp_tk = QtWidgets.QPushButton(self.p2bodydesc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sp_tk.sizePolicy().hasHeightForWidth())
        self.sp_tk.setSizePolicy(sizePolicy)
        self.sp_tk.setMinimumSize(QtCore.QSize(100, 50))
        self.sp_tk.setMaximumSize(QtCore.QSize(200, 50))
        self.sp_tk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sp_tk.setObjectName("sp_tk")
        self.gridLayout.addWidget(self.sp_tk, 4, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.p2bodydesc)
        self.verticalLayout_6.addWidget(self.p2_body)
        self.stackedWidget.addWidget(self.page3)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hope Chat Bot"))
        self.label_usernm.setText(_translate("MainWindow", "User Name:"))
        self.passw_lbl.setText(_translate("MainWindow", "Password:"))
        self.login_btn.setText(_translate("MainWindow", "LogIn"))
        self.reg_btn.setText(_translate("MainWindow", "Sign Up"))
        self.label.setText(_translate("MainWindow", "TALKING HOPE 😎🎶"))
        self.btn1.setText(_translate("MainWindow", "HOME"))
        self.btn2.setText(_translate("MainWindow", "START"))
        self.btn3.setText(_translate("MainWindow", "ABOUT ME"))
        self.btn5.setText(_translate("MainWindow", "Manage DB"))
        self.btn4.setText(_translate("MainWindow", "Log Out"))
        self.label_2.setText(_translate("MainWindow", "What is Talking Hope Chat Bot & What Can It Do:\n"
"\n"
"Well as Its abvious This Is A Chat Bot Designed\n"
"For Fun And Talknig a Lot, The Features Are Yet\n"
"Unknown.\n"
""))
        self.p2_header_lbl.setText(_translate("MainWindow", "TALKING HOPE 😎🎶"))
        self.btn1_2.setText(_translate("MainWindow", "HOME"))
        self.btn2_2.setText(_translate("MainWindow", "START"))
        self.btn3_2.setText(_translate("MainWindow", "ABOUT ME"))
        self.btn5_2.setText(_translate("MainWindow", "Manage DB"))
        self.btn4_2.setText(_translate("MainWindow", "Log Out"))
        self.submit_btn.setText(_translate("MainWindow", "Submit"))
        self.head_lbl.setText(_translate("MainWindow", "Lets Talk Type In Some Thing \n"
" Or click \"Speach Talk\" Button\n and im case sensitive!"))
        self.result.setText(_translate("MainWindow", "Hope Says:"))
        self.sp_tk.setText(_translate("MainWindow", "Speach Talk"))