# 0: Сreating a list of odd numbers in 3 degrees

numbers = []
for number in range(0, 1001):
    if number % 2 != 0:
        numbers.append(number ** 3)
print(numbers)

# 1: Calculate the sum of those numbers whose sum of digits is completely divisible by 7

result = 0
for num in numbers:
    num_tmp = num
    summ_digit = 0
    while num > 0:
        summ_digit += num % 10
        num //= 10
    if summ_digit % 7 == 0:
       result += num_tmp
print('result1 = ', result)

# 2: Add 17 to each element of the list

numbers_new = [num + 17 for num in numbers]

# Re-calculate the sum of the numbers from the new list, the sum of digits is completely divided by 7

result = 0
for num in numbers_new:
    num_tmp = num
    summ_digit = 0
    while num > 0:
        summ_digit += num % 10
        num //= 10
    if summ_digit % 7 == 0:
        result += num_tmp
print('result2 = ', result)

# 3: Solve the problem under the previous item without creating a new list

result = 0
for num in numbers:
    num += 17
    num_tmp = num
    summ_digit = 0
    while num > 0:
        summ_digit += num % 10
        num //= 10
    if summ_digit % 7 == 0:
        result += num_tmp
print('result3 = ', result)
