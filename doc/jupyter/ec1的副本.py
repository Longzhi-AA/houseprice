# import pandas as pd
# import numpy as np
# import xlrd
#
# # a = {'name':'zhangsan','age':18,'tel':11111111}
# # t = pd.Series(a)
#
# # print(t)
# # print(t[:2])
# # print(t[[1,2]])
# # print(len(t))
# # print(t[['name','age']])
#
# x = [{'name':'zhangsan','age':18,'tel':11111111},
#      {'name':'lisi','age':18,'tel':11111111},
#      {'name':'xiaoming','age':18,'tel':11111111}]
#
# t = pd.DataFrame(x)
# print(t)


# import plotly
# import plotly.plotly as py
# import plotly.graph_objs as go
#
# trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], marker={'color': 'red', 'symbol': 104, 'size': "10"},
#                     mode="markers+lines", text=["one", "two", "three"], name='1st Trace')
#
# data = go.Data([trace1])
# layout = go.Layout(title="First Plot", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
# figure = go.Figure(data=data, layout=layout)
# py.iplot(figure, filename='pyguide_1')

# from pyecharts import charts
#
#
#
# bar = charts.Bar()
# # bar.use_theme('dark')                                  #暗色背景色
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.render('./picture1.html')
#
# import datetime
# import random
#
# from pyecharts import options as opts
# from pyecharts.charts import Calendar
#
#
# def calendar_base() -> Calendar:
#     begin = 4000
#     end = 50000
#     data = [
#         [str(begin), random.randint(1000, 25000)]
#
#     ]
#
#     c = (
#         Calendar()
#         .add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况"),
#             visualmap_opts=opts.VisualMapOpts(
#                 max_=20000,
#                 min_=500,
#                 orient="horizontal",
#                 is_piecewise=True,
#                 pos_top="230px",
#                 pos_left="100px",
#             ),
#         )
#     )
#     return c
# c = calendar_base()
# c.render('./picture2.html')


# from pyecharts import options as opts
# from pyecharts.charts import Gauge, Page
#
# import matplotlib.pyplot as plt
# import numpy as np
# from pymongo import MongoClient
# from matplotlib import font_manager
#
# #myfont让图标显示中文字体
# my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
# #实例化客户端
# client = MongoClient(host='127.0.0.1', port=27017)
# #绑定数据库
# db = client.test
# #绑定数据集合
# collection = db['test']
#
# #不同区域的小区总数并按区域分组的查找代码
# pipeline= [{"$group":{"_id":'$district', "count":{'$sum':1}}}]
#
# #plt.figure定义图表大小
# plt.figure(figsize=(20,8), dpi=80)
#
# #使用聚合查询
# m = collection.aggregate(pipeline)
# x=[]
# y=[]
# #查出来的数据标示不同轴
# for i in m:
#     x.append(i['_id'])
#     y.append(i['count'])
# y = [round(j*100/sum(y),2) for j in y]
# # print(x,y)
# def gauge_base(a,b) -> Gauge:
#     c = (
#         Gauge()
#         .add("", [(a, b)])
#         .set_global_opts(title_opts=opts.TitleOpts(title="房源占比"))
#     )
#     return c
#
# for j in range(len(x)):
#     print(j)
#     c = gauge_base(x[j],y[j])
#     c.render('./{}.html'.format(j))


from example.commons import Faker

from pyecharts import options as opts
from pyecharts.charts import Page, Pie


def pie_rosetype() -> Pie:
    v = Faker.choose()
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
    )
    return c

