import math

def is_prime(num):
    if num <= 1:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def prime_list(nums):
    output=[]
    for num in nums:
        if is_prime(num):
            output.append(num)
    return output

nums=[2,3,4,5,6,7,8,9]
print(prime_list(nums))
