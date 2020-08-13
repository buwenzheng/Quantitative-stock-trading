# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def testPrototype():
    math_store = {
        'Manadon': 1
    }
    # print(math_store, id(math_store))
    xList = [1, 2, 3]
    its = xList.__iter__()
    # print(its)
    # print(next(its))
    #  遍历一个范围内的数字
    # for i in range(2):
    #     print(i)
    #     正/反向遍历一个集合
    colors = ['red', 'green', 'gray', 'blue', 'yellow']
    names = ['huawei', 'xiaomi']
    # 正序
    # for i in range(len(colors)):
    # print(colors[i])
    # 倒序
    # for color in reversed(colors):
    #     print(color)
    #     遍历集合及其下标 enumerate()
    # for i, color in enumerate(colors):
    #     print(i, color)
    # #         遍历两个集合
    # for name, color in zip(names, colors):
    #     print(name, color)
    # lambda s:s[1]
    # def keyProcess(s):
    #     print('keyProcess', s[0])
    #     return s[1]
    #    5、 有序遍历 key reverse
    colors2 = [('red', 1), ('green', 3), ('blue', 5), ('yellow', 2)]
    for color in sorted(colors2, key=lambda s: s[1], reverse=True):
        print(color)

    # 遍历字典key value


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testPrototype()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
