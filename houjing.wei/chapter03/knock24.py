'''24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．'''
import re


if __name__ == '__main__':
    with open('../data/knock20.txt', 'r', encoding='utf-8') as f:
        # 把正则表达式编码为pattern对象
        head = re.compile(r'\|略名.+')
        mediafile = re.compile(r'.*(ファイル|File|file):(.*[a-zA-Z0-9]+.*)')
        section = re.compile(r'\=\=(.+)\=\=')
        lable = 1
        for line in f.readlines():
            if head.match(line):
                print(line)
            if section.match(line):
                print('[' + str(lable) + ']:' + line.strip())
                lable += 1
            file = mediafile.findall(line)
            if file:
                print(''.join(file[0][0])+':'+''.join(file[0][1]))

