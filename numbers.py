
def is_prime_number(n):
    number_divisors = 0
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            number_divisors += 1
        divisor += 1
    if number_divisors == 2:
        return True
    else:
        return False


def list_primes(n):
    list_prime_number = []
    for i in range(2, n):
        if is_prime_number(i):
            list_prime_number.append(i)
    return list_prime_number


def count_primes(s):
    dictionary = {}
    for item in s:
        if eh_primo(item):
            if item in dictionary:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
    return dictionary


def is_armstrong(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])**len(n)
    if sum == int(n):
        return True
    else:
        return False


def is_almost_armstrong(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])**len(n)
    if sum == int(n) + 1 or sum == int(n)-1:
        return True
    else:
        return False


def list_armstrong(n):
    list_armstrong = []
    for i in range(0, n):
        if is_armstrong(i):
            list_armstrong.append(i)
    return list_armstrong


def is_perfect(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    if soma == n:
        return True
    else:
        return False


def list_perfect(n):
    list_perfect = []
    for i in range(1, n):
        if is_perfect(i):
            list_perfect.append(i)
    return list_perfect
