import math

for i in range(1, 1001):
    for j in range(1, 1001-i):
        c = math.sqrt(i*i + j*j)
        if c % 1 == 0 and i + j + c == 1000:
            print("a: " + str(i) + " b: " + str(j) + " c: " + str(c))