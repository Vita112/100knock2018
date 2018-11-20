'''25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．'''
import json
import demjson
import re


# 打开并解码json文件
def basicinfo(path):
    dic = {}
    with open(path, 'r', encoding='utf-8') as f:
        fstr = f.read().replace('\n', '  ').replace('\n\n','  ').split('  ')     # class str，以双空格切分字符串后，存入列表
        # print(fstr)
        for i in fstr:
            if '基礎情報' in i:
                print(i)
            if '=' in i:
                i = i.split(' = ')
                dic[i[0]] = i[1]
                print(dic)
            if i == '}}':     # 当代码为 "'if '}}' in i:  break  "时，为什么不显示"print(dic)"打印结果。
                break








if __name__ == '__main__':
    pathfile = '../data/knock20.json'
    basicinfo(pathfile)

