import sqlite3

# 连接到数据库，如果不存在则创建一个新的数据库
conn = sqlite3.connect('鸿天光伏电站')

# 创建一个游标对象
cursor = conn.cursor()

# # 执行更新操作
# cursor.execute("UPDATE 设备用户及密码 SET 备注 =? WHERE  设备名= ?",
#                ("新一代智慧系统：用户名/密码：hongtian/oms.2023",  "OMS"))
# # 执行查询语句
# cursor.execute('SELECT * FROM 设备用户及密码')

# # 执行更新操作
# cursor.execute("UPDATE 厂家联系方式 SET 姓名 =? WHERE 公司 = ?",
#                ("柴红斌",  "充氮灭火器厂家"))
# # 执行查询语句
# cursor.execute('SELECT * FROM 厂家联系方式')

# # 执行更新操作
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.8",  "2024.1.14",'卢奥琪'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.8",  "2024.1.14",'于龙辉'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.8",  "2024.1.14",'郝荣'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.8",  "2024.1.14",'张永杰'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.8",  "2024.1.14",'锁铭旺'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.15",  "2024.1.21",'田申'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.15",  "2024.1.21",'朱嘉航'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.15",  "2024.1.21",'柳琪琪'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.15",  "2024.1.21",'包小龙'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.22",  "2024.1.28",'曹征'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.22",  "2024.1.28",'商恒博'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.22",  "2024.1.28",'吴昊'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.22",  "2024.1.28",'胡红红'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.3",  "2024.1.9",'安华'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.3",  "2024.1.9",'尚会军'))
# cursor.execute("UPDATE 场站休假人员名单 SET 休假起始时间 =? ,休假结束时间=? WHERE 姓名 = ?",
#                ("2024.1.2",  "2024.1.8",'叶家琪'))
# 执行查询语句
cursor.execute('SELECT * FROM 场站休假人员名单')
# 获取查询结果
results = cursor.fetchall()

# 打印结果
for row in results:
    print(row)

# 提交更改并关闭连接
conn.commit()
conn.close()