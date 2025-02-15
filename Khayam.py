from functools import lru_cache


@lru_cache
def khayam (n):
    a = [0] * n
    if n == 2 :
        return [1, 1]
    else :
           
        for i in range(n):
            
            if i == 0 or i == n - 1 :
                a[i] = 1
            else :
                
                a[i] = khayam(n - 1)[i] + khayam(n - 1)[i - 1]
                
        return a
    

m = int(input())
for i in range(1, m + 1):
    print(*khayam(i))