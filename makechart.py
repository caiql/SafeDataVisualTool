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
#全部恐怖袭击数量柱状图
def make_bigbar(data):
    data.set_yeardata()
    chart.make_barchart(data.year,data.count_year,data.chart_name,data.chart_title,data.x_name,data.y_name,data.filename)
#全部恐怖袭击折线图
def make_bigline(data):
    data.set_yeardata()
    chart.make_line_plots(data.year,data.count_year,data.chart_name,data.chart_title,data.x_name,data.y_name,data.filename)
#持续超过24小时占比折线图
def make_bigextended(data):
    data.set_extended()
    chart.make_line_plots(data.year,data.extended_per,data.chart_name,data.chart_title,data.x_name,data.y_name,data.filename)