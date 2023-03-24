import copy
import collections


def first(peoples, k):
    copy_peoples = copy.deepcopy(peoples)
    n = len(copy_peoples)

    while n > 1:
        if n < k:
            indx_del = k - n
            while indx_del > n:
                indx_del -= n

            copy_peoples.pop(indx_del - 1)
        else:
            copy_peoples.pop(n - k - 1)

        n = len(copy_peoples)

    last_el = copy_peoples[0]
    return peoples.index(last_el)


def second(list_):
    _dict = {}
    output = []
    count = len(list_)
    for i in range(4):
        for j in range(count):
            b = list_[j][i]
            if b in _dict:
                _dict[b] += 1
            else:
                _dict[b] = 1
        s = sorted(_dict.items(), key=lambda x: x[1], reverse=True)[0]
        output.append(s[0])
        _dict.clear()

    return ''.join(output)


def thrid(periods: list[tuple]):
    for i in periods:
        if i[0] > i[1]:
            return False

    sorted_periods = sorted(periods, key=lambda x: x[0])
    count = len(sorted_periods)

    for i in range(0, count-1):

        elem, next = sorted_periods[i][1], sorted_periods[i+1][0]
        if elem > next:
            return False

    return True


if __name__ == '__main__':
    # peoples = ["pet", "karl", "nil", "bill"]
    # print(first(peoples, 6))

    # list_ = ["ATTA", "ACTA", "AGCA", "ACAA"]
    # print(second(list_))

    periods = [(1, 3), (6, 8), (9, 12), (17, 20), (14, 16), (4, 5)]

    if thrid(periods):
        print("Хватит")
    else:
        print("Не хватит")

