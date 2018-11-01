# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．


def col_list(pathfile, n):
    result = []
    for line in open(pathfile,'r').readlines():
        line_array = line.split(' ')
        result.append(line_array[n-1] + '\n')
    print(result)

if __name__ == '__main__':
    path = '../hightemp.txt'
    col_list(path,1)

