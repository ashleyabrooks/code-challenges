def summation(numbers):
    i = numbers[0]
    sum = 0
    
    for num in numbers[1:i+1]:
        sum += num
    
    print sum

summation([4, 1, 2, 3, 4])