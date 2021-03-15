import itertools

for m in itertools.count():
    if 100000 < m < 100020:
        print (m)
    if m > 1000000:
        break
