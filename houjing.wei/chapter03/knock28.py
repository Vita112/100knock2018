'''28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．'''
from knock27 import linkMarkup_remove


def wikimark_remove(path):
    with open(path, 'w+', encoding='utf-8') as f:
        dic = linkMarkup_remove('../data/knock20.json')
        for item in dic:
            n_value = dic[item]+'\n'
            dic[item] = n_value
            f.write(item + '=' + dic[item])
    return print(dic)


if __name__ == '__main__':
    path = '../data/knock28.txt'
    wikimark_remove(path)

