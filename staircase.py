def StairCase(n):
    for i in range(1, n + 1):
        print (' ' * (n - i)) + ('#' * i) 

StairCase(6)