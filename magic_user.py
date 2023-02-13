from pyecharts.globals import ThemeType
from pyecharts.charts import Map
from pyecharts import options as opts

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='flaskdb')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询，获取数据库版本
cursor.execute("SELECT * from users")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

# print(data)

# 关闭不使用的游标对象
cursor.close()
# 关闭数据库连接
db.close()


# 最终数据
# conaddata = [("内蒙古", 1), ("河南", 2)]
conaddata = [("内蒙古自治区", 10000), ("河南省", 340), ("湖北省", 3100), ("山东省", 1300), ("湖南省", 300),
             ("广西壮族自治区", 3000), ("台湾省", 3000), ("新疆维吾尔自治区", 3000), ("江苏省", 400),
             ("贵州省", 200), ("四川省", 23000), ("西藏自治区", 3000), ("青海省", 4000), ("广东省", 1000), ("云南省", 6000)]
connumdata = [("内蒙古自治区", 10), ("河南省", 34), ("湖北省", 30), ("山东省", 13), ("湖南省", 30),
             ("广西壮族自治区", 30), ("台湾省", 30), ("新疆维吾尔自治区", 30), ("江苏省", 40),
             ("贵州省", 20), ("四川省", 23), ("西藏自治区", 30), ("青海省", 40), ("广东省", 10), ("云南省", 60)]



# 创建一个地图对象
map = Map(init_opts=opts.InitOpts(width="1400px", height='600px', theme=ThemeType.ROMANTIC))  # 对全局进行设置
map.set_global_opts(
    # 设置标题
    title_opts=opts.TitleOpts(title="魔友分布"),
    legend_opts=opts.LegendOpts(is_show=True),
    visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                      pieces=[
                                          {"min": 100000,
                                           "label": '>100000人',
                                           "color": "#FF0000"},
                                          {"min": 10000, "max":100000,
                                           "label": '>10000人',
                                           "color": "#6F171F"},
                                          {"min": 5000, "max": 10000,
                                           "label": '5000-10000人',
                                           "color": "#C92C34"},
                                          {"min": 1000, "max": 4999,
                                           "label": '1000-4999人',
                                           "color": "#E35B52"},
                                          {"min": 100, "max": 999,
                                           "label": '100-999人',
                                           "color": "#F39E86"},
                                          {"min": 10, "max": 99,
                                           "label": '10-99人',
                                           "color": "pink"},
                                          {"min": 1, "max": 9,
                                           "label": '1-9人',
                                           "color": "#FDEBD0"}]))
map.add("新增魔友", conaddata, maptype="china", is_map_symbol_show = True)
map.add('所有魔友', connumdata, maptype='china', is_map_symbol_show = True)
map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))      # 标签不显示(国家名称不显示)，显示出来很乱

map.render("magic.html")       # 生成html文件
