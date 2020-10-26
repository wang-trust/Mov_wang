import sys
from src.main_Window import *
from PyQt5.QtWidgets import *
from src.CheckDialog import *
from src.Edit_Window import *


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)