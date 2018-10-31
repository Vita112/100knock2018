# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．


def tab_to_space(pathfile):
    f = open(pathfile,'r').read()
    temp_f = f.replace('\t',' ')
    with open(pathfile,'w') as new_f:
        new_f.write(temp_f)
        for line in open('new_f'):
            print(line)
    return new_f


if __name__ == '__main__':
    path = '../hightemp.txt'
    print(tab_to_space(path))