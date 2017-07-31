


import csv

lee_file = open("lee.txt", "r")
lee_list = []
for line in lee_file:
    lee_list.append(line[:-5].strip().replace(" ",""))

input = open('Remaining.csv', 'rb')
output = open('Remaining_edit.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if row[0] not in lee_list:
        writer.writerow(row)
input.close()
output.close()




input = open('Remaining.csv', 'rb')
output = open('Remaining_edit.csv', 'rb')
count = 0
for row in csv.reader(input):
	count += 1
print 'before: %s' % count 

count = 0
for row in csv.reader(output):
	count += 1
print 'after: %s' % count
input.close()
output.close()
