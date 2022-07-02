import pandas as pd
import numpy as np
import xlrd

target = []
info = []
line = 0
rank = '101'

path1 = 'D:\\pythonProject\\excel\\Rank_Config.xlsx'

wb = pd.read_excel(path1, sheet_name=None, header=None, engine="openpyxl", )

for sheetname, content in wb.items():
    #print('df',df)
    for row_index, row in content.iterrows():
        for val in row:
            val = str(val)
            if val is np.nan:
                continue
            if val == rank:
                #target.append((sheetname, row_index + 1))
                line = row_index

wb1 = pd.read_excel(path1, header=None)

key = wb1.loc[line].values

#print(key)

win_score_limit = key[3]  # 英雄胜场评分段位限制

rank_score_limit = key[4]  # 英雄排位表现评分段位限制

win_score_standard = key[5]  # 英雄胜场评分段位标准

rank_score_standard = key[6]  # 英雄排位表现分标准

rank_score_add = key[7]  # 英雄评分段位加成系数

print('胜场评分限制：', win_score_limit)



# 英雄战斗力评分=（胜场战力分+排位表现分）*（段位系数+时间系数）



# pre_rating = 1000 # 当前评分
#
# rank_config = 0 / 10000
#
# time_config = 10000 /10000
#
# win_score = 20
#
# rank_score = 20
#
# rating = (win_score + rank_score) * (rank_config + time_config)
#
# print(rating)


