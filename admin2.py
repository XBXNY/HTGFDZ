import sqlite3
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QTableView, QTableWidget
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
# 创建应用程序对象
class admin2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("鸿天光伏场站")
        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)
        self.resize(1000, 750)

    def keshihua2(self, name):
        a = name
        if a=='场站全体人员名单':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 场站人员名单', conn)
        elif a=='站长名单':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站人员名单 where 职位='站长'", conn)
        elif a=='值长名单':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站人员名单 where 职位='值长'", conn)
        elif a=='职员名单':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站人员名单 where 职位='职员'", conn)
        elif a=='后勤人员名单':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站人员名单 where 职位='后勤人员'", conn)
        elif a=='安全员名单':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 场站人员名单 where 职位='安全员'", conn)
        # elif a=='功率预测厂家':
        #     conn = sqlite3.connect('鸿天光伏电站')
        #     df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='功率预测厂家'", conn)
        # elif a=='箱变':
        #     conn = sqlite3.connect('鸿天光伏电站')
        #     df = pd.read_sql_query('SELECT * FROM 厂家联系方式 where 序号=7', conn)
        # elif a=='逆变器':
        #     conn = sqlite3.connect('鸿天光伏电站')
        #     df = pd.read_sql_query('SELECT * FROM 厂家联系方式 where 序号=8', conn)
        # elif a=='综合自动化装置及继电保护装置':
        #     conn = sqlite3.connect('鸿天光伏电站')
        #     df = pd.read_sql_query('SELECT * FROM 厂家联系方式 where 序号=9', conn)
        # elif a=='直流系统':
        #     conn = sqlite3.connect('鸿天光伏电站')
        #     df = pd.read_sql_query('SELECT * FROM 厂家联系方式 where 序号=10', conn)
        # elif a=='UPS系统':
        #     conn = sqlite3.connect('鸿天光伏电站')
        #     df = pd.read_sql_query('SELECT * FROM 厂家联系方式 where 序号=11', conn)
        # elif a=='通讯系统':
        #     conn = sqlite3.connect('鸿天光伏电站')
        #     df = pd.read_sql_query('SELECT * FROM 厂家联系方式 where 序号=12', conn)


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