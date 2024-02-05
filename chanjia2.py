import sqlite3
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QTableView, QTableWidget
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
# 创建应用程序对象
class chanjia2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("鸿天光伏场站")
        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)
        self.resize(1000, 750)

    def keshihua2(self, name):
        a = name
        if a=='全部厂家':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query('SELECT * FROM 厂家联系方式', conn)
        elif a=='35kV SF6气体在线检测装置':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='35kV SF6气体在线检测装置'", conn)
        elif a=='调度数据网，二次安防':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='调度数据网，二次安防'", conn)
        elif a=='故障录波':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 when 公司='故障录波'", conn)
        elif a=='国电南瑞':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='国电南瑞'", conn)
        elif a=='五防厂家':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='五防厂家'", conn)
        elif a=='功率预测厂家':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='功率预测厂家'", conn)
        elif a=='高压开关柜厂家':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='高压开关柜厂家(泰开)'", conn)
        elif a=='充氮灭火器厂家':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='充氮灭火器厂家'", conn)
        elif a=='电能量采集终端（华立）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='电能量采集终端（华立）'", conn)
        elif a=='电能量采集终端（威思顿）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='电能量采集终端（威思顿）'", conn)
        elif a=='恶意代码':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='恶意代码'", conn)
        elif a=='小电阻接地变成套装置':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='小电阻接地变成套装置'", conn)
        elif a=='GIS（西电）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='GIS（西电）'", conn)
        elif a=='主变（华鹏）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='主变（华鹏）'", conn)
        elif a=='35kV，400V开关柜（泰开）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='35kV，400V开关柜（泰开）'", conn)
        elif a=='SVG（新风光）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='SVG（新风光）'", conn)
        elif a=='数据网，网络安全监测':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='数据网，网络安全监测'", conn)
        elif a=='光端机通信（西安德悦）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='光端机通信（西安德悦）'", conn)
        elif a=='交直流（许继电源）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='交直流（许继电源）'", conn)
        elif a=='交直流（许继电源）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='交直流（许继电源）'", conn)
        elif a=='主变温控箱（福建力得）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='主变温控箱（福建力得）'", conn)
        elif a=='站用变（泰开箱变）':
            conn = sqlite3.connect('鸿天光伏电站')
            df = pd.read_sql_query("SELECT * FROM 厂家联系方式 where 公司='站用变（泰开箱变）'", conn)


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