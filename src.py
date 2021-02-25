str1 = 'caberqiitefg'
k = 5
j = k
max = 0
max_sub = ""
arr = ["a","e","i","o","u"]
for i in range(len(str1)):
    sub = str1[i:j]
    p= 0
    for m in arr:
        p += sub.count(m)
    if p!= 0 and p>max:
        max = p
        max_sub = sub
    j+=1
print(max_sub)
