def avg_even_nums(lst):
    sum = 0
    count = 0

    for num in lst:
        if num % 2 == 0:
            sum += num
            count += 1

    print sum / count

lst = [1, 2, 4, 8]
avg_even_nums(lst)