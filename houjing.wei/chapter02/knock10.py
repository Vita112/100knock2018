# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

def count_line(path):
    count = 0
    for index, line in enumerate(open(r'path', 'r')):
       count += 1

   # return count

file = 'H:\weihoujing\PyCharm Community Edition 2018.2.4\100knock2018\hightem.txt'
print(count_line(file))

