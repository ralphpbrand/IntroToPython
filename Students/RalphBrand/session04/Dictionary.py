StringNum = ["zero", "one", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "eleven", "twelve",
    "thirteen", "fourteen", "fifteen"]


HexNum = []

for i in range(16):
    HexNum.append( hex( i ) )

d = {}
for i, j in zip( StringNum, HexNum ):
    d.setdefault( i, j )
print d

e = {}

for i in d:
    e.setdefault( i, i.count("t") )
print e