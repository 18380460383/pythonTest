import MySQLdb

class mysqlCon(object):
    mysql_add='localhost'
    mysql_user='root'
    mysql_pass='mn19940708'
    mysql_dataBase='information_schema'
    db=None
    cursor=None
    __instance = None

    def __init__(self,mysql_add,mysql_user,mysql_pass,mysql_dataBase):
        self.mysql_add=mysql_add
        self.mysql_user=mysql_user
        self.mysql_pass=mysql_pass
        self.mysql_dataBase=mysql_dataBase

    # 打开数据库连接
    def openInformation(self):
        if mysqlCon.__instance is None:
            self.db = MySQLdb.connect(self.mysql_add, self.mysql_user, self.mysql_pass, self.mysql_dataBase)
            # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        return self.cursor