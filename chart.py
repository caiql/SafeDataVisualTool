import plotly.plotly
from plotly.graph_objs import *


def make_mapchart(lat, lon, text, filename='html/bigmap.html', year=0):
    if year == 0:
        title = '所有恐怖袭击数据(经纬度、国家、死亡总数、发生袭击的次数)'
    else:
        title = '%s%s' % (str(year), '年度恐怖袭击数据(经纬度、国家、第一恐怖组织名称、该次死亡总数)')
    data = Data([Scattermapbox(lat=lat, lon=lon, mode='markers', marker=Marker(size=6), text=text)])
    layout = Layout(title=title, autosize=True, hovermode='closest', mapbox=dict(
        accesstoken='pk.eyJ1IjoiY2FpcWlhb2xpbmciLCJhIjoiY2plc2wzYWFhMGFidDMzbXA3ZGhnaTVmNSJ9.5oedGm4F-mj6hqpMrL_PMQ',
        bearing=0, center=dict(lat=38.92, lon=-77.07), pitch=0, zoom=1))
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig,filename=filename,auto_open=False)


def make_barchart(x, y, name, title, x_name, y_name, filename):
    data_b = []
    tr_y1 = Bar(
        x=x,
        y=y,
        name=name
    )
    data_b.append(tr_y1)
    layout = Layout(title=title, xaxis={'title': x_name}, yaxis={'title': y_name})
    fig = Figure(data=data_b, layout=layout)
    filename = '%s%s%s' % ('html/', filename, 'bar.html')
    plotly.offline.plot(fig, filename=filename,auto_open=False)


def make_line_plots(x, y, name, title, x_name, y_name, filename):
    data_l = []
    tr_x = Scatter(
        x=x,
        y=y,
        name=name
    )
    data_l.append(tr_x)
    layout = Layout(title=title, xaxis={'title': x_name}, yaxis={'title': y_name})
    fig = Figure(data=data_l, layout=layout)
    filename = '%s%s%s' % ('html/', filename, 'line.html')
    plotly.offline.plot(fig, filename=filename,auto_open=False)