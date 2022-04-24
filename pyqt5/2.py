import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QLabel, QLineEdit,
    QPushButton, QApplication)



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 900, 700)
        # 设置窗口的标题
        self.setWindowTitle('Example1')
        # 设置窗口的图标，引用当前目录下的web.png图片
        #self.setWindowIcon(QIcon('web.png'))

        # 创建一个PushButton并为他设置一个tooltip
        btn1 = QPushButton('确定', self)
        btn1.setToolTip('This is a <b>QPushButton</b> widget')
        btn1.clicked.connect(self.buttonClicked)

        self.label_obj1 = QLabel(self)  # 静态标签
        self.label_obj1.setText(u"静态文本框在这里")
        self.line_edit_obj1 = QLineEdit(self)  # 单行编辑框

        self.line_edit_obj1.move(60, 70)  # 编辑框位置
        self.label_obj1.move(60, 40)  # label位置

        # 显示窗口
        self.show()

    def getNum(self):
        #test_1 =
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())