import math
import time


def sum_of_triangular_number(n):
    return (n*(n+1)*(n+2))//6


def triangular_number(n):
    return n*(n+1)//2


def catalan_number(n):
    if n == 0 :
        return 1
    else :

        return int(2*(2*n - 1)/(n+1)*catalan_number(n-1))


def lucas_sequence(n):
    if n == 1:
        return 1
    elif n == 2 :
        return 3
    else:
        return lucas_sequence(n-1)+lucas_sequence(n-2)


def fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)


def factorial(n, m, r):  # factorial of any positive integer
    if (m-r) == n or n == 0:
        return 1
    else :
        return n * factorial(n-1, m, r)


def combination(n, r):   # combination of any set nCr
    return factorial(n, n, r)//factorial(r, r, r)


def sieve_primes(n):     # generate a primes list below or equl of n , p<=n
    A = [True] * (n + 1)
    upper_limit = int(math.sqrt(n)) + 1

    for i in range(2, upper_limit):
        if A[i]:
            for j in range(i ** 2, n + 1, i):
                A[j] = False

    primes = []
    for i in range(2, len(A)):
        if A[i]:
            primes.append(i)
    return primes


def prime_check(n):     # it checks a given number is prime or not
    prime_list = sieve_primes(n)
    if n in prime_list:
        return True
    else:
        return False


def greatest_common_divisor(a, b):   # find gcd of any two integers
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return greatest_common_divisor(b, a % b)


def lowestCommonMultiplor(a, b):  # find the lcm of any two integer
     gcd = greatest_common_divisor(a, b)
     return (a * b) // gcd


def sumOfNaturalNumber(n):  # sum of n natural numbers
     return (n*(n+1))//2


def sumOfsqureNaturalnumber(n):  # sum of n squre of natural numbers
    return (n * (n + 1) * (2*n + 1))//6


def sumOfCubeOfNaturalNumber(n):  # sum of n cube natural numbers
    return ((n*(n+1))//2)**2


def nthOddnumber(n):  # nth odd number
    return 2*n - 1


def sum_of_n_odd_number(n):  # sum of n odd numbers
    return n**2


def nthEvenNumber(n):  # nth even number
    return 2*n


def binomial_theorem(a, b, n):  # binomial theorem
    ans = 0
    for k in range(0, n+1):
        ans += combination(n, k)*(a**(n-k)*(b**k))
    return ans


def kth_binomial_coefficient(n, k):
    return combination(n, k-1)


def pascals_tringle(n):  # pascals_tringle
   for i in range(0, n+1):
       for j in range(0, i+1):
           print(combination(i, j), end="  ")
       print(" ")


def solveEquation(a,b,c):
    return (a**2 + b**2 + c**2 +2*a*b + 2*b*c + 2*c*a)


def giveDay():  # it returns which day on that date
    x = input("Enter the date in formate (dd/mm/yyyy):").split("/")
    x = list(map(int , x))
    d = x[0]
    m = x[1]
    c = x[2]//100
    y = x[2] % 100
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",  5: "Friday", 6: "Saturday"};
    if m > 2:
        m = m-2
    else:
        y = y-1
        m = m+10
    i = (d + math.floor(2.6*m - 0.2) - 2*c + y + math.floor(c/4) + math.floor(y/4)) % 7

    return (days[i])


def decimal_to_k_base_convert(number, b):  # it convert decimal to k base(like  as : binary, hexa etc)
    convert_list = []
    n = number
    if n > b:
        while n > 0:
            convert_list.append( n % b)
            n = n // b
        return ''.join(map(str, convert_list[::-1]))
    else:
        convert_list.append(n)
        return ''.join(map(str, convert_list[::-1]))


def k_base_to_decimal(arr, b):  # it convert k base to decimal
    lista =list(map(int, str(arr)))
    pattern = lista[::-1]
    number = 0
    for i in range(0,len(pattern)):
        number += pattern[i]*(b**i)
    return number


def all_posible_divisor(n):  # all posible divisor of a particular integer
    i = 1
    divisor_list = []
    while i <= math.sqrt(n):
        if n % i == 0:
            if n // i == i:
                divisor_list.append(i)
            else:
                divisor_list.append(i)
                divisor_list.append(n//i)
        i += 1
    return divisor_list


def co_prime_list_in_range(start, end):  # coprime list
    coprimelist = []
    for i in range(start, end):
        if greatest_common_divisor(end, i) == 1:
            coprimelist.append(i)
    return coprimelist


def gcd_continued_fraction(a, b, arr):
    if b > a:
        arr.append(0)
        a, b = b, a
    if a % b == 0:
        arr.append(a//b)
        return b, arr
    else:
        arr.append(a//b)
        return gcd_continued_fraction(b, a % b, arr)


def convergents_of_fraction(arr):
    list_p = list()
    list_q = list()
    list_p.append(arr[0])
    list_p.append((arr[1]*arr[0])+1)
    list_q.append(1)
    list_q.append(arr[1])
    for i in range(2,len(arr)):
        list_p.append((arr[i]*list_p[i-1])+list_p[i-2])
        list_q.append((arr[i]*list_q[i-1])+list_q[i-2])
    return (list_p, list_q)


def linear_diophantine_eqn(a, b, c):  # linear Diophanite Equation solution
    d = greatest_common_divisor(a, b)
    if c % d == 0:
        print(f"{a}x + {b}y = {c}")
        print("We can write as")
        a = a//d
        b = b // d
        c = c // d

        print(f"{a}x + {b}y = {c}")
        if a == b:
            print(f" x = y = {c//(2*a)}")
        else:
            fractions = gcd_continued_fraction(a, b, [])
            p_q_values = convergents_of_fraction(fractions[1])
            if (len(p_q_values[0]) - 2) % 2 == 0:
                print(f"x = {p_q_values[1][len(p_q_values[1]) - 2] * c}")
                print(f"y = -{p_q_values[0][len(p_q_values[0]) - 2] * c}")
            else:
                print(f"x = -{p_q_values[1][len(p_q_values[1]) - 2] * c}")
                print(f"y = {p_q_values[0][len(p_q_values[0]) - 2] * c}")

    else:
        print(f"{a}x + {b}y = {c} has no solution")




