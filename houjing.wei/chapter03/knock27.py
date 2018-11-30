'''27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．'''
from knock26 import emphasis_remove
import re

def linkMarkup_remove(pathfile):
    dic = emphasis_remove(pathfile)
    # linkMarkup= re.compile(r'\[http:.*')
    for item in dic:
        linkMarkupstr = re.search(r'\[http:.*',dic[item]).group()
        if linkMarkupstr in dic[item]:
            print(linkMarkupstr)
        # if linkMarkupstr in item:
        #      dic[item] = ''.join(dic[item])
        # else:
        #     dic[item] =item

    return dic




if __name__ == '__main__':
    path = '../data/knock20.json'
    print(linkMarkup_remove(path))
