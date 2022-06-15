infile = open('D:/python/input.txt', 'r')
#나는 처음 3바이트만 읽을꺼야!
str = infile.read(3)
#현재위치는?
position = infile.tell()
print(position)
#내가 위치 바꾸고 싶다, 제일 처음으로~
position = infile.seek(0)
print(position)
infile.close()