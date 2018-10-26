# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# （例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
# その実行結果を確認せよ．

import random

def shuffle_str():
    w_list = raw_txt.replace(':', '').replace('.', '').strip().split()
    print w_list
    result = ''
    for w in w_list:
        if len(w) < 4:
            n_word = w
        else:
            n_word = w[0] + ''.join(random.shuffle(list(w[1:-2]))) + w[-1]
        result += n_word
        
    return result
                
    


if __name__ == '__main__':
    raw_txt = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    
    
