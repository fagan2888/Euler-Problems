sum_squares = 0
square_sum = 0
i: int
for i in range(1, 101):
    sum_squares += i*i
    square_sum += i

square_sum *= square_sum
ans = square_sum - sum_squares
print(ans)