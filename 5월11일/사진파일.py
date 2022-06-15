infile = open('D:/python/123.jpg', 'rb')
outfile = open('D:/python/1234.jpg', 'wb')

while True:
    buf = infile.read(1024)
    if not buf:
        break
    outfile.write(buf)

infile.close()
outfile.close()