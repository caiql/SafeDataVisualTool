import pandas as pd
import plotly.plotly
from plotly.graph_objs import *
data_list = pd.read_table('D:/普通话/globalterrorismdb_0617dist.csv',engine='python',sep=',')
#extended_data = data_list.pivot_table(values='region',index=['iyear','extended'],columns='region_txt',aggfunc='count',fill_value=0,margins=True)
extended_data1 = pd.crosstab(data_list.iyear,data_list.extended,margins=True)
extended_data2 = {'more than 24 hours/all':extended_data1[1]/extended_data1['All']}
extended_data = pd.DataFrame(extended_data2)
#yeardata = data_list['iyear'].values
#year_group = pd.value_counts(yeardata,sort=False)
#year_all = {'event count in year':year_group}
#extended_data = pd.DataFrame(year_all)
data_ln = []
for columns in extended_data.columns:
    tr_x = Scatter(
        x=extended_data.index,
        y=extended_data[columns].values,
        name=columns
    )
    data_ln.append(tr_x)
layout = Layout(title='是否持续超过24小时数据图', xaxis={'title': '年份'}, yaxis={'title': '袭击次数'})
fig = Figure(data=data_ln, layout=layout)
filename = 'html/testline.html'
plotly.offline.plot(fig, filename=filename)