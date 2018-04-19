import ui.ui_main
import datadel
import makechart
#import sys, os, time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from PyQt5 import QtCore, QtGui
#from PIL import Image,ImageEnhance,ImageFilter
#from PyQt5.QtWebEngineWidgets import *
#from PyQt5.QtWebChannel import QWebChannel
import pandas as pd

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = ui.ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.move(200,0)
        self.data = None

        self.ui.treeWidget.setColumnCount(1)
        self.ui.treeWidget.setHeaderLabels(['Key'])

        self.root = QTreeWidgetItem(self.ui.treeWidget)
        self.root.setText(0, '经纬度地图')
        child1 = QTreeWidgetItem(self.root)
        child1.setText(0, '大地图')

        root1 = QTreeWidgetItem(self.ui.treeWidget)
        root1.setText(0, '恐怖袭击数量统计分析')
        child1 = QTreeWidgetItem(root1)
        child1.setText(0, '年度恐怖袭击数量图')
        child2 = QTreeWidgetItem(root1)
        child2.setText(0, '年度恐怖袭击数量占比饼图')
        child3 = QTreeWidgetItem(root1)
        child3.setText(0, '月份恐怖袭击数量图')
        child4 = QTreeWidgetItem(root1)
        child4.setText(0, '月份恐怖袭击数量占比饼图')
        child5 = QTreeWidgetItem(root1)
        child5.setText(0, '地区年度恐怖袭击数量图')
        child6 = QTreeWidgetItem(root1)
        child6.setText(0, '地区月份恐怖袭击数量图')
        child7 = QTreeWidgetItem(root1)
        child7.setText(0, '地区恐怖袭击数量占比饼图')
        child8 = QTreeWidgetItem(root1)
        child8.setText(0, '国家年度恐怖袭击数量图')
        child9 = QTreeWidgetItem(root1)
        child9.setText(0, '国家月份恐怖袭击数量图')
        child10 = QTreeWidgetItem(root1)
        child10.setText(0, '国家恐怖袭击数量占比饼图')


        root2 = QTreeWidgetItem(self.ui.treeWidget)
        root2.setText(0, '伤亡人数统计分析')
        child1 = QTreeWidgetItem(root2)
        child1.setText(0, '年度伤亡人数图')
        child2 = QTreeWidgetItem(root2)
        child2.setText(0, '伤亡人数占比饼图')
        child3 = QTreeWidgetItem(root2)
        child3.setText(0, '地区年度伤亡人数图')
        child4 = QTreeWidgetItem(root2)
        child4.setText(0, '地区伤亡人数占比饼图')

        root3 = QTreeWidgetItem(self.ui.treeWidget)
        root3.setText(0, '恐怖组织统计分析')
        child1 = QTreeWidgetItem(root3)
        child1.setText(0, '恐怖组织年度袭击数量折线图')
        child2 = QTreeWidgetItem(root3)
        child2.setText(0, '恐怖组织年度袭击数量柱状图')
        child3 = QTreeWidgetItem(root3)
        child3.setText(0, '恐怖组织袭击数量占比饼图')

        root4 = QTreeWidgetItem(self.ui.treeWidget)
        root4.setText(0, '袭击情况统计分析')
        child1 = QTreeWidgetItem(root4)
        child1.setText(0, '袭击成败年度数量图')
        child1_1 = QTreeWidgetItem(root4)
        child1_1.setText(0, '袭击成败数量占比饼图')
        child2 = QTreeWidgetItem(root4)
        child2.setText(0, '地区年度袭击成败数量图')
        child3 = QTreeWidgetItem(root4)
        child3.setText(0, '地区成败数量占比饼图')
        child4 = QTreeWidgetItem(root4)
        child4.setText(0, '自杀式年度数量图')
        child4_1 = QTreeWidgetItem(root4)
        child4_1.setText(0, '自杀式数量占比饼图')
        child5 = QTreeWidgetItem(root4)
        child5.setText(0, '地区年度自杀式袭击数量图')
        child6 = QTreeWidgetItem(root4)
        child6.setText(0, '地区自杀式袭击数量占比饼图')
        child7 = QTreeWidgetItem(root4)
        child7.setText(0, '年度恐怖袭击种类数量图')
        child8 = QTreeWidgetItem(root4)
        child8.setText(0, '年度恐怖袭击种类数量占比饼图')
        child9 = QTreeWidgetItem(root4)
        child9.setText(0, '地区年度恐怖袭击种类数量图')
        child10 = QTreeWidgetItem(root4)
        child10.setText(0, '地区恐怖袭击种类数量占比饼图')
        child11 = QTreeWidgetItem(root4)
        child11.setText(0, '年度是否持续超过24小时的袭击次数图')
        child12 = QTreeWidgetItem(root4)
        child12.setText(0, '是否持续超过24小时的袭击次数占比饼图')
        child13 = QTreeWidgetItem(root4)
        child13.setText(0, '地区年度是否持续超过24小时的袭击次数图')
        child14 = QTreeWidgetItem(root4)
        child14.setText(0, '地区是否持续超过24小时的袭击次数占比饼图')

        root5 = QTreeWidgetItem(self.ui.treeWidget)
        root5.setText(0, '恐怖袭击性质统计分析')
        child1 = QTreeWidgetItem(root5)
        child1.setText(0, '年度四种恐怖袭击性质数量图')
        child2 = QTreeWidgetItem(root5)
        child2.setText(0, '四种恐怖袭击性质数量占比饼图')
        child3 = QTreeWidgetItem(root5)
        child3.setText(0, '地区年度四种恐怖袭击性质数量图')
        child4 = QTreeWidgetItem(root5)
        child4.setText(0, '地区四种恐怖袭击性质数量占比饼图')

        root6 = QTreeWidgetItem(self.ui.treeWidget)
        root6.setText(0, '受害者类型统计分析')
        child1 = QTreeWidgetItem(root6)
        child1.setText(0, '年度目标受害者类型数量图')
        child2 = QTreeWidgetItem(root6)
        child2.setText(0, '目标受害者类型数量占比图')
        child3 = QTreeWidgetItem(root6)
        child3.setText(0, '地区年度受害者类型数量图')
        child4 = QTreeWidgetItem(root6)
        child4.setText(0, '地区受害者类型数量占比饼图')

        root7 = QTreeWidgetItem(self.ui.treeWidget)
        root7.setText(0, '使用武器类型统计分析')
        child1 = QTreeWidgetItem(root7)
        child1.setText(0, '年度袭击武器类型数量图')
        child2 = QTreeWidgetItem(root7)
        child2.setText(0, '袭击武器类型数量占比饼图')
        child3 = QTreeWidgetItem(root7)
        child3.setText(0, '地区年度袭击武器类型数量图')
        child4 = QTreeWidgetItem(root7)
        child4.setText(0, '地区袭击武器类型数量占比饼图')

        root8 = QTreeWidgetItem(self.ui.treeWidget)
        root8.setText(0, '赎金与人质结局相关统计分析')
        child1 = QTreeWidgetItem(root8)
        child1.setText(0, '年度已付赎金数量图')
        child2 = QTreeWidgetItem(root8)
        child2.setText(0, '地区年度已付赎金数量图')
        child3 = QTreeWidgetItem(root8)
        child3.setText(0, '地区已付赎金数量占比饼图')
        child4 = QTreeWidgetItem(root8)
        child4.setText(0, '年度人质结局数量图')
        child5 = QTreeWidgetItem(root8)
        child5.setText(0, '人质结局数量占比饼图')
        child6 = QTreeWidgetItem(root8)
        child6.setText(0, '地区年度人质结局数量图')
        child7 = QTreeWidgetItem(root8)
        child7.setText(0, '地区人质结局数量占比饼图')
        child8 = QTreeWidgetItem(root8)
        child8.setText(0, '年度已付赎金与人质结局对比图')
        child9 = QTreeWidgetItem(root8)
        child9.setText(0, '地区年度已付赎金与人质结局对比图')
        child10 = QTreeWidgetItem(root8)
        child10.setText(0, '已付赎金中年度人质结局数量图')
        child11 = QTreeWidgetItem(root8)
        child11.setText(0, '已付赎金中人质结局数量占比饼图')
        child12 = QTreeWidgetItem(root8)
        child12.setText(0, '已付赎金中地区年度人质结局数量图')
        child13 = QTreeWidgetItem(root8)
        child13.setText(0, '已付赎金中地区人质结局数量占比饼图')

        self.ui.treeWidget.addTopLevelItem(self.root)
        self.ui.treeWidget.addTopLevelItem(root1)
        self.ui.treeWidget.addTopLevelItem(root2)
        self.ui.treeWidget.addTopLevelItem(root3)
        self.ui.treeWidget.addTopLevelItem(root4)
        self.ui.treeWidget.addTopLevelItem(root5)
        self.ui.treeWidget.addTopLevelItem(root6)
        self.ui.treeWidget.addTopLevelItem(root7)
        self.ui.treeWidget.addTopLevelItem(root8)

        self.ui.pushButton.clicked.connect(self.open_file)
        self.ui.treeWidget.clicked.connect(self.treeselect)

    def treeselect(self):
        # ---获得点击treewidget的index----
        cur_index = self.ui.treeWidget.currentIndex().row()
        par_index = self.ui.treeWidget.currentIndex().parent().row()
        if self.get_data.data:
            if par_index == -1:
                if cur_index == 0:
                    string = 'null.html'
            elif par_index == 0:
                if cur_index == 0:
                    string = '0/1bigmap.html'
                else:
                    string1 = self.ui.treeWidget.currentItem().text(0)
                    string = '%s%s%s' %('0/', string1 ,'map.html')
            elif par_index == 1:
                if cur_index == 0:
                    string = '1/year_databar_line.html'
                elif cur_index == 1:
                    string = '1/year_grouppie.html'
                elif cur_index == 2:
                    string = '1/month_databar_line.html'
                elif cur_index == 3:
                    string = '1/month_grouppie.html'
                elif cur_index == 4:
                    string = '1/region_yearbar_line.html'
                elif cur_index == 5:
                    string = '1/region_monthbar_line.html'
                elif cur_index == 6:
                    string = '1/region_grouppie.html'
                elif cur_index == 7:
                    string = '1/country_yearbar_line.html'
                elif cur_index == 8:
                    string = '1/country_monthbar_line.html'
                elif cur_index == 9:
                    string = '1/country_grouppie.html'
                else:
                    string = 'null.html'
            elif par_index == 2:
                if cur_index == 0:
                    string = '2/year_nkill_nwoundbar_line.html'
                elif cur_index == 1:
                    string = '2/year_nkill_nwound_grouppie.html'
                elif cur_index == 2:
                    string = '2/region_year_nkill_nwoundbar_line.html'
                elif cur_index == 3:
                    string = '2/region_nkill_nwoundpie.html'
                else:
                    string = 'null.html'
            elif par_index == 3:
                if cur_index == 0:
                    string = '3/gnameline.html'
                elif cur_index == 1:
                    string = '3/gnamebar.html'
                elif cur_index == 2:
                    string = '3/gname_grouppie.html'
                else:
                    string = 'null.html'
            elif par_index == 4:
                if cur_index == 0:
                    string = '4/successbar_line.html'
                elif cur_index == 1:
                    string = '4/success_grouppie.html'
                elif cur_index == 2:
                    string = '4/region_successbar_line.html'
                elif cur_index == 3:
                    string = '4/region_success_grouppie.html'
                elif cur_index == 4:
                    string = '4/suicidebar_line.html'
                elif cur_index == 5:
                    string = '4/suicide_grouppie.html'
                elif cur_index == 6:
                    string = '4/region_suicidebar_line.html'
                elif cur_index == 7:
                    string = '4/region_suicide_grouppie.html'
                elif cur_index == 8:
                    string = '4/attacktypebar_line.html'
                elif cur_index == 9:
                    string = '4/attacktype_grouppie.html'
                elif cur_index == 10:
                    string = '4/region_attacktypebar_line.html'
                elif cur_index == 11:
                    string = '4/region_attacktype_grouppie.html'
                elif cur_index == 12:
                    string = '4/extendedbar_line.html'
                elif cur_index == 13:
                    string = '4/extended_grouppie.html'
                elif cur_index == 14:
                    string = '4/region_extendedbar_line.html'
                elif cur_index == 15:
                    string = '4/region_extended_grouppie.html'
                else:
                    string = 'null.html'
            elif par_index == 5:
                if cur_index == 0:
                    string = '5/attackwhybar_line.html'
                elif cur_index == 1:
                    string = '5/attackwhy_grouppie.html'
                elif cur_index == 2:
                    string = '5/region_attackwhybar_line.html'
                elif cur_index == 3:
                    string = '5/region_attackwhy_grouppie.html'
                else:
                    string ='null.html'
            elif par_index == 6:
                if cur_index == 0:
                    string = '6/targtypebar_line.html'
                elif cur_index == 1:
                    string = '6/targtype_grouppie.html'
                elif cur_index == 2:
                    string = '6/region_targtypebar_line.html'
                elif cur_index == 3:
                    string = '6/region_targtype_grouppie.html'
                else:
                    string ='null.html'
            elif par_index == 7:
                if cur_index == 0:
                    string = '7/weaptypebar_line.html'
                elif cur_index == 1:
                    string = '7/weaptype_grouppie.html'
                elif cur_index == 2:
                    string = '7/region_weaptypebar_line.html'
                elif cur_index == 3:
                    string = '7/region_weaptype_grouppie.html'
                else:
                    string ='null.html'
            elif par_index == 8:
                if cur_index == 0:
                    string = '8/ransompaidbar_line.html'
                elif cur_index == 1:
                    string = '8/region_ransompaidbar_line.html'
                elif cur_index == 2:
                    string = '8/region_ransompaid_grouppie.html'
                elif cur_index == 3:
                    string = '8/hostkidoutcomebar_line.html'
                elif cur_index == 4:
                    string = '8/hostkidoutcome_grouppie.html'
                elif cur_index == 5:
                    string = '8/region_hostkidoutcomebar_line.html'
                elif cur_index == 6:
                    string = '8/region_hostkidoutcome_grouppie.html'
                elif cur_index == 7:
                    string = '8/ransompaid_hostkidoutcomebar_line.html'
                elif cur_index == 8:
                    string = '8/region_ransompaid_hostkidoutcomebar_line.html'
                elif cur_index == 9:
                    string = '8/paid_hostkidoutcomebar_line.html'
                elif cur_index == 10:
                    string = '8/paid_hostkidoutcome_grouppie.html'
                elif cur_index == 11:
                    string = '8/region_paid_hostkidoutcomebar_line.html'
                elif cur_index == 12:
                    string = '8/region_paid_hostkidoutcome_grouppie.html'
                else:
                    string ='null.html'
        else:
            QMessageBox.critical(None, "Critical", "总数据未导入！")
        try:
            self.set_html("file:/html/%s" % string)
        except Exception as e:
            QMessageBox.critical(None, "Critical", "%s" % e)

    def open_file(self):
        self.str_get_folder = QFileDialog.getOpenFileName(None, "Open file dialog","/")[0]
        self.filename = str(self.str_get_folder)
        self.ui.lineEdit.setText(self.filename)
        self.get_data = thread1(self,self.filename)
        self.get_data.start()

    def set_html(self,url_string):
        self.ui.webView.load(QUrl(url_string))
        self.ui.webView.show()

class thread1(QThread):
    sendData = pyqtSignal(int)
    def __init__(self,MyForm,data_path=""):
        QThread.__init__(self)
        self.MyForm = MyForm
        self.path = data_path
        self.data = None

    def __del__(self):
        self.wait()

    def run(self):
        self.sendData.emit(0)
        try:
            self.data = datadel.datadel(self.path)
            self.data.set_year()
            for index in self.data.year_group.index:
                child = QTreeWidgetItem(self.MyForm.root)
                child.setText(0, str(index))
            # makechart.make_bigmap(self.data)
            # makechart.make_yearmap(self.data)
            #makechart.make_year_data_pic(self.data)
            #makechart.make_region_year_pic(self.data)
            #makechart.make_region_group_pic(self.data)
            # makechart.make_year_region_pic(self.data)
            # makechart.make_extended_data_pic(self.data)
            # makechart.make_region_extended_data_pic(self.data)
            # makechart.make_year_nkill_nwound_pic(self.data)
            # makechart.make_region_year_nkill_nwound_pic(self.data)
            # makechart.make_region_nkill_nwound_pic(self.data)
            # makechart.make_gname(self.data)
            # makechart.make_success(self.data)
            # makechart.make_suicide(self.data)
            # makechart.make_region_success(self.data)
            # makechart.make_region_success_group(self.data)
            # makechart.make_region_suicide(self.data)
            # makechart.make_region_suicide_group(self.data)
            #makechart.make_attacktype(self.data)
            #makechart.make_region_attacktype(self.data)
            #makechart.make_region_attacktype_group(self.data)
            #makechart.make_attackwhy(self.data)
            #makechart.make_region_attackwhy(self.data)
            #makechart.make_targtype(self.data)
            #makechart.make_region_targtype(self.data)
            #makechart.make_weaptype(self.data)
            #makechart.make_region_weaptype(self.data)
            #makechart.make_ransompaid(self.data)

        except Exception as e:
            print("%s---%s" % (sys._getframe().f_lineno, e))
            self.sendData.emit(-1)
        self.sendData.emit(1)


def mycodestart():
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    import sys, threading
    sys.setrecursionlimit(100000)
    threading.stack_size(200000000)
    thread = threading.Thread(target=mycodestart)
    thread.start()