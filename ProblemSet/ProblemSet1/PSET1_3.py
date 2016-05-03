s = 'azcbobobegghakl'
found = list()
index = 0

for i in range(0,len(s)-1):
    #print 'index = ', index
    #print s[i], s[i+1]
    if s[i] <= s[i+1]:
        #print True
        found.append(s[index:i+2])
    else:
        #print False
        #print i
        found.append(s[i])
        index = i + 1
print found

print "Longest substring in alphabetical order is:", max(found, key=len)