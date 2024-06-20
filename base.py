def base_10_to_idk(num, divisor):
    
    reminders = str(num % divisor)
    while num / divisor >= 1:
        num = num // divisor
        reminders += str(num % divisor)
    return reminders[::-1]


print(base_10_to_idk(74, 23))
