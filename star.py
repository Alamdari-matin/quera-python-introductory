n, m = map(int, input().split()) 
a = []
star = 0


for i in range(n):
    a.append(input())

for i in range(n):
    for j in range(len(a[i])):
        
        if a[i][j] == "*":
            star += 1
            

print(star)