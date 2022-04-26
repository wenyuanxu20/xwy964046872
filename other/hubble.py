# -*- coding:utf-8 -*-
import urllib3
import urllib.request
import json
import requests

data = {
    "scope": "test",#release
    "device_model": "vivo/vivo X9",
    "user_name": "七月是你谎言",
    "user_id": "88888888",
    "platform":"android",
    "host_id":1001,
    "engine_version":"1.1.1",
    "script_version":"1.1.1",
    "channel":"app_store",
    "gpu_name":"Apple A7 GPU",
    "os_version":"ios 10.2",
    "fps": 50,
    "vertex_count":1000,
    "draw_call": 1000,
    "mem_usage":1024*1024*500
}
headers = {'Content-Type': 'application/json'
       }
url = 'https://sigma-performance-c1hmt.proxima.nie.netease.com'
url1 = 'https://sigma-performance-c1na.proxima.nie.easebar.com'
response = urllib.request.urlopen(url=url1)
the_page = response.read()
print(the_page)