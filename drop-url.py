import os, sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QListWidget
from PyQt5.QtCore import Qt, QUrl

class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.ui = QUiLoader().loadUi("dropurl.ui")
        self.listbox_view = ListBoxWidget(self)

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

app = QApplication(sys.argv)
window = ListBoxWidget()
window.ui.show()
app.exec_()