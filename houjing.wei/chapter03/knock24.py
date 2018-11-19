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
        for line in f.readlines():    # 遍历逐行读取文件所有行，line为字符串
            if head.match(line):
                print(line)
            if section.match(line):       # 列出并打印分区名
                print('[' + str(lable) + ']:' + line.strip())
                lable += 1
            file = mediafile.findall(line)
            '''findall(str)将在str中从最开始查找符合pattern对象的内容，返回列表。
            本题列表中只有一个元组元素，元组中包含两个字符串
            '''
            if file:
                print(''.join(file[0][0])+':'+''.join(file[0][1]))   # 列表元素字符串化

    # 本题的最终输出效果为：输出每个分区名，列出每个分区下的文件名。
