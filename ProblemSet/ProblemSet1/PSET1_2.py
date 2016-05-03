start = 0
match = 0

while True:
    start = s.find('bob', start)
    if start < 0:
        break

    start += 1
    match += 1

print 'Number of times bob occurs is:', match