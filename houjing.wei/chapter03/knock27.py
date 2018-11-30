'''27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．'''
from knock26 import emphasis_remove
import re

dic = emphasis_remove()
linkMarkup= re.compile()
