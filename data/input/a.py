# coding:utf-8
import pandas as pd
import tushare as ts
import psycopg2
import csv
import os
from sqlalchemy import create_engine
import tushare as ts



def get_data():
    df = ts.get_stock_basics()
    # df.to_csv('a.csv', sep='\t', encoding='utf-8')
    # df.to_csv('c:/day/000875.csv', encoding='utf-8',columns=['open', 'high', 'low', 'close'])
    engine = create_engine('mysql://root:123456@192.168.56.1/docker_qunat?charset=utf8')
    # 存入数据库
    df.to_sql('stock', engine,if_exists='append')

# writer = pd.ExcelWriter('a.xlsx')
# df.to_excel(writer,'Sheet1')
# writer.save()
def to_db():
    csv_data = csv.reader('a.csv')

    database = psycopg2.connect(database="***", user="***", password="***", host="localhost", port="5432")

    cursor = database.cursor()


    cursor.execute("""Create Table stock
                    (id seial,
                     code varchar(10),
                     name varchar(10)
                    );""")



    for row in csv_data:
        cursor.execute("INSERT INTO stock (code, name)" \
                       "VALUES (%s,%s,%s,%s,%s)",
                       row)

    cursor.close()
    database.commit()
    database.close()

if __name__ == '__main__':
    get_data()
    # to_db()