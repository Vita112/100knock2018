# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．


def col_list(pathfile):
    # result = []
    # line_array =[]
    for line in open(pathfile, 'r', encoding='utf-8'):
        # line_array = line.split(' ')
        return line.split(' ')
        # result.append(line_array[n-1] + '\n')
    # return line_array
if __name__ == '__main__':
    path = '../hightemp_test.txt'
    # col_list(path, 1)

    with open('../col1.txt', 'w',encoding='utf-8') as col1_out, open('../col2.txt', 'w') as col2_out:
        for col_list in col_list(path):
            # new_str = ''.join(col_list(path, 1))
            # print(new_str)
            col1_out.write(col_list[0])
            # col2_out.write(new_str)









