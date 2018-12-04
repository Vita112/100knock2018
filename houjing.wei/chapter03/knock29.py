'''29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）'''
from knock25 import basicinfo
import re
import requests

def get_url(svgyname):
    param = {'action':'query','format':'json','prop':'imageinfo','iiprop':'url','titles':'File:{}'.format(svgyname)}
    response = requests.get(r'https://en.wikipedia.org/w/api.php',params=param)
    return response.json()

if __name__ == '__main__':
    basicinfodic = basicinfo('../data/knock20.txt')
    # result = ''
    for item in basicinfodic:
        if item == '|国旗画像':
            svgname = basicinfodic[item]
            urlstr = str(get_url(svgname))
            print(urlstr)
            pattern = re.compile(r"'url':'\s(.+)'")
            result = pattern.search(urlstr)
            print(result.group(1))
        else:
            pass


