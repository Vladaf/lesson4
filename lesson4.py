from functools import wraps


all_res = []
all_names = []


def res_save(func):
    @wraps(func)
    def _wrapper(*args):
        all_res.append(func(*args))
        func(*args)
    return _wrapper


def name_save(func):
    @wraps(func)
    def _wraps(*args):
        all_names.append(func.__name__)
        func(*args)      
    return _wraps


@name_save
@res_save
def func1(a, b):
    res = a + b
    return res


@name_save
@res_save
def func2(a, b):
    res = a ** b
    return res


@name_save
@res_save
def func3():
    res = 'Test text'
    return res


def main():
    func1(3, 6)
    func2(4, 5)
    func3()
    print("\n\nИмя декорируемой функции:\tРезультат:")
    for n, r in zip(all_names, all_res):
        print("\t\t" + str(n) + "\t\t   " + str(r))
    print("\n")


if __name__ == '__main__':
    main()