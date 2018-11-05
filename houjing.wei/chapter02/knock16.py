# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．


def file_split(pathfile, n):
    with open(pathfile, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines_size = int(len(lines))
    unit_size = lines_size//n
    res = lines_size%n
    indeces = [0]
    for i in range(1, n):
        indeces.append(indeces[-1]+unit_size)
        if res >0:
            indeces[-1]+=1
            res -=1
    indeces.append(lines_size)

    for i in range(len(indeces)):
        with open('../hightemp_split"+_str(i)+".txt', 'rw', encoding ='utf-8') as output_file:
            output_file.writelines(lines[indeces[i]:indeces[i+unit_size]])


if __name__ == '__main__':
    path = '../hightemp.txt'
    input_num = int(input('文本将被切分 次？' ))
    file_split(path,input_num)
