import math


def fib(n):
    """
    Calculate the nth term in the Fibonacci sequence
    """
    if n < 1:
        return 'ERROR'
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

    
def is_prime(n):
    """
    check if integer n is a prime
    """
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def max_prime_factor(n):
    """
    Iterate through all numbers between 1 and the square root of n, check to see if that number is prime,
    check if that number is a factor of n, set that number equal to max prime
    """
    max_prime = 0
    for i in range(1, int(n**0.5)+1):
        if is_prime(i) and n % i == 0:
            max_prime = i
    return max_prime


def check_for_palindrome(n):
    """
    Take in a number, then check if that number is equal to the reverse of that number
    """
    if n == int(str(n)[::-1]):
        return True
    else:
        return False


def num_factors(n):
    """
    Take in a number, iterate through all numbers between 1 and 1 less than the square root of the given number.
    If the current iteration is a factor of the given number, add 2 to the count of factors for the 
    multiplicand(i.e. current iteration) and multiplier(i.e. given number divided by multiplicand).
    """
    factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            factors += 2
    return factors


def collatz_sequence(n):
    """
    Take in a number and calculate the full collatz sequence for that number. Then, return the length of that sequence.
    
    Collatz sequence: if the current number is even, divide it by 2; if the current number is odd, multiply it by 3 and add 1;
    stop when the current number equals 1.
    """
    current_num = n
    sequence_length = 0
    while current_num != 1:
        if current_num == 0:
            sequence_length = 0
            current_num = 1
        elif current_num % 2 == 0:
            current_num = current_num / 2
            sequence_length += 1
        else:
            current_num = 3 * current_num + 1
            sequence_length += 1
    return sequence_length


def factorial(n):
    """
    Calculate the value of a factorial without using recursion. In a simple function like this, 
    the speed of automatic allocation does not outweigh the slowness of recursive calculation.
    """
    total_factorial = 1
    for i in range(n, 1, -1):
        total_factorial *= i

    return total_factorial


def recursive_factorial(n):
    """
    Calculate the value of a factorial using recursion. Despite being slower than iterative calculation, 
    the code is cleaner and easier to follow. 
    When the calculation time is not significantly different, recursion is used.
    """
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n-1)


def fib_no_recursion(n):
    """
    Calculate the fibonacci sequence using iteration instead of recursion. 
    See factorial docstring for reasoning on iteration over recursion.
    """
    nth_num = 1
    a = 0
    previous_num = 0
    if n == 1 or n == 2:
        return nth_num
    else:
        for spot in range(n, 1, -1):
            previous_num = nth_num
            nth_num = nth_num + a
            a = previous_num

        return nth_num


def single_permutation(n, k):
    """
    Calculate the number of permutations for a single value of (n,k).
    """
    num_permutations = (recursive_factorial(n) / recursive_factorial(n - k))
    return num_permutations


def permutations(n, k):
    """
    Calculate the total number of permutations for a varying value of n.
    """
    num_permutations = 0
    if k == 0:
        num_permutations = factorial(n)
        n = 0
    while n >= 1:
        num_permutations += (factorial(n) / factorial(n - k))
        n -= 1
    return num_permutations


def single_combination(n, k):
    """
    Calculate the number of combinations for a single value of (n,k).
    """
    num_combinations = 0
    if k == 0:
        num_combinations = 1
        n = 0
    if n >= 1:
        num_combinations = (factorial(n) / (factorial(n - k) * factorial(k)))
    return num_combinations


def combinations(n, k):
    """
    Calculate the total number of combinations for a varying value of n.
    """
    num_combinations = 0
    if k == 0:
        num_combinations = 1
        n = 0
    while n >= 1:
        num_combinations += (factorial(n) / (factorial(n - k) * factorial(k)))
        n -= 1
    return num_combinations


def get_factors(n):
    """
    Take in a number, find all the factors of the given number and return a list of the factors.
    """
    factors_list = [1]
    for i in range(2, (n//2) + 1):
        if n % i == 0:
            factors_list.append(i)

    return factors_list
