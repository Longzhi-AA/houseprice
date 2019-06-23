from urllib.request import urlopen, quote
import json

from our_project.dbs import Mongo


class IngLat:
    """地址转换"""

    def __init__(self, *args):
        """组合拼接成一个完整地址"""
        self.address = ""  # 成都市高新区天府大道

        for data in args:
            self.address += data

    def transform_pos(self):
        """通过地址获取经纬度"""

        data = [self.address]

        url = 'http://api.map.baidu.com/geocoder/v2/'
        output = 'json'
        ak = 'sAAq4yGnqR9hEe2ra4ENh8XVYmVGoix6'
        address = quote(self.address)  # URL编码

        # 拼接一个url，可通过百度生成一个对应地址的经纬度
        url = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak

        try:
            req = urlopen(url)  # 有的地址可能转换失败抛异常

        except Exception as e:
            print(e)

        else:
            res = req.read().decode("utf8")
            temp = json.loads(res)  # 将json数据转换成字典格式

            lat = temp["result"]["location"]["lat"]  # 获取纬度
            lng = temp["result"]["location"]["lng"]  # 获取经度

            data.append((lat, lng))
            return data

    def storage_pos(self):
        """把地址和对应的经纬度存入数据库"""
        my_set = Mongo().connect_mongo('runoob', 'pos')  # 存入到mongodb中runoob库pos集合中
        data = self.transform_pos()  # 调用transform_pos方法转换地址为经纬度

        dt = {"address": data[0], "position": data[-1]}
        my_set.insert_one(dt)  # 存入mongodb数据库


