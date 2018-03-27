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
#        url_string = "file:///html/bigmap.html"
#        self.ui.webView.load(QUrl(url_string))
#        self.ui.webView.show()

    def open_file(self):
        self.str_get_folder = QFileDialog.getOpenFileName(None, "Open file dialog","/")[0]
        self.filename = str(self.str_get_folder)
        self.ui.lineEdit.setText(self.filename)
        self.data = datadel.datadel(self.filename)
#        makechart.make_bigmap(self.data)
#        makechart.make_yearmap(self.data)
#        makechart.make_bigline(self.data)
#        makechart.make_bigextended(self.data)
        makechart.make_bigregion(self.data)
        url_string = "file:///html/big_regionbar.html"
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