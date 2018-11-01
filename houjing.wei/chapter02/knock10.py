# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

import os
import sys

def count_line(path):
    line_num = 0            # 全局变量，函数返回值
    for i, line in enumerate(open(path,'r',encoding='utf-8')):     # 索引枚举迭代器中的元素，返回迭代器对象
        line_num += 1
        # print(line_num,line)   # 打印行号，内容
    return line_num

if __name__ == '__main__':
    f = '../hightemp.txt'      # 文件相对路径
    # print(os.getcwd())   打印文件所在路径
    print(count_line(f))

