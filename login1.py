from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox
import keshihua
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QMainWindow
import ht
from PyQt5 import QtCore, QtGui, QtWidgets
class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setWindowTitle("登录")
        self.resize(300, 200)

        self.label_username = QLabel(self)
        self.label_username.setGeometry(50, 50, 80, 30)
        self.label_username.setText("用户名:")
        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setGeometry(140, 50, 120, 30)

        self.label_password = QLabel(self)
        self.label_password.setGeometry(50, 100, 80, 30)
        self.label_password.setText("密码:")
        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setGeometry(140, 100, 120, 30)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton(self)
        self.button_login.setGeometry(120, 150, 60, 30)
        self.button_login.setText("登录")
        self.button_login.clicked.connect(self.login)

    def login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        # 在这里添加登录验证逻辑
        # ...

        if username == "admin" and password == "password":
            self.accept()
        else:
            QMessageBox.warning(self, "登录失败", "用户名或密码错误")

# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(640, 480)
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(110, 130, 141, 31))
#         self.label.setObjectName("label")
#         self.comboBox = QtWidgets.QComboBox(Form)
#         self.comboBox.setGeometry(QtCore.QRect(270, 130, 131, 31))
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.pushButton = QtWidgets.QPushButton(Form)
#         self.pushButton.setGeometry(QtCore.QRect(160, 230, 93, 28))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(Form)
#         self.pushButton_2.setGeometry(QtCore.QRect(310, 230, 93, 28))
#         self.pushButton_2.setObjectName("pushButton_2")
#
#         self.retranslateUi(Form)
#         self.pushButton.clicked.connect(self.call_keshihua)
#         self.pushButton_2.clicked.connect(Form.close)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.label.setText(_translate("Form", "请输入要查询的信息："))
#         self.comboBox.setItemText(0, _translate("Form", "设备基础信息统计表"))
#         self.comboBox.setItemText(1, _translate("Form", "厂家联系方式"))
#         self.comboBox.setItemText(2, _translate("Form", "场站人员名单"))
#         self.comboBox.setItemText(3, _translate("Form", "场站休假人员名单"))
#         self.pushButton.setText(_translate("Form", "确定"))
#         self.pushButton_2.setText(_translate("Form", "取消"))
#
#     def call_keshihua(self):
#         # text = self.lineEdit.text()
#         combo_text = self.comboBox.currentText()
#         # print(text)
#         # my_form.close()
#
#         if combo_text != '':
#             self.main_window = keshihua.keshihua1()
#             self.main_window.keshihua2(combo_text)
#             self.main_window.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    login_window = LoginWindow()
    if login_window.exec_() == QDialog.Accepted:
        main_window = QDialog()
        ui = ht.Ui_Form()
        ui.setupUi(main_window)
        main_window.show()

    sys.exit(app.exec_())
