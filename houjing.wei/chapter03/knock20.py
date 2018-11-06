'''20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．'''
import json


# with open(pathfile, 'r') as f:
#     print(json.load(f))




if __name__ == '__main__':
    path = '../data/jawiki-country.json'
    with open(path, encoding='utf-8') as f:
        for line in f.readlines():
            d = json.loads(line)  #JSON数据已转换为python字典型
            # print(type(d))
            print(d)
