# 텍스트 파일 읽기#
file = open('D:/python/test.txt', 'r')
result = file.read()
print('type of result: ', type(result))
print('result : ', result)
file.close()

# 텍스트 파일 읽어서 int 계산#
file = open('D:/python/number.txt', 'r')
result = file.read()
print('result = ', result)
sum = int(result) + 1
print('sum = ', sum)
file.close()

# 파일 내용 한 줄씩 리스트 형태#
f = open('D:/python/새파일.txt', 'r')
#line = f.readline() # 첫번째 줄만 읽어 출력
while True: # 모든 줄 읽고 출력
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트를 반환
f = open('D:/python/새파일.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# 파일 쓰기
memo = input('메모를 입력하세요')
file = open('D:/python/myMemo.txt', 'a')
file.write(memo)
file.close()