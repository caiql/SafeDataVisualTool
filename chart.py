import plotly.plotly
from plotly.graph_objs import *


def make_mapchart(lat, lon, text, filename='html/0/1bigmap.html', year=0):
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

def make_bar_linechart(dataset_all,title,x_name,y_name,filename):
    data_bl = []
    for dataset in dataset_all:
        for columns in dataset.columns:
            tr_x = Bar(
                x=dataset.index,
                y=dataset[columns].values,
                name=columns
            )
            tr_y = Scatter(
                x=dataset.index,
                y=dataset[columns].values,
                name=columns
            )
            data_bl.append(tr_x)
            data_bl.append(tr_y)
    layout = Layout(title=title, xaxis={'title': x_name}, yaxis={'title': y_name})
    fig = Figure(data=data_bl, layout=layout)
    filename = '%s%s%s' % ('html/', filename, 'bar_line.html')
    plotly.offline.plot(fig, filename=filename, auto_open=False)

def make_bar_linechart1(dataset_all,title,x_name,y_name,filename,La_all):
    data_bl = []
    for dataset,La in zip(dataset_all,La_all):
        for columns,x in zip(dataset.columns,La):
            tr_x = Bar(
                x=dataset.index,
                y=dataset[columns].values,
                name=x
            )
            tr_y = Scatter(
                x=dataset.index,
                y=dataset[columns].values,
                name=x
            )
            data_bl.append(tr_x)
            data_bl.append(tr_y)
    layout = Layout(title=title, xaxis={'title': x_name}, yaxis={'title': y_name})
    fig = Figure(data=data_bl, layout=layout)
    filename = '%s%s%s' % ('html/', filename, 'bar_line.html')
    plotly.offline.plot(fig, filename=filename, auto_open=False)

def make_nbarchart(dataset,title,x_name,y_name,filename):
    data_bn = []
    for index in dataset.index:
        tr_x = Bar(
            x=dataset.columns,
            y=dataset.ix[index].values,
            name=index
        )
        data_bn.append(tr_x)
    layout = Layout(title=title, xaxis={'title': x_name}, yaxis={'title': y_name})
    fig = Figure(data=data_bn, layout=layout)
    filename = '%s%s%s' % ('html/', filename, 'bar.html')
    plotly.offline.plot(fig, filename=filename,auto_open=False)

def make_nline_plots(dataset,tiltle,x_name,y_name,filename):
    data_ln = []
    for index in dataset.index:
        tr_x = Scatter(
            x=dataset.columns,
            y=dataset.ix[index].values,
            name=index
        )
        data_ln.append(tr_x)
    layout = Layout(title=tiltle, xaxis={'title': x_name}, yaxis={'title': y_name})
    fig = Figure(data=data_ln, layout=layout)
    filename = '%s%s%s' % ('html/', filename, 'line.html')
    plotly.offline.plot(fig, filename=filename, auto_open=False)

def make_pie_charts(dataset,title,filename):
    data_g = []
    tr_p = Pie(
        labels = dataset.index,
        values = dataset.values,
        sort = False
    )
    data_g.append(tr_p)
    layout = Layout(title=title)
    fig = Figure(data=data_g, layout=layout)
    filename = '%s%s%s' % ('html/', filename, 'pie.html')
    plotly.offline.plot(fig, filename=filename, auto_open=False)

def make_pie_charts1(dataset,Lp,title,filename):
    data_g = []
    tr_p = Pie(
        labels = Lp,
        values = dataset.values,
        sort = False
    )
    data_g.append(tr_p)
    layout = Layout(title=title)
    fig = Figure(data=data_g, layout=layout)
    filename = '%s%s%s' % ('html/', filename, 'pie.html')
    plotly.offline.plot(fig, filename=filename, auto_open=False)