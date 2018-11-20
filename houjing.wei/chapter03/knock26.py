'''26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．'''
import sys
sys.path.append(r'H:\weihoujing\PyCharm Community Edition 2018.2.4\projects\houjing.wei\chapter03')
from knock25 import basicinfo
import re


def emphasis_remove():
    dic = basicinfo('../data/knock20.json')
    # print(dic)
    emphasis = re.compile(r'(\'\'+)|"')
    for item in dic:
        dic[item] = emphasis.sub('', dic[item])
    return dic


# if __name__ == '__main_':
    # path = '../data/knock20.json'
print(emphasis_remove())
