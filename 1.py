import os, sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QListWidget, QMainWindow
from PySide2.QtCore import Qt, QUrl
from PySide2.QtCore import QFile, QStringListModel
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton

class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        qfile = QFile('dropURL.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 加载UI文件
        self.ui = QUiLoader().load(qfile)
        self.listbox_view = QListWidget(self)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):

        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
            self.addItems(links)
        else:
            event.ignore()




app = QApplication([])
window = ListBoxWidget()
window.ui.show()
app.exec_()