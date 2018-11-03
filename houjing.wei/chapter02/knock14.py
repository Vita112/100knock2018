# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．


import itertools


def head(pathfile, n):
    with open(pathfile, 'r', encoding='utf-8') as f:
        for x in itertools.islice(f, 0, n):
            print(x.strip())


if __name__ == '__main__':
    path = '../hightemp.txt'
    head(path, 6)


