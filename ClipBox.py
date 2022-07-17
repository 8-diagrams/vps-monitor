import sys,os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QMimeData
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel,
                             QMenuBar, QMenu, QAction)
 
class DemoClipboard(QMainWindow):
    def __init__(self, parent=None):
        super(DemoClipboard, self).__init__(parent)   
        
         # 设置窗口标题
        self.setWindowTitle('Myclipbox')      
        # 设置窗口大小
        self.resize(800, 600)
      
        self.initUi()
        
        self.clipType=''
        
    def initUi(self):
        self.initMenu()
        
        self.showBox = QLabel()
        self.showBox.setFrameShape(QFrame.Box)
        self.showBox.setLineWidth(1)
        self.showBox.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(self.showBox)
        
    def initMenu(self):
        mBar = self.menuBar()
        
        #文件菜单
        menuFile = mBar.addMenu('文件')
        #退出
        aExit = QAction('退出', self)
        aExit.triggered.connect(self.close)
        menuFile.addAction(aExit)
        
        #编辑菜单
        menuEdit = mBar.addMenu('编辑')
        aCopyText = QAction('复制文本', self)
        aCopyText.triggered.connect(self.onCopyText)
        aCopyHtml = QAction('复制Html文本', self)
        aCopyHtml.triggered.connect(self.onCopyHtml)
        aCopyImage = QAction('复制图像',self)
        aCopyImage.triggered.connect(self.onCopyImage)
        
        aPaste = QAction('粘贴', self)
        aPaste.triggered.connect(self.onPaste)
        
        menuEdit.addAction(aCopyText)
        menuEdit.addAction(aCopyHtml)
        menuEdit.addAction(aCopyImage)
        menuEdit.addSeparator()
        menuEdit.addAction(aPaste)
        
    def onCopyText(self):
        #设置剪贴板文本
        clipboard = QApplication.clipboard()
        clipboard.setText('这是一段剪贴板文本')
        
    def onCopyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)
        
    def onCopyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap(os.path.dirname(__file__) + "/python-logo.png"))
        
    def onPaste(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        print(mimeData.formats())
        if mimeData.hasFormat('text/plain'):
            self.showBox.setText(clipboard.text())
            #也可以使用下面方式
            #self.showBox.setText(mimeData.text())
        elif mimeData.hasHtml():
            self.showBox.setText(mimeData.html())
        elif mimeData.hasFormat('application/x-qt-image'):
            self.showBox.setPixmap(clipboard.pixmap())
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoClipboard()
    window.show()
    sys.exit(app.exec_())