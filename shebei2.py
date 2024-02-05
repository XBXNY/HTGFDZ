import sqlite3
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QTableView, QTableWidget
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
# 创建应用程序对象
class shebei(QtWidgets.QMainWindow):
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
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表', conn)
        elif a=='送出线路':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=1', conn)
        elif a=='GIS':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=2', conn)
        elif a=='主变':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=3', conn)
        elif a=='高压设备开关':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=4', conn)
        elif a=='400V配电系统':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=5', conn)
        elif a=='集电线路':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=6', conn)
        elif a=='箱变':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=7', conn)
        elif a=='逆变器':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=8', conn)
        elif a=='综合自动化装置及继电保护装置':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=9', conn)
        elif a=='直流系统':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=10', conn)
        elif a=='UPS系统':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=11', conn)
        elif a=='通讯系统':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 设备基础信息统计表 where 序号=12', conn)


        self.table_widget.setColumnCount(len(df.columns))
        self.table_widget.setRowCount(len(df.index))
        self.table_widget.setHorizontalHeaderLabels(df.columns)
        for row in range(len(df.index)):
            for col in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.table_widget.setItem(row, col, item)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
# app = QApplication([])
# main_window = shebei()
# main_window.keshihua2('送出线路')
# main_window.show()
# app.exec_()