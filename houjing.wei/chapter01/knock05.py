# 05. n-gram(单词预测模型)
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
# "I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

raw_t = 'I am an NLPer'
w_list = raw_t.strip().split()
c_list = list(raw_t)
w_list2 = t_list[1:]
c_list2 = c_list[1:]
bigramw = zip(w_list, w_list2)
bigramc = zip(c_list, c_list2)
print bigramw, bigramc
