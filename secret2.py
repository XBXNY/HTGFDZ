import sqlite3
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QTableView, QTableWidget
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
# 创建应用程序对象
class secret2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("鸿天光伏场站")
        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)
        self.resize(1000, 750)

    def keshihua2(self, name):
        a = name
        if a=='全部信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备用户及密码', conn)
        elif a=='五防机':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='五防机'", conn)
        elif a=='AGC/AVC机':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='AGC/AVC机'", conn)
        elif a=='光功率预测机':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='光功率预测机'", conn)
        elif a=='拷贝工作站':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='拷贝工作站'", conn)
        elif a=='OMS':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='OMS'", conn)
        elif a=='光伏区主机':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='光伏区主机'", conn)
        elif a=='光伏区备机':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='光伏区备机'", conn)
        elif a=='升压站主机':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='升压站主机'", conn)
        elif a=='升压站备机':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='升压站备机'", conn)
        elif a=='保护及故障信息子站柜':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='保护及故障信息子站柜'", conn)
        elif a=='二次安防柜':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='二次安防柜'", conn)
        elif a=='快速频率控制柜':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='快速频率控制柜'", conn)
        elif a=='AGC/AVC控制系统柜（服务器1，4n）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='AGC/AVC控制系统柜（服务器1，4n）'", conn)
        elif a=='AGC/AVC控制系统柜（服务器2，5n）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='AGC/AVC控制系统柜（服务器2，5n）'", conn)
        elif a=='历史服务器柜（服务器1，4n）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='历史服务器柜（服务器1，4n）'", conn)
        elif a=='历史服务器柜（服务器2，5n）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='历史服务器柜（服务器2，5n）'", conn)
        elif a=='数据处理服务器柜（服务器1，4n）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='数据处理服务器柜（服务器1，4n）'", conn)
        elif a=='数据处理服务器柜（服务器2，5n）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='数据处理服务器柜（服务器2，5n）'", conn)
        elif a=='光功率服务器柜（服务器1，最上侧）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='光功率服务器柜（服务器1，最上侧）'", conn)
        elif a=='光功率服务器柜（服务器2，中间侧）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='光功率服务器柜（服务器2，中间侧）'", conn)
        elif a=='光功率服务器柜（服务器3，最下侧）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='光功率服务器柜（服务器3，最下侧）'", conn)
        elif a=='SDH通信设备柜':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='SDH通信设备柜'", conn)
        elif a=='故障录波柜':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='故障录波柜'", conn)
        elif a=='监控室后台':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='监控室后台'", conn)
        elif a=='电能量信息采集（华立）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 设备用户及密码 where 设备名='电能量信息采集（华立）'", conn)



        self.table_widget.setColumnCount(len(df.columns))
        self.table_widget.setRowCount(len(df.index))
        self.table_widget.setHorizontalHeaderLabels(df.columns)
        for row in range(len(df.index)):
            for col in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.table_widget.setItem(row, col, item)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
# app = QApplication([])
# main_window = chanjia2()
# main_window.keshihua2('全部厂家')
# main_window.show()
# app.exec_()