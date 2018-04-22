import pandas as pd
from itertools import product
import chart
#数据处理
class datadel(object):
    def __init__(self,filename):
        self.data_list = pd.read_table(filename,engine='python',sep=',')
        self.mapdata =None
        self.year_group = None#UI need
        self.month_group = None#UI need
        self.YEAR = False
        self.MONTH = False
        self.set_year()
        self.set_month()

    def make_chart(self):
        self.set_mapdata()
        self.set_year_mapdata()
        self.set_year_data()
        self.set_month_data()
        self.set_region_year()
        self.set_region_month()
        self.set_year_region()
        self.set_month_region()
        self.set_country_year()
        self.set_country_month()
        self.set_year_nkill_nwound()
        self.set_region_year_nkill_nwound()
        self.set_gname()
        self.set_success()
        self.set_region_success()
        self.set_suicide()
        self.set_region_suicide()
        self.set_attacktype()
        self.set_region_attacktype()
        self.set_extended()
        self.set_region_extended()
        self.set_attackwhy()
        self.set_region_attackwhy()
        self.set_targtype()
        self.set_region_targtype()
        self.set_weaptype()
        self.set_region_weaptype()
        self.set_ransompaid()
        self.set_region_ransompaid()
        self.set_hostkidoutcome()
        self.set_region_hostkidoutcome()
        self.set_ransompaid_hostkidoutcome()
        self.set_region_ransompaid_hostkidoutcome()
        self.set_paid_hostkidoutcome()
        self.set_region_paid_hostkidoutcome()

    def de_bar_line(self,a1,a2,a3,a4):
        try:
            L = []
            data = pd.crosstab(self.data_list[a1],self.data_list[a2])
            L.append(data)
            chart_title = '%s%s%s' % (a3,a4,'数量图')
            chart.make_bar_linechart(L, chart_title, a3, a4, '9/define_')
        except:
            pass

    def de_pie(self,a1,a3):
        try:
            data = self.data_list[a1].values
            group = pd.value_counts(data, sort=False)
            chart_title = '%s%s'%(a3,'占比图')
            chart.make_pie_charts(group, chart_title, '9/define_')
        except:
            pass

    def set_year(self):
        try:
            yeardata = self.data_list['iyear'].values
            self.year_group = pd.value_counts(yeardata, sort=False)
            self.YEAR = True
        except:
            pass

    def set_month(self):
        try:
            month = self.data_list['imonth'].values
            self.month_group = pd.value_counts(month, sort=False)
            self.month_group.drop(0, inplace=True)
            self.MONTH = True
        except:
            pass

    # 大地图数据的封装:经纬度、国家、死亡总数、发生袭击的次数，1-1
    def set_mapdata(self):
        try:
            self.mapdata = self.data_list[self.data_list['specificity'] != 5]
            mapdata = self.mapdata[['country_txt', 'latitude', 'longitude', 'nkill']]
            mapdata['count'] = 1
            latlonggroup = mapdata.groupby(['country_txt', 'latitude', 'longitude']).sum().reset_index()
            latdata = latlonggroup['latitude']
            londata = latlonggroup['longitude']
            loctext = latlonggroup[['country_txt', 'nkill', 'count']]
            blat = latdata.values
            blon = londata.values
            btext = loctext.values
            chart.make_mapchart(blat, blon, btext)
        except:
            pass
    # 每年地图数据的封装：经纬度、国家、第一恐怖组织名称、该年死亡总数1-2
    def set_year_mapdata(self):
        try:
            yearmapdata = self.mapdata[['iyear', 'country_txt', 'latitude', 'longitude', 'gname', 'nkill']]
            latlonggroup_year = yearmapdata.groupby('iyear')
            for name, group in latlonggroup_year:
                latdata = group['latitude']
                londata = group['longitude']
                loctext = group[['country_txt', 'gname', 'nkill']]
                yfilename = '%s%s%s' % ('html/0/', str(name), 'map.html')
                ylat = latdata.values
                ylon = londata.values
                ytext = loctext.values
                chart.make_mapchart(ylat, ylon, ytext, yfilename, name)
        except:
            pass

    def set_year_data(self):
        try:
            year_data = []
            year_all = {'All_events': self.year_group}
            self.year_data1 = pd.DataFrame(year_all)
            year_data.append(self.year_data1)
            chart.make_bar_linechart(year_data, '年度恐怖袭击数量图', '年份', '恐怖袭击次数', '1/year_data')
            chart.make_pie_charts(self.year_group, '年度恐怖袭击数量占比图', '1/year_group')
        except:
            pass

    def set_month_data(self):
        try:
            month_data = []
            month_all = {'All': self.month_group}
            month_data1 = pd.DataFrame(month_all)
            month_data.append(month_data1)
            chart.make_bar_linechart(month_data, '月份恐怖袭击数量图', '月份', '恐怖袭击次数', '1/month_data')
            chart.make_pie_charts(self.month_group, '月份恐怖袭击数量占比图', '1/month_group')
        except:
            pass
    #def set_month_group(self):

    def set_region_year(self):
        try:
            region_year = []
            self.region_year1 = pd.crosstab(self.data_list.iyear, self.data_list.region_txt, margins=True)
            self.region_group = self.region_year1.loc['All']
            self.region_group.drop('All', inplace=True)
            self.region_year2 = self.region_year1.drop('All')
            region_year.append(self.region_year2)
            chart.make_bar_linechart(region_year, '地区年度恐怖袭击数量图', '年份', '恐怖袭击次数', '1/region_year')
            chart.make_pie_charts(self.region_group, '地区恐怖袭击数量占比图', '1/region_group')
        except:
            pass

    def set_region_month(self):
        try:
            region_month = []
            self.region_month1 = pd.crosstab(self.data_list.imonth, self.data_list.region_txt, margins=True)
            self.region_month1.drop(0, inplace=True)
            self.region_month1.drop('All', inplace=True)
            region_month.append(self.region_month1)
            chart.make_bar_linechart(region_month, '地区月份恐怖袭击数量图', '月份', '恐怖袭击次数', '1/region_month')
        except:
            pass
    #def set_region_group(self):

    # 按年份查看各个地区数量比例，饼图 2-8
    def set_year_region(self):
        try:
            for index in self.year_group.index:
                year_region = self.region_year2.loc[index]
                chart_title = '%s%s' % (index, '年度地区恐怖袭击数量占比图')
                filename = '%s%s%s' % ('1/', index, '_region')
                chart.make_pie_charts(year_region, chart_title, filename)
        except:
            pass

    # 按月份查看各个地区数量比例，饼图 2-8
    def set_month_region(self):
        try:
            for index in self.month_group.index:
                month_region = self.region_month1.loc[index]
                chart_title = '%s%s' % (index, '月份地区恐怖袭击数量占比图')
                filename = '%s%s%s' % ('1/', index, '_region')
                chart.make_pie_charts(month_region, chart_title, filename)
        except:
            pass

    def set_country_year(self):
        try:
            country_year = []
            country_year1 = pd.crosstab(self.data_list.iyear, self.data_list.country_txt, margins=True)
            country_group = country_year1.loc['All']
            country_group.drop('All', inplace=True)
            country_year1.drop('All', inplace=True)
            country_year.append(country_year1)
            chart.make_bar_linechart(country_year, '国家年度恐怖袭击数量图', '年份', '恐怖袭击次数', '1/country_year')
            chart.make_pie_charts(country_group, '国家恐怖袭击数量占比图', '1/country_group')
        except:
            pass

    def set_country_month(self):
        try:
            country_month = []
            country_month1 = pd.crosstab(self.data_list.imonth, self.data_list.country_txt, margins=True)
            country_month1.drop(0, inplace=True)
            country_month1.drop('All', inplace=True)
            country_month.append(country_month1)
            chart.make_bar_linechart(country_month, '国家月份恐怖袭击数量图', '月份', '恐怖袭击次数', '1/country_month')
        except:
            pass

    #年度伤亡人数统计图（柱状图，折线图）3-1、3-2
    def set_year_nkill_nwound(self):
        try:
            year_nkill_nwound = []
            year_nkill_nwound1 = self.data_list.pivot_table(values=['nkill', 'nwound'], index='iyear', aggfunc='sum',
                                                            fill_value=0, margins=True)
            year_nkill_nwound_group = year_nkill_nwound1.loc['All']
            year_nkill_nwound1.drop('All', inplace=True)
            year_nkill_nwound.append(year_nkill_nwound1)
            year_nkill_nwound.append(self.year_data1)
            chart.make_bar_linechart(year_nkill_nwound, '年度伤亡人数统计图', '年份', '死(nkill)/伤(nwound)人数',
                                     '2/year_nkill_nwound')
            chart.make_pie_charts(year_nkill_nwound_group, '年度伤亡人数占比图', '2/year_nkill_nwound_group')
        except:
            pass

    #def set_year_nkill_nwound_group(self):

    #按地区查看年度伤亡人数（柱状图，折线图）3-3、3-4、3-7、3-8
    def set_region_year_nkill_nwound(self):
        try:
            region_year_nkill_nwound = []
            region_year_nkill = self.data_list.pivot_table(values='nkill', index='iyear', columns='region_txt',
                                                           aggfunc='sum', fill_value=0, margins=True)
            region_year_nwound = self.data_list.pivot_table(values='nwound', index='iyear', columns='region_txt',
                                                            aggfunc='sum', fill_value=0, margins=True)
            region_year_nkill_nwound1 = region_year_nkill.add(region_year_nwound)
            region_year_nkill.rename(columns=lambda x: 'nkill_' + x, inplace=True)
            region_year_nwound.rename(columns=lambda x: 'nwound_' + x, inplace=True)
            region_year_nkill_nwound1.rename(columns=lambda x: 'nkill_nwound_' + x, inplace=True)

            region_nkill = region_year_nkill.loc['All']
            region_nwound = region_year_nwound.loc['All']
            region_nkill_nwound = region_year_nkill_nwound1.loc['All']
            region_nkill_nwound.drop('nkill_nwound_All', inplace=True)

            region_year_nkill.drop('All', inplace=True)
            region_year_nwound.drop('All', inplace=True)
            region_year_nkill_nwound1.drop('All', inplace=True)

            region_nkill_nwound_group = pd.concat([region_nkill, region_nwound, region_nkill_nwound])
            region_year_nkill_nwound.append(region_year_nkill)
            region_year_nkill_nwound.append(region_year_nwound)
            region_year_nkill_nwound.append(region_year_nkill_nwound1)
            region_year_nkill_nwound.append(self.region_year2)
            chart.make_bar_linechart(region_year_nkill_nwound, '地区年度伤亡人数统计图', '年份', '死(nkill)/伤(nwound)人数',
                                     '2/region_year_nkill_nwound')
            chart.make_pie_charts(region_nkill_nwound_group, '地区伤亡人数占比图', '2/region_nkill_nwound')
        except:
            pass
    #各地区伤亡总人数比例-饼图3-5，3-6
    #def set_region_nkill_nwound(self):

    #各个恐怖组织年度袭击数量，数量太多,4-1
    def set_gname(self):
        try:
            gname = pd.crosstab(self.data_list.gname, self.data_list.iyear, margins=True)
            if len(gname.index) > 800:
                gname = gname[gname.All > 5]
            gname_group = gname.All
            gname_group.drop('All', inplace=True)
            gname.drop('All', axis=1, inplace=True)
            chart.make_nbarchart(gname, '恐怖组织年度袭击数量图', '年份', '袭击数量', '3/gname')
            chart.make_nline_plots(gname, '恐怖组织年度袭击数量图', '年份', '袭击数量', '3/gname')
            chart.make_pie_charts(gname_group, '恐怖组织袭击数量占比图', '3/gname_group')
        except:
            pass

    #各个恐怖组织袭击数量占比饼图
    #def set_gname_group(self):

    #袭击成败年度数量,5-1
    def set_success(self):
        try:
            success = []
            success1 = pd.crosstab(self.data_list.iyear, self.data_list.success, margins=True)
            success1.rename(columns={0: 'fail', 1: 'success'}, inplace=True)
            success_group = success1.loc['All']
            success_group.drop('All', inplace=True)
            success1.drop('All', inplace=True)
            success.append(success1)
            chart.make_bar_linechart(success, '袭击成败年度数量图', '年份', '袭击数量', '4/success')
            chart.make_pie_charts(success_group, '袭击成败数量占比图', '4/success_group')
        except:
            pass

    #按地区查看袭击成败年度数量,列名待重置,5-2,5-4
    def set_region_success(self):
        try:
            region_success = []
            region_success1 = self.data_list.pivot_table(values='success', index='iyear', columns='region_txt',
                                                         aggfunc='sum', fill_value=0, margins=True)
            region_fail = self.region_year1.sub(region_success1, fill_value=0)
            region_success1.rename(columns=lambda x: 'success_' + x, inplace=True)
            region_fail.rename(columns=lambda x: 'fail_' + x, inplace=True)
            region_success_group1 = region_success1.loc['All']
            region_fail_group = region_fail.loc['All']
            region_success1.drop('All', inplace=True)
            region_fail.drop('All', inplace=True)

            region_success_group = pd.concat([region_success_group1, region_fail_group, self.region_group])
            region_success.append(region_success1)
            region_success.append(region_fail)
            region_success.append(self.region_year2)

            chart.make_bar_linechart(region_success, '地区年度袭击成败数量图', '年份', '袭击数量', '4/region_success')
            chart.make_pie_charts(region_success_group, '地区袭击成败占比图', '4/region_success_group')
        except:
            pass
    #查看地区成败数量占比饼状图,5-3
    #def set_region_success_group(self):

    # 自杀式袭击年度数量,列名待重置,5-5
    def set_suicide(self):
        try:
            suicide = []
            suicide1 = pd.crosstab(self.data_list.iyear, self.data_list.suicide, margins=True)
            suicide1.rename(columns={0: 'suicide', 1: 'other'}, inplace=True)
            suicide_group = suicide1.loc['All']
            suicide_group.drop('All', inplace=True)
            suicide1.drop('All', inplace=True)
            suicide.append(suicide1)
            chart.make_bar_linechart(suicide, '自杀式年度数量统计图', '年份', '袭击数量', '4/suicide')
            chart.make_pie_charts(suicide_group, '自杀式数量占比图', '4/suicide_group')
        except:
            pass

    # 按地区查看自杀式袭击的年度数量,列名待重置,5-6,5-8
    def set_region_suicide(self):
        try:
            region_suicide = []
            region_suicide1 = self.data_list.pivot_table(values='suicide', index='iyear', columns='region_txt',
                                                         aggfunc='sum', fill_value=0, margins=True)
            region_other = self.region_year1.sub(region_suicide1, fill_value=0)
            region_suicide1.rename(columns=lambda x: 'suicide_' + x, inplace=True)
            region_other.rename(columns=lambda x: 'other_' + x, inplace=True)
            region_suicide_group1 = region_suicide1.loc['All']
            region_other_group = region_other.loc['All']
            region_suicide1.drop('All', inplace=True)
            region_other.drop('All', inplace=True)

            region_suicide_group = pd.concat([region_suicide_group1, region_other_group, self.region_group])
            region_suicide.append(region_suicide1)
            region_suicide.append(region_other)
            region_suicide.append(self.region_year2)
            chart.make_bar_linechart(region_suicide, '地区年度自杀式袭击数量图', '年份', '袭击数量', '4/region_suicide')
            chart.make_pie_charts(region_suicide_group, '地区自杀式袭击占比图', '4/region_suicide_group')
        except:
            pass

    # 查看地区自杀式袭击数量占比饼状图,5-7
    #def set_region_suicide_group(self):

    #年度袭击种类数量图，5-10
    def set_attacktype(self):
        try:
            attacktype = []
            attacktype1 = pd.crosstab(self.data_list.iyear, self.data_list.attacktype1_txt, margins=True)
            attacktype2 = pd.crosstab(self.data_list.iyear, self.data_list.attacktype2_txt, margins=True)
            attacktype3 = pd.crosstab(self.data_list.iyear, self.data_list.attacktype3_txt, margins=True)
            attacktype4 = attacktype1.add(attacktype2.add(attacktype3, fill_value=0), fill_value=0)
            attacktype1.rename(columns=lambda x: 'type1_' + x, inplace=True)
            attacktype2.rename(columns=lambda x: 'type2_' + x, inplace=True)
            attacktype3.rename(columns=lambda x: 'type3_' + x, inplace=True)
            attacktype4.rename(columns=lambda x: 'All_' + x, inplace=True)
            self.attacktype1_group = attacktype1.loc['All']
            self.attacktype2_group = attacktype2.loc['All']
            self.attacktype3_group = attacktype3.loc['All']
            attacktype_group1 = attacktype4.loc['All']
            attacktype_group1.drop('All_All', inplace=True)
            attacktype1.drop('All', inplace=True)
            attacktype2.drop('All', inplace=True)
            attacktype3.drop('All', inplace=True)
            attacktype4.drop('All', inplace=True)

            attacktype_group = pd.concat(
                [self.attacktype1_group, self.attacktype2_group, self.attacktype3_group, attacktype_group1])
            attacktype.append(attacktype1)
            attacktype.append(attacktype2)
            attacktype.append(attacktype3)
            attacktype.append(attacktype4)
            chart.make_bar_linechart(attacktype, '年度恐怖袭击种类数量图', '年份', '袭击数量', '4/attacktype')
            chart.make_pie_charts(attacktype_group, '年度恐怖袭击种类占比图', '4/attacktype_group')
        except:
            pass
    #def set_attacktype_group(self):

    def set_region_attacktype(self):
        try:
            region_attacktype = []
            region_attacktype1 = pd.crosstab(self.data_list.iyear,
                                             [self.data_list.region_txt, self.data_list.attacktype1_txt], dropna=False)
            region_attacktype1_group = region_attacktype1.sum()
            region_attacktype.append(region_attacktype1)
            region_attacktype2 = pd.crosstab(self.data_list.iyear,
                                             [self.data_list.region_txt, self.data_list.attacktype2_txt], dropna=False)
            region_attacktype2_group = region_attacktype2.sum()
            region_attacktype.append(region_attacktype2)
            region_attacktype3 = pd.crosstab(self.data_list.iyear,
                                             [self.data_list.region_txt, self.data_list.attacktype3_txt], dropna=False)
            region_attacktype3_group = region_attacktype3.sum()
            region_attacktype.append(region_attacktype3)
            region_attacktype.append(self.region_year2)
            region_attacktype_group = pd.concat(
                [region_attacktype1_group, region_attacktype2_group, region_attacktype3_group])
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
            Lp = []
            La = []
            for x, y in product(L, L1):
                str = '%s%s%s' % (x, '_', y)
                La1.append(str)
            La.append(La1)
            Lp.extend(La1)
            for x, y in product(L, L2):
                str = '%s%s%s' % (x, '_', y)
                La2.append(str)
            La.append(La2)
            Lp.extend(La2)
            for x, y in product(L, L3):
                str = '%s%s%s' % (x, '_', y)
                La3.append(str)
            La.append(La3)
            La.append(L)
            Lp.extend(La3)
            chart.make_bar_linechart1(region_attacktype, '地区年度恐怖袭击种类数量图', '年份', '袭击数量', '4/region_attacktype', La)
            chart.make_pie_charts1(region_attacktype_group, Lp, '地区恐怖袭击种类数量占比图', '4/region_attacktype_group')
        except:
            pass
    #def set_region_attacktype_group(self):

    # 统计每年持续超过24小时的袭击次数比（柱状图、折线图）2-2
    def set_extended(self):
        try:
            extended = []
            extended1 = pd.crosstab(self.data_list.iyear, self.data_list.extended, margins=True)
            extended1.rename(columns={0: 'not_extended', 1: 'extended'}, inplace=True)
            extended_group = extended1.loc['All']
            extended_group.drop('All', inplace=True)
            extended1.drop('All', inplace=True)
            extended.append(extended1)
            chart.make_bar_linechart(extended, '年度是否持续超过24小时的袭击次数图', '年份', '袭击数量', '4/extended')
            chart.make_pie_charts(extended_group, '是否持续超过24小时的袭击次数占比图', '4/extended_group')
        except:
            pass

    # 按地区查看每年持续超过24小时的袭击次数比（柱状图、折线图）2-4、2-6
    def set_region_extended(self):
        try:
            region_extended = []
            region_extended1 = self.data_list.pivot_table(values='extended', index='iyear', columns='region_txt',
                                                          aggfunc='sum', fill_value=0, margins=True)
            region_not_extended = self.region_year1.sub(region_extended1, fill_value=0)
            region_extended1.rename(columns=lambda x: 'extended_' + x, inplace=True)
            region_not_extended.rename(columns=lambda x: 'not_extended_' + x, inplace=True)
            region_extended_group1 = region_extended1.loc['All']
            region_fail_group = region_not_extended.loc['All']
            region_extended1.drop('All', inplace=True)
            region_not_extended.drop('All', inplace=True)

            region_extended_group = pd.concat([region_extended_group1, region_fail_group, self.region_group])
            region_extended.append(region_extended1)
            region_extended.append(region_not_extended)
            region_extended.append(self.region_year2)
            chart.make_bar_linechart(region_extended, '地区年度是否持续超过24小时的袭击次数图', '年份', '袭击数量', '4/region_extended')
            chart.make_pie_charts(region_extended_group, '地区是否持续超过24小时的袭击次数占比图', '4/region_extended_group')
        except:
            pass
    #def set_region_extended_group(self):

    def set_attackwhy(self):
        try:
            attackwhy = []
            int_log = pd.crosstab(self.data_list.iyear, self.data_list.INT_LOG)
            int_ideo = pd.crosstab(self.data_list.iyear, self.data_list.INT_IDEO)
            int_misc = pd.crosstab(self.data_list.iyear, self.data_list.INT_MISC)
            int_any = pd.crosstab(self.data_list.iyear, self.data_list.INT_ANY)
            int_log.rename(columns={0: 'NOT_INT_LOG:非本地到国际化的', 1: 'INT_LOG:本地到国际化的', -9: 'unknown_INT_LOG：未知'},
                           inplace=True)
            int_ideo.rename(columns={0: 'NOT_INT_IDEO:非意识形态国际化的', 1: 'INT_IDEO:意识形态国际化的', -9: 'unknown_INT_IDEO：未知'},
                            inplace=True)
            int_misc.rename(columns={0: 'NOT_INT_MISC:受害者不是本地的', 1: 'INT_MISC:受害者是本地的', -9: 'unknown_INT_MISC：未知'},
                            inplace=True)
            int_any.rename(columns={0: 'NOT_INT_ANY:非某一方面国际化的', 1: 'INT_ANY:某一方面是国际化的', -9: 'unknown_INT_ANY：未知'},
                           inplace=True)
            self.int_log_group = int_log.sum()
            self.int_ideo_group = int_ideo.sum()
            self.int_misc_group = int_misc.sum()
            self.int_any_group = int_any.sum()
            attackwhy_group = pd.concat(
                [self.int_log_group, self.int_ideo_group, self.int_misc_group, self.int_any_group])
            attackwhy.append(int_log)
            attackwhy.append(int_ideo)
            attackwhy.append(int_misc)
            attackwhy.append(int_any)
            attackwhy.append(self.year_data1)
            chart.make_bar_linechart(attackwhy, '年度四种恐怖袭击性质数量图', '年份', '袭击数量', '5/attackwhy')
            chart.make_pie_charts(attackwhy_group, '四种恐怖袭击性质数量占比图', '5/attackwhy_group')
        except:
            pass
    #def set_attackwhy_group(self):

    def set_region_attackwhy(self):
        try:
            region_attackwhy = []
            region_int_log = pd.crosstab(self.data_list.iyear, [self.data_list.region_txt, self.data_list.INT_LOG],
                                         dropna=False)
            region_int_ideo = pd.crosstab(self.data_list.iyear, [self.data_list.region_txt, self.data_list.INT_IDEO],
                                          dropna=False)
            region_int_misc = pd.crosstab(self.data_list.iyear, [self.data_list.region_txt, self.data_list.INT_MISC],
                                          dropna=False)
            region_int_any = pd.crosstab(self.data_list.iyear, [self.data_list.region_txt, self.data_list.INT_ANY],
                                         dropna=False)
            region_int_log_group = region_int_log.sum()
            region_int_ideo_group = region_int_ideo.sum()
            region_int_misc_group = region_int_misc.sum()
            region_int_any_group = region_int_any.sum()
            region_attackwhy_group = pd.concat(
                [region_int_log_group, region_int_ideo_group, region_int_misc_group, region_int_any_group])
            region_attackwhy.append(region_int_log)
            region_attackwhy.append(region_int_ideo)
            region_attackwhy.append(region_int_misc)
            region_attackwhy.append(region_int_any)
            region_attackwhy.append(self.region_year2)
            L = self.region_group.index
            L1 = self.int_log_group.index
            La1 = []
            L2 = self.int_ideo_group.index
            La2 = []
            L3 = self.int_misc_group.index
            La3 = []
            L4 = self.int_any_group.index
            La4 = []
            Lp = []
            La = []
            for x, y in product(L, L1):
                str = '%s%s%s' % (x, '_', y)
                La1.append(str)
            La.append(La1)
            Lp.extend(La1)
            for x, y in product(L, L2):
                str = '%s%s%s' % (x, '_', y)
                La2.append(str)
            La.append(La2)
            Lp.extend(La2)
            for x, y in product(L, L3):
                str = '%s%s%s' % (x, '_', y)
                La3.append(str)
            La.append(La3)
            Lp.extend(La3)
            for x, y in product(L, L4):
                str = '%s%s%s' % (x, '_', y)
                La4.append(str)
            La.append(La4)
            Lp.extend(La4)
            La.append(L)
            chart.make_bar_linechart1(region_attackwhy, '地区年度四种恐怖袭击性质数量图', '年份', '袭击数量', '5/region_attackwhy', La)
            chart.make_pie_charts1(region_attackwhy_group, Lp, '地区四种恐怖袭击性质数量占比图', '5/region_attackwhy_group')
        except:
            pass
    #def set_region_attackwhy_group(self):

    def set_targtype(self):
        try:
            targtype = []
            targtype1 = pd.crosstab(self.data_list.iyear, self.data_list.targtype1_txt)
            targtype2 = pd.crosstab(self.data_list.iyear, self.data_list.targtype2_txt)
            targtype3 = pd.crosstab(self.data_list.iyear, self.data_list.targtype3_txt)
            targtype1.rename(columns=lambda x: 'type1_' + x, inplace=True)
            targtype2.rename(columns=lambda x: 'type2_' + x, inplace=True)
            targtype3.rename(columns=lambda x: 'type3_' + x, inplace=True)
            self.targtype1 = targtype1.sum()
            self.targtype2 = targtype2.sum()
            self.targtype3 = targtype3.sum()
            targtype_group = pd.concat([self.targtype1, self.targtype2, self.targtype3])
            targtype.append(targtype1)
            targtype.append(targtype2)
            targtype.append(targtype3)
            targtype.append(self.year_data1)
            chart.make_bar_linechart(targtype, '年度目标受害者类型数量图', '年份', '袭击数量', '6/targtype')
            chart.make_pie_charts(targtype_group, '目标受害者类型数量占比图', '6/targtype_group')
        except:
            pass
    #def set_targtype_group(self):

    def set_region_targtype(self):
        try:
            region_targtype = []
            region_targtype1 = pd.crosstab(self.data_list.iyear,
                                           [self.data_list.region_txt, self.data_list.targtype1_txt], dropna=False)
            region_targtype2 = pd.crosstab(self.data_list.iyear,
                                           [self.data_list.region_txt, self.data_list.targtype2_txt], dropna=False)
            region_targtype3 = pd.crosstab(self.data_list.iyear,
                                           [self.data_list.region_txt, self.data_list.targtype3_txt], dropna=False)
            region_targtype1_group = region_targtype1.sum()
            region_targtype2_group = region_targtype2.sum()
            region_targtype3_group = region_targtype3.sum()
            region_targtype_group = pd.concat([region_targtype1_group, region_targtype2_group, region_targtype3_group])
            region_targtype.append(region_targtype1)
            region_targtype.append(region_targtype2)
            region_targtype.append(region_targtype3)
            region_targtype.append(self.region_year2)
            L = self.region_group.index
            L1 = self.targtype1.index
            La1 = []
            L2 = self.targtype2.index
            La2 = []
            L3 = self.targtype3.index
            La3 = []
            Lp = []
            La = []
            for x, y in product(L, L1):
                str = '%s%s%s' % (x, '_', y)
                La1.append(str)
            La.append(La1)
            Lp.extend(La1)
            for x, y in product(L, L2):
                str = '%s%s%s' % (x, '_', y)
                La2.append(str)
            La.append(La2)
            Lp.extend(La2)
            for x, y in product(L, L3):
                str = '%s%s%s' % (x, '_', y)
                La3.append(str)
            La.append(La3)
            Lp.extend(La3)
            La.append(L)
            chart.make_bar_linechart1(region_targtype, '地区年度受害者类型数量图', '年份', '袭击数量', '6/region_targtype', La)
            chart.make_pie_charts1(region_targtype_group, Lp, '地区受害者类型数量占比图', '6/region_targtype_group')
        except:
            pass
    #def set_region_targtype_group(self):

    def set_weaptype(self):
        try:
            weaptype = []
            weaptype1 = pd.crosstab(self.data_list.iyear, self.data_list.weaptype1_txt, margins=True)
            weaptype2 = pd.crosstab(self.data_list.iyear, self.data_list.weaptype2_txt, margins=True)
            weaptype3 = pd.crosstab(self.data_list.iyear, self.data_list.weaptype3_txt, margins=True)
            weaptype4 = pd.crosstab(self.data_list.iyear, self.data_list.weaptype4_txt, margins=True)
            weaptype5 = weaptype1.add(weaptype2.add(weaptype3.add(weaptype4, fill_value=0), fill_value=0), fill_value=0)
            weaptype1.rename(columns=lambda x: 'type1_' + x, inplace=True)
            weaptype2.rename(columns=lambda x: 'type2_' + x, inplace=True)
            weaptype3.rename(columns=lambda x: 'type3_' + x, inplace=True)
            weaptype4.rename(columns=lambda x: 'type4_' + x, inplace=True)
            weaptype5.rename(columns=lambda x: 'All_' + x, inplace=True)
            self.weaptype1 = weaptype1.loc['All']
            self.weaptype2 = weaptype2.loc['All']
            self.weaptype3 = weaptype3.loc['All']
            self.weaptype4 = weaptype4.loc['All']
            weaptype_group1 = weaptype5.loc['All']
            weaptype_group1.drop('All_All', inplace=True)
            weaptype1.drop('All', inplace=True)
            weaptype2.drop('All', inplace=True)
            weaptype3.drop('All', inplace=True)
            weaptype4.drop('All', inplace=True)
            weaptype5.drop('All', inplace=True)
            weaptype_group = pd.concat(
                [self.weaptype1, self.weaptype2, self.weaptype3, self.weaptype4, weaptype_group1])
            weaptype.append(weaptype1)
            weaptype.append(weaptype2)
            weaptype.append(weaptype3)
            weaptype.append(weaptype4)
            weaptype.append(weaptype5)
            chart.make_bar_linechart(weaptype, '年度袭击武器类型数量图', '年份', '袭击数量', '7/weaptype')
            chart.make_pie_charts(weaptype_group, '袭击武器类型数量占比图', '7/weaptype_group')
        except:
            pass
    #def set_weaptype_group(self):

    def set_region_weaptype(self):
        try:
            region_weaptype = []
            region_weaptype1 = pd.crosstab(self.data_list.iyear,
                                           [self.data_list.region_txt, self.data_list.weaptype1_txt], dropna=False)
            region_weaptype1_group = region_weaptype1.sum()
            region_weaptype.append(region_weaptype1)
            region_weaptype2 = pd.crosstab(self.data_list.iyear,
                                           [self.data_list.region_txt, self.data_list.weaptype2_txt], dropna=False)
            region_weaptype2_group = region_weaptype2.sum()
            region_weaptype.append(region_weaptype2)
            region_weaptype3 = pd.crosstab(self.data_list.iyear,
                                           [self.data_list.region_txt, self.data_list.weaptype3_txt], dropna=False)
            region_weaptype3_group = region_weaptype3.sum()
            region_weaptype.append(region_weaptype3)
            region_weaptype4 = pd.crosstab(self.data_list.iyear,
                                           [self.data_list.region_txt, self.data_list.weaptype4_txt], dropna=False)
            region_weaptype4_group = region_weaptype4.sum()
            region_weaptype.append(region_weaptype4)
            region_weaptype.append(self.region_year2)
            region_weaptype_group = pd.concat(
                [region_weaptype1_group, region_weaptype2_group, region_weaptype3_group, region_weaptype4_group])
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
            Lp = []
            La = []
            for x, y in product(L, L1):
                str = '%s%s%s' % (x, '_', y)
                if len(str) > 70:
                    str = str[:70]
                La1.append(str)
            La.append(La1)
            Lp.extend(La1)
            for x, y in product(L, L2):
                str = '%s%s%s' % (x, '_', y)
                if len(str) > 70:
                    str = str[:70]
                La2.append(str)
            La.append(La2)
            Lp.extend(La2)
            for x, y in product(L, L3):
                str = '%s%s%s' % (x, '_', y)
                if len(str) > 70:
                    str = str[:70]
                La3.append(str)
            La.append(La3)
            Lp.extend(La3)
            for x, y in product(L, L4):
                str = '%s%s%s' % (x, '_', y)
                if len(str) > 70:
                    str = str[:70]
                La4.append(str)
            La.append(La4)
            Lp.extend(La4)
            La.append(L)
            chart.make_bar_linechart1(region_weaptype, '地区年度袭击武器类型数量图', '年份', '袭击数量', '7/region_weaptype', La)
            chart.make_pie_charts1(region_weaptype_group, Lp, '地区袭击武器类型数量占比图', '7/region_weaptype_group')
        except:
            pass
    #def set_region_weaptype_group(self):

    def set_ransompaid(self):
        try:
            self.ransompaid_all = self.data_list[self.data_list['ransompaid'] > 0]
            self.ransompaid = []
            ransompaid = self.ransompaid_all.pivot_table(values='ransompaid', index='iyear', aggfunc='sum',
                                                         fill_value=0)
            self.ransompaid.append(ransompaid)
            self.ransompaid.append(self.year_data1)
            chart.make_bar_linechart(self.ransompaid, '年度已付赎金数量图', '年份', '已付赎金', '8/ransompaid')
        except:
            pass


    def set_region_ransompaid(self):
        try:
            self.region_ransompaid = []
            region_ransompaid = self.ransompaid_all.pivot_table(values='ransompaid', index='iyear',
                                                                columns='region_txt', aggfunc='sum', fill_value=0,
                                                                margins=True)
            self.region_ransompaid_group = region_ransompaid.loc['All']
            self.region_ransompaid_group.drop('All', inplace=True)
            region_ransompaid.drop('All', inplace=True)
            self.region_ransompaid.append(region_ransompaid)
            chart.make_bar_linechart(self.region_ransompaid, '地区年度已付赎金数量图', '年份', '已付赎金', '8/region_ransompaid')
            chart.make_pie_charts(self.region_ransompaid_group, '地区已付赎金数量占比图', '8/region_ransompaid_group')
        except:
            pass
    #def set_region_ransompaid_group(self):

    def set_hostkidoutcome(self):
        try:
            self.hostkidoutcome = []
            hostkidoutcome = pd.crosstab(self.data_list.iyear, self.data_list.hostkidoutcome_txt, margins=True)
            self.hostkidoutcome_group = hostkidoutcome.loc['All']
            self.hostkidoutcome_group.drop('All', inplace=True)
            self.hostkidoutcome_group.rename(columns={'All': 'hostkidoutcome_All'}, inplace=True)
            hostkidoutcome.drop('All', inplace=True)
            self.hostkidoutcome.append(hostkidoutcome)
            chart.make_bar_linechart(self.hostkidoutcome, '年度人质结局数量图', '年份', '袭击数量', '8/hostkidoutcome')
            chart.make_pie_charts(self.hostkidoutcome_group, '人质结局数量占比图', '8/hostkidoutcome_group')
        except:
            pass
    #def set_hostkidoutcome_group(self):

    def set_region_hostkidoutcome(self):
        try:
            self.region_hostkidoutcome = []
            region_hostkidoutcome = pd.crosstab(self.data_list.iyear,
                                                [self.data_list.region_txt, self.data_list.hostkidoutcome_txt],
                                                dropna=False)
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
            chart.make_bar_linechart1(self.region_hostkidoutcome, '地区年度人质结局数量图', '年份', '袭击数量',
                                      '8/region_hostkidoutcome', self.La_a)
            chart.make_pie_charts1(self.region_hostkidoutcome_group, self.Lp_a, '地区人质结局数量占比图',
                                   '8/region_hostkidoutcome_group')
        except:
            pass
    #def set_region_hostkidoutcome_group(self):

    def set_ransompaid_hostkidoutcome(self):
        try:
            self.ransompaid.extend(self.hostkidoutcome)
            chart.make_bar_linechart(self.ransompaid, '年度已付赎金与人质结局对比图', '年份', '袭击数量/已付赎金',
                                     '8/ransompaid_hostkidoutcome')
        except:
            pass


    def set_region_ransompaid_hostkidoutcome(self):
        try:
            self.region_ransompaid.extend(self.region_hostkidoutcome)
            L = self.region_ransompaid_group.index
            La = []
            La1 = []
            for x in L:
                str = '%s%s' % ('paid_', x)
                La1.append(str)
            La.append(La1)
            La.extend(self.La_a)
            chart.make_bar_linechart1(self.region_ransompaid, '地区年度已付赎金与人质结局对比图', '年份', '袭击数量',
                                      '8/region_ransompaid_hostkidoutcome', La)
        except:
            pass


    def set_paid_hostkidoutcome(self):
        try:
            paid_hostkidoutcome = []
            paid_hostkidoutcome1 = pd.crosstab(self.ransompaid_all.iyear, self.ransompaid_all.hostkidoutcome_txt,
                                               margins=True)
            paid_hostkidoutcome1.rename(columns=lambda x: 'paid_' + x, inplace=True)
            self.paid_hostkidoutcome_group1 = paid_hostkidoutcome1.loc['All']
            self.paid_hostkidoutcome_group1.drop('paid_All', inplace=True)
            paid_hostkidoutcome_group = pd.concat([self.paid_hostkidoutcome_group1, self.hostkidoutcome_group])
            paid_hostkidoutcome1.drop('All', inplace=True)
            paid_hostkidoutcome.append(paid_hostkidoutcome1)
            paid_hostkidoutcome.extend(self.hostkidoutcome)
            chart.make_bar_linechart(paid_hostkidoutcome, '是否付赎金年度人质结局对比图', '年份', '袭击数量', '8/paid_hostkidoutcome')
            chart.make_pie_charts(paid_hostkidoutcome_group, '是否付赎金人质结局对比图', '8/paid_hostkidoutcome_group')
        except:
            pass
    #def set_paid_hostkidoutcome_group(self):

    def set_region_paid_hostkidoutcome(self):
        try:
            region_paid_hostkidoutcome = []
            region_paid_hostkidoutcome1 = pd.crosstab(self.ransompaid_all.iyear, [self.ransompaid_all.region_txt,
                                                                                  self.ransompaid_all.hostkidoutcome_txt],
                                                      dropna=False)
            region_paid_hostkidoutcome_group = region_paid_hostkidoutcome1.sum()
            region_paid_hostkidoutcome_group = pd.concat(
                [region_paid_hostkidoutcome_group, self.region_hostkidoutcome_group])
            region_paid_hostkidoutcome.append(region_paid_hostkidoutcome1)
            region_paid_hostkidoutcome.extend(self.region_hostkidoutcome)
            region_paid_hostkidoutcome.append(self.region_year2)
            L = self.region_group.index
            L1 = self.paid_hostkidoutcome_group1.index
            La1 = []
            Lp = []
            La = []
            for x, y in product(L, L1):
                str = '%s%s%s' % (x, '_', y)
                La1.append(str)
            La.append(La1)
            Lp.extend(La1)
            La.extend(self.La_a)
            Lp.extend(self.Lp_a)
            chart.make_bar_linechart1(region_paid_hostkidoutcome, '是否付赎金地区年度人质结局对比图', '年份', '袭击数量',
                                      '8/region_paid_hostkidoutcome', La)
            chart.make_pie_charts1(region_paid_hostkidoutcome_group, Lp, '是否付赎金中地区人质结局对比图',
                                   '8/region_paid_hostkidoutcome_group')
        except:
            pass
    #def set_region_paid_hostkidoutcome_group(self):