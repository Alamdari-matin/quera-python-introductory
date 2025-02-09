l = list(input().split())   
my_dic = {}
for i in range(len(l)):
    my_dic [l[i]] = 0

while True :
    z = input()
    if z == 'End' :
        break
    else :
        x, y = z.split()
        
        my_dic[x] += int(y)
        

l2 = list(my_dic.values())
for k in my_dic.keys():
    if my_dic[k] == max(l2):
        print(k)

