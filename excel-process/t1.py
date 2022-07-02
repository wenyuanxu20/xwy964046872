# import requests, json
#
# url = 'http://redmineapi.nie.netease.com/api/custom_query'
# # generate get data
# param = {}
# param['token'] = 'd4dc67a34d8dc1a8d092b732af11bd6e'
# param['host'] = 'qatools.pm.netease.com'
# param['project'] ='c1'
# param['query_id'] = 86
# param['offset'] = '0'
#
#
# #get data
# r = requests.get(url, params=param)
# result = r.json()
# print(result)

import requests


url = 'http://redmineapi.nie.netease.com/api/status'
# generate get data
param = {}
param['token'] = 'd4dc67a34d8dc1a8d092b732af11bd6e'  # 填写自己的token
param['host'] = 'qatools.pm.netease.com'


#get data
r = requests.get(url, params=param)
if r.status_code==200:
    result = r.json()
    print(result)


