'''
#1. file open
outfile = open('D:/python/input.txt','w')

#2. file read, write
outfile.write('hello hello hello!\n')
print('홍길동', file = outfile)
age = 20
outfile.write('홍길동 나이 %s\n' % age)

#3.file close
outfile.close()
'''
############
'''
#file read
#한 줄 단위로 읽기
infile = open('D:/python/input.txt', 'r')
for line in infile:
    print(line, end= '')
infile.close()
'''
#한 줄 단위로 읽은 다음 단어 분리해 볼까?
infile = open('D:/python/input.txt', 'r')
for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()