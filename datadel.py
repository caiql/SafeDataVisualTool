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
        #恐怖袭击数量-全部
        self.year_group = None
        self.year = None
        self.count_year = None
        self.chart_name = None
        self.chart_title = None
        self.x_name = None
        self.y_name = None
        self.filename = None

        self.extended_per = None

    # 大地图数据的封装:经纬度、国家、死亡总数、发生袭击的次数
    def del_mapdata(self):
        if self.mapdata == None:
            self.mapdata = self.data_list[self.data_list['specificity'] != 5]
        mapdata = self.mapdata[['country_txt', 'latitude', 'longitude', 'nkill']]
        mapdata['count'] = 1
        latlonggroup = mapdata.groupby(['country_txt', 'latitude', 'longitude']).count().reset_index()
        latdata = latlonggroup['latitude']
        londata = latlonggroup['longitude']
        loctext = latlonggroup[['country_txt', 'nkill', 'count']]
        self.blat = latdata.values
        self.blon = londata.values
        self.btext = loctext.values

    # 每年地图数据的封装：经纬度、国家、第一恐怖组织名称、该年死亡总数
    def set_year_mapdata(self):
        if self.mapdata == None:
            self.mapdata = self.data_list[self.data_list['specificity'] != 5]
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

    def set_yeardata(self):
        if self.year_group ==None:
            yeardata = self.data_list['iyear'].values
            self.year_group = pd.value_counts(yeardata,sort=False)
        self.year = self.year_group.index
        self.count_year = self.year_group.values
        self.chart_name = '年度恐怖袭击数量'
        self.chart_title = '年度恐怖袭击数量图'
        self.x_name = '年份'
        self.y_name = '恐怖袭击次数'
        self.filename = 'big'

    def set_extended(self):
        if self.year_group ==None:
            yeardata = self.data_list['iyear'].values
            self.year_group = pd.value_counts(yeardata,sort=False)
        extended_data = self.data_list[self.data_list['extended']==1]
        extended_yeardata = extended_data['iyear'].values
        extended_yeardata_group = pd.value_counts(extended_yeardata,sort=False)
        extended_yeardata_per = extended_yeardata_group.div(self.year_group,fill_value=0)
        self.year = extended_yeardata_per.index
        self.extended_per = extended_yeardata_per.values
        self.chart_name = '年度持续超过24小时的袭击次数占比'
        self.chart_title = '年度持续超过24小时的袭击次数占比图'
        self.x_name = '年份'
        self.y_name = '持续超过24小时的袭击次数/袭击次数'
        self.filename = 'big_extended'