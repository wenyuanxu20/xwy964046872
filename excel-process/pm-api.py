import requests
import json

# http://redmineapi.nie.netease.com/home/#/api/doc#query_tracker

url = 'http://redmineapi.nie.netease.com/api/filter_query_v6' #'http://redmineapi.nie.netease.com/api/project'
# generate get data
param = {}
param['token'] = 'd4dc67a34d8dc1a8d092b732af11bd6e' #填写自己的token
param['host'] = 'm1.pm.netease.com'
#param['issue_id'] = '49060'
param['project'] = 'c1'
param['f'] = ['assigned_to_id','status_id']
param['op'] = json.dumps({'assigned_to_id':'=','status_id':'o'})
param['v'] = json.dumps({'assigned_to_id':[274]})

#get data
r = requests.get(url, params=param)
result = json.loads(r.text)
print(result)
print(param)


