# -*- coding:utf-8 -*-


#


#def get_index(self,N,X,A,B,C,k,d,a,dmg,k_all,d_all,a_all,dmg_all,bomb_time,bomb_win,first_blood_time):
N = 100
X = 3
A = 200
B = 200
C = 100


k = 3
d = 9
a = 0
dmg = 27
k_all = 3
d_all = 41
a_all = 1
dmg_all = 40
bomb_time = 0
bomb_win = 0
first_blood_time = 0

#return N,X,A,B,C,k,d,a,dmg,k_all,d_all,a_all,dmg_all,bomb_time,bomb_win,first_blood_time


def pure_score_cal():
    contri = (1.2 * (k / k_all) - 1.2 * (d / d_all) + 0.2 * (a / a_all) + (0.12 * dmg / dmg_all)) * N

    if contri > 0:
        pure_score = contri ** 0.4
    else:
        pure_score = -((-contri) ** 0.4)

    return pure_score

def tactics_score_cal():
    # 拆装包评分=(拆装包次数*A+拆装包致胜次数*B)/1000

    bombScore = (bomb_time * A + bomb_win * B) / 1000

    # 首杀评分=首杀次数*C/1000
    first_blood_score = first_blood_time * C / 1000

    # 战术评分=拆装包评分+首杀评分
    tactics_score = bombScore + first_blood_score

    return tactics_score


def basic_score():
    pure_score = pure_score_cal()
    tactics_score = tactics_score_cal()


    # 基础评分=0+X （若净值评分+战术评分＜0）
    if pure_score + tactics_score < 0:
        basic_score = 0 + X

    # 基础评分=净值评分+战术评分+X （若净值评分+战术评分≥0）

    else:
        basic_score = pure_score + tactics_score + X

    # 最终评分=基础评分+((个人击杀+助攻*0.25)*2.5/全队击杀)^0.4

    return basic_score


def score():

    score = basic_score() + ((k + a * 0.25) * 2.5 / k_all) ** 0.4

    return score


print('净值评分：', '%.1f' % pure_score_cal())

print('战术评分：', '%.1f' % tactics_score_cal())

print('基础评分评分：', '%.1f' % basic_score())

print('最终评分：', '%.1f' % score())


