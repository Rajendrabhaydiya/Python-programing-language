from collections import Counter

def matchingStrings(strings, queries):
    c = Counter(strings)
    return (c[i] for i in queries)

n = int(input())
strings = [input() for _ in range(n)]
q = int(input())
queries = [input() for _ in range(q)]
print(*matchingStrings(strings, queries),sep="\n")
