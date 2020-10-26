import sys
from experimental_Data.main_Window import *
from PyQt5 import QtWidgets

 

if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
