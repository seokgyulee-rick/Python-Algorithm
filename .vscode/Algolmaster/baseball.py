T = int(input())
ary = []
for i in range(T):
    num, k, b = map(int,input().split())
    ary.append({'num': num, 'k':k, 'b':b})

for i in range(1000):
    n = str(i).zfill(3)
    if(n[0] == n[1] or n[1] == n[2] or n[0] ==n[2]):
        continue
    else:
        for j in ary:
            if(j.k == 1):
                

