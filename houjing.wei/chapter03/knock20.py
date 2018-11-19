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
                with open('../data/knock20.json', 'w+', encoding='utf-8') as f:
                    f.write(dic['text'])


if __name__ == '__main__':
    path = '../data/jawiki-country.json'
    get_UK_data(path)

'''JSON是一种轻量级的数据交换格式。python中导入json库后，
json.dumps()：将python对象（dic）编码为JSON字符串（str），实现格式化输出。
              参数sort_keys=True时，按照字典排序对对象排序；
              参数indent=4表示缩进；
              参数separator的作用是：去掉“""和：”后面的空格，精简数据，方便传输
              参数skipkeys：跳过非string对象，不将其作为key处理。
json.dump():将数据写入json文件中。
json.loads()：将已编码的JSON字符串（str）解码为Python对象（dic）。
json.load()：读取json文件，并把字符串解python数据类型。'''
