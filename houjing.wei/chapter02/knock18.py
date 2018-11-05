# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）


from numpy import *
import numpy as np
import pprint


def sort_by_col(a, col_index):
    a1 = a.T
    print(a1)

    col_max = a.shape[0]-1
    print(col_max)

    if col_index < col_max:
        # 将索引列与最后一列互换。ps：因经过转置，在原数组中应为行。
        a1[col_index], a1[col_max] = a1[col_max], a1[col_index]

        a2 = np.lexsort(a1)

        a1[col_index], a1[col_max] = a1[col_max], a1[col_index]
    else:
        a2 = np.lexsort(a1)

    return a[a2]


if __name__ == '__main__':
    path = '../hightemp.txt'
    a = list()
    a.append([line.strip().split() for line in open(path, 'r', encoding='utf-8').readlines()])
    print(a)
    a = np.array(a)
    print(type(a))
    print('排序前：')
    pprint.pprint(a)

    print(sort_by_col(a, 2))









