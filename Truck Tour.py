a=[]

for i in range(int(input())):
    a.append(list(map(int, input().split())))
    a[i] = a[i][0] - a[i][1]

sum = 0
fin = 0
shift = 0
while (fin < len(a)):
    sum+=a[fin]
    if sum < 0:
        for _ in range(fin + 1):
            a.append(a.pop(0))
        sum = 0
        shift += fin + 1
        fin=0
    else:
        fin = fin + 1
            
print (shift)
