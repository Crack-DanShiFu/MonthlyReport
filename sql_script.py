import pymysql as mdb
import openpyxl
from openpyxl import load_workbook

import uuid

def insert_db(result):
    conn = mdb.connect(host='47.107.173.225', port=3306, user='root', passwd='root', db='MonthlyReport', charset='utf8mb4')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO details_list('
                       'uid,'
                       'designation,'
                       'odd_num,'
                       'flow,'
                       'budget,'
                       'submit_date,'
                       'submit_m,'
                       'department_apply,'
                       'budget_dept,'
                       'beyond_bud,'
                       'company,'
                       'tax_inclusive,'
                       'no_tax,'
                       'distinguish,'
                       'budget_account,'
                       'time_frame,'
                       'remark,'
                       'flow_id,'
                       'state,'
                       'submitter'
                       ') values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       result)
    conn.commit()
    conn.close()


def insert_db2(result):
    conn = mdb.connect(host='47.107.173.225', port=3306, user='root', passwd='root', db='MonthlyReport', charset='utf8mb4')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO examine_list('
                       'uid,'
                       'reply_time,'
                       'node_type,'
                       'odd_num,'
                       'officer,'
                       'flow,'
                       'reply_b,'
                       'time_frame,'
                       'node_name,'
                       'flow_type'
                       ') values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       result)
    conn.commit()
    conn.close()




wb = load_workbook('appList.xlsx')
wb.guess_types = True  # 猜测格式类型
ws = wb.active

result=[]
for w in ws:
    r=[ '' if i.value is None else i.value for i in w ]
    r.insert(0,str(uuid.uuid1()))
    print(r)
    result.append(r)

insert_db(result[1:])





