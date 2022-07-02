import pandas as pd
import numpy as np
import xlrd

win = 1
rank_lv = 101

res_score = 0 # 结算评分
if res_score == 0:
    res_score += 1

# 胜场战力分
path2 = 'D:\\pythonProject\\excel\\HeroScore_Config.xlsx'

wb = pd.read_excel(path2, sheet_name='胜场分差值参考表', header=None, engine="openpyxl")
#
# res = 1 # 1 win 0 fail
# cur_win_score = 0
#
# standard_diff = []
#
# if res == 1:
#     for i in range(8,28):
#         standard_diff.append(wb[5][i])
#     print(standard_diff)
#
# else:
#     for i in range(28,37):
#         print(wb[5][i])
#
#
#
#
# 查rank_config 找英雄胜场评分段位标准
path3 = 'D:\\pythonProject\\excel\\Rank_Config.xlsx'
wb3 = pd.read_excel(path3, sheet_name='Rank_Table', header=None, engine="openpyxl")
# win_standard = []
#
# for i in range(8,31):
#     win_standard.append(wb3[5][i])
#
# print(win_standard)
#
#
#
# # 根据目前段位，定位当前标准分的行数
# row_num = 0
# for i in range(8,31):
#     if wb3[1][i] == rank_lv:
#         #print(i)
#         row_num = i
#
# # 根据得到的行数，找到当前段位的胜场标准分
# win_standard_index = wb3[5][row_num]
#
# print(win_standard_index)
#
# # 根据取到的胜场标准分计算diff
# diff = cur_win_score - win_standard_index
# print('diff:', diff)
#
# # 根据diff找加成系数
#
# range_index = 0
#
# for i in range(len(standard_diff)):
#     if diff > standard_diff[i]:
#         range_index = i + 8
#         print(range_index)  # 定位到第n行
#         break
#
# #  找对应的加成系数
# Hero_ScoreGap_Mum = wb[6][range_index]
# print('对应的胜场战力加成系数', Hero_ScoreGap_Mum)
#
# #计算最终 胜场战力分
# new_win_score = 20 * (1 + Hero_ScoreGap_Mum/10000)
#
# print('增加的胜场战力分：', new_win_score)


#                                                              ### 排位表现分 ###
#
# # 读表“排位结算表现分加成”
#
# wb4 = pd.read_excel(path2, sheet_name='排位结算表现分加成', header=None, engine="openpyxl")
#
# res_score_range = []
# row_num2 = 0
# if win == 1:
#     for i in range(8, 16):
#         if res_score > wb4[4][i]:
#             row_num2 = i
#             break
#
#
#         #res_score_range.append(wb4[4][i])
# else:
#     for i in range(17,24):
#         if res_score > wb4[4][i]:
#             row_num2 = i
#             break
#
# print('结算分行数', row_num2)
#
#
# #根据行数找加成系数
# Hero_ScoreRank_Num = wb4[5][row_num2]
#
#
# # for i in range(8,24):
# #     Hero_ScoreRank_Num_l.append(wb4[5][i])
# #     #Hero_ScoreRank_Num_l = wb4
#
#
# print('结算分加成系数', Hero_ScoreRank_Num)
#
# # 根据实际结算评分，找到加成系数那一行
# # row_num2 = 0
# # #print(res_score)
# # for i in range(len(res_score_range)):
# #     #print(res_score_range[i])
# #     if res_score > res_score_range[i]:
# #         row_num2 = i
# #     #break
# #
# # print('结算分行数', row_num2)
# # Hero_ScoreRank_Num = Hero_ScoreRank_Num_l[row_num2]
# # print('结算分加成系数：', Hero_ScoreRank_Num)
#
# # 根据目前段位标准分找表现分段位系数
# cur_res_score = 0
# res_standard = []
# for i in range(8,31):
#     res_standard.append(wb3[6][i])
#
# print('表现分标准：', res_standard,len(res_standard))
#
# # 根据目前段位取表现分标准
# row_num3 = 0
# for i in range(8,31):
#     if wb3[1][i] == rank_lv:
#         #print(i)
#         row_num3 = i
#
# # 根据得到的行数，找到当前段位的表现标准分
# res_standard_index = wb3[6][row_num3]
#
# print('表现标准分：', res_standard_index)
#
# # 根据取到的胜场标准分计算diff
# diff2 = cur_res_score - res_standard_index
# print('diff:', diff2)
#
# # 根据diff来找段位表现分系数行数
# row_num4 = 0
# if win == 1:
#     for i in range(8,28):
#         #print(wb[5][i])
#         if diff2 > wb[5][i]:
#             row_num4 = i
#
#     print('行数',row_num4)
#
# if win == 0:
#     for i in range(9,38):
#         # print(wb[5][i])
#         if diff2 > wb[5][i]:
#             row_num4 = i
#             break
#
#
#
#
# res_config = wb[6][row_num4]
# print('胜场分差值系数：', res_config)


# 计算最终表现分
# base_score = 0
# if win == 1:
#     base_score = 30
#
# else:
#     base_score = -20
#
# res_final_score = base_score * (Hero_ScoreRank_Num/10000)
# print('对局表现分：', res_final_score)


    




