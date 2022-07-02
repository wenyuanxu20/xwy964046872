                                                             ### 排位表现分 ###



# 读表“排位结算表现分加成”

wb4 = pd.read_excel(path2, sheet_name='排位结算表现分加成', header=None, engine="openpyxl")

res_score_range = []

if win == 1:
    for i in range(8,16):
        res_score_range.append(wb4[4][i])
else:
    for i in range(17,24):
        res_score_range.append(wb4[4][i])

print('res_score_range', res_score_range)

#根据行数找加成系数
Hero_ScoreRank_Num_l = []
#Hero_ScoreRank_Num_l = wb4[5]

for i in range(8,24):
    Hero_ScoreRank_Num_l.append(wb4[5][i])
    #Hero_ScoreRank_Num_l = wb4


print('结算分加成系数', Hero_ScoreRank_Num_l)

# 根据实际结算评分，找到加成系数那一行
row_num2 = 0
#print(res_score)
for i in range(len(res_score_range)):
    #print(res_score_range[i])
    if res_score > res_score_range[i]:
        row_num2 = i
    #break

print('结算分行数', row_num2)
Hero_ScoreRank_Num = Hero_ScoreRank_Num_l[row_num2]
print('结算分加成系数：', Hero_ScoreRank_Num)

# 根据目前段位标准分找表现分段位系数
cur_res_score = 0
res_standard = []
for i in range(8,31):
    res_standard.append(wb3[6][i])

print('表现分标准：', res_standard,len(res_standard))

# 根据目前段位取表现分标准
row_num3 = 0
for i in range(8,31):
    if wb3[1][i] == rank_lv:
        #print(i)
        row_num3 = i

# 根据得到的行数，找到当前段位的表现标准分
res_standard_index = wb3[6][row_num3]

print('表现标准分：', res_standard_index)

# 根据取到的胜场标准分计算diff
# diff = cur_win_score - win_standard_index
# print('diff:', diff)

# 根据取到的系数来计算排位结算表现分
# base_score = 0
# if win == 1:
#     base_score = 30
#
# else:
#     base_score = -20
#
# res_final_score = base_score * (Hero_ScoreRank_Num/10000)
# print('对局表现分：', res_final_score)