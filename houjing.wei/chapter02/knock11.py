# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．


def tab_to_space(pathfile):
    f = open(pathfile, 'r', encoding='utf-8').read()              # 使用utf-8编码，本地文件使用utf-8保存。
    temp_f = f.replace('\t', ' ')
    with open(pathfile, 'w+', encoding='utf-8') as new_f:
        new_f.write(temp_f)  # 以读写模式打开文件，读取文件内容，修改后关闭。此时内容从内存中写入磁盘。


if __name__ == '__main__':
    path = '../hightemp.txt'
    tab_to_space(path)
    new_f = open(path, 'rb').read()  # 以二进制形式打开并读取文件,此时不需要指定

    print(new_f)  # 打印结果显示，'\t'已经被空格代替

