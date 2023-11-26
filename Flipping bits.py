import sys

t = int(sys.stdin.readline().strip())
for tests in range(t):
    n = int(sys.stdin.readline().strip())
    s = ['0' for x in range(32)]
    s_n = "{0:b}".format(n)
    for x in range(len(s_n)):
        s[31-x] = s_n[len(s_n) - 1 - x]
    for x in range(32):
        if s[x] == '0':
            s[x] = '1'
        else:
            s[x] = '0'
    print(int(''.join(s), 2))

