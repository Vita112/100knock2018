# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．


def tail(pathfile, n):
    with open(pathfile, encoding='utf-8') as f:
        lines = f.readlines()
        result = []
        for i in range(1, n):
            i = -i
            result.append(lines[i].strip())
        result.reverse()

    return print(result)


if __name__ == '__main__':
    path = '../hightemp_test.txt'
    tail(path, 6)
