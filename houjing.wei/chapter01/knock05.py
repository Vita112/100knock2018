# 字符串切分为列表，存放指定位置信息
txt = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
txt = txt.replace('.', '').split()
id_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

# 枚举字符串列表元素，当属于指定位置时，截取元素首字母；否则，截取元素头两个字母，结果返回字典型。
result = {}
for i, word in enumerate(txt):
    if i+1 in id_list:
        result[i+1] = word[0]
    else:
        result[i+1] = word[:2]
        
print(result)        

# 05. n-gram(单词预测模型)
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
# "I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

