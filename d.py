def reverse (a):
    a = int(a)
    b = 0
    while (a != 0) :
        b *= 10
        b += (a % 10)
        a = a // 10
    return b

p = 1
list = []
while p == 1 :
    char = input()
    if char != 'End':
        list.append(int(char))
    elif char == 'End':
        p = 0

for i in range(len(list) - 1, -1, -1):
    print(reverse(list[i]))
