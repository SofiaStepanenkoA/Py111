def is_subsequence(s: str, t: str) -> bool:
    j = 0
    count = 0
    if not s:
        return True
    for i in range(len(t)):
        if t[i] == s[j]:
            j += 1
            count += 1
    return count == len(s)


t='abcde'
s='ace'
print(is_subsequence(s,t))