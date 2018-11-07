'''21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ'''
import re


if __name__ == '__main__':
    with open('../data/knock20.txt', 'r', encoding='utf-8') as f:
        category = re.compile(r'\[\[Category:.+\]\]')
        for line in f.readlines():    # 遍历字符串列表中的str元素。[' ', ' ']
            if category.match(line):
                print(line.strip())



