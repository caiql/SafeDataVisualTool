import pandas as pd
#数据处理
class datadel(object):
    def __init__(self,filename):
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
        self.region_nkill_nwound = None#查看地区伤亡总数比例-饼图
        self.gname = None
        self.success = None

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
        self.region_year_group1 = pd.crosstab(self.data_list.iyear,self.data_list.region_txt,margins=True)
        self.region_year_group = self.region_year_group1.drop('All')
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

    #年度伤亡人数统计图（柱状图，折线图）3-1、3-2
    def set_year_nkill_nwound(self):
        self.year_nkill_nwound = self.data_list.pivot_table(values=['nkill','nwound'],index='iyear',aggfunc='sum',fill_value=0,margins=True)
        self.year_nkill_nwound.drop('All',inplace=True)
        self.x_name = '年份'
        self.y_name = '死(nkill)/伤(nwound)人数'
        self.chart_title = '年度伤(nwound)亡(nkill)人数统计图'
        self.filename = 'year_nkill_nwound'

    #按地区查看年度伤亡人数（柱状图，折线图）3-3、3-4、3-7、3-8
    def set_region_year_nkill_nwound(self):
        region_year_nkill = self.data_list.pivot_table(values='nkill',index='iyear',columns='region_txt',aggfunc='sum',fill_value=0,margins=True)
        region_year_nwound = self.data_list.pivot_table(values='nwound',index='iyear',columns='region_txt',aggfunc='sum',fill_value=0,margins=True)
        region_year_nkil_nwound = region_year_nkill.add(region_year_nwound)
        self.region_year_nkill_nwound = region_year_nkill.join(region_year_nwound,lsuffix='_nkill',rsuffix='_nwound').join(region_year_nkil_nwound)
        self.region_nkill_nwound = self.region_year_nkill_nwound.loc['All']
        self.region_year_nkill_nwound.drop('All',inplace=True)
        self.chart_title = '地区年度伤(nwound)亡(nkill)人数统计图'
        self.x_name = '年份'
        self.y_name = '死(nkill)/伤(nwound)人数'
        self.filename = 'region_year_nkill_nwound'

    #各地区伤亡总人数比例-饼图3-5，3-6
    def set_region_nkill_nwound(self):
        self.region_nkill_nwound.drop('All',inplace=True)
        self.chart_title = '地区伤(nwound)亡(nkill)人数统计图'
        self.filename = 'region_nkill_nwound'

    #各个恐怖组织年度袭击数量，数量太多,4-1
    def set_gname(self):
        self.gname = pd.crosstab(self.data_list.iyear,self.data_list.gname)
        self.chart_title = '恐怖组织年度袭击数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename  = 'gname'

    #袭击成败年度数量,5-1
    def set_success(self):
        self.success = pd.crosstab(self.data_list.iyear,self.data_list.success,margins=True)
        self.success.rename(columns={0:'fail',1:'success'},inplace=True)
        self.success.drop('All',inplace=True)
        self.chart_title = '袭击成败数量统计图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = 'success'

    #按地区查看袭击成败年度数量,列名待重置,5-2,5-4
    def set_region_success(self):
        region_success = self.data_list.pivot_table(values='success',index='iyear',columns='region_txt',aggfunc='sum',fill_value=0,margins=True)
        region_fail = self.region_year_group1.sub(region_success,fill_value=0)
        self.region_success = region_success.join(region_fail,lsuffix='_success',rsuffix='_fail').join(self.region_year_group)
        self.region_success_group = self.region_success.loc['All']
        self.region_success.drop('All',inplace = True)
        self.chart_title = '地区年度袭击成败数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = 'region_success'

    #查看地区成败数量占比饼状图,5-3
    def set_region_success_group(self):
        self.chart_title = '地区袭击成败占比图'
        self.filename = 'region_success_group'

    # 自杀式袭击年度数量,列名待重置,5-5
    def set_suicide(self):
        self.suicide = pd.crosstab(self.data_list.iyear, self.data_list.suicide, margins=True)
        self.suicide.rename(columns={0: 'suicide', 1: 'other'}, inplace=True)
        self.suicide.drop('All', inplace=True)
        self.chart_title = '自杀式数量统计图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = 'suicide'

    # 按地区查看自杀式袭击的年度数量,列名待重置,5-6,5-8
    def set_region_suicide(self):
        region_suicide = self.data_list.pivot_table(values='suicide', index='iyear', columns='region_txt',aggfunc='sum',fill_value=0, margins=True)
        region_other = self.region_year_group1.sub(region_suicide,fill_value=0)
        self.region_suicide = region_suicide.join(region_other,lsuffix='_suicide',rsuffix='_other').join(self.region_year_group)
        self.region_suicide_group = self.region_suicide.loc['All']
        self.region_suicide.drop('All', inplace=True)
        self.chart_title = '地区年度自杀式袭击数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = 'region_suicide'

    # 查看地区自杀式袭击数量占比饼状图,5-7
    def set_region_suicide_group(self):
        self.chart_title = '地区自杀式袭击占比图'
        self.filename = 'region_suicide_group'

    #年度袭击种类数量图，5-10
    def set_attacktype(self):
        attacktype1 = pd.crosstab(self.data_list.iyear,self.data_list.attacktype1_txt,margins=True)
        #attacktype1.drop(['All'],axis=1,inplace=True)
        attacktype2 = pd.crosstab(self.data_list.iyear,self.data_list.attacktype2_txt,margins=True)
        #attacktype2.drop(['All'], axis=1, inplace=True)
        attacktype3 = pd.crosstab(self.data_list.iyear,self.data_list.attacktype3_txt,margins=True)
        #attacktype3.drop(['All'], axis=1, inplace=True)
        attacktype = attacktype1.add(attacktype2.add(attacktype3,fill_value=0),fill_value=0)
        attacktype.drop(['All'],axis=1,inplace=True)
        attacktype_group1 = attacktype1.join(attacktype2,lsuffix='_type1',rsuffix='_type2')
        attacktype_group2 = attacktype3.join(attacktype,lsuffix='_type3')
        self.attacktype = attacktype_group1.join(attacktype_group2)
        self.attacktype_group = self.attacktype.loc['All']
        self.attacktype.drop('All',inplace=True)
        self.chart_title = '年度恐怖袭击种类数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = 'attacktype'

    def set_attacktype_group(self):
        self.attacktype_group.drop('All',inplace=True)
        self.chart_title = '年度恐怖袭击种类占比图'
        self.filename = 'attacktype_group'