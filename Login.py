# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QMainWindow
import shebei1
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import chanjia1
import admin1
import holiday1
import secret1
class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setWindowTitle("登录")
        self.resize(600, 500)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(210, 90, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setMidLineWidth(0)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(160, 200, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(250, 200, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(170, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(250, 250, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)   #隐藏密码

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(160, 330, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 330, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录界面"))
        self.label.setText(_translate("Form", "鸿天光伏场站"))
        self.label_2.setText(_translate("Form", "用户名"))
        self.comboBox.setItemText(0, _translate("Form", "商恒博"))
        self.comboBox.setItemText(1, _translate("Form", "曹征"))
        self.label_3.setText(_translate("Form", "密码"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "取消"))

    def login(self):
        combo_text = self.comboBox.currentText()
        label_text=self.lineEdit.text()

        # print(combo_text)
        # print(label_text)

        # 在这里添加登录验证逻辑
        # ...
        if combo_text == "商恒博" and label_text == "123456":
            self.accept()
        elif combo_text == "曹征" and label_text == "123456":
            self.accept()
        else:
            QMessageBox.warning(self, "登录失败", "用户名或密码错误")

class HT(LoginWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 130, 141, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(270, 130, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 230, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.call_keshihua)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "场站内部信息"))
        self.label.setText(_translate("Form", "请输入要查询的信息："))
        self.comboBox.setItemText(0, _translate("Form", "设备基础信息统计表"))
        self.comboBox.setItemText(1, _translate("Form", "厂家联系方式"))
        self.comboBox.setItemText(2, _translate("Form", "场站人员名单"))
        self.comboBox.setItemText(3, _translate("Form", "场站休假人员名单"))
        self.comboBox.setItemText(4, _translate("Form", "场站生活作息表"))
        self.comboBox.setItemText(5, _translate("Form", "主控室及二次设备用户及密码"))

        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))

    def call_keshihua(self):
        # text = self.lineEdit.text()
        combo_text = self.comboBox.currentText()
        # print(text)
        # my_form.close()

        # if combo_text != '':
        #     self.main_window = keshihua.keshihua1()
        #     self.main_window.keshihua2(combo_text)
        #     self.main_window.show()
        if combo_text=='设备基础信息统计表':
            self.main_window=shebei1.shebei_Form()
            self.main_window1 = QDialog()
            self.main_window.setupUi1(self.main_window1)
            # self.main_window.call_shebei()
            self.main_window1.show()
        elif combo_text=='厂家联系方式':
            self.main_window=chanjia1.chajia1_Form()
            self.main_window1=QDialog()
            self.main_window.setupUi1(self.main_window1)
            self.main_window1.show()
        elif combo_text=='场站人员名单':
            self.main_window=admin1.admin1_Form()
            self.main_window1=QDialog()
            self.main_window.setupUi1(self.main_window1)
            self.main_window1.show()
        elif combo_text=='场站休假人员名单':
            self.main_window=holiday1.holiday1_Form()
            self.main_window1=QDialog()
            self.main_window.setupUi1(self.main_window1)
            self.main_window1.show()
        elif combo_text=='主控室及二次设备用户及密码':
            self.main_window=secret1.secret1_Form()
            self.main_window1=QDialog()
            self.main_window.setupUi1(self.main_window1)
            self.main_window1.show()



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    login_window = LoginWindow()
    if login_window.exec_() == QDialog.Accepted:
        main_window = QDialog()
        ht =HT()
        ht.setupUi(main_window)
        main_window.show()
        sys.exit(app.exec_())