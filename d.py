n = int(input())

l = list(map(int, input().split()))

ll = [0] * 101

for i in range(len(l)):
    ll[l[i]] += 1

for i in range(len(ll)):
    if ll[i] == 0 :
        ll[i] = 101

print(ll)
print(ll.index(min(ll)+1))