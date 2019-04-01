from math import floor
import time

pal_list = [0]
t0 = time.time()
for i in range(100, 1000):
    k = 1099 - i
    for j in range(100, 1000):
        is_pal = True
        l = 1099 - j
        m = k*l
        num = str(m)
        length_str = len(num)
        n = 0
        while n < floor(length_str/2):
            p = num[n]
            q = num[length_str-n-1]
            if p is not q:
                is_pal = False
            n += 1
        if is_pal:
            pal_list.append(m)
t1 = time.time()
print(max(pal_list))
t = str("{:10.4f}".format(t1-t0))
print(t + " seconds")
