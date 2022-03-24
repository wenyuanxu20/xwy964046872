# x = 1
# def funx():
#     def fun1():
#
#     #x = 10
#         print(x)  # 打印出10
#     fun1()
#
# funx()
# print(x) # 打印出1
#
#
# # 高级函数
# # 1. 函数名作为返回值
# def outer():
#     def inner():
#         pass
#     return inner
#
# s = outer()
# print(s)  #  <function outer.<locals>.inner at 0x000002369A2B4438>
#
# # 2. 函数名作为参数
#
# def index():
#     print("index func")
#
#
# def outer(index):
#     s = index
#     s()
#
# outer(index)

# 闭包函数必须满足两个条件:1.函数内部定义的函数 2.包含对外部作用域而非全局作用域的引用
# x = 1 不能引用全局变量
y = 2
def outer():
    x = 1
    def inner():  # 1.函数内部定义的函数
        print("x=%s" % x)  # 2.包含对外部作用域而非全局作用域的引用
        print("y=%s" % y)
        print("inner func excuted")

    print('inner.__closure__', inner.__closure__)
    inner()
    print("outer func excuted")
    return inner

print(outer())