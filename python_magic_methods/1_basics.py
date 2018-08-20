def foo():
    print(1 + 5)
    print('a' + 'b')

    print(dir(1))
    print(dir('a'))

    print(int('1').__add__(1))

    print('a'.__add__(' b'))


if __name__ == '__main__':
    foo()