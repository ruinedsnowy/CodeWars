a = [1, 5.2, 4, 0, -1]

def sum_array(a):
    if len(a) == 0:
        return 0
    else:
        sum = 0
        for x in range(len(a)):
            sum += a[x]
        return sum

sum_array(a)