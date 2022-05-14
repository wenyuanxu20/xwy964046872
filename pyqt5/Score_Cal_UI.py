import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QLabel, QLineEdit,QTextBrowser,QInputDialog,
    QPushButton, QApplication)

class Score_Cal(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法
        self.CalculateClick()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 900, 700)
        # 设置窗口的标题
        self.setWindowTitle('Score Calculator')

        # 创建PushButton并设置一个tooltip
        btn1 = QPushButton('计算分数', self)
        btn1.setToolTip('This is a <b>QPushButton</b> widget')
        btn1.clicked.connect(self.CalculateClick)
        btn1.move(300, 300)  # 调整按钮位置


        self.label_obj1 = QLabel(self)  # 静态标签
        self.label_obj1.setText(u"K(击杀数)")
        self.i1 = QLineEdit(self)  # 单行编辑框

        self.label_obj2 = QLabel(self)  # 静态标签
        self.label_obj2.setText(u"D(死亡数)")
        self.i2 = QLineEdit(self)  # 单行编辑框

        self.label_obj3 = QLabel(self)  # 静态标签
        self.label_obj3.setText(u"A(助攻数)")
        self.i3 = QLineEdit(self)  # 单行编辑框

        self.label_obj4 = QLabel(self)  # 静态标签
        self.label_obj4.setText(u"造成伤害")
        self.i4 = QLineEdit(self)  # 单行编辑框

        self.label_obj5 = QLabel(self)  # 静态标签
        self.label_obj5.setText(u"全队击杀")
        self.i5 = QLineEdit(self)  # 单行编辑框

        self.label_obj6 = QLabel(self)  # 静态标签
        self.label_obj6.setText(u"全队死亡")
        self.i6 = QLineEdit(self)  # 单行编辑框

        self.label_obj7 = QLabel(self)  # 静态标签
        self.label_obj7.setText(u"全队助攻")
        self.i7 = QLineEdit(self)  # 单行编辑框

        self.label_obj8 = QLabel(self)  # 静态标签
        self.label_obj8.setText(u"全队伤害")
        self.i8 = QLineEdit(self)  # 单行编辑框

        self.label_obj9 = QLabel(self)  # 静态标签
        self.label_obj9.setText(u"装拆包次数")
        self.i9 = QLineEdit(self)  # 单行编辑框

        self.label_obj10 = QLabel(self)  # 静态标签
        self.label_obj10.setText(u"装拆包制胜")
        self.i10 = QLineEdit(self)  # 单行编辑框

        self.label_obj11 = QLabel(self)  # 静态标签
        self.label_obj11.setText(u"一血次数")
        self.i11 = QLineEdit(self)  # 单行编辑框

        # 输出框1
        self.out_1 = QTextBrowser(self)
        self.out_1.move(400, 50)
        self.out_1.resize(130, 25)
        self.label_out1 = QLabel(self)
        self.label_out1.setText(u"净值分")
        self.label_out1.move(345, 55)  # label位置

        # 输出框2
        self.out_2 = QTextBrowser(self)
        self.out_2.move(400, 70)
        self.out_2.resize(130, 25)
        self.label_out2 = QLabel(self)
        self.label_out2.setText(u"战术分")
        self.label_out2.move(345, 75)  # label位置

        # 输出框3
        self.out_3 = QTextBrowser(self)
        self.out_3.move(400, 90)
        self.out_3.resize(130, 25)
        self.label_out3 = QLabel(self)
        self.label_out3.setText(u"基础分")
        self.label_out3.move(345, 95)  # label位置

        # 输出框4
        self.out_4 = QTextBrowser(self)
        self.out_4.move(400, 110)
        self.out_4.resize(130, 25)
        self.label_out4 = QLabel(self)
        self.label_out4.setText(u"最终分")
        self.label_out4.move(345, 115)  # label位置

        # 公式展示框
        self.out_5 = QTextBrowser(self)
        self.out_5.move(300, 400)
        self.out_5.resize(500, 200)
        self.label_out5 = QLabel(self)
        self.label_out5.setText(u"公式说明")
        self.label_out5.move(250, 450)  # label位置

        self.i1.move(100, 70)  # 编辑框1位置
        self.i2.move(100, 90)  # 编辑框2位置
        self.i3.move(100, 110)  # 编辑框3位置
        self.i4.move(100, 130)  # 编辑框4位置
        self.i5.move(100, 150)  # 编辑框5位置
        self.i6.move(100, 170)  # 编辑框6位置
        self.i7.move(100, 190)  # 编辑框7位置
        self.i8.move(100, 210)  # 编辑框8位置
        self.i9.move(100, 230)  # 编辑框9位置
        self.i10.move(100, 250)  # 编辑框10位置
        self.i11.move(100, 270)  # 编辑框11位置

        self.label_obj1.move(30, 70)  # label1位置
        self.label_obj2.move(30, 90)  # label2位置
        self.label_obj3.move(30, 110)  # label2位置
        self.label_obj4.move(30, 130)  # label2位置
        self.label_obj5.move(30, 150)  # label2位置
        self.label_obj6.move(30, 170)  # label2位置
        self.label_obj7.move(30, 190)  # label2位置
        self.label_obj8.move(30, 210)  # label2位置
        self.label_obj9.move(30, 230)  # label2位置
        self.label_obj10.move(30, 250)  # label2位置
        self.label_obj11.move(30, 270)  # label2位置

        # 显示窗口
        self.show()

    def CalculateClick(self):

        # 净值分计算
        contri = 0
        k_kall = 0
        d_dall = 0
        a_aall = 0
        dmg_dmgall = 0
        N = 100
        if self.i1.text() != '':
            k_kall = 1.2 * int(self.i1.text()) / int(self.i5.text())
            d_dall = 1.2 * int(self.i2.text()) / int(self.i6.text())
            a_aall = 0.2 * int(self.i3.text()) / int(self.i7.text())
            dmg_dmgall = 0.12 * int(self.i4.text()) / int(self.i8.text())
            contri = (k_kall - d_dall + a_aall + dmg_dmgall) * N

        if contri > 0:
            pure_score = contri ** 0.4
        else:
            pure_score = -((-contri) ** 0.4)

        # 战术分计算
        tactics_score = 0
        A = 200
        B = 200
        C = 100
        if self.i9.text() != '':
            bombScore = (int(self.i9.text()) * A + int(self.i10.text()) * B) / 1000
            first_blood_score = int(self.i11.text()) * C / 1000
            tactics_score = bombScore + first_blood_score

        # 基础分计算
        basic_score = 0
        X = 3
        # 基础评分=0+X （若净值评分+战术评分＜0）
        if pure_score + tactics_score < 0:
            basic_score = 0 + X

        # 基础评分=净值评分+战术评分+X （若净值评分+战术评分≥0）

        else:
            basic_score = pure_score + tactics_score + X

        # 最终分计算
        score = 0
        if self.i1.text() != '':
            score = basic_score + ((int(self.i1.text()) + int(self.i3.text()) * 0.25) * 2.5 / int(self.i5.text())) ** 0.4


        self.out_1.setText(str(pure_score))
        self.out_2.setText(str(tactics_score))
        self.out_3.setText(str(basic_score))
        self.out_4.setText(str(score))
        self.out_5.setText('贡献分 =\n (1.2*(击杀数/全队击杀数) - 1.2*(死亡数/全队死亡数) + 0.2*(助攻数/全队助攻数) + (0.12*造成伤害/全队伤害))*N \n'
                           '（贡献分大于0）净值分 = 贡献分的0.4次方\n'
                           '（贡献分不大于0）净值分 = -（（-贡献分）的0.4次方）\n'
                           '拆装包评分 = (拆装包次数*A+拆装包致胜次数*B)/1000 \n'
                           '首杀评分 = 首杀次数*C/1000 \n'
                           '战术评分 = 拆装包评分+首杀评分 \n'
                           '（若净值评分+战术评分＜0）基础评分 = 0+X \n'
                           '（若净值评分+战术评分≥0）基础评分 = 净值评分+战术评分+X \n'
                           '最终评分 = 基础评分+((个人击杀+助攻*0.25)*2.5/全队击杀)^0.4')

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Score_Cal()
    sys.exit(app.exec_())