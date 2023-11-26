n = int(input())
ar = list(map(int, input().split()))

tot = [0]*100

for j in range(0,n):
    temp = ar[j]
    tot[temp] += 1
print(*tot, sep =' ')    
