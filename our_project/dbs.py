from pymongo import MongoClient

from our_project.settings import DATABASES


class Mongo:
    """操作mongodb数据库"""
    database = DATABASES["default"]["OPTIONS"]

    def __init__(self, host=database["HOST"], port=database["PORT"]):
        self.conn = MongoClient(host, port)

    def connect_mongo(self, db_name, set_name):
        my_db = self.conn[db_name]  # 数据库名
        my_col = my_db[set_name]  # 集合名

        return my_col



















