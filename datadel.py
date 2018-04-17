import pandas as pd
from itertools import product
#数据处理
class datadel(object):
    def __init__(self,filename):
        self.data_list = pd.read_table(filename,engine='python',sep=',')
        #self.data_list = data_list
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
        self.year = None#年份组合,series
        #self.year_data = []#年度恐怖袭击折线图，dataframe
        self.extended = None
        #self.extended_data = None#持续超过24小时占比组合折线图，dataframe
        #self.region_extended_data = None
        #self.region_year = None#年份+恐怖袭击数量+地区组合折线图，dataframe
        self.region_group = None#各个地区恐怖袭击数量占比-饼图，series
        self.year_region = None#按年份查看各个地区数量占比-饼图，dataframe
        #self.year_nkill_nwound =None#年度伤亡人数
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
        self.yfilename = '%s%s%s' % ('html/0/', str(year), 'map.html')
        self.ylat = latdata.values
        self.ylon = londata.values
        self.ytext = loctext.values

    def set_year(self):
        yeardata = self.data_list['iyear'].values
        self.year = pd.value_counts(yeardata, sort=False)

    #所有年度恐怖袭击数量（柱状图、折线图）2-1
    def set_year_data(self):
        self.year_data = []
        year_all = {'All':self.year}
        self.year_data1 = pd.DataFrame(year_all)
        self.year_data.append(self.year_data1)
        self.chart_title = '年度恐怖袭击数量图'
        self.x_name = '年份'
        self.y_name = '恐怖袭击次数'
        self.filename = '1/year_data'

    # 按地区查看每年恐怖袭击总次数（柱状图、折线图）2-3、2-5
    def set_region_year(self):
        self.region_year = []
        self.region_year1 = pd.crosstab(self.data_list.iyear, self.data_list.region_txt, margins=True)
        self.region_group = self.region_year1.loc['All']
        self.region_group.drop('All', inplace=True)
        self.region_year2 = self.region_year1.drop('All')
        self.region_year.append(self.region_year2)
        self.chart_title = '年度各个地区恐怖袭击总次数图'
        self.x_name = '年份'
        self.y_name = '恐怖袭击次数'
        self.filename = '1/region_year'

    #统计每年持续超过24小时的袭击次数比（柱状图、折线图）2-2
    def set_extended_data(self):
        self.extended_data = []
        self.extended = self.data_list[self.data_list['extended'] == 1]
        extended_data1 = pd.value_counts(self.extended['iyear'].values, sort=False)
        extended_data2 = {'extended': extended_data1}
        self.extended_data1 = pd.DataFrame(extended_data2)
        self.extended_data1 = self.extended_data1.div(self.year,axis=0)
        self.extended_data.append(self.extended_data1)
        self.chart_title = '年度持续超过24小时的袭击次数占比图'
        self.x_name = '年份'
        self.y_name = '持续超过24小时的袭击次数/袭击次数'
        self.filename = '1/extended_data'

    # 按地区查看每年持续超过24小时的袭击次数比（柱状图、折线图）2-4、2-6
    def set_region_extended_data(self):
        self.region_extended_data = []
        self.region_extended_data1 = pd.crosstab(self.extended.iyear,self.extended.region_txt, margins=False)
        self.region_extended_data1 = self.region_extended_data1.div(self.year,axis=0)
        self.region_extended_data.append(self.region_extended_data1)
        self.chart_title = '地区年度持续超过24小时的袭击次数占比图'
        self.x_name = '年份'
        self.y_name = '持续超过24小时的袭击次数/袭击次数'
        self.filename = '1/region_extended_data'

    # 地区恐怖袭击数量-饼图 2-7
    def set_region_group(self):
        #region = self.data_list['region_txt'].values
        #self.region_group = pd.value_counts(region)
        self.chart_title = '地区恐怖袭击数量占比图'
        self.filename = '1/region_group'

    # 按年份查看各个地区数量比例，饼图 2-8
    def set_year_region(self, year):
        self.year_region = self.region_year2.loc[year]
        self.chart_title = '%s%s' % (year, '年度各地区恐怖袭击数量占比图')
        self.filename = '%s%s%s' % ('1/',year, '_region')

    #年度伤亡人数统计图（柱状图，折线图）3-1、3-2
    def set_year_nkill_nwound(self):
        self.year_nkill_nwound = []
        self.year_nkill_nwound1 = self.data_list.pivot_table(values=['nkill','nwound'],index='iyear',aggfunc='sum',fill_value=0,margins=True)
        self.year_nkill_nwound1.drop('All',inplace=True)
        self.year_nkill_nwound.append(self.year_nkill_nwound1)
        self.year_nkill_nwound.append(self.year_data1)
        self.x_name = '年份'
        self.y_name = '死(nkill)/伤(nwound)人数'
        self.chart_title = '年度伤(nwound)亡(nkill)人数统计图'
        self.filename = '2/year_nkill_nwound'

    #按地区查看年度伤亡人数（柱状图，折线图）3-3、3-4、3-7、3-8
    def set_region_year_nkill_nwound(self):
        self.region_year_nkill_nwound = []
        region_year_nkill = self.data_list.pivot_table(values='nkill',index='iyear',columns='region_txt',aggfunc='sum',fill_value=0,margins=True)
        region_year_nwound = self.data_list.pivot_table(values='nwound',index='iyear',columns='region_txt',aggfunc='sum',fill_value=0,margins=True)
        region_year_nkill_nwound = region_year_nkill.add(region_year_nwound)
        region_year_nkill.rename(columns=lambda x: 'nkill_' + x, inplace=True)
        region_year_nwound.rename(columns=lambda x: 'nwound_' + x, inplace=True)
        region_year_nkill_nwound.rename(columns=lambda x: 'nkill_nwound_' + x, inplace=True)

        region_nkill = region_year_nkill.loc['All']
        region_nwound = region_year_nwound.loc['All']
        region_nkill_nwound = region_year_nkill_nwound.loc['All']
        region_nkill_nwound.drop('nkill_nwound_All',inplace=True)

        region_year_nkill.drop('All', inplace=True)
        region_year_nwound.drop('All', inplace=True)
        region_year_nkill_nwound.drop('All', inplace=True)

        self.region_nkill_nwound = pd.concat([region_nkill,region_nwound,region_nkill_nwound])

        self.region_year_nkill_nwound.append(region_year_nkill)
        self.region_year_nkill_nwound.append(region_year_nwound)
        self.region_year_nkill_nwound.append(region_year_nkill_nwound)
        self.region_year_nkill_nwound.append(self.region_year2)
        self.chart_title = '地区年度伤(nwound)亡(nkill)人数统计图'
        self.x_name = '年份'
        self.y_name = '死(nkill)/伤(nwound)人数'
        self.filename = '2/region_year_nkill_nwound'

    #各地区伤亡总人数比例-饼图3-5，3-6
    def set_region_nkill_nwound(self):
        #self.region_nkill_nwound.drop('All',inplace=True)
        self.chart_title = '地区伤(nwound)亡(nkill)人数占比图'
        self.filename = '2/region_nkill_nwound'

    #各个恐怖组织年度袭击数量，数量太多,4-1
    def set_gname(self):
        #self.gname = pd.crosstab(self.data_list.iyear,self.data_list.gname,margins=True)
        self.gname = pd.crosstab(self.data_list.gname,self.data_list.iyear,margins=True)
        if len(self.gname.index) > 800:
            self.gname = self.gname[self.gname.All > 5]
        self.gname_group = self.gname.All
        self.gname.drop('All',axis=1,inplace=True)
        self.chart_title = '恐怖组织年度袭击数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename  = '3/gname'

    #各个恐怖组织袭击数量占比饼图
    def set_gname_group(self):
        self.gname_group.drop('All',inplace=True)
        self.chart_title = '恐怖组织袭击数量占比图'
        self.filename = '3/gname_group'

    #袭击成败年度数量,5-1
    def set_success(self):
        self.success = []
        self.success1 = pd.crosstab(self.data_list.iyear,self.data_list.success,margins=True)
        self.success1.rename(columns={0:'fail',1:'success'},inplace=True)
        self.success1.drop('All',inplace=True)
        self.success.append(self.success1)
        self.chart_title = '袭击成败数量统计图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '4/success'

    #按地区查看袭击成败年度数量,列名待重置,5-2,5-4
    def set_region_success(self):
        self.region_success = []
        region_success = self.data_list.pivot_table(values='success',index='iyear',columns='region_txt',aggfunc='sum',fill_value=0,margins=True)
        region_fail = self.region_year1.sub(region_success,fill_value=0)
        region_success.rename(columns=lambda x: 'success_' + x, inplace=True)
        region_fail.rename(columns=lambda x: 'fail_' + x, inplace=True)
        region_success_group = region_success.loc['All']
        region_fail_group = region_fail.loc['All']
        region_success.drop('All', inplace=True)
        region_fail.drop('All', inplace=True)

        self.region_success_group = pd.concat([region_success_group,region_fail_group,self.region_group])
        self.region_success.append(region_success)
        self.region_success.append(region_fail)
        self.region_success.append(self.region_year2)

        self.chart_title = '地区年度袭击成败数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '4/region_success'

    #查看地区成败数量占比饼状图,5-3
    def set_region_success_group(self):
        self.chart_title = '地区袭击成败占比图'
        self.filename = '4/region_success_group'

    # 自杀式袭击年度数量,列名待重置,5-5
    def set_suicide(self):
        self.suicide = []
        self.suicide1 = pd.crosstab(self.data_list.iyear, self.data_list.suicide, margins=True)
        self.suicide1.rename(columns={0: 'suicide', 1: 'other'}, inplace=True)
        self.suicide1.drop('All', inplace=True)
        self.suicide.append(self.suicide1)
        self.chart_title = '自杀式数量统计图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '4/suicide'

    # 按地区查看自杀式袭击的年度数量,列名待重置,5-6,5-8
    def set_region_suicide(self):
        self.region_suicide = []
        self.region_suicide_group = []
        region_suicide = self.data_list.pivot_table(values='suicide', index='iyear', columns='region_txt',aggfunc='sum',fill_value=0, margins=True)
        region_other = self.region_year1.sub(region_suicide, fill_value=0)
        region_suicide.rename(columns=lambda x: 'suicide_' + x, inplace=True)
        region_other.rename(columns=lambda x: 'other_' + x, inplace=True)
        region_suicide_group = region_suicide.loc['All']
        region_other_group = region_other.loc['All']
        region_suicide.drop('All', inplace=True)
        region_other.drop('All', inplace=True)

        self.region_suicide_group = pd.concat([region_suicide_group,region_other_group,self.region_group])
        self.region_suicide.append(region_suicide)
        self.region_suicide.append(region_other)
        self.region_suicide.append(self.region_year2)

        self.chart_title = '地区年度自杀式袭击数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '4/region_suicide'

    # 查看地区自杀式袭击数量占比饼状图,5-7
    def set_region_suicide_group(self):
        self.chart_title = '地区自杀式袭击占比图'
        self.filename = '4/region_suicide_group'

    #年度袭击种类数量图，5-10
    def set_attacktype(self):
        self.attacktype = []
        attacktype1 = pd.crosstab(self.data_list.iyear,self.data_list.attacktype1_txt,margins=True)
        attacktype2 = pd.crosstab(self.data_list.iyear,self.data_list.attacktype2_txt,margins=True)
        attacktype3 = pd.crosstab(self.data_list.iyear,self.data_list.attacktype3_txt,margins=True)
        attacktype = attacktype1.add(attacktype2.add(attacktype3, fill_value=0), fill_value=0)
        attacktype1.rename(columns=lambda x: 'type1_' + x, inplace=True)
        attacktype2.rename(columns=lambda x: 'type2_' + x, inplace=True)
        attacktype3.rename(columns=lambda x: 'type3_' + x, inplace=True)
        attacktype.rename(columns=lambda x: 'All_' + x, inplace=True)
        self.attacktype1_group = attacktype1.loc['All']
        self.attacktype2_group = attacktype2.loc['All']
        self.attacktype3_group = attacktype3.loc['All']
        attacktype_group = attacktype.loc['All']
        attacktype_group.drop('All_All', inplace=True)
        attacktype1.drop('All', inplace=True)
        attacktype2.drop('All', inplace=True)
        attacktype3.drop('All', inplace=True)
        attacktype.drop('All', inplace=True)

        self.attacktype_group = pd.concat([self.attacktype1_group,self.attacktype2_group,self.attacktype3_group,attacktype_group])
        self.attacktype.append(attacktype1)
        self.attacktype.append(attacktype2)
        self.attacktype.append(attacktype3)
        self.chart_title = '年度恐怖袭击种类数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '4/attacktype'

    def set_attacktype_group(self):
        self.chart_title = '年度恐怖袭击种类占比图'
        self.filename = '4/attacktype_group'

    def set_region_attacktype(self):
        self.region_attacktype = []
        region_attacktype1 = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt,self.data_list.attacktype1_txt],dropna=False)
        region_attacktype1_group = region_attacktype1.sum()
        self.region_attacktype.append(region_attacktype1)
        region_attacktype2 = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt, self.data_list.attacktype2_txt],dropna=False)
        region_attacktype2_group = region_attacktype2.sum()
        self.region_attacktype.append(region_attacktype2)
        region_attacktype3 = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt, self.data_list.attacktype3_txt],dropna=False)
        region_attacktype3_group = region_attacktype3.sum()
        self.region_attacktype.append(region_attacktype3)
        self.region_attacktype.append(self.region_year2)
        self.region_attacktype_group = pd.concat([region_attacktype1_group,region_attacktype2_group,region_attacktype3_group])
        self.attacktype1_group.drop('type1_All', inplace=True)
        self.attacktype2_group.drop('type2_All', inplace=True)
        self.attacktype3_group.drop('type3_All', inplace=True)
        L = self.region_group.index
        L1 = self.attacktype1_group.index
        La1 = []
        L2 = self.attacktype2_group.index
        La2 = []
        L3 = self.attacktype3_group.index
        La3 = []
        self.Lp = []
        self.La = []
        for x,y in product(L,L1):
            str = '%s%s%s' %(x,'_',y)
            La1.append(str)
        self.La.append(La1)
        self.Lp.extend(La1)
        for x,y in product(L,L2):
            str = '%s%s%s' %(x,'_',y)
            La2.append(str)
        self.La.append(La2)
        self.Lp.extend(La2)
        for x,y in product(L,L3):
            str = '%s%s%s' %(x,'_',y)
            La3.append(str)
        self.La.append(La3)
        self.La.append(L)
        self.Lp.extend(La3)
        self.chart_title = '地区年度恐怖袭击种类数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '4/region_attacktype'

    def set_region_attacktype_group(self):
        self.chart_title = '地区恐怖袭击种类数量占比图'
        self.filename = '4/region_attacktype_group'

    def set_attackwhy(self):
        self.attackwhy = []
        int_log = pd.crosstab(self.data_list.iyear,self.data_list.INT_LOG)
        int_ideo = pd.crosstab(self.data_list.iyear, self.data_list.INT_IDEO)
        int_misc = pd.crosstab(self.data_list.iyear, self.data_list.INT_MISC)
        int_any = pd.crosstab(self.data_list.iyear, self.data_list.INT_ANY)
        int_log.rename(columns={0: 'NOT_INT_LOG:非本地到国际化的', 1: 'INT_LOG:本地到国际化的',-9:'unknown_INT_LOG：未知'}, inplace=True)
        int_ideo.rename(columns={0: 'NOT_INT_IDEO:非意识形态国际化的', 1: 'INT_IDEO:意识形态国际化的',-9:'unknown_INT_IDEO：未知'}, inplace=True)
        int_misc.rename(columns={0: 'NOT_INT_MISC:受害者不是本地的', 1: 'INT_MISC:受害者是本地的',-9:'unknown_INT_MISC：未知'}, inplace=True)
        int_any.rename(columns={0: 'NOT_INT_ANY:非某一方面国际化的', 1: 'INT_ANY:某一方面是国际化的',-9:'unknown_INT_ANY：未知'}, inplace=True)
        self.int_log_group = int_log.sum()
        self.int_ideo_group = int_ideo.sum()
        self.int_misc_group = int_misc.sum()
        self.int_any_group = int_any.sum()
        self.attackwhy_group = pd.concat([self.int_log_group,self.int_ideo_group,self.int_misc_group,self.int_any_group])
        self.attackwhy.append(int_log)
        self.attackwhy.append(int_ideo)
        self.attackwhy.append(int_misc)
        self.attackwhy.append(int_any)
        self.attackwhy.append(self.year_data1)
        self.chart_title = '年度四种恐怖袭击性质数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '5/attackwhy'

    def set_attackwhy_group(self):
        self.chart_title = '四种恐怖袭击性质数量占比图'
        self.filename = '5/attackwhy_group'

    def set_region_attackwhy(self):
        self.region_attackwhy = []
        region_int_log = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt,self.data_list.INT_LOG],dropna=False)
        region_int_ideo = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt,self.data_list.INT_IDEO],dropna=False)
        region_int_misc = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt,self.data_list.INT_MISC],dropna=False)
        region_int_any = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt,self.data_list.INT_ANY],dropna=False)
        region_int_log_group = region_int_log.sum()
        region_int_ideo_group = region_int_ideo.sum()
        region_int_misc_group = region_int_misc.sum()
        region_int_any_group = region_int_any.sum()
        self.region_attackwhy_group = pd.concat([region_int_log_group, region_int_ideo_group, region_int_misc_group, region_int_any_group])
        self.region_attackwhy.append(region_int_log)
        self.region_attackwhy.append(region_int_ideo)
        self.region_attackwhy.append(region_int_misc)
        self.region_attackwhy.append(region_int_any)
        self.region_attackwhy.append(self.region_year2)
        L = self.region_group.index
        L1 = self.int_log_group.index
        La1 = []
        L2 = self.int_ideo_group.index
        La2 = []
        L3 = self.int_misc_group.index
        La3 = []
        L4 = self.int_any_group.index
        La4 = []
        self.Lp = []
        self.La = []
        for x, y in product(L, L1):
            str = '%s%s%s' % (x, '_', y)
            La1.append(str)
        self.La.append(La1)
        self.Lp.extend(La1)
        for x, y in product(L, L2):
            str = '%s%s%s' % (x, '_', y)
            La2.append(str)
        self.La.append(La2)
        self.Lp.extend(La2)
        for x, y in product(L, L3):
            str = '%s%s%s' % (x, '_', y)
            La3.append(str)
        self.La.append(La3)
        self.Lp.extend(La3)
        for x, y in product(L, L4):
            str = '%s%s%s' % (x, '_', y)
            La4.append(str)
        self.La.append(La4)
        self.Lp.extend(La4)
        self.La.append(L)
        self.chart_title = '地区年度四种恐怖袭击性质数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '5/region_attackwhy'

    def set_region_attackwhy_group(self):
        self.chart_title = '地区四种恐怖袭击性质数量占比图'
        self.filename = '5/region_attackwhy_group'

    def set_targtype(self):
        self.targtype = []
        targtype1 = pd.crosstab(self.data_list.iyear,self.data_list.targtype1_txt)
        targtype2 = pd.crosstab(self.data_list.iyear,self.data_list.targtype2_txt)
        targtype3 = pd.crosstab(self.data_list.iyear,self.data_list.targtype3_txt)
        targtype1.rename(columns=lambda x: 'type1_' + x, inplace=True)
        targtype2.rename(columns=lambda x: 'type2_' + x, inplace=True)
        targtype3.rename(columns=lambda x: 'type3_' + x, inplace=True)
        self.targtype1 = targtype1.sum()
        self.targtype2 = targtype2.sum()
        self.targtype3 = targtype3.sum()
        self.targtype_group = pd.concat([self.targtype1, self.targtype2, self.targtype3])
        self.targtype.append(targtype1)
        self.targtype.append(targtype2)
        self.targtype.append(targtype3)
        self.targtype.append(self.year_data1)
        self.chart_title = '年度目标受害者类型数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '6/targtype'

    def set_targtype_group(self):
        self.chart_title = '目标受害者类型数量占比图'
        self.filename = '6/targtype_group'

    def set_region_targtype(self):
        self.region_targtype = []
        region_targtype1 = pd.crosstab(self.data_list.iyear, [self.data_list.region_txt, self.data_list.targtype1_txt],dropna=False)
        region_targtype2 = pd.crosstab(self.data_list.iyear, [self.data_list.region_txt, self.data_list.targtype2_txt],dropna=False)
        region_targtype3 = pd.crosstab(self.data_list.iyear, [self.data_list.region_txt, self.data_list.targtype3_txt],dropna=False)
        region_targtype1_group = region_targtype1.sum()
        region_targtype2_group = region_targtype2.sum()
        region_targtype3_group = region_targtype3.sum()
        self.region_targtype_group = pd.concat([region_targtype1_group, region_targtype2_group, region_targtype3_group])
        self.region_targtype.append(region_targtype1)
        self.region_targtype.append(region_targtype2)
        self.region_targtype.append(region_targtype3)
        self.region_targtype.append(self.region_year2)
        L = self.region_group.index
        L1 = self.targtype1.index
        La1 = []
        L2 = self.targtype2.index
        La2 = []
        L3 = self.targtype3.index
        La3 = []
        self.Lp = []
        self.La = []
        for x, y in product(L, L1):
            str = '%s%s%s' % (x, '_', y)
            La1.append(str)
        self.La.append(La1)
        self.Lp.extend(La1)
        for x, y in product(L, L2):
            str = '%s%s%s' % (x, '_', y)
            La2.append(str)
        self.La.append(La2)
        self.Lp.extend(La2)
        for x, y in product(L, L3):
            str = '%s%s%s' % (x, '_', y)
            La3.append(str)
        self.La.append(La3)
        self.Lp.extend(La3)
        self.La.append(L)
        self.chart_title = '地区年度受害者类型数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '6/region_targtype'

    def set_region_targtype_group(self):
        self.chart_title = '地区受害者类型数量占比图'
        self.filename = '6/region_targtype_group'

    def set_weaptype(self):
        self.weaptype = []
        weaptype1 = pd.crosstab(self.data_list.iyear, self.data_list.weaptype1_txt,margins=True)
        weaptype2 = pd.crosstab(self.data_list.iyear, self.data_list.weaptype2_txt,margins=True)
        weaptype3 = pd.crosstab(self.data_list.iyear, self.data_list.weaptype3_txt,margins=True)
        weaptype4 = pd.crosstab(self.data_list.iyear, self.data_list.weaptype4_txt,margins=True)
        weaptype = weaptype1.add(weaptype2.add(weaptype3.add(weaptype4,fill_value=0), fill_value=0), fill_value=0)
        weaptype1.rename(columns=lambda x: 'type1_' + x, inplace=True)
        weaptype2.rename(columns=lambda x: 'type2_' + x, inplace=True)
        weaptype3.rename(columns=lambda x: 'type3_' + x, inplace=True)
        weaptype4.rename(columns=lambda x: 'type4_' + x, inplace=True)
        weaptype.rename(columns=lambda x: 'All_' + x, inplace=True)
        self.weaptype1 = weaptype1.loc['All']
        self.weaptype2 = weaptype2.loc['All']
        self.weaptype3 = weaptype3.loc['All']
        self.weaptype4 = weaptype4.loc['All']
        weaptype_group = weaptype.loc['All']
        weaptype_group.drop('All_All',inplace=True)
        weaptype1.drop('All',inplace=True)
        weaptype2.drop('All',inplace=True)
        weaptype3.drop('All',inplace=True)
        weaptype4.drop('All',inplace=True)
        weaptype.drop('All',inplace=True)
        self.weaptype_group = pd.concat([self.weaptype1, self.weaptype2, self.weaptype3, self.weaptype4,weaptype_group])
        self.weaptype.append(weaptype1)
        self.weaptype.append(weaptype2)
        self.weaptype.append(weaptype3)
        self.weaptype.append(weaptype4)
        self.weaptype.append(weaptype)
        self.chart_title = '年度袭击武器类型数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '7/weaptype'

    def set_weaptype_group(self):
        self.chart_title = '袭击武器类型数量占比图'
        self.filename = '7/weaptype_group'

    def set_region_weaptype(self):
        self.region_weaptype = []
        region_weaptype1 = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt, self.data_list.weaptype1_txt], dropna=False)
        region_weaptype1_group = region_weaptype1.sum()
        self.region_weaptype.append(region_weaptype1)
        region_weaptype2 = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt, self.data_list.weaptype2_txt], dropna=False)
        region_weaptype2_group = region_weaptype2.sum()
        self.region_weaptype.append(region_weaptype2)
        region_weaptype3 = pd.crosstab(self.data_list.iyear,[self.data_list.region_txt, self.data_list.weaptype3_txt], dropna=False)
        region_weaptype3_group = region_weaptype3.sum()
        self.region_weaptype.append(region_weaptype3)
        region_weaptype4 = pd.crosstab(self.data_list.iyear, [self.data_list.region_txt, self.data_list.weaptype4_txt],dropna=False)
        region_weaptype4_group = region_weaptype4.sum()
        self.region_weaptype.append(region_weaptype4)
        self.region_weaptype.append(self.region_year2)
        self.region_weaptype_group = pd.concat([region_weaptype1_group, region_weaptype2_group, region_weaptype3_group,region_weaptype4_group])
        self.weaptype1.drop('type1_All', inplace=True)
        self.weaptype2.drop('type2_All', inplace=True)
        self.weaptype3.drop('type3_All', inplace=True)
        self.weaptype4.drop('type4_All', inplace=True)
        L = self.region_group.index
        L1 = self.weaptype1.index
        La1 = []
        L2 = self.weaptype2.index
        La2 = []
        L3 = self.weaptype3.index
        La3 = []
        L4 = self.weaptype4.index
        La4 = []
        self.Lp = []
        self.La = []
        for x, y in product(L, L1):
            str = '%s%s%s' % (x, '_', y)
            if len(str)>70:
                str = str[:70]
            La1.append(str)
        self.La.append(La1)
        self.Lp.extend(La1)
        for x, y in product(L, L2):
            str = '%s%s%s' % (x, '_', y)
            if len(str)>70:
                str = str[:70]
            La2.append(str)
        self.La.append(La2)
        self.Lp.extend(La2)
        for x, y in product(L, L3):
            str = '%s%s%s' % (x, '_', y)
            if len(str)>70:
                str = str[:70]
            La3.append(str)
        self.La.append(La3)
        self.Lp.extend(La3)
        for x, y in product(L, L4):
            str = '%s%s%s' % (x, '_', y)
            if len(str)>70:
                str = str[:70]
            La4.append(str)
        self.La.append(La4)
        self.Lp.extend(La4)
        self.La.append(L)
        self.chart_title = '地区年度袭击武器类型数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '7/region_weaptype'

    def set_region_weaptype_group(self):
        self.chart_title = '地区年度袭击武器类型数量占比图'
        self.filename = '7/region_weaptype_group'

    def set_ransompaid(self):
        self.ransompaid_all = self.data_list[self.data_list['ransompaid']>0]
        self.ransompaid = []
        ransompaid = self.ransompaid_all.pivot_table(values='ransompaid',index='iyear',aggfunc='sum',fill_value=0)
        self.ransompaid.append(ransompaid)
        self.ransompaid.append(self.year_data1)
        self.chart_title = '年度已付赎金数量图'
        self.x_name = '年份'
        self.y_name = '已付赎金'
        self.filename = '8/ransompaid'

    def set_region_ransompaid(self):
        self.region_ransompaid = []
        region_ransompaid = self.ransompaid_all.pivot_table(values='ransompaid',index='iyear',columns='region_txt',aggfunc='sum',fill_value=0,margins=True)
        self.region_ransompaid_group = region_ransompaid.loc['All']
        self.region_ransompaid_group.drop('All',inplace=True)
        region_ransompaid.drop('All',inplace=True)
        self.region_ransompaid.append(region_ransompaid)
        self.chart_title = '地区年度已付赎金数量图'
        self.x_name = '年份'
        self.y_name = '已付赎金'
        self.filename = '8/region_ransompaid'

    def set_region_ransompaid_group(self):
        self.chart_title = '地区已付赎金数量图'
        self.filename = '8/region_ransompaid_group'

    def set_hostkidoutcome(self):
        self.hostkidoutcome = []
        hostkidoutcome = pd.crosstab(self.data_list.iyear, self.data_list.hostkidoutcome_txt,margins=True)
        self.hostkidoutcome_group = hostkidoutcome.loc['All']
        self.hostkidoutcome_group.drop('All', inplace=True)
        self.hostkidoutcome_group.rename(columns={'All':'hostkidoutcome_All'},inplace=True)
        hostkidoutcome.drop('All', inplace=True)
        self.hostkidoutcome.append(hostkidoutcome)
        self.chart_title = '年度人质结局数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '8/hostkidoutcome'

    def set_hostkidoutcome_group(self):
        self.chart_title = '人质结局数量占比图'
        self.filename = '8/hostkidoutcome_group'

    def set_region_hostkidoutcome(self):
        self.region_hostkidoutcome = []
        region_hostkidoutcome = pd.crosstab(self.data_list.iyear, [self.data_list.region_txt,self.data_list.hostkidoutcome_txt],dropna=False)
        self.region_hostkidoutcome_group = region_hostkidoutcome.sum()
        self.region_hostkidoutcome.append(region_hostkidoutcome)
        self.region_hostkidoutcome.append(self.region_year2)
        L = self.region_group.index
        L1 = self.hostkidoutcome_group.index
        La1 = []
        self.Lp_a = []
        self.La_a = []
        for x, y in product(L, L1):
            str = '%s%s%s' % (x, '_', y)
            La1.append(str)
        self.La_a.append(La1)
        self.Lp_a.extend(La1)
        self.La_a.append(L)
        self.chart_title = '地区年度人质结局数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量/已付赎金'
        self.filename = '8/region_hostkidoutcome'

    def set_region_hostkidoutcome_group(self):
        self.chart_title = '地区人质结局数量占比图'
        self.filename = '8/region_hostkidoutcome_group'

    def set_ransompaid_hostkidoutcome(self):
        self.ransompaid.extend(self.hostkidoutcome)
        self.chart_title = '年度已付赎金与人质结局对比图'
        self.x_name = '年份'
        self.y_name = '袭击数量/已付赎金'
        self.filename = '8/ransompaid_hostkidoutcome'

    def set_region_ransompaid_hostkidoutcome(self):
        self.region_ransompaid.extend(self.region_hostkidoutcome)
        L = self.region_ransompaid_group.index
        self.La = []
        La1 = []
        for x in L:
            str = '%s%s' % ('paid_', x)
            La1.append(str)
        self.La.append(La1)
        self.La.extend(self.La_a)
        self.chart_title = '地区年度已付赎金与人质结局对比图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '8/region_ransompaid_hostkidoutcome'

    def set_paid_hostkidoutcome(self):
        self.paid_hostkidoutcome = []
        paid_hostkidoutcome = pd.crosstab(self.ransompaid_all.iyear, self.ransompaid_all.hostkidoutcome_txt, margins=True)
        paid_hostkidoutcome.rename(columns=lambda x: 'paid_' + x, inplace=True)
        self.paid_hostkidoutcome_group1 = paid_hostkidoutcome.loc['All']
        self.paid_hostkidoutcome_group1.drop('paid_All', inplace=True)
        self.paid_hostkidoutcome_group = pd.concat([self.paid_hostkidoutcome_group1,self.hostkidoutcome_group])
        paid_hostkidoutcome.drop('All', inplace=True)
        self.paid_hostkidoutcome.append(paid_hostkidoutcome)
        self.paid_hostkidoutcome.extend(self.hostkidoutcome)
        self.chart_title = '已付赎金中年度人质结局数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '8/paid_hostkidoutcome'

    def set_paid_hostkidoutcome_group(self):
        self.chart_title = '已付赎金中人质结局数量占比图'
        self.filename = '8/paid_hostkidoutcome_group'

    def set_region_paid_hostkidoutcome(self):
        self.region_paid_hostkidoutcome = []
        region_paid_hostkidoutcome = pd.crosstab(self.ransompaid_all.iyear, [self.ransompaid_all.region_txt,self.ransompaid_all.hostkidoutcome_txt],dropna=False)
        region_paid_hostkidoutcome_group = region_paid_hostkidoutcome.sum()
        self.region_paid_hostkidoutcome_group = pd.concat([region_paid_hostkidoutcome_group,self.region_hostkidoutcome_group])
        self.region_paid_hostkidoutcome.append(region_paid_hostkidoutcome)
        self.region_paid_hostkidoutcome.extend(self.region_hostkidoutcome)
        self.region_paid_hostkidoutcome.append(self.region_year2)
        L = self.region_group.index
        L1 = self.paid_hostkidoutcome_group1.index
        La1 = []
        La2 = []
        self.Lp = []
        self.La = []
        for x, y in product(L, L1):
            str = '%s%s%s' % (x, '_', y)
            La1.append(str)
        self.La.append(La1)
        self.Lp.extend(La1)
        self.La.extend(self.La_a)
        self.Lp.extend(self.Lp_a)
        self.chart_title = '已付赎金中地区年度人质结局数量图'
        self.x_name = '年份'
        self.y_name = '袭击数量'
        self.filename = '8/region_paid_hostkidoutcome'

    def set_region_paid_hostkidoutcome_group(self):
        self.chart_title = '已付赎金中地区人质结局数量占比图'
        self.filename = '8/region_paid_hostkidoutcome_group'