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

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = ui.ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.move(200,0)
        self.ui.pushButton.clicked.connect(self.open_file)
        self.filename = None
        self.data = None

    def open_file(self):
        self.str_get_folder = QFileDialog.getOpenFileName(None, "Open file dialog","/")[0]
        self.filename = str(self.str_get_folder)
        self.ui.lineEdit.setText(self.filename)
        self.data = datadel.datadel(self.filename)
        self.ui.treeWidget.setColumnCount(1)
        # 设置头部信息，因为上面设置列数为2，所以要设置两个标识符
        self.ui.treeWidget.setHeaderLabels(['Key'])

        # 设置root为self.tree的子树，所以root就是跟节点
        root = QTreeWidgetItem(self.ui.treeWidget)
        # 设置根节点的名称
        root.setText(0, '经纬度地图')
        self.data.set_year_group()
        for index in self.data.year_group.index:
            child = QTreeWidgetItem(root)
            child.setText(0,str(index))

        root1 = QTreeWidgetItem(self.ui.treeWidget)
        root1.setText(0, '恐怖袭击数量统计分析')
        child1 = QTreeWidgetItem(root1)
        child1.setText(0, '年度袭击总数图')
        child2 = QTreeWidgetItem(root1)
        child2.setText(0, '年度持续超过24小时占比图')
        child3 = QTreeWidgetItem(root1)
        child3.setText(0, '年度各地区恐怖袭击数量图')
        child4 = QTreeWidgetItem(root1)
        child4.setText(0, '年度地区持续超过24小时占比图')
        child5 = QTreeWidgetItem(root1)
        child5.setText(0, '地区数量占比饼图')
        for index in self.data.year_group.index:
            child = QTreeWidgetItem(child5)
            child.setText(0,str(index))

        root2 = QTreeWidgetItem(self.ui.treeWidget)
        root2.setText(0, '伤亡人数统计分析')
        child1 = QTreeWidgetItem(root2)
        child1.setText(0, '年度伤亡人数图')
        child2 = QTreeWidgetItem(root2)
        child2.setText(0, '地区年度伤亡人数图')
        child3 = QTreeWidgetItem(root2)
        child3.setText(0, '地区伤亡人数占比饼图')

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
        child2 = QTreeWidgetItem(root4)
        child2.setText(0, '地区年度袭击成败数量图')
        child3 = QTreeWidgetItem(root4)
        child3.setText(0, '地区成败数量占比饼图')
        child4 = QTreeWidgetItem(root4)
        child4.setText(0, '自杀式年度数量图')
        child5 = QTreeWidgetItem(root4)
        child5.setText(0, '地区年度自杀式袭击数量图')
        child6 = QTreeWidgetItem(root4)
        child6.setText(0, '地区自杀式袭击数量占比饼图')
        child7 = QTreeWidgetItem(root4)
        child7.setText(0,'年度恐怖袭击种类数量图')
        child8 = QTreeWidgetItem(root4)
        child8.setText(0,'年度恐怖袭击种类数量占比饼图')


        self.ui.treeWidget.addTopLevelItem(root)
        self.ui.treeWidget.addTopLevelItem(root1)
        self.ui.treeWidget.addTopLevelItem(root2)
        self.ui.treeWidget.addTopLevelItem(root3)
        self.ui.treeWidget.addTopLevelItem(root4)

        #makechart.make_bigmap(self.data)
        #makechart.make_yearmap(self.data)
        #makechart.make_year_data_pic(self.data)
        #makechart.make_region_year_group_pic(self.data)
        #makechart.make_region_group_pic(self.data)
        #makechart.make_year_region_pic(self.data)
        #makechart.make_extended_data_pic(self.data)
        #makechart.make_region_extended_data_pic(self.data)
        #makechart.make_year_nkill_nwound_pic(self.data)
        #makechart.make_region_year_nkill_nwound_pic(self.data)
        #makechart.make_region_nkill_nwound_pic(self.data)
        makechart.make_gname(self.data)
        #makechart.make_success(self.data)
        #makechart.make_region_success(self.data)
        #makechart.make_region_success_group(self.data)
        #makechart.make_region_suicide(self.data)
        #makechart.make_region_suicide_group(self.data)
        #makechart.make_attacktype(self.data)
        url_string = "file:///html/attacktypebar_line.html"
        self.view_html(url_string)

    def view_html(self,url_string):
        self.ui.webView.load(QUrl(url_string))
        self.ui.webView.show()

# -----------------------code input----------------------------------------
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