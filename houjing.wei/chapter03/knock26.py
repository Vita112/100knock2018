'''26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．'''
import sys
sys.path.append(r'H:\weihoujing\PyCharm Community Edition 2018.2.4\projects\houjing.wei\chapter03')
from knock25 import basicinfo
import re


def emphasis_remove(pathfile):
    dic = basicinfo(pathfile)
    # print(dic)
    emphasis = re.compile(r'(\'\'+)|"')
    for item in dic:
        dic[item] = emphasis.sub('', dic[item])
        # re.sub(pattern, repl, string, count=0, flags=0),
        # 语法解释：在string中按照pattern找到匹配对象，用repl将其替换掉。返回被替换后的string。
        # repl可以是字符串，或函数。字符串中的\被当做转义符号处理。count表示匹配几次。
    return dic


if __name__ == '__main__':
    path = '../data/knock20.json'
    print(emphasis_remove(path))
