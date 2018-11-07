'''23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．'''
import re


if __name__ == '__main__':
    with open('../data/knock20.txt', 'r', encoding='utf-8') as f:
        section = re.compile(r'==(.+)==')
        lable = 1
        for line in f.readlines():
            if section.match(line):
                print('[' + str(lable) + ']:' + line.strip())
                lable += 1

