from django.shortcuts import render
from django.http import HttpResponse
from pyecharts.charts import *
from pyecharts import options as opts

import matplotlib.pyplot as plt
from wordcloud import WordCloud
# from imread import imread  # 读取图片
import jieba  # 利用一个中文词库，确定汉字之间的关联概率
import json

from our_project.dbs import Mongo
from example.commons import Faker


def pie1(request):
    """各个区县新房 饼图"""
    # 数据准备
    address = {}
    cursor = Mongo().connect_mongo('runoob', 'test').find()  # 获取数据库数据

    for data in cursor:
        if data["district"] not in address:
            address[data["district"]] = 1
        else:
            address[data["district"]] += 1

    attr = [i for i in address]  # 区县
    v1 = [j for j in address.values()]  # 各个区县新房数量

    # 绘图
    c = (
        Pie()
        .add("",
             [list(z) for z in zip(attr, v1)],  # 导入数据
             center=["55%", "55%"],  # 设置位置
             radius=["10%", "70%"],  # 设置大小
             rosetype="area")  # 设置玫瑰图

        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="成都各区县新房数量",
                pos_left="40%",
            ),

            legend_opts=opts.LegendOpts(
                orient="vertical",  # 垂直显示
                pos_left="2%",  # 左边距
                pos_top="5%",  # 上边距

            )  # legend_opts调整图例位置
        )

        .set_series_opts(
            label_opts=opts.LabelOpts(formatter="{b}{d}%  {c}")
        )
    )

    c.render("templates/pie1.html")
    return HttpResponse(c.render_embed())


def pie2(request):
    """成都新房的种类和数量"""
    # 数据准备
    res = Mongo().connect_mongo('runoob', 'test').find()
    datas = {}

    for dt in res:
        if dt["type"] not in datas:
            datas[dt["type"]] = 1
        else:
            datas[dt["type"]] += 1

    c = (
        Pie()
        .add("", [list(z) for z in zip([x for x in datas.keys()], [y for y in datas.values()])])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="成都新房的种类和数量"),
            legend_opts=opts.LegendOpts(  # 调整位置
                orient="vertical",
                pos_top="15%",
                pos_left="2%"
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}{d}%  {c}"))
    )

    c.render("templates/pie2.html")
    return HttpResponse(c.render_embed())


def pie3(request):
    """成都各种类房的数量和均价"""
    # 数据准备
    res = Mongo().connect_mongo('runoob', 'test').find()
    datas = {}

    for dt in res:
        if dt["type"] not in datas:
            datas[dt["type"]] = [1, float(dt["price"])]
        else:
            datas[dt["type"]][0] += 1
            datas[dt["type"]][-1] += float(dt["price"])

    # 绘制图形
    v = [v for v in datas.keys()]
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(v, [x[0] for x in datas.values()])],
            radius=["20%", "55%"],
            center=["30%", "40%"],
            rosetype="radius",
            # label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "",
            [list(z) for z in zip(v, [x[-1]//x[0] for x in datas.values()])],
            radius=["20%", "55%"],
            center=["70%", "40%"],
            rosetype="radius",
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="成都各种类新房的数量和均价",
                pos_left="35%"
            ),
            legend_opts=opts.LegendOpts(
                orient="vertical",
                pos_top="5%",
                pos_left="2%"
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}  {c}"))
    )
    c.render("templates/pie3.html")
    return HttpResponse(c.render_embed())


def bar_line(request):
    """各种类型房屋的平均价格和数量 柱状图——折线图"""

    districts = []  # 区县名称
    infos = {}  # 各类新房的总数和均价
    # {'商业': [821, 21854707.0], '住宅': [567, 6424626.0], '别墅': [79, 1200119.0], '写字楼': [77, 1120913.0]}

    cursor = Mongo().connect_mongo('runoob', 'test').find()
    for data in cursor:
        if data["district"] not in districts:  # 获取区县
            districts.append(data["district"])

        if data["type"] not in infos:
            infos[data["type"]] = [1, float(data["price"])]
        else:
            infos[data["type"]][0] += 1
            infos[data["type"]][-1] += float(data["price"])

    x_data = [x for x in infos.keys()]
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            "平均价格",
            ["{:.2f}".format(x[-1]/x[0]) for x in infos.values()],
            yaxis_index=0,
            color="#675bba",
            category_gap="65%",
        )

        .extend_axis(
            yaxis=opts.AxisOpts(
                name="",
                type_="value",
                # min_=0,
                # max_=250,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            )
        )

        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="",
                # min_=0,
                # max_=25,
                position="none",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=False, linestyle_opts=opts.LineStyleOpts(opacity=1)
                )
            )
        )

        .set_global_opts(
            title_opts=opts.TitleOpts(title="成都各种类型新房价格与数量")
        )
    )

    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis(
            "新房数量",
            ["{}".format(x[0]) for x in infos.values()],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=True),
        )
    )

    bar.overlap(line)

    bar.overlap(line).render("templates/barline.html")
    return HttpResponse(bar.overlap(line).render_embed())


def markline(request):
    """各种类型的新房每个价位的数量"""

    res = Mongo().connect_mongo('runoob', 'test').find()
    datas = {}

    for dt in res:
        if dt["type"] not in datas:
            datas[dt["type"]] = [dt["price"]]
        else:
            datas[dt["type"]].append(dt["price"])

    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), is_smooth=True)
        .add_yaxis("商家B", Faker.values(), is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-smooth"))
    )

    c.render("templates/markline.html")
    return HttpResponse(c.render_embed())


def addr_map(request):
    """新房地址在成都的分布"""
    my_set = Mongo().connect_mongo('runoob', 'pos')

    address_longitude = []  # 存放地址经度
    address_latitude = []  # 存放地址的纬度
    address_data = []  # 存放整个经纬度

    for data in my_set.find():
        address_longitude.append(data["position"][-1])
        address_latitude.append(data["position"][0])
        address_data.append(data["address"])

    return render(request, 'address.html',
                  {'address_longitude': json.dumps(address_longitude),
                   'address_latitude': json.dumps(address_latitude),
                   'address_data': json.dumps(address_data)})


# def word_cloud():
#     # 获取小地址，存入到writing文档中
#     res = Mongo().connect_mongo('runoob', 'test').find()  # 连接mongo，获取数据
#
#     with open("../static/other/writing.txt", 'a') as f:
#         for i in res:
#             data = i["address"] + i["district"]
#             f.write("{}".format(data))
#
#     f.close()
#
#     # 读取writing文档，实现词云转换
#     fr = open('../static/other/writing.txt', 'r')
#
#     s = ""
#     data = {}
#
#     for line in fr:
#         line = line.strip()
#         for x in range(0, len(line)):
#             if line[x] in [' ', '\t', '\n', '。', '，', '[', ']', '（', '）', ':', '-',
#                            '？', '！', '《', '》', '、', '；', '“', '”', '……', '0', '1', '2', '3', '4', '5',
#                            '6', '7', '8', '9', '=', '~', '…', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']:
#                 continue
#             s += str(line[x])
#
#     seg_list = jieba.cut(s, cut_all=False, HMM=True)
#     for word in seg_list:
#         if len(word) >= 2:
#             if not data.__contains__(word):
#                 data[word] = 0
#             data[word] += 1
#
#     my_wordcloud = WordCloud(
#         background_color='white',  # 设置背景颜色
#         max_words=400,  # 设置最大实现的字数
#         font_path=r'../static/other/SimHei.ttf',  # 设置字体格式，如不设置显示不了中文
#         mask=imread('chengdu_map.jpg'),
#         width=1000,
#         height=1000,
#     ).generate_from_frequencies(data)
#     plt.figure()
#     plt.imshow(my_wordcloud)
#     plt.axis('off')
#     plt.show()  # 展示词云
#     my_wordcloud.to_file('result.jpg')
#     fr.close()


def index(request):
    return render(request, "index.html")





