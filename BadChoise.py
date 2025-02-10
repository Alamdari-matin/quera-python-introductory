import statistics
dic = {}
while True :
    n = input()
    if n == 'End':
        break
    else :
        name, score = n.split()
        dic[name] = float(score)
list = list(dic.values())
list2 = []
list3 = []
min = statistics.mean(list)

for key in dic.keys() :
    if dic[key] >= min :
        list2.append(key)
        list3.append(dic[key])
print(list2)
print(statistics.mean(list3))