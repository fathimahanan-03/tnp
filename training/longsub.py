def sub(s):
    from collections import defaultdict
    count = defaultdict(int)
    l = 0
    res = 0

    for r in range(len(s)):
        count[s[r]] += 1
        while len(count) > k:
            count[s[l]]-=1
            if count[s[l]]==0:
                del count[s[l]]
            l += 1
        res = max(res, r - l + 1)
    print(res)

s = input()
k = int(input())
sub(s)
