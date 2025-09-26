def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    if num % 2 == 0:
        sum_of_divisors += 2
        while num % 2 == 0:
            num //= 2
    n = 3
    while num > 1:
        if num % n == 0:
            sum_of_divisors += n
            while num % n == 0:
                num //= n
        n += 2

    return sum_of_divisors
