import sys
from pathlib import Path
from PyQt5 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton,QTextBrowser
from PySide2.QtCore import Qt, QUrl
from PySide2.QtCore import QFile, QStringListModel
from PySide2.QtUiTools import QUiLoader

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.setCentralWidget(self.textBrowser)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        paths = [Path(url.toLocalFile()) for url in urls]

        self.textBrowser.setText('\n'.join([str(p) for p in paths]))


# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainWindow(app)
#     window.show()
#     app.exec()
#
#
# if __name__ == '__main__':
#     main()
app = QApplication([])
window = MainWindow(app)
window.show()
app.exec_()