import datadel
import chart

#def make_data(filename):
#    data = datadel.datadel(filename)
#    return data
#大地图
def make_bigmap(data):
    data.del_mapdata()
    chart.make_mapchart(data.blat,data.blon,data.btext)
#年度地图
def make_yearmap(data):
    data.del_year_mapdata(1996)
    chart.make_mapchart(data.ylat,data.ylon,data.ytext,data.yfilename,1996)
#全部恐怖袭击图
def make_year_data_pic(data):
    data.set_year_data()
    chart.make_nbarchart(data.year_data,data.chart_title,data.x_name,data.y_name,data.filename)
    chart.make_nline_plots(data.year_data, data.chart_title, data.x_name, data.y_name, data.filename)

#持续超过24小时占比图
def make_extended_data_pic(data):
    data.set_extended_data()
    chart.make_nbarchart(data.extended_data,data.chart_title,data.x_name,data.y_name,data.filename)
    chart.make_nline_plots(data.extended_data,data.chart_title,data.x_name,data.y_name,data.filename)

#地区年度恐怖袭击柱状图
def make_region_year_group_pic(data):
    data.set_region_year_group()
    chart.make_nbarchart(data.region_year_group,data.chart_title,data.x_name,data.y_name,data.filename)
    chart.make_nline_plots(data.region_year_group,data.chart_title,data.x_name,data.y_name,data.filename)

#各个地区数量占比饼图
def make_region_group_pic(data):
    data.set_region_group()
    chart.make_pie_charts(data.region_group,data.chart_title,data.filename)