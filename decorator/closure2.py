from urllib.request import urlopen

def index(url): # url也属于函数内部
    def get():
        return urlopen(url).read()
    return get

python = index("http://www.python.org") # 返回的是get函数的地址
print(python()) # 执行get函数《并且将返回的结果打印出来
baidu = index("http://www.baidu.com")
print(baidu())