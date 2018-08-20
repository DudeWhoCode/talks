class MyList(list):
    def __getitem__(self, item):
        return item+1


a = [1, 2, 3]

for number in a:
    print(number)


b = MyList(a)

for number in b:
    print number