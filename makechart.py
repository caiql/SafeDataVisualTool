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
    #chart.make_nbarchart(data.year_data,data.chart_title,data.x_name,data.y_name,data.filename)
    #chart.make_nline_plots(data.year_data, data.chart_title, data.x_name, data.y_name, data.filename)
    chart.make_bar_linechart(data.year_data, data.chart_title, data.x_name, data.y_name, data.filename)

#持续超过24小时占比图
def make_extended_data_pic(data):
    data.set_extended_data()
    #chart.make_nbarchart(data.extended_data,data.chart_title,data.x_name,data.y_name,data.filename)
    #chart.make_nline_plots(data.extended_data,data.chart_title,data.x_name,data.y_name,data.filename)
    chart.make_bar_linechart(data.extended_data,data.chart_title,data.x_name,data.y_name,data.filename)

#地区年度恐怖袭击图
def make_region_year_pic(data):
    data.set_region_year()
    #chart.make_nbarchart(data.region_year,data.chart_title,data.x_name,data.y_name,data.filename)
    #chart.make_nline_plots(data.region_year,data.chart_title,data.x_name,data.y_name,data.filename)
    chart.make_bar_linechart(data.region_year,data.chart_title,data.x_name,data.y_name,data.filename)

#各个地区数量占比饼图
def make_region_group_pic(data):
    data.set_region_group()
    chart.make_pie_charts(data.region_group,data.chart_title,data.filename)

#按年份查看各个地区数量占比图
def make_year_region_pic(data):
    data.set_year_region(1996)
    chart.make_pie_charts(data.year_region,data.chart_title,data.filename)

#按地区查看24小时占比图
def make_region_extended_data_pic(data):
    data.set_region_extended_data()
    #chart.make_nbarchart(data.region_extended_data,data.chart_title,data.x_name,data.y_name,data.filename)
    #chart.make_nline_plots(data.region_extended_data,data.chart_title,data.x_name,data.y_name,data.filename)
    chart.make_bar_linechart(data.region_extended_data,data.chart_title,data.x_name,data.y_name,data.filename)

def make_year_nkill_nwound_pic(data):
    data.set_year_nkill_nwound()
    #chart.make_nbarchart(data.year_nkill_nwound,data.chart_title,data.x_name,data.y_name,data.filename)
    #chart.make_nline_plots(data.year_nkill_nwound,data.chart_title,data.x_name,data.y_name,data.filename)
    chart.make_bar_linechart(data.year_nkill_nwound,data.chart_title,data.x_name,data.y_name,data.filename)

def make_region_year_nkill_nwound_pic(data):
    data.set_region_year_nkill_nwound()
    #chart.make_nbarchart(data.region_year_nkill_nwound,data.chart_title,data.x_name,data.y_name,data.filename)
    #chart.make_nline_plots(data.region_year_nkill_nwound,data.chart_title,data.x_name,data.y_name,data.filename)
    chart.make_bar_linechart(data.region_year_nkill_nwound,data.chart_title,data.x_name,data.y_name,data.filename)

def make_region_nkill_nwound_pic(data):
    data.set_region_nkill_nwound()
    chart.make_pie_charts(data.region_nkill_nwound,data.chart_title,data.filename)

def make_gname(data):
    data.set_gname()
    chart.make_nbarchart(data.gname,data.chart_title,data.x_name,data.y_name,data.filename)
    chart.make_nline_plots(data.gname,data.chart_title,data.x_name,data.y_name,data.filename)
    data.set_gname_group()
    chart.make_pie_charts(data.gname_group,data.chart_title,data.filename)

def make_success(data):
    data.set_success()
    chart.make_bar_linechart(data.success,data.chart_title,data.x_name,data.y_name,data.filename)

def make_region_success(data):
    data.set_region_success()
    chart.make_bar_linechart(data.region_success,data.chart_title,data.x_name,data.y_name,data.filename)

def make_region_success_group(data):
    data.set_region_success_group()
    chart.make_pie_charts(data.region_success_group,data.chart_title,data.filename)
	
def make_suicide(data):
    data.set_suicide()
    chart.make_bar_linechart(data.suicide,data.chart_title,data.x_name,data.y_name,data.filename)

def make_region_suicide(data):
    data.set_region_suicide()
    chart.make_bar_linechart(data.region_suicide,data.chart_title,data.x_name,data.y_name,data.filename)

def make_region_suicide_group(data):
    data.set_region_suicide_group()
    chart.make_pie_charts(data.region_suicide_group,data.chart_title,data.filename)

def make_attacktype(data):
    data.set_attacktype()
    chart.make_bar_linechart(data.attacktype,data.chart_title,data.x_name,data.y_name,data.filename)
    data.set_attacktype_group()
    chart.make_pie_charts(data.attacktype_group,data.chart_title,data.filename)

def make_region_attacktype(data):
    data.set_region_attacktype()
    chart.make_bar_linechart1(data.region_attacktype,data.chart_title,data.x_name,data.y_name,data.filename,data.La)

def make_region_attacktype_group(data):
    data.set_region_attacktype_group()
    chart.make_pie_charts1(data.region_attacktype_group,data.Lp,data.chart_title,data.filename)

def make_attackwhy(data):
    data.set_attackwhy()
    chart.make_bar_linechart(data.attackwhy,data.chart_title,data.x_name,data.y_name,data.filename)
    data.set_attackwhy_group()
    chart.make_pie_charts(data.attackwhy_group,data.chart_title,data.filename)

def make_region_attackwhy(data):
    data.set_region_attackwhy()
    chart.make_bar_linechart1(data.region_attackwhy,data.chart_title,data.x_name,data.y_name,data.filename,data.La)
    data.set_region_attackwhy_group()
    chart.make_pie_charts1(data.region_attackwhy_group,data.Lp,data.chart_title,data.filename)

def make_targtype(data):
    data.set_targtype()
    chart.make_bar_linechart(data.targtype,data.chart_title,data.x_name,data.y_name,data.filename)
    data.set_targtype_group()
    chart.make_pie_charts(data.targtype_group,data.chart_title,data.filename)

def make_region_targtype(data):
    data.set_region_targtype()
    chart.make_bar_linechart1(data.region_targtype,data.chart_title,data.x_name,data.y_name,data.filename,data.La)
    data.set_region_targtype_group()
    chart.make_pie_charts1(data.region_targtype_group,data.Lp,data.chart_title,data.filename)

def make_weaptype(data):
    data.set_weaptype()
    chart.make_bar_linechart(data.weaptype,data.chart_title,data.x_name,data.y_name,data.filename)
    data.set_weaptype_group()
    chart.make_pie_charts(data.weaptype_group,data.chart_title,data.filename)

def make_region_weaptype(data):
    data.set_region_weaptype()
    chart.make_bar_linechart1(data.region_weaptype,data.chart_title,data.x_name,data.y_name,data.filename,data.La)
    data.set_region_weaptype_group()
    chart.make_pie_charts1(data.region_weaptype_group,data.Lp,data.chart_title,data.filename)

def make_ransompaid(data):
    data.set_ransompaid()
    chart.make_bar_linechart(data.ransompaid,data.chart_title,data.x_name,data.y_name,data.filename)
    data.set_region_ransompaid()
    chart.make_bar_linechart(data.region_ransompaid,data.chart_title,data.x_name,data.y_name,data.filename)
    data.set_region_ransompaid_group()
    chart.make_pie_charts(data.region_ransompaid_group,data.chart_title,data.filename)
    data.set_hostkidoutcome()
    chart.make_bar_linechart(data.hostkidoutcome, data.chart_title, data.x_name, data.y_name, data.filename)
    data.set_hostkidoutcome_group()
    chart.make_pie_charts(data.hostkidoutcome_group,data.chart_title,data.filename)
    data.set_region_hostkidoutcome()
    chart.make_bar_linechart1(data.region_hostkidoutcome,data.chart_title,data.x_name,data.y_name,data.filename,data.La_a)
    data.set_region_hostkidoutcome_group()
    chart.make_pie_charts1(data.region_hostkidoutcome_group,data.Lp_a,data.chart_title,data.filename)
    data.set_ransompaid_hostkidoutcome()
    chart.make_bar_linechart(data.ransompaid, data.chart_title, data.x_name, data.y_name, data.filename)
    data.set_region_ransompaid_hostkidoutcome()
    chart.make_bar_linechart1(data.region_ransompaid, data.chart_title, data.x_name, data.y_name, data.filename,data.La)
    data.set_paid_hostkidoutcome()
    chart.make_bar_linechart(data.paid_hostkidoutcome, data.chart_title, data.x_name, data.y_name, data.filename)
    data.set_paid_hostkidoutcome_group()
    chart.make_pie_charts(data.paid_hostkidoutcome_group, data.chart_title, data.filename)
    data.set_region_paid_hostkidoutcome()
    chart.make_bar_linechart1(data.region_paid_hostkidoutcome, data.chart_title, data.x_name, data.y_name, data.filename,data.La)
    data.set_region_paid_hostkidoutcome_group()
    chart.make_pie_charts1(data.region_paid_hostkidoutcome_group, data.Lp, data.chart_title, data.filename)