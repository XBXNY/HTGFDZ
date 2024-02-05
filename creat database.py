import sqlite3

# 连接到数据库，如果不存在则创建一个新的数据库
conn = sqlite3.connect('鸿天光伏电站')

# 创建一个游标对象
cursor = conn.cursor()

# 创建一个名为 "SVG" 的表格
cursor.execute('''
    CREATE TABLE 设备用户及密码
    (
     设备名 TEXT,
     合同号 TEXT,
     机器名 TEXT,
     用户名 TEXT,
     密码 TEXT,
     系统信息 TEXT,
     软件信息 TEXT,
     ip地址 TEXT,
     备注 TEXT
     )''')


# # 执行查询数据操作
# cursor.execute("SELECT * FROM 场站休假人员名单")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


# 提交更改并关闭连接
conn.commit()
conn.close()
