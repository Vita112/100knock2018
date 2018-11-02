# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．


def new_txt(path1, path2):
    with open(path1, 'r', encoding='utf-8') as f_a, open(path2, 'r',encoding='utf-8') as f_b:
        list_a = list(f_a)
        list_b = list(f_b)

    return list_a, list_b


if __name__ == '__main__':
    path_1,path_2 = '../col1.txt', '../col2.txt'
    n_list = list(new_txt(path_1, path_2))
    print(n_list)
    with open('./knock13.txt', 'w', encoding='utf-8') as f_out:
        for line1, line2 in zip(n_list[0],n_list[1]):
            n_line = line1.strip() + '\t' + line2.strip() + '\n'
            print(n_line)
            f_out.write(n_line)
