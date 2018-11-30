'''27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．'''
from knock26 import emphasis_remove
import re

def linkMarkup_remove(pathfile):
    dic = emphasis_remove(pathfile)
    linkMarkup= re.compile(r'.*(\[http:.*).*')
    for item in dic:
        linkMarkupstr = linkMarkup.search(dic[item])
        if linkMarkupstr:
            linkMarkupSub_temp =linkMarkupstr.group(1).split()
            linkMarkupSub = re.sub(r'/{1,}',r'_',linkMarkupSub_temp[0])
            # 匹配‘//‘或’/‘后，使用’_'替换，虽然去除了链接，但是改变了内容
            # print(linkMarkupSub)
            dic[item] = linkMarkupSub

    return dic




if __name__ == '__main__':
    path = '../data/knock20.json'
    print(linkMarkup_remove(path))
