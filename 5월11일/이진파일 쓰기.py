outfile = open('D:/python/binary', 'wb')

byteArray = [1,2,3,4,5]
outfile.write(bytes(byteArray))

outfile.close()

#이진파일 읽기
infile = open('D:/python/binary', 'rb')
byteArray = infile.read()
for b in byteArray:
    print(b)
infile.close()