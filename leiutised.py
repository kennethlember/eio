f = open("eio/ykssis.txt", "r")

A = f.readline()
print(A)

alist = A.split()
amath = int(alist[0]) + int(alist[1]) * 10
print(amath)

maksimum = amath

leiutised = []
for line in f:
    print(line)
    data = line.split()
    math = int(data[0]) + int(data[1]) * 10
    print(math)
    if maksimum > math:
        print(0)

print(leiutised)
