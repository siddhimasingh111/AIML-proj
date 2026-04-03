def integer_sqrt(n):
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number.")
    return int(n ** 0.5)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_integer_log2(n):
    if n <= 0:
        return 0
    count = 0
    power_of_2 = 1
    while power_of_2 <= n:
        power_of_2 *= 2
        count += 1
    return count - 1

def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def mean_of_digits(n):
    if n < 0:
        raise ValueError("Input must be non-negative.")
    s = str(n)
    if not s:
        return 0.0
    digit_sum = sum(int(digit) for digit in s)
    count = len(s)
    return digit_sum / count

def digital_root(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    return (n - 1) % 9 + 1

def aliquot_sum(n):
    if n <= 1:
        return 0
        
    sum_divisors = 1
    limit = integer_sqrt(n)
    
    for i in range(2, limit + 1):
        if n % i == 0:
            sum_divisors += i
            if i * i != n:
                sum_divisors += (n // i)
                
    return sum_divisors

def is_abundant(n):
    return aliquot_sum(n) > n

def is_deficient(n):
    return aliquot_sum(n) < n

def is_harshad(n):
    if n <= 0:
        return False
    s = str(n)
    digit_sum = sum(int(digit) for digit in s)
    if digit_sum == 0:
        return False
    return n % digit_sum == 0

def is_automorphic(n):
    if n < 0:
        return False
    square = n * n
    num_digits = len(str(n))
    last_digits_of_square = square % power(10, num_digits)
    return last_digits_of_square == n

def is_pronic(n):
    if n < 0:
        return False
    k = integer_sqrt(n)
    return k * (k + 1) == n

def is_prime_trial_division(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    if n <= 1:
        return []
        
    factors = []
    d = 2
    temp_n = n
    
    while temp_n % d == 0:
        factors.append(d)
        temp_n //= d
        
    d = 3
    limit = integer_sqrt(temp_n)
    while d <= limit:
        while temp_n % d == 0:
            factors.append(d)
            temp_n //= d
            limit = integer_sqrt(temp_n)
        d += 2
        
    if temp_n > 1:
        factors.append(temp_n)
        
    return factors

def count_distinct_prime_factors(n):
    factors = prime_factors(n)
    unique = []
    for f in factors:
        if f not in unique:
            unique.append(f)
    return len(unique)

def is_prime_power(n):
    if n <= 1:
        return False
        
    factors = prime_factors(n)
    if not factors:
        return False
    
    first_factor = factors[0]
    for factor in factors:
        if factor != first_factor:
            return False
    return True

def is_mersenne_prime(p):
    if not is_prime_trial_division(p):
        return False
        
    mersenne_number = power(2, p) - 1
    
    return is_prime_trial_division(mersenne_number)

def twin_primes(limit):
    if limit < 5:
        return []
        
    pairs = []
    
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    
    limit_sqrt = integer_sqrt(limit)
    for p in range(2, limit_sqrt + 1):
        if is_p[p]:
            for i in range(p * p, limit + 1, p):
                is_p[i] = False
                
    for p in range(2, limit - 1):
        if is_p[p] and is_p[p + 2]:
            pairs.append((p, p + 2))
            
    return pairs

def count_divisors(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    count = 0
    limit = integer_sqrt(n)
    
    for i in range(1, limit + 1):
        if n % i == 0:
            count += 1
            if i * i != n:
                count += 1
                
    return count

get_aliquot_sum = aliquot_sum

def are_amicable(a, b):
    if a <= 1 or b <= 1 or a == b:
        return False
        
    sum_a = aliquot_sum(a)
    sum_b = aliquot_sum(b)
    
    return sum_a == b and sum_b == a

def multiplicative_persistence(n):
    if n < 0:
        raise ValueError("Input must be a non-negative number.")
    if n < 10:
        return 0
        
    persistence = 0
    current_n = n
    
    while current_n >= 10:
        product = 1
        temp_n = current_n
        
        while temp_n > 0:
            digit = temp_n % 10
            product *= digit
            temp_n //= 10
            
        current_n = product
        persistence += 1
        
    return persistence

def is_highly_composite(n):
    if n <= 1:
        return True
        
    max_divisors_so_far = 0
    
    for i in range(1, n):
        div_count = count_divisors(i)
        if div_count > max_divisors_so_far:
            max_divisors_so_far = div_count
            
    return count_divisors(n) > max_divisors_so_far

def mod_exp(base, exponent, modulus):
    if modulus == 1:
        return 0
    
    base = base % modulus
    result = 1
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        exponent //= 2
        base = (base * base) % modulus
        
    return result

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd_val, x, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    
    if g != 1:
        return None
    else:
        return (x % m + m) % m

def crt(remainders, moduli):
    if not remainders or not moduli or len(remainders) != len(moduli):
        raise ValueError("Inputs must be non-empty lists of the same length.")

    M = 1
    for m in moduli:
        M *= m
        
    result = 0
    
    for r_i, m_i in zip(remainders, moduli):
        M_i = M // m_i
        N_i = mod_inverse(M_i, m_i)
        
        if N_i is None:
            return None 
            
        result = (result + r_i * M_i * N_i) % M
        
    return result

def is_quadratic_residue(a, p):
    if not is_prime_trial_division(p) or p == 2:
        raise ValueError("Modulus p must be an odd prime number.")
        
    if a % p == 0:
        return True
        
    legendre_symbol = mod_exp(a, (p - 1) // 2, p)
    
    return legendre_symbol == 1

def order_mod(a, n):
    if gcd(a, n) != 1:
        return None

    result = 1
    k = 1
    a_mod = a % n
    
    while True:
        result = (result * a_mod) % n
        
        if result == 1:
            return k
            
        k += 1
        if k > n:
            return None 

def is_fibonacci_prime(n):
    if not is_prime_trial_division(n):
        return False

    n_squared = n * n
    
    def is_perfect_square(k):
        if k < 0: return False
        root = integer_sqrt(k)
        return root * root == k

    return is_perfect_square(5 * n_squared + 4) or is_perfect_square(5 * n_squared - 4)

def lucas_sequence(n):
    if n <= 0: return []
    if n == 1: return [2]
    if n == 2: return [2, 1]
        
    sequence = [2, 1]
    
    for _ in range(2, n):
        next_lucas = sequence[-1] + sequence[-2]
        sequence.append(next_lucas)
        
    return sequence

def is_perfect_power(n):
    if n <= 1:
        return False

    max_exponent = get_integer_log2(n)
    
    for b in range(2, max_exponent + 1):
        a = round(n ** (1 / b))
        
        if power(a, b) == n:
            return True
            
    return False

def collatz_length(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
        
    steps = 0
    current_n = n
    
    while current_n != 1:
        if current_n % 2 == 0:
            current_n //= 2
        else:
            current_n = 3 * current_n + 1
            
        steps += 1
        
    return steps

def polygonal_number(s, n):
    if s < 3 or n < 1:
        raise ValueError("s (sides) must be >= 3 and n (position) must be >= 1.")
        
    result = ((s - 2) * n * n - (s - 4) * n) // 2
    
    return result

def is_carmichael(n):
    if is_prime_trial_division(n) or n < 561:
        return False
        
    for a in range(2, 20): 
        if gcd(a, n) == 1:
            if mod_exp(a, n - 1, n) != 1:
                return False
                
    return True

MILLER_RABIN_WITNESSES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] 

def is_prime_miller_rabin(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    def witness_check(a):
        x = mod_exp(a, d, n)
        if x == 1 or x == n - 1:
            return True
        
        for _ in range(s - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                return True
        return False

    for a in MILLER_RABIN_WITNESSES:
        if a >= n:
            break
        if not witness_check(a):
            return False
            
    return True

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if is_prime_trial_division(n):
        return n
        
    x = 2
    y = 2
    c = 1 
    d = 1 
    
    def func(val, const, mod):
        return (val * val + const) % mod

    while d == 1:
        x = func(x, c, n)
        y = func(func(y, c, n), c, n)
        
        diff = x - y
        if diff < 0:
            diff = -diff
            
        d = gcd(diff, n)
        
        if d == n:
            return None
            
    return d

def zeta_approx(s, terms):
    if s <= 1:
        raise ValueError("Series approximation only converges for s > 1.")
    if terms <= 0:
        return 0.0
        
    approximation = 0.0
    
    for k in range(1, terms + 1):
        term = 1.0 / power(k, s)
        approximation += term
        
    return approximation

def partition_function(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
        
    p = [0] * (n + 1)
    p[0] = 1

    for i in range(1, n + 1):
        sum_val = 0
        k = 1
        
        while True:
            g_k_pos = k * (3 * k - 1) // 2
            if i - g_k_pos < 0:
                break

            g_k_neg = k * (3 * k + 1) // 2
            
            sign = 1 if k % 4 <= 2 and k % 4 != 0 else -1
            
            sum_val += sign * p[i - g_k_pos]
            
            if i - g_k_neg >= 0:
                sum_val += sign * p[i - g_k_neg]
                
            k += 1
            
        p[i] = sum_val
        
    return p[n]




print(f"1. Factorial(5): {factorial(5)}")
print(f"2. Is Palindrome(121): {is_palindrome(121)}")
print(f"3. Mean of Digits(1234): {mean_of_digits(1234):.2f}")
print(f"4. Digital Root(458): {digital_root(458)}")
print(f"5. Is Abundant(12): {is_abundant(12)}") 
print(f"6. Is Deficient(10): {is_deficient(10)}")
print(f"7. Is Harshad(18): {is_harshad(18)}")
print(f"8. Is Automorphic(25): {is_automorphic(25)}")
print(f"9. Is Pronic(42): {is_pronic(42)}")
print(f"10. Prime Factors(60): {prime_factors(60)}")
print(f"11. Count Distinct Prime Factors(60): {count_distinct_prime_factors(60)}")
print(f"12. Is Prime Power(8): {is_prime_power(8)}")
print(f"13. Is Mersenne Prime(3): {is_mersenne_prime(3)}")
print(f"14. Twin Primes(30): {twin_primes(30)}")
print(f"15. Count Divisors(12): {count_divisors(12)}")
print(f"16. Aliquot Sum(28): {get_aliquot_sum(28)}")
print(f"17. Are Amicable(220, 284): {are_amicable(220, 284)}")
print(f"18. Multiplicative Persistence(39): {multiplicative_persistence(39)}")
print(f"19. Is Highly Composite(12): {is_highly_composite(12)}")
print(f"20. Modular Exponentiation(5^3 mod 7): {mod_exp(5, 3, 7)}")
print(f"21. Modular Inverse (3^-1 mod 11): {mod_inverse(3, 11)}")
print(f"22. CRT Solver (x≡2 mod 3, x≡3 mod 5): {crt([2, 3], [3, 5])}")
print(f"23. Is Quadratic Residue (4 mod 7): {is_quadratic_residue(4, 7)}")
print(f"24. Order Mod (2 mod 7): {order_mod(2, 7)}")
print(f"25. Is Fibonacci Prime(5): {is_fibonacci_prime(5)}")
print(f"26. Lucas Sequence(5): {lucas_sequence(5)}")
print(f"27. Is Perfect Power(27): {is_perfect_power(27)}")
print(f"28. Collatz Length(6): {collatz_length(6)}")
print(f"29. Polygonal Number (5-gonal, 3rd): {polygonal_number(5, 3)}")
print(f"30. Is Carmichael(561): {is_carmichael(561)}")
print(f"31. Miller-Rabin Prime Check(97): {is_prime_miller_rabin(97)}")
print(f"32. Pollard Rho Factorization(91): {pollard_rho(91)}")
print(f"33. Riemann Zeta Approx(s=2, terms=10): {zeta_approx(2, 10):.4f}")
print(f"34. Partition Function(5): {partition_function(5)}")
