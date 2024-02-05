import sqlite3
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QTableView, QTableWidget
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
# 创建应用程序对象
class holiday2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("鸿天光伏场站")
        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)
        self.resize(1000, 750)

    def keshihua2(self, name):
        a = name
        if a=='第一批休假人员信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站休假人员名单 where 休假起始时间='2024.1.8'", conn)
        elif a=='第二批休假人员信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站休假人员名单 where 休假起始时间='2024.1.15'", conn)
        elif a=='第三批休假人员信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站休假人员名单 where 休假起始时间='2024.1.22'", conn)
        elif a=='站长休假信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站休假人员名单 where 姓名='安华'", conn)
        elif a=='后勤人员休假信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站休假人员名单 where 姓名='尚会军'", conn)
        elif a=='安全员休假信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站休假人员名单 where 姓名='叶家琪'", conn)
        elif a == '第四批休假人员信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站休假人员名单 where 休假起始时间='2024.1.29'", conn)
        elif a=='第五批休假人员信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站休假人员名单 where 休假起始时间='2024.2.5'", conn)
        elif a=='第六批休假人员信息':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站休假人员名单 where 休假起始时间='2024.2.12'", conn)



        self.table_widget.setColumnCount(len(df.columns))
        self.table_widget.setRowCount(len(df.index))
        self.table_widget.setHorizontalHeaderLabels(df.columns)
        for row in range(len(df.index)):
            for col in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.table_widget.setItem(row, col, item)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
# app = QApplication([])
# main_window = holiday2()
# main_window.keshihua2('全部成员的休假信息')
# main_window.show()
# app.exec_()