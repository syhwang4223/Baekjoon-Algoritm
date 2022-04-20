from sys import stdin

n = int(stdin.readline())
wordCount = {}
for i in range(n):
    word = stdin.readline().rstrip()
    for j in range(len(word)):
        if word[j] in wordCount:
            wordCount[word[j]] += pow(10, len(word)-j-1)
        else:
            wordCount[word[j]] = pow(10, len(word)-j-1)


l = sorted(wordCount.items(), key=lambda x : x[1], reverse=True)
ans = 0
idx = 9

for alpha, value in l:
    ans += idx * value
    idx -= 1

print(ans)