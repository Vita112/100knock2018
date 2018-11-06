# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．


def col_list(pathfile):
    result = []
    for line in open(pathfile, 'r', encoding='utf-8').readlines():    # 打开并读取文件的所有行
        line_array = line.strip().split()                            # 去掉字符串首位的空格，并以空格切分每一行，返回字符串列表
        result.append(line_array)                                    # 将字符串列表追加至result列表中

    return result


if __name__ == '__main__':
    path = '../hightemp.txt'
    list = col_list(path)

    # 'with open('文件路径',模式,编码) as 文件名:'：以某种模式打开'文件路径'的文件，执行语句后自动关闭
    with open('../knock12_col1.txt', 'w',encoding='utf-8') as col1_out, open('../knock12_col2.txt', 'w',encoding='utf-8') as col2_out:

        for i in list:
            col1_out.write(i[0]+'\n')               # 将内容写入'文件路径'文件中
            col2_out.write(i[1]+'\n')










