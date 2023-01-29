import mysql.connector as connector
import time

# データベース操作はすべてここで行う


class OperateDatabase:
    # データベース接続
    def connect(self):
        self.cnx = connector.connect(
            host='localhost', port='3306', user='root')
        return self.cnx

    # データベース作成
    def create(self, cnx):
        cur = cnx.cursor()
        with open("createtable.txt") as f:
            sql = f.read()
        try:
            cur.execute("create database test;")
        except Exception as e:
            print(e)
        cur.execute("use test;")
        try:
            cur.execute(sql)
        except Exception as e:
            print(e)

    # 実行時間計測
    def cal_exec_time(self, sql, cnx):
        cur = cnx.cursor(buffered=True)
        try:
            start = time.time()
            cur.execute(sql)
            end = time.time()
        except Exception as e:
            print(e)
            return 0
        return str('{:.3e}'.format(end - start)) + "秒"
