import pymysql

# 우리가 원할 때 동작하게 하려면 ?
#   - 함수로 만들기.
#   - 클래스로 만들어 클래스 안에 넣기.

class Database():
    # 클래스 변수 != 맴버 변수
    def __init__(self):
        self.con = pymysql.connect(host="127.0.0.1", user="root", password="1234", database="chat")
        self.cur = self.con.cursor()

    def execute(self, sql):
        self.cur.execute(sql)

    def fetchall(self):
        return self.cur.fetchall()

    def commit(self):
        self.con.commit()

database = Database()
execute = database.execute
fetchall = database.fetchall
commit = database.commit