import time, random

def find_range_zeros(lst):
    for i in range(len(lst)):
        if lst[i] != 0:
            b = [list(reversed(lst[:i + 1])), lst[i:]]
            left = b[0].index(0) if 0 in b[0] else len(lst)
            right = b[1].index(0) if 0 in b[1] else len(lst)
            lst[i] = min(left, right)
    print(*lst)
if __name__ == '__main__':
    res_time = 0
    for i in range(20):
        t1 = time.time()
        for j in range(100):
            lst = []
            n = 500
            for i in range(n):
                lst.append(random.randint(-5,5))
            find_range_zeros(lst)
        t2 = time.time()
        res_time += t2-t1
    print(res_time)
