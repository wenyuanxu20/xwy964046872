# https://www.cnblogs.com/huchong/p/7725564.html
import time, random


def outer(func):  # 将index的地址传递给func
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)   # fun = index  即func保存了外部index函数的地址
        end_time = time.time()
        print("运行时间为%s"%(end_time - start_time))
    return inner  # 返回inner的地址


@outer
def index():
    time.sleep(random.randrange(1, 5))
    print("welcome to index page")

#index = outer(index)  # 这里返回的是inner的地址，并重新赋值给index

index()