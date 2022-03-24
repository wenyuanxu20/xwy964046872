class Deco(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Deco    # test = Deco(test)
def test():
    print('test')


test()    # Deco(test)()

# 结果
# class decorator runing
# test
# class decorator ending