import pandas as pd
#数据处理
class datadel(object):
    def __init__(self,filename):
#        self.data_list = pd.read_csv(filename,engine='python')
        self.data_list = pd.read_table(filename,engine='python',sep=',')
        #大地图
        self.mapdata =None
        self.blat = None
        self.blon = None
        self.btext = None
        #年度地图
        self.latlonggroup_year = None
        self.ylat = None
        self.ylon = None
        self.ytext = None
        self.yfilename = None

        #恐怖袭击数量统计分析
        self.year_group = None#年份组合,series
        self.year_data = None#年度恐怖袭击折线图，dataframe
        self.extended = None
        self.extended_data = None#持续超过24小时占比组合折线图，dataframe
        self.region_extended_data = None
        self.region_year_group = None#年份+恐怖袭击数量+地区组合折线图，dataframe
        self.region_group = None#各个地区恐怖袭击数量占比-饼图，series
        self.year_region = None#按年份查看各个地区数量占比-饼图，dataframe
        self.year_nkill_nwound =None#年度伤亡人数
        self.region_year_nkill_nwound = None#按地区查看年度伤亡人数

        self.chart_title = None#图表的标题
        self.x_name = None#X轴名称
        self.y_name = None#Y轴名称
        self.filename = None#html文件名关键字

    # 大地图数据的封装:经纬度、国家、死亡总数、发生袭击的次数，1-1
    def del_mapdata(self):
        self.mapdata = self.data_list[self.data_list['specificity'] != 5]
        mapdata = self.mapdata[['country_txt', 'latitude', 'longitude', 'nkill']]
        mapdata['count'] = 1
        latlonggroup = mapdata.groupby(['country_txt', 'latitude', 'longitude']).sum().reset_index()
        latdata = latlonggroup['latitude']
        londata = latlonggroup['longitude']
        loctext = latlonggroup[['country_txt', 'nkill', 'count']]
        self.blat = latdata.values
        self.blon = londata.values
        self.btext = loctext.values

    # 每年地图数据的封装：经纬度、国家、第一恐怖组织名称、该年死亡总数1-2
    def set_year_mapdata(self):
        yearmapdata = self.mapdata[['iyear', 'country_txt', 'latitude', 'longitude', 'gname', 'nkill']]
        self.latlonggroup_year = yearmapdata.groupby('iyear')

    def del_year_mapdata(self,year):
        if self.latlonggroup_year ==None:
            self.set_year_mapdata()
        latlonggroup = self.latlonggroup_year.get_group(year)
        latdata = latlonggroup['latitude']
        londata = latlonggroup['longitude']
        loctext = latlonggroup[['country_txt', 'gname', 'nkill']]
        self.yfilename = '%s%s%s' % ('html/', str(year), 'map.html')
        self.ylat = latdata.values
        self.ylon = londata.values
        self.ytext = loctext.values

    def set_year_group(self):
        yeardata = self.data_list['iyear'].values
        self.year_group = pd.value_counts(yeardata, sort=False)

    #所有年度恐怖袭击数量（柱状图、折线图）2-1
    def set_year_data(self):
        year_all = {'event count in year':self.year_group}
        self.year_data = pd.DataFrame(year_all)
        self.chart_title = '年度恐怖袭击数量图'
        self.x_name = '年份'
        self.y_name = '恐怖袭击次数'
        self.filename = 'year_data'

    #统计每年持续超过24小时的袭击次数比（柱状图、折线图）2-2
    def set_extended_data(self):
        self.extended = self.data_list[self.data_list['extended'] == 1]
        extended_data1 = pd.value_counts(self.extended['iyear'].values, sort=False)
        extended_data2 = {'extended': extended_data1}
        extended_data = pd.DataFrame(extended_data2)
        self.extended_data = extended_data.div(self.year_group,axis=0)
        self.chart_title = '年度持续超过24小时的袭击次数占比图'
        self.x_name = '年份'
        self.y_name = '持续超过24小时的袭击次数/袭击次数'
        self.filename = 'extended_data'

    # 按地区查看每年持续超过24小时的袭击次数比（柱状图、折线图）2-4、2-6
    def set_region_extended_data(self):
        region_extended_data = pd.crosstab(self.extended.iyear,self.extended.region_txt, margins=False)
        self.region_extended_data = region_extended_data.div(self.year_group,axis=0)
        self.chart_title = '年度持续超过24小时的袭击次数占比图'
        self.x_name = '年份'
        self.y_name = '持续超过24小时的袭击次数/袭击次数'
        self.filename = 'region_extended_data'

    #按地区查看每年恐怖袭击总次数（柱状图、折线图）2-3、2-5
    def set_region_year_group(self):
        self.region_year_group = pd.crosstab(self.data_list.iyear,self.data_list.region_txt,margins=False)
        self.chart_title = '年度各个地区恐怖袭击总次数图'
        self.x_name = '年份'
        self.y_name = '恐怖袭击次数'
        self.filename = 'region_year_group'

    # 地区恐怖袭击数量-饼图 2-7
    def set_region_group(self):
        region = self.data_list['region_txt'].values
        self.region_group = pd.value_counts(region)
        self.chart_title = '地区恐怖袭击数量占比图'
        self.filename = 'region_group'

    # 按年份查看各个地区数量比例，饼图 2-8
    def set_year_region(self, year):
        self.year_region = self.region_year_group.loc[year]
        self.chart_title = '%s%s' % (year, '年度各地区恐怖袭击数量占比图')
        self.filename = '%s%s' % (year, '_region')

    def set_year_nkill_nwound(self):
        self.year_nkill_nwound = self.data_list.pivot_table(values=['nkill','nwound'],index='iyear',aggfunc='sum')
        self.x_name = '年份'
        self.y_name = '死(nkill)/伤(nwound)人数'
        self.chart_title = '年度伤亡人数统计图'
        self.filename = 'year_nkill_nwound'

    def set_region_year_nkill_nwound(self):
        self.region_year_nkill_nwound = self.data_list.pivot_table(values=['nkill','nwound'],index='iyear',columns='region_txt',aggfunc='sum')
        self.chart_title = '地区年度死亡人数统计图'
        self.x_name = '年份'
        self.y_name = '死(nkill)/伤(nwound)人数'
        self.filename = 'region_year_nkill_nwound'

