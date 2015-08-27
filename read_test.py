# -*- coding: UTF-8 -*-
'''测试读取excel '''

__author__ = 'Admin'


import xlrd

def open_excel(file):
    try:
        PCC_workbook = xlrd.open_workbook(file)
        return PCC_workbook
    except Exception:
        print ("error")


def read_excel(workbook_name,sheet_name):
    sheet_list = workbook_name.sheet_names()
    if workbook_name is not None and sheet_name in sheet_list:
        PE_sheet = workbook_name.sheet_by_name(sheet_name) #按表名获取表
        title = PE_sheet.row_values(0)                     #获取表头名称
        #创建数据库表和字段
        create_table_sql = ('CREATE TABLE `student` ('\
                          + title[0] + ' VARCHAR (20) NOT NULL,'\
                          + title[1] + ' int(11) NOT NULL,'\
                          + title[2] + ' varchar(4) DEFAULT NULL,'\
                          + title[3] + ' varchar(4) DEFAULT NULL,'\
                          + title[4] + ' varchar(4) DEFAULT NULL,'\
                          + title[5] + ' varchar(4) DEFAULT NULL,'\
                          + title[6] + ' varchar(4) DEFAULT NULL,'\
                          + title[7] + ' varchar(4) DEFAULT NULL,'\
                          + title[8] + ' varchar(4) DEFAULT NULL,'\

                          + 'PRIMARY KEY (`id`)'\
                        )


        for row in range(0,PE_sheet.nrows):
            print (PE_sheet.row_values(row))
    else :
        print ('sheet don`t exist')

def main():
    file = 'D:\\backup\\data\\2015 PE execution table.xlsx'
    PE_workbook = open_excel(file)
    read_excel(PE_workbook,'Plant')


if __name__ == '__main__' :
    main()
