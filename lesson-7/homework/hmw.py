#task 1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(4))  
print(is_prime(7))  
print(is_prime(1))  
print(is_prime(13)) 
#task 2
def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10
        k //= 10
    return total
print(digit_sum(24))  
print(digit_sum(502)) 
print(digit_sum(99))  
#task 3
def powers_of_two(n):
    power = 1
    while power <= n:
        print(power, end=" ")
        power *= 2
powers_of_two(10)   

