#!/usr/bin/env python3

def rl(T=str):
    return list(map(T,input().split()))

T, = rl(int)
for _ in range((T)):
    N,K = rl(int)
    A = rl(int)
    B = rl(int)
    A.sort()
    B.sort(reverse=True)
    bad = len([a+b for a,b in zip(A,B) if a+b<K ])>0
    print("NO" if bad else "YES")
