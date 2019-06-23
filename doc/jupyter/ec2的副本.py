#个区县新房均价，不同类型

import xlrd
from matplotlib import font_manager
import matplotlib.pyplot as plt

import numpy as np
from pyecharts.commons.utils import JsCode

my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

file = 'test.xls'

wb = xlrd.open_workbook(filename=file)

s1 = wb.sheet_by_index(0)

data_list = []

for i in range(1544):
    data_list.append(s1.row_values(i))

data_list= data_list[1:]
datas = np.array(data_list)
districts = datas[0:,1:2]
prices = datas[0:,3:4]
prices = prices.astype("float")
types = datas[0:,4:5]
# # print(prices)
# # print(districts)
#
# #
jinjiang = []
wuhou = []
gaoxin = []
jinniu = []
chenghua = []
tianfu = []
wenjiang = []
shuangliu = []
longquan = []
# #
# # #把数据合并为同一个数组
# data_arry = np.hstack((districts,prices))
#
data_type = np.hstack((types,prices))
# # print(data_arry[0])
# #按不同划分取数据
# for data in data_arry:
#     # print(data)
#     if data[0] == '锦江':
#         if float(data[1]) != 0:
#             jinjiang.append(data[1])
#     if data[0] == '武侯':
#         if float(data[1]) != 0:
#             wuhou.append(data[1])
#     if data[0] == '高新':
#         if float(data[1]) != 0:
#             gaoxin.append(data[1])
#     if data[0] == '成华':
#         if float(data[1]) != 0:
#             chenghua.append(data[1])
#     if data[0] == '金牛':
#         if float(data[1]) != 0:
#             jinniu.append(data[1])
#     if data[0] == '天府新区':
#         if float(data[1]) != 0:
#             tianfu.append(data[1])
#     if data[0] == '温江':
#         if float(data[1]) != 0:
#             wenjiang.append(data[1])
#     if data[0] == '双流':
#         if float(data[1]) != 0:
#             shuangliu.append(data[1])
#     if data[0] == '龙泉驿':
#         if float(data[1]) != 0:
#             longquan.append(data[1])
#     else:
#         continue
# shangy =[]
# zhuz = []
# xiezl = []
# bies = []
# for data in data_type:
#
#     if data[0] == '商业':
#         if float(data[1]) != 0:
#             shangy.append(data[1])
#     if data[0] == '住宅':
#         if float(data[1]) != 0:
#             zhuz.append(data[1])
#     if data[0] == '写字楼':
#         if float(data[1]) != 0:
#             xiezl.append(data[1])
#     if data[0] == '别墅':
#         if float(data[1]) != 0:
#             bies.append(data[1])
#     else:
#         continue
#
# #把取出的数据转化成floa型
# jinjiang= np.array(jinjiang).astype(float)
# #取出的数据求均值
# y_jinj = round(jinjiang.mean(),2)
# wuhou= np.array(wuhou).astype(float)
# y_wuh = round(wuhou.mean(),2)
# jinniu= np.array(jinniu).astype(float)
# y_jinn = round(jinniu.mean(),2)
# gaoxin= np.array(gaoxin).astype(float)
# y_gaox = round(gaoxin.mean(),2)
# chenghua= np.array(chenghua).astype(float)
# y_chengh = round(chenghua.mean(),2)
# tianfu= np.array(tianfu).astype(float)
# y_tianf = round(tianfu.mean(),2)
# wenjiang= np.array(wenjiang).astype(float)
# y_wenj = round(wenjiang.mean(),2)
# longquan= np.array(longquan).astype(float)
# y_longq = round(longquan.mean(),2)
# shuangliu= np.array(shuangliu).astype(float)
# y_shuangl = round(shuangliu.mean(),2)
#
# shangy = np.array(shangy).astype(float)
# y_shany = round(shangy.mean(),2)
# zhuz= np.array(zhuz).astype(float)
# y_zhuz = round(zhuz.mean(),2)
# xiezl= np.array(xiezl).astype(float)
# y_xiezil = round(xiezl.mean(),2)
# bies= np.array(bies).astype(float)
# y_bies = round(bies.mean(),2)
#
#
# a = ['锦江','武侯', '金牛','成华','高新','天府新区','温江','双流','龙泉驿']
from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Page, Pie, Bar, Scatter, Line


#
# def pie_base() -> Pie:
#     c = (
#         Pie()
#         .add("", [('锦江',y_jinj),('武侯',y_wuh),('金牛',y_jinn),('成华',y_chengh),('高新',y_gaox),('天府新区',y_tianf),('温江',y_wenj),('双流',y_shuangl),('龙泉驿',y_longq)])
#         .set_global_opts(title_opts=opts.TitleOpts(title="各区域平均房价"))
#         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     )
#     return c

# def pie_rosetype() -> Pie:
#
#     d = (
#         Pie()
#
#         .add(
#             "",
#             [('商业',y_shany),('住宅',y_zhuz),('写字楼',y_xiezil),('别墅',y_bies)],
#             radius=["30%", "75%"],
#             center=["75%", "50%"],
#             rosetype="area",
#
#         )
#         .set_global_opts(title_opts=opts.TitleOpts(title="不同类型的房价均价"))
#     )
#     return d
#
# d= pie_rosetype()
# d.render('./n.html')



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
#
# #使用聚合查询
# m = collection.aggregate(pipeline)
# x=[]
# y=[]
# #查出来的数据标示不同轴
# for i in m:
#     x.append(i['_id'])
#     y.append(i['count'])
#
# def bar_datazoom_both() -> Bar:
#     c = (
#         Bar()
#         .add_xaxis(x)
#         .add_yaxis("各区域新房数量", y, color=Faker.rand_color(),markpoint_opts=opts.MarkPointOpts(
#                 data=[opts.MarkPointItem(name="自定义标记点", coord=[x[2], y[2]], value=y[2])]
#             ),)
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title=""),
#             datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
#         )
#     )
#
#
#     return c
#
# c = bar_datazoom_both()
# c.render('./n.html')




# data_arry = np.hstack((districts,prices))
#
# # print(data_arry[0])
# #按不同划分取数据
# for data in data_arry:
#     # print(data)
#     if data[0] == '锦江':
#         if float(data[1]) != 0:
#             jinjiang.append(data[1])
#     if data[0] == '武侯':
#         if float(data[1]) != 0:
#             wuhou.append(data[1])
#     if data[0] == '高新':
#         if float(data[1]) != 0:
#             gaoxin.append(data[1])
#     if data[0] == '成华':
#         if float(data[1]) != 0:
#             chenghua.append(data[1])
#     if data[0] == '金牛':
#         if float(data[1]) != 0:
#             jinniu.append(data[1])
#     if data[0] == '天府新区':
#         if float(data[1]) != 0:
#             tianfu.append(data[1])
#     if data[0] == '温江':
#         if float(data[1]) != 0:
#             wenjiang.append(data[1])
#     if data[0] == '双流':
#         if float(data[1]) != 0:
#             shuangliu.append(data[1])
#     if data[0] == '龙泉驿':
#         if float(data[1]) != 0:
#             longquan.append(data[1])
#     else:
#         continue
#
# def scatter_visualmap_color() -> Scatter:
#     c = (
#         Scatter()
#         .add_xaxis(
#             ['锦江','武侯', '金牛','成华','高新','天府新区','温江','双流','龙泉驿'])
#
#         .add_yaxis('区间房价',[jinjiang,wuhou,jinniu,chenghua,gaoxin,tianfu,wenjiang,shuangliu,longquan])
#
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
#             visualmap_opts=opts.VisualMapOpts(type_="size", max_=500, min_=50),
#         )
#     )
#     return c
# print(jinjiang.count)
# def scatter_muti_dimension_data() -> Scatter:
#     c = (
#         Scatter()
#         .add_xaxis(['锦江','武侯', '金牛','成华','高新','天府新区','温江','双流','龙泉驿'])
#         .add_yaxis(
#             '区间房价',[jinjiang,wuhou,jinniu,chenghua,gaoxin,tianfu,wenjiang,shuangliu,longquan],
#             label_opts=opts.LabelOpts(
#                 formatter=JsCode(
#                     "function(params){return params.value[1] +' : '+ params.value[2];}"
#                 )
#             ),
#         )
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="Scatter-多维度数据"),
#             tooltip_opts=opts.TooltipOpts(
#                 formatter=JsCode(
#                     "function (params) {return params.name + ' : ' + params.value[2];}"
#                 )
#             ),
#             visualmap_opts=opts.VisualMapOpts(
#                 type_="color", max_=150, min_=20, dimension=1
#             ),
#         )
#     )
#     return c
#
# c = scatter_muti_dimension_data()
# c.render('./m.html')

a= ['住宅', '商业', '写字楼','别墅']
z4=[]
z6=[]
z8=[]
z10=[]
z12=[]
z14=[]
z16=[]
z18=[]
z20=[]
z22=[]
z24=[]
z26=[]
z28=[]
z30=[]
z40=[]
s4=[]
s6=[]
s8=[]
s10=[]
s12=[]
s14=[]
s16=[]
s18=[]
s20=[]
s22=[]
s24=[]
s26=[]
s28=[]
s30=[]
s40=[]
x4=[]
x6=[]
x8=[]
x10=[]
x12=[]
x14=[]
x16=[]
x18=[]
x20=[]
x22=[]
x24=[]
x26=[]
x28=[]
x30=[]
x40=[]
b4=[]
b6=[]
b8=[]
b10=[]
b12=[]
b14=[]
b16=[]
b18=[]
b20=[]
b22=[]
b24=[]
b26=[]
b28=[]
b30=[]
b40=[]
for data in data_type:
    # print(type(data[1]))
    if data[0] == a[0]:

        if float(data[1]) <= 4000:
            z4.append(float(data[1]))
        elif float(data[1]) <= 6000:
            z6.append(float(data[1]))
        elif float(data[1]) <= 8000:
            z8.append(float(data[1]))
        elif float(data[1]) <= 10000:
            z10.append(float(data[1]))
        elif float(data[1]) <= 12000:
            z12.append(float(data[1]))
        elif float(data[1]) <= 14000:
            z14.append(float(data[1]))
        elif float(data[1]) <= 16000:
            z16.append(float(data[1]))
        elif float(data[1]) <= 18000:
            z18.append(float(data[1]))
        elif float(data[1]) <= 20000:
            z20.append(float(data[1]))
        elif float(data[1]) <= 22000:
            z22.append(float(data[1]))
        elif float(data[1]) <= 24000:
            z24.append(float(data[1]))
        elif float(data[1]) <= 26000:
            z26.append(float(data[1]))
        elif float(data[1]) <= 28000:
            z28.append(float(data[1]))
        elif float(data[1]) <= 30000:
            z30.append(float(data[1]))
        else:
            z40.append(float(data[1]))
    if data[0] == a[1]:

        if float(data[1]) <= 4000:
            s4.append(float(data[1]))
        elif float(data[1]) <= 6000:
            s6.append(float(data[1]))
        elif float(data[1]) <= 8000:
            s8.append(float(data[1]))
        elif float(data[1]) <= 10000:
            s10.append(float(data[1]))
        elif float(data[1]) <= 12000:
            s12.append(float(data[1]))
        elif float(data[1]) <= 14000:
            s14.append(float(data[1]))
        elif float(data[1]) <= 16000:
            s16.append(float(data[1]))
        elif float(data[1]) <= 18000:
            s18.append(float(data[1]))
        elif float(data[1]) <= 20000:
            s20.append(float(data[1]))
        elif float(data[1]) <= 22000:
            s22.append(float(data[1]))
        elif float(data[1]) <= 24000:
            s24.append(float(data[1]))
        elif float(data[1]) <= 26000:
            s26.append(float(data[1]))
        elif float(data[1]) <= 28000:
            s28.append(float(data[1]))
        elif float(data[1]) <= 30000:
            s30.append(float(data[1]))
        else:
            s40.append(float(data[1]))
    if data[0] == a[2]:

        if float(data[1]) <= 4000:
            x4.append(float(data[1]))
        elif float(data[1]) <= 6000:
            x6.append(float(data[1]))
        elif float(data[1]) <= 8000:
            x8.append(float(data[1]))
        elif float(data[1]) <= 10000:
            x10.append(float(data[1]))
        elif float(data[1]) <= 12000:
            x12.append(float(data[1]))
        elif float(data[1]) <= 14000:
            x14.append(float(data[1]))
        elif float(data[1]) <= 16000:
            x16.append(float(data[1]))
        elif float(data[1]) <= 18000:
            x18.append(float(data[1]))
        elif float(data[1]) <= 20000:
            x20.append(float(data[1]))
        elif float(data[1]) <= 22000:
            x22.append(float(data[1]))
        elif float(data[1]) <= 24000:
            x24.append(float(data[1]))
        elif float(data[1]) <= 26000:
            x26.append(float(data[1]))
        elif float(data[1]) <= 28000:
            x28.append(float(data[1]))
        elif float(data[1]) <= 30000:
            x30.append(float(data[1]))
        else:
            x40.append(float(data[1]))
    if data[0] == a[3]:

        if float(data[1]) <= 4000:
            b4.append(float(data[1]))
        elif float(data[1]) <= 6000:
            b6.append(float(data[1]))
        elif float(data[1]) <= 8000:
            b8.append(float(data[1]))
        elif float(data[1]) <= 10000:
            b10.append(float(data[1]))
        elif float(data[1]) <= 12000:
            b12.append(float(data[1]))
        elif float(data[1]) <= 14000:
            b14.append(float(data[1]))
        elif float(data[1]) <= 16000:
            b16.append(float(data[1]))
        elif float(data[1]) <= 18000:
            b18.append(float(data[1]))
        elif float(data[1]) <= 20000:
            b20.append(float(data[1]))
        elif float(data[1]) <= 22000:
            b22.append(float(data[1]))
        elif float(data[1]) <= 24000:
            b24.append(float(data[1]))
        elif float(data[1]) <= 26000:
            b26.append(float(data[1]))
        elif float(data[1]) <= 28000:
            b28.append(float(data[1]))
        elif float(data[1]) <= 30000:
            b30.append(float(data[1]))
        else:
            b40.append(float(data[1]))

b = ['4000','6000','8000','10000','12000','14000','16000','18000','20000','22000','24000','26000','28000','30000','3w+']

def line_smooth() -> Line:
    c = (
        Line()
        .add_xaxis(b)
        .add_yaxis("住宅", [len(z4),len(z6),len(z8),len(z10),len(z12),len(z14),len(z16),len(z18),len(z20),len(z22),len(z24),len(z26),len(z28),len(z30),len(z40)], is_smooth=True)
        .add_yaxis("商业", [len(s4),len(s6),len(s8),len(s10),len(s12),len(s14),len(s16),len(s18),len(s20),len(s22),len(s24),len(s26),len(s28),len(s30),len(s40)], is_smooth=True)
        .add_yaxis("写字楼",
                       [len(x4),len(x6),len(x8),len(x10),len(x12),len(x14),len(x16),len(x18),len(x20),len(x22),len(x24),len(x26),len(x28),len(x30),len(x40)], is_smooth=True)

        .add_yaxis("别墅",
                       [len(b4),len(b6),len(b8),len(b10),len(b12),len(b14),len(b16),len(b18),len(b20),len(b22),len(b24),len(b26),len(b28),len(b30),len(b40)], is_smooth=True)

        .set_global_opts(title_opts=opts.TitleOpts(title="各区域各区间房价房源数量"))
    )
    return c

c = line_smooth()
c.render('./h.html')