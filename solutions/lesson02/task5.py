def get_gcd(num1: int, num2: int) -> int:
    if num1 > num2:
        n1 = num1
        n2 = num2
    else:
        n1 = num2
        n2 = num1
    while n2 > 0:
        x = n1 % n2
        if x == 0:
            return n2
        else:
            n1 = n2
            n2 = x
