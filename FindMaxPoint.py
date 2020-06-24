import sys
# input
List = []
list_new = []
num = 0
for line in sys.stdin:
    list_new = line.split()
    List.extend(list_new)
    if len(List) >= (int(List[0])*2+1):
        List = List[0:int(List[0])*2+1]
        break
# convert str to int
num = int(List[0])
array = [0]*(len(List)-1)
x = []
y = []
delIndex = []

for i,element in enumerate(List[1:]):
    if (i % 2) == 0:
        x.append(int(element))
    else:
        y.append(int(element))

axi0 = x.copy()
axi0.sort()
# for i in range(num):
for i,element in axi0:
    if element != axi0[-1]:
        if y[x.index(element)] :
            delIndex.append(i)

delIndex = list(set(delIndex))
originalx = x.copy()
originaly = y.copy()
for i in delIndex:
    originalx.remove(x[i])
    originaly.remove(y[i])

x = originalx
y = originaly

temp = x.copy()
x.sort()

for axi0,axi1 in zip(x,y):
    print(axi0,y[temp.index(axi0)])

