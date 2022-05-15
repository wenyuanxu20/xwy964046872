import sys

from PyQt5 import QtWidgets, QtCore


if __name__ == '__main__':


    #每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QtWidgets.QApplication(sys.argv)

    #QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    widget = QtWidgets.QWidget()

    #resize()方法调整窗口的大小。这离是250px宽150px高
    widget.resize(250, 150)

    #move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
    widget.move(300, 300)


    widget.setWindowTitle("PyQt Widget")
    widget.show()
    exit(app.exec_())


