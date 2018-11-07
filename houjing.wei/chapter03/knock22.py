'''22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ'''
import re


if __name__ == '__main__':
    with open('../data/knock20.txt', 'r', encoding='utf-8') as f:
        category = re.compile(r'\[\[Category:.+\]\]')
        category_name = re.compile(r':')
        for line in f.readlines():
            if category.match(line):
                print(category_name.split(line)[1].strip())
