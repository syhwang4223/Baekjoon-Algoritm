s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)

lcs = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

for i in range(1,l1+1):
    for j in range(1,l2+1):
        if s1[i-1]==s2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
            
print(lcs[-1][-1])
for l in lcs:
    print(l)
