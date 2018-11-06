# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）
import numpy as np
import pprint
'''此函数更适用于数字数组按照某列进行排序。由于使用np.array()生成的数组内数据类型必须统一，按照字符串大小排序,
并不是此题的答案。作为学习numpy模块的例子，保留此记录。'''


def sort_by_col(a, col_index):
    a1 = a.T  # 对原数组进行转置，此时得到 4*24 数组
    pprint.pprint(a1)
    col_max =int(a.shape[1]-1)    # 得到转置后的最后一行索引，对应原数组的最后一列。
    print(col_max)
    if col_index < col_max:
        # 将a1的索引行与最后一行互换。ps：因经过转置，对应原数组中的列。由此可想到数组的列互换。
        a1[[col_index, col_max],:] = a1[[col_max, col_index],:]
        # 此方法对数组按最后一行元素由小到大排序。此时a1的最后一行即为索引行，也就是转置前的索引列。
        a2 = np.lexsort(a1)
        print('输出排序后的列索引：')
        pprint.pprint(a2)      # 输出排序列索引
        a1[[col_index, col_max], :] = a1[[col_max, col_index], :]   # 换回到行原来的位置，保证a[a2]后与原数组列索引保持一致。
    else:
        a2 = np.lexsort(a1)

    return a[a2]


if __name__ == '__main__':
    path = '../hightemp.txt'
    lines = [tuple(line.strip().split()) for line in open(path, 'r', encoding='utf-8')]
    print('将文本转换成字符串列表后：\n',lines)       # 输出元祖元素的列表
    # 定义一个元组数组中，元组中各元素的数据类型
    t = np.dtype([('KEN', str, 20), ('SHI', str, 20), ('hightemp', float), ('date', str, 20)])
    a = np.array(lines, dtype=t)     # 数组每一行为一个元组，元组中[2]气温数据类型为浮点型。
    print('排序前数组：')
    pprint.pprint(a)           # 输出tuple array，tuple中[2]是浮点型
    b = a.tolist()             # 将array转化为list,形如[[],[]]
    temp_list = []
    for i in b:
        li_i = list(i)
        # print(li_i)
        temp_list.append(li_i)      # temp_list列表中，元素为列表

    c = np.array(temp_list)
    print('更改元组中的数据类型后，生成的数组：')
    pprint.pprint(c)                  # 输出列表数组，list[2]是string。因数组中数据类型必须统一。
    index = 2
    pprint.pprint(sort_by_col(c, 2))










