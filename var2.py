import time, random

def find_range_zeros(lst):
    res = [0]*n
    if not 0 in lst:
        print("No zeros found")
        return
    left = lst.index(0)
    for i in range(left, len(lst)):
        if lst[i] == 0:
            res[i] = 0
        else:
            res[i] = res[i-1] + 1
    right = len(lst) - lst[::-1].index(0) - 1
    for i in range(right, left, -1):
        if lst[i] == 0:
            res[i] = 0
        else:
            res[i] = min(res[i+1] + 1, res[i])
    for i in range(left-1, -1, -1):
        res[i] = res[i+1] + 1
    print(*res)

if __name__ == '__main__':
    res_time = 0
    for i in range(20):
        t1 = time.time()
        for j in range(100):
            lst = []
            n = 500
            for i in range(n):
                lst.append(random.randint(-5, 5))
            find_range_zeros(lst)
        t2 = time.time()
        res_time += t2 - t1
    print(res_time)
