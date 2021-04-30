import pymysql
import re


class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='stu',
                                  charset='utf8')
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def register(self, user, passwd):
        sql = "select name from user where name = %s;"
        self.cur.execute(sql, user)
        result = self.cur.fetchone()
        if result:
            print("该用户存在")
            return
        try:
            sql = "insert into user (name,password) values(%s,%s);"
            self.cur.execute(sql, [user, passwd])
            self.db.commit()
        except:
            self.db.rollback()



db = Database()
db.register("test12", '7777')
db.close()
