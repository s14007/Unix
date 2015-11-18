# coding: UTF-8
import datetime
f = open('access.log.1')
data = f.read().split('\n')
f.close()

i = 0
max_size = len(data) - 1

while i < max_size:
    line = data[i]
    rear_cut = line[14:]
    unixTime = float(line[0:13])
    dateTime = datetime.datetime.fromtimestamp(unixTime)

    print str(dateTime) + rear_cut
    i += 1
