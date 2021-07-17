number = int(input('Введите колличество процентов от 0 до 20'))

if number == 1:
    print(number, 'процент')
elif 1 < number < 5:
    print(number, 'процента')
else:
    print(number, 'процентов')

# output of all declensions for verification

print('-------Вывод всех склонений для проверки-------')
for i in range(0, 21):
    if i == 1:
        print('1 процент')
    elif 1 < i < 5:
        print(i, 'процента')
    else:
        print(i, 'процентов')
