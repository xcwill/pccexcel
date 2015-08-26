# -*- coding: UTF-8 -*-
''' 读取excel表格数据并保存数据库'''

__author__ = 'Admin'

from sqlite3 import *

def drop_table_test():
    '''删除数据库表测试'''
    print('删除数据库表测试...')
    conn = get_conn(DB_FILE_PATH)
    drop_table(conn, TABLE_NAME)

def create_table_test(create_table_sql):
    '''创建数据库表测试'''
    print('创建数据库表测试...')

    conn = get_conn(DB_FILE_PATH)
    create_table(conn, create_table_sql)

def save_test(save_sql,data):
    '''保存数据测试...'''
    print('保存数据测试...')

    conn = get_conn(DB_FILE_PATH)
    save(conn, save_sql, data)

def fetchall_test():
    '''查询所有数据...'''
    print('查询所有数据...')
    fetchall_sql = 'SELECT * FROM student'
    conn = get_conn(DB_FILE_PATH)
    fetchall(conn, fetchall_sql)

def fetchone_test():
    '''查询一条数据...'''
    print('查询一条数据...')
    fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
    data = 1
    conn = get_conn(DB_FILE_PATH)
    fetchone(conn, fetchone_sql, data)

def update_test():
    '''更新数据...'''
    print('更新数据...')
    update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenBB', 2),
            ('HongtenCC', 3),
            ('HongtenDD', 4)]
    conn = get_conn(DB_FILE_PATH)
    update(conn, update_sql, data)

def delete_test():
    '''删除数据...'''
    print('删除数据...')
    delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenCC', 3)]
    conn = get_conn(DB_FILE_PATH)
    delete(conn, delete_sql, data)

###############################################################
####            测试操作     END
###############################################################

def read_excel():
     create_table_sql = '''CREATE TABLE `student` (
                          `id` int(11) NOT NULL,
                          `name` varchar(20) NOT NULL,
                          `gender` varchar(4) DEFAULT NULL,
                          `age` int(11) DEFAULT NULL,
                          `address` varchar(200) DEFAULT NULL,
                          `phone` varchar(20) DEFAULT NULL,
                           PRIMARY KEY (`id`)
                        )'''

     save_sql = 'INSERT INTO student values (?, ?, ?, ?, ?, ?)'
     data = [(1, 'Hongten', '男', 20, '广东省广州市', '13423****62'),
            (2, 'Tom', '男', 22, '美国旧金山', '15423****63'),
            (3, 'Jake', '女', 18, '广东省广州市', '18823****87'),
            (4, 'Cate', '女', 21, '广东省广州市', '14323****32')]
     return (create_table_sql,save_sql,data)


def init():
    '''初始化方法'''
    #数据库文件绝句路径
    global DB_FILE_PATH
    DB_FILE_PATH = 'D:\\backup\\code\\Python\\pccexcel\\pcc.db'
    #数据库表名称
    global TABLE_NAME
    TABLE_NAME = 'student'
    #是否打印sql
    global SHOW_SQL
    SHOW_SQL = True
    print('show_sql : {}'.format(SHOW_SQL))
    #如果存在数据库表，则删除表
    drop_table_test()
    #创建数据库表student
    create_table_test()
    #向数据库表中插入数据
    save_test()

def main():
    init()
    fetchall_test()
    print('#' * 50)
    fetchone_test()
    print('#' * 50)
    update_test()
    print('#' * 50)
    delete_test()
    fetchall_test()

if __name__ == '__main__':
    main()



