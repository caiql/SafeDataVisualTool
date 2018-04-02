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
#        makechart.make_bigmap(self.data)
#        makechart.make_yearmap(self.data)
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

        # 设置root为self.tree的子树，所以root就是跟节点
        root2 = QTreeWidgetItem(self.ui.treeWidget)
        # 设置根节点的名称
        root2.setText(0, '恐怖袭击数量统计分析')

        # 为root节点设置子结点
        child1 = QTreeWidgetItem(root2)
        child1.setText(0, '年度总数-柱状图')
        child2 = QTreeWidgetItem(root2)
        child2.setText(0, '年度总数-折线图')
        child3 = QTreeWidgetItem(root2)
        child3.setText(0, '年度持续超过24小时占比-柱状图')
        child4 = QTreeWidgetItem(root2)
        child4.setText(0, '年度持续超过24小时占比-折线图')

        self.data.set_region_group()
        child5 = QTreeWidgetItem(root2)
        child5.setText(0, '年度各地区恐怖袭击数量-柱状图')
        child6 = QTreeWidgetItem(root2)
        child6.setText(0, '年度各地区恐怖袭击数量-折线图')

        child7 = QTreeWidgetItem(root2)
        child7.setText(0, '年度地区持续超过24小时占比-柱状图')
        child8 = QTreeWidgetItem(root2)
        child8.setText(0, '年度地区持续超过24小时占比-折线图')

        child9 = QTreeWidgetItem(root2)
        child9.setText(0, '地区总数-饼状图')
        for index in self.data.year_group.index:
            child = QTreeWidgetItem(child9)
            child.setText(0,str(index))

        self.ui.treeWidget.addTopLevelItem(root)
        self.ui.treeWidget.addTopLevelItem(root2)

        #makechart.make_bigmap(self.data)
        #makechart.make_yearmap(self.data)
        #makechart.make_year_data_pic(self.data)
        #makechart.make_region_year_group_pic(self.data)
        #makechart.make_region_group_pic(self.data)
        #makechart.make_year_region_pic(self.data,1996)
        #makechart.make_extended_data_pic(self.data)
        #makechart.make_region_extended_data_pic(self.data)
        #makechart.make_year_nkill_nwound_pic(self.data)
        #makechart.make_region_year_nkill_nwound_pic(self.data)
        #makechart.make_region_nkill(self.data)
        #makechart.make_region_nwound(self.data)
        url_string = "file:///html/region_nkillpie.html"
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