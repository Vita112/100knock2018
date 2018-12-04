import MeCab

sentence = '太郎はこの本を二郎を見た女性に渡した。'
mecab = MeCab.Tagger('-Ochasen')
mecab_wakati = MeCab.Tagger('-Owakati')
mecab_yomi = MeCab.Tagger('-Oyomi')
print(mecab.parse(sentence))
print(mecab_wakati.parse(sentence))
print(mecab_yomi.parse(sentence))