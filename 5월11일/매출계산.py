infile = open('D:/python/input.txt', 'r')
outfile = open('D:/python/summary.txt', 'w')

sum = 0
count = 0
line = infile.readline()
while line !='':
    s = int(line)
    sum += s
    count += 1
    line = infile.readline()

outfile.write("총 매출: " + str(sum) + '\n')
outfile.write("평균 일 매출: " + str(sum/count) + '\n')

infile.close()
outfile.close()