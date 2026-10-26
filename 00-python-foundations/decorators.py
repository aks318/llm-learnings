def mydecorator(aks):
    def outWrapper(func):
        def innerwrapper(*arg):
            print("============================")
            b = 5
            func(*arg, b, aks)
            print("============================")
        return innerwrapper
    return outWrapper

def mydecorator2(k):
    def outWrapper(func):
        def innerwrapper(*arg):
            print("============================")
            a = 6
            func(a, k, *arg)
            print("============================")
        return innerwrapper
    return outWrapper


@mydecorator(23)
@mydecorator2(32)
def akash(*arg):
    print (f"hello world {arg}")

akash()


def checkDt(*args):
    print(type(*args))

checkDt(1)
checkDt("1")
checkDt([1,2])