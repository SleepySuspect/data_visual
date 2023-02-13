import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd

# 根据注册/更新时间 生成y轴
def create_y(y_date: list, size) -> list:
    y_axis = [0] * size
    for created in y_date:
        year = int(created[0:4])
        if created[5:6] == '0':
            month = int(created[6:7])
        else:
            month = int(created[5:7])
        year_gap = year - 2007
        y_axis[year_gap * 12 + month - 1] += 1
    # 列表所有0替换为None
    bbb = [None if i == 0 else i for i in y_axis]
    return bbb

if __name__ == '__main__':
    # 生成x轴
    x_list = []  # 2007 11 / 5   2018 /12
    for year in range(2007, 2019):
        for month in range(1, 13):
            if month < 10:
                x_item = str(year) + "-0" + str(month)
            else:
                x_item = str(year) + "-" + str(month)
            x_list.append(x_item)

    data = pd.read_csv('excel/large_twitch_features.csv', header=0, index_col=False, usecols=[3, 4],
                       na_values=["None"])
    columns = data.columns
    res = []
    for c in columns:
        d = data[c].values.tolist()
        res.append(d)
    created_list = res[0]
    update_list = res[1]
    # 生成y轴  -- 注册时间
    y_created = create_y(created_list, len(x_list))
    # 生成y轴  -- 更新时间
    y_update = create_y(update_list, len(x_list))
    line = (
        Line()
            .add_xaxis(xaxis_data=x_list)
            .add_yaxis(series_name="注册时间", y_axis=y_created, is_smooth=True)
            .set_global_opts(title_opts=opts.TitleOpts(title="Teitch网站创建时间分析"))
    )
    line.render("created_at.html")  # 生成html文件

    line = (
        Line()
            .add_xaxis(xaxis_data=x_list)
            .add_yaxis(series_name="更新时间", y_axis=y_update, is_smooth=True)
            .set_global_opts(title_opts=opts.TitleOpts(title="Teitch网站修改时间分析"))
    )
    line.render("updated_at.html")  # 生成html文件


