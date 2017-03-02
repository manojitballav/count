import collections

wordcount = collections.Counter()
with open("C:\\Users\\Xiaomi\\Documents\\count\\text.txt","r+") as file:
    for line in file:
        wordcount.update(line.split())

for k,v in wordcount.iteritems():
    print k,v