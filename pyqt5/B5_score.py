# -*- coding:utf-8 -*-

# 策划配置参数
N = 100

A = 200
B = 200
C = 100

D = 1
E = 1
F = 1
G = 1
H = 1

# 对局数据

k = 0
d = 0
a = 0
dmg = 0
k_all = 0
d_all = 0
a_all = 0
dmg_all = 0
bomb_remove = 0
bomb_deploy = 0
bomb_win = 0


first_blood_time = 0
double_kill = 0
triple_kill = 0
quadra_kill = 0
penta_kill = 0


# 1 win 0 fail
win = 0

if win == 1:
    X = 5
else:
    X = 2


def pure_score_cal():

    if k_all == 0 or d_all == 0 or a_all == 0 or dmg_all == 0:
        contri = (1.2 * (k / 1) - 1.2 * (d / 1) + 0.2 * (a / 1) + (0.12 * (dmg / 1))) * N

    else:
        contri = (1.2 * (k / k_all) - 1.2 * (d / d_all) + 0.2 * (a / a_all) + (0.12 * (dmg / dmg_all))) * N

    if contri > 0:
        pure_score = contri ** 0.4
    else:
        pure_score = -((-contri) ** 0.4)

    return pure_score

def tactics_score_cal():
    # 拆装包评分=(拆包次数*A+装包次数*B+装包致胜次数*C)/1000

    bombScore = (bomb_remove * A + bomb_deploy * B + bomb_win * C) / 1000

    #特殊击杀评分 = ( 首杀次数 * D + 双杀次数 * E + 三杀次数 * F + 四杀次数 * G + 五杀次数 * H ) / 1000
    kill_score = (first_blood_time * D + double_kill * E + triple_kill * F + quadra_kill * G + penta_kill * H) / 1000

    # 首杀评分=首杀次数*C/1000 作废
    #first_blood_score = first_blood_time * C / 1000

    # 战术评分=拆装包评分+特殊击杀评分
    tactics_score = bombScore + kill_score

    return tactics_score

def score():

    # 浮动评分 = ( ( 个人击杀 + 个人助攻 * 0.25 ) * 2.5 / 全队击杀 ) ^ 0.4
    # if k_all == 0:
    #     k_all = 1
    if k_all == 0:

        float_score = ((k + a * 0.25) * 2.5 / 1) ** 0.4

    else:
        float_score = ((k + a * 0.25) * 2.5 / k_all) ** 0.4

    pure_score = pure_score_cal()
    tactics_score = tactics_score_cal()
    # 最终评分=结算底分X + 浮动评分 （若净值评分+战术评分＜0）
    if pure_score + tactics_score < 0:
        score = float_score + X

    else:
        score = float_score + X + pure_score + tactics_score

    return score


if k_all == 0:

    float_score = ((k + a * 0.25) * 2.5 / 1) ** 0.4

else:
    float_score = ((k + a * 0.25) * 2.5 / k_all) ** 0.4

print('底分：', X)

print('净值评分：', '%.1f' % pure_score_cal())

print('战术评分：', '%.1f' % tactics_score_cal())

print('最终评分：', '%.1f' % score())

print('浮动评分：', float_score)

