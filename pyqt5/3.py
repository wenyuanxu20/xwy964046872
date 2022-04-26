import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QLabel, QLineEdit,QTextBrowser,QInputDialog,
    QPushButton, QApplication)

import score



class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法
        #self.buttonClicked()
        self.CalculateClcik()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 900, 700)
        # 设置窗口的标题
        self.setWindowTitle('Example1')
        # 设置窗口的图标，引用当前目录下的web.png图片
        #self.setWindowIcon(QIcon('web.png'))

        #self.qle = QLineEdit(self)

        # 创建一个PushButton并为他设置一个tooltip
        btn1 = QPushButton('确定', self)
        btn1.setToolTip('This is a <b>QPushButton</b> widget')
        btn1.clicked.connect(self.CalculateClcik)

        self.label_obj1 = QLabel(self)  # 静态标签
        self.label_obj1.setText(u"K")
        self.i1 = QLineEdit(self)  # 单行编辑框

        self.label_obj2 = QLabel(self)  # 静态标签
        self.label_obj2.setText(u"D")
        self.i2 = QLineEdit(self)  # 单行编辑框



        # 输出框1
        self.text_browser = QTextBrowser(self)
        self.text_browser.move(400, 50)

        self.i1.move(100, 70)  # 编辑框1位置
        self.i2.move(100, 90)  # 编辑框2位置


        self.label_obj1.move(30, 70)  # label1位置
        self.label_obj2.move(30, 90)  # label2位置


        #x = self.line_edit_obj1.text()

        #print(x)

        # 显示窗口
        self.show()
    #


    def CalculateClcik(self):
        #x = self.pure_score_cal()
        #x = float(x)
        #try:
        if self.i1.text() != '':

            sum = int(self.i1.text()) + int(self.i2.text())
            self.text_browser.setText(str(sum))

        # except:
        #     print('请输入正确的整数')
        #     self.text_browser.setText("")

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())