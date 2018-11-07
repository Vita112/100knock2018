'''20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．'''
import json


def get_UK_data(pathfile):
    with open(pathfile, encoding='utf-8') as f:
        for line in f.readlines():
            dic = json.loads(line)  #JSON数据已转换为python字典型
            # print(dic)
            # print(type(dic))    print(dic['title'])
            if dic['title'] == 'イギリス':
                with open('../data/knock20.json', 'w', encoding='utf-8') as f:
                    f.write(dic['text'])





if __name__ == '__main__':
    path = '../data/jawiki-country.json'
    get_UK_data(path)


